# Step 3 Cross-image Validation 可视化

[返回主 README](README.md)

本页展示 **Qwen3-VL-8B** 当前已完成的 Step 3 结果：Step 2 bbox、Lingshu caption、跨图目标定位、IoU 匹配、strong/partial/not support 定位支持关系，以及 strong/partial pair 的定量大小与定性语义一致性。

**关系定义：**

- `STRONG SUPPORT`：跨图返回框与目标图已有 bbox 的 IoU >= 0.5，属于 bbox-to-bbox。
- `PARTIAL SUPPORT`：目标图找到了新框，但没有已有 bbox 达到阈值，属于 bbox-to-image。
- `NOT SUPPORT`：目标图返回 `null`，属于 bbox-to-image。

**Caption 来源：**

- `STRONG SUPPORT`：展示 A、B 两端已有 bbox 的原始 Step 2 Lingshu caption。
- `PARTIAL SUPPORT`：展示 A 端已有 bbox 的原始 Step 2 Lingshu caption，以及 B 端跨图 re-ground bbox 重新送入 Lingshu 后得到的 caption。
- `NOT SUPPORT`：展示 A 端原始 Step 2 Lingshu caption；由于目标图返回 `null`，B 端没有 bbox，也没有 re-ground caption。
- 中文内容为对模型原始 caption 的逐条忠实翻译，仅用于对照阅读，不修正模型可能存在的医学错误。

**定量 / 定性验证：**

- 定量验证使用两张带 bbox 的图像及对应 Lingshu caption，输出 `consistent` 或 `inconsistent`。
- 定性验证只使用两条 Lingshu caption 判断语义兼容性，输出 `consistent` 或 `inconsistent`。
- 仅 strong-support 与 partial-support pair 接受这两项验证；not-support 不执行。

**Overlay 图例：** 红框为跨图新定位；绿框为达到阈值的已有 bbox；黄框为未达到阈值的已有 bbox。

## Overall Summary

共 **20** 个病例、**237** 条实际执行或复用的定向跨图查询。当前目录中未发现 Qwen3-VL-32B 的完整 Step 3 case evidence，因此本次只展示 8B 结果。

| Status | Count | Percentage |
|---|---:|---:|
| Strong support | 20 | 8.44% |
| Partial support | 69 | 29.11% |
| Not support | 148 | 62.45% |
| Parse error | 0 | 0.00% |

### Quantitative and Qualitative Validation

共 **89** 个 strong/partial pair 完成定量与定性验证。

| Location relation | Pairs | Quantitative consistent | Quantitative inconsistent | Qualitative consistent | Qualitative inconsistent |
|---|---:|---:|---:|---:|---:|
| Strong support | 20 | 8 | 12 | 10 | 10 |
| Partial support | 69 | 34 | 35 | 28 | 41 |
| **Total** | **89** | **42** | **47** | **38** | **51** |

## Cases

| Case | Images | Findings | Queries | Strong | Partial | Not support | Strong relations | Skipped |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [Aspergilloma](step3_cases/aspergilloma-1.md) (`aspergilloma-1`) | 4 | 7 | 12 | 2 | 5 | 5 | 2 | 1 |
| [Calcified abdominal lymph nodes](step3_cases/calcified-abdominal-lymph-nodes.md) (`calcified-abdominal-lymph-nodes`) | 5 | 5 | 4 | 0 | 1 | 3 | 0 | 0 |
| [Congenital esophageal stenosis](step3_cases/congenital-esophageal-stenosis-1.md) (`congenital-esophageal-stenosis-1`) | 5 | 7 | 15 | 0 | 6 | 9 | 0 | 0 |
| [Focal hepatic steatosis](step3_cases/focal-hepatic-steatosis.md) (`focal-hepatic-steatosis`) | 7 | 13 | 48 | 2 | 13 | 33 | 2 | 3 |
| [Gastric band induced megaesophagus presenting as a neck mass](step3_cases/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass.md) (`gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass`) | 6 | 5 | 11 | 0 | 3 | 8 | 0 | 0 |
| [Giant cell tumor of bone](step3_cases/giant-cell-tumor-of-bone-1.md) (`giant-cell-tumor-of-bone-1`) | 4 | 4 | 5 | 1 | 4 | 0 | 1 | 0 |
| [Giant internal carotid artery aneurysm](step3_cases/giant-internal-carotid-artery-aneurysm-1.md) (`giant-internal-carotid-artery-aneurysm-1`) | 7 | 9 | 21 | 3 | 6 | 12 | 3 | 10 |
| [High grade ductal carcinoma in situ: MRI findings](step3_cases/high-grade-ductal-carcinoma-in-situ-mri-findings.md) (`high-grade-ductal-carcinoma-in-situ-mri-findings`) | 7 | 5 | 7 | 1 | 3 | 3 | 1 | 3 |
| [Infected emphysematous bulla](step3_cases/infected-emphysematous-bulla.md) (`infected-emphysematous-bulla`) | 4 | 4 | 6 | 2 | 1 | 3 | 2 | 0 |
| [Insulinoma](step3_cases/insulinoma-3.md) (`insulinoma-3`) | 8 | 5 | 23 | 0 | 3 | 20 | 0 | 0 |
| [Invasive lobular carcinoma](step3_cases/invasive-lobular-carcinoma-10.md) (`invasive-lobular-carcinoma-10`) | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| [Jugulotympanic paraganglioma](step3_cases/jugulotympanic-paraganglioma-9.md) (`jugulotympanic-paraganglioma-9`) | 4 | 5 | 9 | 0 | 1 | 8 | 0 | 0 |
| [Loculated pneumothorax](step3_cases/loculated-pneumothorax.md) (`loculated-pneumothorax`) | 4 | 7 | 10 | 1 | 5 | 4 | 1 | 1 |
| [Morgagni hernia](step3_cases/morgagni-hernia-8.md) (`morgagni-hernia-8`) | 5 | 1 | 3 | 0 | 1 | 2 | 0 | 0 |
| [Sclerotic metastases from carcinoma of the prostate](step3_cases/sclerotic-metastases-from-carcinoma-of-the-prostate.md) (`sclerotic-metastases-from-carcinoma-of-the-prostate`) | 7 | 7 | 24 | 3 | 8 | 13 | 3 | 3 |
| [Sheared Port-a-Cath remnant](step3_cases/sheared-port-a-cath-remnant.md) (`sheared-port-a-cath-remnant`) | 5 | 2 | 1 | 0 | 0 | 1 | 0 | 0 |
| [Sinus pericranii](step3_cases/sinus-pericranii-5.md) (`sinus-pericranii-5`) | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| [Sister Mary Joseph nodule](step3_cases/sister-mary-joseph-nodule-7.md) (`sister-mary-joseph-nodule-7`) | 5 | 7 | 6 | 1 | 3 | 2 | 1 | 1 |
| [Upper tract urothelial carcinoma](step3_cases/upper-tract-urothelial-carcinoma-1.md) (`upper-tract-urothelial-carcinoma-1`) | 10 | 9 | 30 | 3 | 6 | 21 | 3 | 11 |
| [Wall echo shadow sign (breast)](step3_cases/wall-echo-shadow-sign-breast.md) (`wall-echo-shadow-sign-breast`) | 5 | 3 | 2 | 1 | 0 | 1 | 1 | 1 |
