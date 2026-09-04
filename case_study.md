# Case Study: Calcified Abdominal Lymph Nodes

[返回主 README](README.md)

本页具体追踪 [Calcified abdominal lymph nodes](https://radiopaedia.org/cases/calcified-abdominal-lymph-nodes?lang=us) 在 **Qwen3-VL-8B Step 1–4** 中的完整信息流，用于分析错误从哪里产生、为什么没有被 cross-image validation 纠正，以及最终诊断为什么失败。

## 1. 病例与参考答案

- **Case ID：** `calcified-abdominal-lymph-nodes`
- **参考诊断：** Calcified abdominal lymph nodes（腹部钙化淋巴结）
- **诊断确定性：** Diagnosis almost certain
- **患者信息：** 65 岁，男性
- **临床背景：** 12 年前患头颈部鳞状细胞癌，接受过放疗和化疗。
- **影像组合：** X-ray 3 张（正位、侧位、双能骨窗）+ CT 2 张（轴位骨窗）。

Radiopaedia 的病例讨论指出，应结合既往头颈部鳞癌治疗史考虑钙化淋巴结的鉴别诊断，首要解释是**治疗后的钙化淋巴结**。

## 2. 原始图片与 Caption

Radiopaedia 在该病例中提供的是 **study-level caption**，同一 study 内的图片共享同一段文字，而不是每张图分别提供 caption。

### 2.1 X-ray Study

| Image 1: Frontal | Image 2: Lateral | Image 3: Dual energy bone window |
|---|---|---|
| <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_1_original.jpeg" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_2_original.jpeg" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_3_original.jpeg" width="100%"> |

**Radiopaedia 原始 caption：**

> Hilar, mediastinal and parenchymal calcification.

**中文翻译：** 肺门、纵隔及肺实质内可见钙化。

### 2.2 CT Study

| Image 4: Axial bone window | Image 5: Axial bone window |
|---|---|
| <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_4_original.jpeg" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_5_original.jpeg" width="100%"> |

**Radiopaedia 原始 caption：**

> Calcified abdominal lymph nodes.

**中文翻译：** 腹部钙化淋巴结。

## 3. Step 1: 逐图 Grounding

Step 1 应定位每张图中的异常并输出紧致 bbox 和简短 finding caption。下表中的右列是实际给后续步骤使用的 grounding 可视化。

### 3.1 Image 1: X-ray Frontal

| Original | Step 1 grounding |
|---|---|
| <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_1_original.jpeg" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_1_step1_bbox.png" width="100%"> |

- **模型结果：** `regions: []`
- **参考影像信息：** 正位片可见肺门、纵隔及肺实质钙化。
- **问题：** Step 1 完全漏检，没有为后续跨视角验证提供 X-ray 正位 anchor。

### 3.2 Image 2: X-ray Lateral

| Original | Step 1 grounding |
|---|---|
| <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_2_original.jpeg" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_2_step1_bbox.png" width="100%"> |

```json
{
  "bbox_2d": [474, 392, 586, 674],
  "caption": "mediastinal mass"
}
```

- **定位：** bbox 大致覆盖了纵隔内串珠状、团块状高密度钙化区域。
- **定性：** 模型没有识别“钙化”，而是将其命名为 `mediastinal mass`。
- **问题性质：** 这是“位置基本命中、finding 语义错误”，并非单纯 bbox 偏移。

### 3.3 Image 3: X-ray Dual Energy Bone Window

| Original | Step 1 grounding |
|---|---|
| <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_3_original.jpeg" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_3_step1_bbox.png" width="100%"> |

- **模型结果：** `regions: []`
- **参考影像信息：** 双能骨窗进一步突出肺门、纵隔及肺实质钙化。
- **问题：** 在本应有助于显示钙化的视图中仍然漏检，使侧位片的错误“肿块”无法被同 study 的另一视图纠正。

### 3.4 Image 4: CT Axial Bone Window

| Original | Step 1 grounding |
|---|---|
| <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_4_original.jpeg" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_4_step1_bbox.png" width="100%"> |

```json
{
  "bbox_2d": [350, 300, 450, 400],
  "caption": "hypodense lesion with irregular margins in the left lobe of the liver"
}
```

- **定位：** bbox 位于钙化灶左上方的肝实质，未紧密覆盖中央高密度钙化淋巴结。
- **定性：** 将骨窗中的显著高密度钙化误写为“左肝低密度不规则病灶”。
- **问题性质：** bbox 与目标均错误，同时出现器官、密度和病灶性质错误。

### 3.5 Image 5: CT Axial Bone Window

| Original | Step 1 grounding |
|---|---|
| <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_5_original.jpeg" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_5_step1_bbox.png" width="100%"> |

```json
[
  {
    "bbox_2d": [430, 300, 570, 420],
    "caption": "large fluid-filled bowel loop with air-fluid level"
  },
  {
    "bbox_2d": [620, 260, 780, 380],
    "caption": "inflammatory or fluid-filled bowel loop with thickened wall"
  },
  {
    "bbox_2d": [300, 240, 420, 360],
    "caption": "small bowel loop with thickened wall and surrounding fat stranding"
  }
]
```

- **定位：** 三个框主要覆盖肝实质、胃肠气体或邻近软组织；第一个框仅在边缘擦到小片钙化。
- **定性：** 三个 finding 全部围绕积液肠袢、肠壁增厚和脂肪浸润展开，未识别真正关键的高密度钙化淋巴结。
- **问题性质：** 明显假阳性，并把同一张低分辨率 CT 中的正常/非目标结构拆成三个“独立异常”。

### 3.6 Step 1 小结

| 指标 | 结果 |
|---|---:|
| 输入图片 | 5 |
| 返回 region 的图片 | 3/5 |
| 返回 region 总数 | 5 |
| 正确识别“钙化/钙化淋巴结”的 region | 0/5 |
| 明显漏检图片 | Image 1、Image 3 |
| 位置接近但语义错误 | Image 2 |
| bbox 和语义均错误 | Image 4、Image 5 |

## 4. Step 2: Crop Caption 与结构化观察

Step 2 对每个 Step 1 region 分别输入“完整原图 + bbox crop”。没有 Step 1 region 的 Image 1 和 Image 3 不会触发 Step 2 调用，因此仍保持 `findings: []`。

### 4.1 Image 2, Finding 1

| Step 1 bbox image | Actual crop supplied to Step 2 |
|---|---|
| <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_2_step1_bbox.png" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_2_crop_1.png" width="100%"> |

```json
{
  "location": "mediastinum",
  "morphology": "irregular, nodular mass",
  "size": {"long_axis": 3, "short_axis": 2, "unit": "cm"},
  "density": "heterogeneous",
  "margin": "indistinct",
  "surrounding": "mediastinal structures",
  "visible_signs": "mediastinal shift",
  "appearance": "irregular, nodular mass with heterogeneous density",
  "description": "An irregular, nodular mass with heterogeneous density and indistinct margins is visible in the mediastinum. The mass appears to be causing a mediastinal shift. The surrounding mediastinal structures are obscured by the mass.",
  "evidence_quality": "moderate",
  "suspicion_level": "high",
  "confidence": 0.9
}
```

**分析：** crop 内实际最突出的证据是多个粗大、团块状高密度钙化影。Step 2 没有纠正 Step 1 的“mass”标签，反而扩写出“不规则肿块、边缘不清、纵隔移位”，并给出未经标尺校准的 `3 × 2 cm` 和 0.9 高置信度。这里发生了明显的**错误语义强化**。

### 4.2 Image 4, Finding 1

| Step 1 bbox image | Actual crop supplied to Step 2 |
|---|---|
| <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_4_step1_bbox.png" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_4_crop_1.png" width="100%"> |

```json
{
  "location": null,
  "morphology": null,
  "size": {"long_axis": null, "short_axis": null, "unit": null},
  "density": null,
  "margin": null,
  "surrounding": null,
  "visible_signs": null,
  "appearance": null,
  "description": null,
  "evidence_quality": null,
  "suspicion_level": null,
  "confidence": 0.0
}
```

**分析：** crop 只有约 `18 × 18` 像素，并且没有覆盖主要钙化灶。Step 2 没有产生可用观察，这一点比继续编造肝病灶更谨慎，但后续 Step 3 不应再把该 Step 1 claim 判为 supported。

### 4.3 Image 5, Findings 1–3

| Finding 1 crop | Finding 2 crop | Finding 3 crop |
|---|---|---|
| <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_5_crop_1.png" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_5_crop_2.png" width="100%"> | <img src="assets_case_study/calcified-abdominal-lymph-nodes/image_5_crop_3.png" width="100%"> |

三个 region 的结构化 description、location、morphology、density、margin、surrounding、visible signs 和 appearance 均为 `null`，confidence 均为 `0.0`。其中：

- Finding 1 crop 为约 `25 × 21` 像素，`size.unit` 被保留成 `mm`，但长短径为空。
- Finding 2 crop 为约 `28 × 21` 像素，size 全为空。
- Finding 3 crop 为约 `21 × 21` 像素，却生成 `0 × 0 mm`。

**分析：** 三个 crop 都过小且来自错误 bbox，没有足够信息支持“肠袢积液、肠壁增厚、脂肪浸润”。Step 2 实际上已经用空 observation 和 0.0 confidence 表达了“无法验证”，但这一负面证据没有被 Step 3 正确消费。

## 5. Step 3: Cross-image Validation

该病例 5 张图两两组合，共执行 10 个 image-pair validation。模型没有建立任何 `same_lesion`、`same_process`、`different_finding` 或 `uncertain` relation，所有 `cross_image_relations` 均为空。

| Pair | Finding assessment | Relation / unmatched | 模型的 pair summary |
|---|---|---|---|
| Image 1–2 | Image 2 F1: bbox `valid`，claim `supported` | Image 2 F1 unmatched | Image 1 无可疑区域；Image 2 有纵隔肿块，因此无法建立关系。 |
| Image 1–3 | 无 finding assessment | 无 relation | 两张图均没有 proposed finding。 |
| Image 1–4 | Image 4 F1: bbox `valid`，claim `supported` | Image 4 F1 unmatched | Image 4 有肝低密度灶；Image 1 无异常，二者无解剖或临床联系。 |
| Image 1–5 | Image 5 F1–F3 全部 `valid/supported` | 三个 finding 均 unmatched | CT 显示肠道病变，胸片无异常，无法建立关系。 |
| Image 2–3 | Image 2 F1: `valid/supported` | Image 2 F1 unmatched | 侧位片有纵隔肿块，双能片无异常，无法建立关系。 |
| Image 2–4 | Image 2 F1、Image 4 F1 均 `valid/supported` | Image 2 F1 unmatched | 纵隔肿块与肝低密度灶被视为两个无关病变。 |
| Image 2–5 | Image 2 F1、Image 5 F1–F3 全部 `valid/supported` | Image 2 F1 unmatched | 纵隔肿块与肠道异常被视为两个无关过程。 |
| Image 3–4 | Image 4 F1: `valid/supported` | Image 4 F1 unmatched | 双能胸片无异常，CT 有肝低密度灶。 |
| Image 3–5 | Image 5 F1–F3 全部 `valid/supported` | 三个 finding 均 unmatched | 双能胸片无异常，CT 有三个肠道 finding。 |
| Image 4–5 | Image 4 F1、Image 5 F1–F3 全部 `valid/supported` | 四个 finding 均 unmatched | 肝病灶与肠道异常被视为互不相关。 |

### 5.1 Comprehensive Review 原始结果

```json
{
  "global_finding_groups": [],
  "independent_findings": [],
  "rejected_findings": [],
  "unresolved_findings": [],
  "image_coverage_audit": [
    {"image_number": 1, "coverage_status": "complete", "covered_finding_numbers": [], "uncovered_suspicious_regions": []},
    {"image_number": 2, "coverage_status": "complete", "covered_finding_numbers": [1], "uncovered_suspicious_regions": []},
    {"image_number": 3, "coverage_status": "complete", "covered_finding_numbers": [], "uncovered_suspicious_regions": []},
    {"image_number": 4, "coverage_status": "complete", "covered_finding_numbers": [1], "uncovered_suspicious_regions": []},
    {"image_number": 5, "coverage_status": "complete", "covered_finding_numbers": [1, 2, 3], "uncovered_suspicious_regions": []}
  ],
  "case_level_consistency": "consistent",
  "case_level_conflicts": [],
  "evidence_summary": "",
  "recommended_reinspection": []
}
```

### 5.2 Step 3 的具体问题

1. **没有真正复核 claim。** Image 4 和 Image 5 的 Step 2 observation 几乎全部为空、confidence 为 0，但 Step 3 仍将相应 Step 1 claim 判为 `supported`。
2. **同一错误被重复支持。** Image 2 的“纵隔肿块”在与 Image 1、3、4、5 的四次配对中都被判为 supported；配对次数增加反而放大了错误置信感。
3. **没有识别 same process。** 正确线索应是不同部位、不同模态中共同出现的钙化过程；由于 Step 1/2 从未抽取“calcification”，Step 3 无法建立 X-ray 与 CT 之间的 `same_process`。
4. **coverage audit 失真。** Image 1 和 Image 3 明明漏掉可见钙化，却被标记为 `coverage_status: complete`，且没有触发 `recommended_reinspection`。
5. **review 内部不一致。** Pair validation 反复声称 5 个 finding 都受支持，但最终既没有 independent、rejected 或 unresolved finding，也没有 global group，`evidence_summary` 为空。

## 6. Step 4: Qwen3-VL-8B 最终诊断

Step 4 实际接收 5 张原图、患者背景，以及下列 reference findings：

```text
Reference findings:
No reference findings were produced.

Please provide the final diagnosis.
```

因此，Step 3 虽然生成了大量 pair validation，但由于 `evidence_summary` 为空，**没有任何结构化验证结果真正进入 Step 4 的决策上下文**。

<details>
<summary><strong>Qwen3-VL-8B 完整原始输出</strong></summary>

<pre>
Based on the provided clinical history and imaging findings, the most likely diagnosis is:

Metastatic lung cancer (likely from a prior head and neck primary) with possible hepatic metastases.

Rationale:

1. Clinical History: The patient is a 65-year-old male with a known history of head and neck squamous cell carcinoma 12 years ago, treated with radiation and chemotherapy. This is a high-risk scenario for developing a second malignancy or metastatic disease, particularly given the long-term follow-up and prior cancer treatment.

2. Chest X-ray Findings (Images 1, 2, 3):
- Image 1 (PA view): Shows a prominent, irregularly shaped, dense opacity in the right hilum (central area of the right lung). This is highly suggestive of a mass lesion, likely involving the bronchus or mediastinal structures. There is also a smaller, less defined opacity in the left lower lung field.
- Image 2 (Lateral view): Confirms the presence of a large, irregular mass in the right hilum, which is causing mediastinal shift and compression of the trachea. The mass appears to be centrally located, consistent with a primary lung tumor or a metastasis to the mediastinum.
- Image 3 (AP view): Shows a large, dense mass in the right hilum, confirming the findings from the other views. The left lung appears relatively clear, though there is a small opacity in the left lower lung field.
- Overall: The imaging findings are highly suggestive of a primary lung cancer (e.g., non-small cell lung cancer) or a large metastatic lesion in the right hilum.

3. CT Scan Findings (Images 4 and 5):
- Image 4: Shows a large, well-defined, hypodense lesion in the right lobe of the liver, which is highly suspicious for a metastatic liver lesion.
- Image 5: Shows another hypodense lesion in the left lobe of the liver.
- Overall: The presence of multiple hepatic lesions on CT strongly suggests metastatic disease.

Conclusion:

The combination of a large central lung mass (right hilum) and multiple liver lesions in a patient with a history of head and neck cancer strongly indicates metastatic disease. Given the anatomical location and the history of prior head and neck cancer, the primary tumor is likely in the lung, and the liver lesions are metastases.

Final Diagnosis:
Metastatic lung cancer with hepatic metastases.

This diagnosis requires further workup, including biopsy of the lung lesion and possibly PET-CT to assess for other potential metastatic sites.
</pre>

</details>

- **中文要点：** 模型将胸片上的钙化影解释为右肺门/纵隔肿块，将 CT 上的钙化淋巴结解释为双侧肝转移灶，并在既往肿瘤病史影响下诊断为“转移性肺癌伴肝转移”。
- **评测结果：** `Incorrect`
- **参考诊断：** Calcified abdominal lymph nodes

## 7. 错误传播结论

该病例不是单一环节偶然失误，而是一条完整的失败链：

```text
Step 1
漏检正位和双能片钙化；侧位钙化被命名为肿块；CT 钙化被误框为肝/肠道病变
    ↓
Step 2
侧位错误被扩写为高置信度纵隔肿块；CT crop 无法提供有效观察
    ↓
Step 3
忽略 Step 2 的空 observation 和 0 confidence，反复支持错误 claim；
未建立任何 same_process；错误地宣布 coverage complete 和 case consistent
    ↓
Comprehensive review
所有 finding 分类均为空，evidence_summary 为空，也没有触发重新检查
    ↓
Step 4
只得到原图、肿瘤病史和“No reference findings”；再次把钙化误读成肿块/转移灶
    ↓
错误诊断：Metastatic lung cancer with hepatic metastases
```

**最主要的失败点是 Step 1 的 visual grounding 与 finding 命名均不可靠；但 Step 3 也没有履行纠错职责。** 如果 Step 3 能将“空 observation + confidence 0”视为反证，将正位/双能片无 region 视为 coverage incomplete，并触发针对 `calcification/high-density foci` 的重新查看，即使 Step 1 出错，也仍有机会恢复。当前实现则把“没有匹配关系”错误地当成“没有冲突”，最终既未纠正错误，也没有向 Step 4 输出任何可用证据。
