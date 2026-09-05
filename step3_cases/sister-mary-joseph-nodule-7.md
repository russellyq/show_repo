# Sister Mary Joseph nodule

[返回 Step 3 总览](../README_STEP3_VISUALIZATION.md)

- **Case ID：** `sister-mary-joseph-nodule-7`
- **Case URL：** [https://radiopaedia.org/cases/sister-mary-joseph-nodule-7?lang=us](https://radiopaedia.org/cases/sister-mary-joseph-nodule-7?lang=us)
- **验证模型：** Qwen3-VL-8B
- **图像 / Step 2 findings：** 5 / 7
- **定位结果：** strong 1；partial 3；not support 2；parse error 0
- **Strong bbox relations：** 1
- **原始 JSON：** [case_evidence.json](../assets_step3/sister-mary-joseph-nodule-7/case_evidence.json)

**Overlay 图例：** 红框为跨图新定位；绿框为 IoU >= 0.5 的已有 bbox；黄框为未达到阈值的已有 bbox。

## Step 2 Finding Nodes

### Finding 1: `study_000_photograph_image_000_enlarging_umbilical_nodule_f01`

<img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_000_photograph_image_000_enlarging_umbilical_nodule_f01.png" width="420">

- **Modality / subcategory：** Photograph / enlarging umbilical nodule
- **bbox_2d：** `[389, 501, 572, 638]`
- **Lingshu caption：** The umbilicus contains a 2 cm diameter, smooth, rounded, red nodule. The surrounding skin appears normal.

### Finding 2: `study_002_ct_image_000_axial_non_contrast_f01`

<img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f01.png" width="420">

- **Modality / subcategory：** CT / Axial non-contrast
- **bbox_2d：** `[380, 280, 620, 440]`
- **Lingshu caption：** The image shows a cross-sectional view of the abdomen. Within the boxed region, there appears to be an area of increased density or opacity, which could potentially indicate the presence of an abnormality such as a mass, lesion, or other pathological process. The surrounding tissues appear relatively normal in appearance. Further evaluation and correlation with clinical information would be necessary to determine the significance of this finding.

### Finding 3: `study_002_ct_image_000_axial_non_contrast_f02`

<img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f02.png" width="420">

- **Modality / subcategory：** CT / Axial non-contrast
- **bbox_2d：** `[220, 360, 400, 500]`
- **Lingshu caption：** The image shows a large mass in the right upper quadrant of the abdomen. The mass appears to be heterogeneous in density, with areas of both high and low attenuation. There is also evidence of surrounding tissue invasion and possible lymphadenopathy. The mass appears to be displacing adjacent structures, including the liver and kidney.

### Finding 4: `study_002_ct_image_000_axial_non_contrast_f03`

<img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f03.png" width="420">

- **Modality / subcategory：** CT / Axial non-contrast
- **bbox_2d：** `[700, 340, 900, 500]`
- **Lingshu caption：** The image shows a large amount of free air in the peritoneal cavity, consistent with pneumoperitoneum. The air appears to be located primarily in the upper abdomen, surrounding the liver and stomach. There is no evidence of bowel perforation or other intra-abdominal pathology. The lungs appear clear, and there is no evidence of pleural effusion or pneumothorax.

### Finding 5: `study_002_ct_image_001_axial_c_portal_venous_phase_f01`

<img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f01.png" width="420">

- **Modality / subcategory：** CT / Axial C+ portal venous phase
- **bbox_2d：** `[175, 230, 350, 550]`
- **Lingshu caption：** The image shows a cross-sectional view of the abdomen, with a focus on the right kidney. Within the red box, there appears to be an area of increased density or attenuation compared to the surrounding renal parenchyma. This could potentially represent a mass, lesion, or other abnormality within the right kidney. The size, shape, and precise location of this finding would require further evaluation to determine its significance. Additionally, the surrounding structures, such as the liver, spleen, and bowel, appear unremarkable in this particular slice.

### Finding 6: `study_002_ct_image_001_axial_c_portal_venous_phase_f02`

<img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f02.png" width="420">

- **Modality / subcategory：** CT / Axial C+ portal venous phase
- **bbox_2d：** `[400, 260, 520, 440]`
- **Lingshu caption：** The image shows a cross-sectional view of the abdomen, with a focus on the right kidney. Within the red box, there appears to be an area of increased density or attenuation compared to the surrounding renal parenchyma. This could potentially represent a lesion or abnormality within the kidney. The overall appearance of the kidney and surrounding structures should be further evaluated to determine the nature and significance of this finding.

### Finding 7: `study_002_ct_image_001_axial_c_portal_venous_phase_f03`

<img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f03.png" width="420">

- **Modality / subcategory：** CT / Axial C+ portal venous phase
- **bbox_2d：** `[700, 200, 900, 480]`
- **Lingshu caption：** The image shows a cross-sectional view of the abdomen, with a focus on the liver. Within the boxed region, there appears to be a distinct area of increased density or attenuation compared to the surrounding liver parenchyma. This could potentially represent a focal lesion or abnormality within the liver. The size, shape, and precise location of this finding would require further evaluation to determine its significance. Additionally, the overall appearance of the liver and other abdominal structures should be carefully assessed for any other potential abnormalities or changes.

## Directed Cross-image Validation

### Anchor 1: `study_000_photograph_image_000_enlarging_umbilical_nodule_f01`

<img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_000_photograph_image_000_enlarging_umbilical_nodule_f01.png" width="420">

**Anchor Lingshu caption：** The umbilicus contains a 2 cm diameter, smooth, rounded, red nodule. The surrounding skin appears normal.

#### location_00001: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_000_photograph_image_000_enlarging_umbilical_nodule_f01.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/images/study_001_ultrasound_image_000_missing.jpeg" width="300"></td></tr>
</table>

- **Target：** `study_001_ultrasound_image_000_missing`; Ultrasound; missing
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

#### location_00002: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_000_photograph_image_000_enlarging_umbilical_nodule_f01.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/images/study_001_ultrasound_image_001_missing.jpeg" width="300"></td></tr>
</table>

- **Target：** `study_001_ultrasound_image_001_missing`; Ultrasound; missing
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

#### location_00003: STRONG SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_ct_image_000_axial_non_contrast_f01</th><th>Existing target bbox: study_002_ct_image_000_axial_non_contrast_f02</th><th>Existing target bbox: study_002_ct_image_000_axial_non_contrast_f03</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_000_photograph_image_000_enlarging_umbilical_nodule_f01.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/grounding/location_00003.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f02.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f03.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_000_axial_non_contrast`; CT; Axial non-contrast
- **Relation：** `bbox_to_bbox` / `strong_support`
- **Returned target bbox：** `[350, 250, 650, 450]`
- **Maximum IoU：** 0.676; threshold=0.5
- **Strong relation IDs：** `[&#x27;strong_location_00003_01&#x27;]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_000_axial_non_contrast_f01`; `[380, 280, 620, 440]` | 0.676 | yes | The image shows a cross-sectional view of the abdomen. Within the boxed region, there appears to be an area of increased density or opacity, which could potentially indicate the presence of an abnormality such as a mass, lesion, or other pathological process. The surrounding tissues appear relatively normal in appearance. Further evaluation and correlation with clinical information would be necessary to determine the significance of this finding. |
| `study_002_ct_image_000_axial_non_contrast_f02`; `[220, 360, 400, 500]` | 0.057 | no | The image shows a large mass in the right upper quadrant of the abdomen. The mass appears to be heterogeneous in density, with areas of both high and low attenuation. There is also evidence of surrounding tissue invasion and possible lymphadenopathy. The mass appears to be displacing adjacent structures, including the liver and kidney. |
| `study_002_ct_image_000_axial_non_contrast_f03`; `[700, 340, 900, 500]` | 0.000 | no | The image shows a large amount of free air in the peritoneal cavity, consistent with pneumoperitoneum. The air appears to be located primarily in the upper abdomen, surrounding the liver and stomach. There is no evidence of bowel perforation or other intra-abdominal pathology. The lungs appear clear, and there is no evidence of pleural effusion or pneumothorax. |

#### location_00004: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_ct_image_001_axial_c_portal_venous_phase_f01</th><th>Existing target bbox: study_002_ct_image_001_axial_c_portal_venous_phase_f02</th><th>Existing target bbox: study_002_ct_image_001_axial_c_portal_venous_phase_f03</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_000_photograph_image_000_enlarging_umbilical_nodule_f01.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/grounding/location_00004.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f01.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f02.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f03.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_001_axial_c_portal_venous_phase`; CT; Axial C+ portal venous phase
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[347, 236, 486, 377]`
- **Maximum IoU：** 0.316; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_001_axial_c_portal_venous_phase_f01`; `[175, 230, 350, 550]` | 0.000 | no | The image shows a cross-sectional view of the abdomen, with a focus on the right kidney. Within the red box, there appears to be an area of increased density or attenuation compared to the surrounding renal parenchyma. This could potentially represent a mass, lesion, or other abnormality within the right kidney. The size, shape, and precise location of this finding would require further evaluation to determine its significance. Additionally, the surrounding structures, such as the liver, spleen, and bowel, appear unremarkable in this particular slice. |
| `study_002_ct_image_001_axial_c_portal_venous_phase_f02`; `[400, 260, 520, 440]` | 0.316 | no | The image shows a cross-sectional view of the abdomen, with a focus on the right kidney. Within the red box, there appears to be an area of increased density or attenuation compared to the surrounding renal parenchyma. This could potentially represent a lesion or abnormality within the kidney. The overall appearance of the kidney and surrounding structures should be further evaluated to determine the nature and significance of this finding. |
| `study_002_ct_image_001_axial_c_portal_venous_phase_f03`; `[700, 200, 900, 480]` | 0.000 | no | The image shows a cross-sectional view of the abdomen, with a focus on the liver. Within the boxed region, there appears to be a distinct area of increased density or attenuation compared to the surrounding liver parenchyma. This could potentially represent a focal lesion or abnormality within the liver. The size, shape, and precise location of this finding would require further evaluation to determine its significance. Additionally, the overall appearance of the liver and other abdominal structures should be carefully assessed for any other potential abnormalities or changes. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

### Anchor 2: `study_002_ct_image_000_axial_non_contrast_f02`

<img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f02.png" width="420">

**Anchor Lingshu caption：** The image shows a large mass in the right upper quadrant of the abdomen. The mass appears to be heterogeneous in density, with areas of both high and low attenuation. There is also evidence of surrounding tissue invasion and possible lymphadenopathy. The mass appears to be displacing adjacent structures, including the liver and kidney.

#### location_00006: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_ct_image_001_axial_c_portal_venous_phase_f01</th><th>Existing target bbox: study_002_ct_image_001_axial_c_portal_venous_phase_f02</th><th>Existing target bbox: study_002_ct_image_001_axial_c_portal_venous_phase_f03</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f02.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/grounding/location_00006.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f01.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f02.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f03.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_001_axial_c_portal_venous_phase`; CT; Axial C+ portal venous phase
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[280, 310, 440, 500]`
- **Maximum IoU：** 0.182; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_001_axial_c_portal_venous_phase_f01`; `[175, 230, 350, 550]` | 0.182 | no | The image shows a cross-sectional view of the abdomen, with a focus on the right kidney. Within the red box, there appears to be an area of increased density or attenuation compared to the surrounding renal parenchyma. This could potentially represent a mass, lesion, or other abnormality within the right kidney. The size, shape, and precise location of this finding would require further evaluation to determine its significance. Additionally, the surrounding structures, such as the liver, spleen, and bowel, appear unremarkable in this particular slice. |
| `study_002_ct_image_001_axial_c_portal_venous_phase_f02`; `[400, 260, 520, 440]` | 0.114 | no | The image shows a cross-sectional view of the abdomen, with a focus on the right kidney. Within the red box, there appears to be an area of increased density or attenuation compared to the surrounding renal parenchyma. This could potentially represent a lesion or abnormality within the kidney. The overall appearance of the kidney and surrounding structures should be further evaluated to determine the nature and significance of this finding. |
| `study_002_ct_image_001_axial_c_portal_venous_phase_f03`; `[700, 200, 900, 480]` | 0.000 | no | The image shows a cross-sectional view of the abdomen, with a focus on the liver. Within the boxed region, there appears to be a distinct area of increased density or attenuation compared to the surrounding liver parenchyma. This could potentially represent a focal lesion or abnormality within the liver. The size, shape, and precise location of this finding would require further evaluation to determine its significance. Additionally, the overall appearance of the liver and other abdominal structures should be carefully assessed for any other potential abnormalities or changes. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

### Anchor 3: `study_002_ct_image_000_axial_non_contrast_f03`

<img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f03.png" width="420">

**Anchor Lingshu caption：** The image shows a large amount of free air in the peritoneal cavity, consistent with pneumoperitoneum. The air appears to be located primarily in the upper abdomen, surrounding the liver and stomach. There is no evidence of bowel perforation or other intra-abdominal pathology. The lungs appear clear, and there is no evidence of pleural effusion or pneumothorax.

#### location_00007: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_ct_image_001_axial_c_portal_venous_phase_f01</th><th>Existing target bbox: study_002_ct_image_001_axial_c_portal_venous_phase_f02</th><th>Existing target bbox: study_002_ct_image_001_axial_c_portal_venous_phase_f03</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f03.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/grounding/location_00007.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f01.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f02.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f03.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_001_axial_c_portal_venous_phase`; CT; Axial C+ portal venous phase
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[625, 262, 775, 400]`
- **Maximum IoU：** 0.153; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_001_axial_c_portal_venous_phase_f01`; `[175, 230, 350, 550]` | 0.000 | no | The image shows a cross-sectional view of the abdomen, with a focus on the right kidney. Within the red box, there appears to be an area of increased density or attenuation compared to the surrounding renal parenchyma. This could potentially represent a mass, lesion, or other abnormality within the right kidney. The size, shape, and precise location of this finding would require further evaluation to determine its significance. Additionally, the surrounding structures, such as the liver, spleen, and bowel, appear unremarkable in this particular slice. |
| `study_002_ct_image_001_axial_c_portal_venous_phase_f02`; `[400, 260, 520, 440]` | 0.000 | no | The image shows a cross-sectional view of the abdomen, with a focus on the right kidney. Within the red box, there appears to be an area of increased density or attenuation compared to the surrounding renal parenchyma. This could potentially represent a lesion or abnormality within the kidney. The overall appearance of the kidney and surrounding structures should be further evaluated to determine the nature and significance of this finding. |
| `study_002_ct_image_001_axial_c_portal_venous_phase_f03`; `[700, 200, 900, 480]` | 0.153 | no | The image shows a cross-sectional view of the abdomen, with a focus on the liver. Within the boxed region, there appears to be a distinct area of increased density or attenuation compared to the surrounding liver parenchyma. This could potentially represent a focal lesion or abnormality within the liver. The size, shape, and precise location of this finding would require further evaluation to determine its significance. Additionally, the overall appearance of the liver and other abdominal structures should be carefully assessed for any other potential abnormalities or changes. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

## Dynamically Skipped Anchors

| Anchor node | Reused strong relations | Skipped target images |
|---|---|---|
| `study_002_ct_image_000_axial_non_contrast_f01` | `[&#x27;strong_location_00003_01&#x27;]` | `[&#x27;study_002_ct_image_001_axial_c_portal_venous_phase&#x27;]` |

## Case-level Location Validation Summary / 病例级定位验证总结

- **Strong support：** 1 个 bbox-to-bbox 关系
- **Partial support：** 3 个 bbox-to-image 关系
- **Not support：** 2 个 bbox-to-image 关系

### Strong Support

#### Strong 1: `study_000_photograph_image_000_enlarging_umbilical_nodule_f01` ↔ `study_002_ct_image_000_axial_non_contrast_f01`

- **Relation / query：** `strong_location_00003_01` / `location_00003`
- **IoU：** 0.676（threshold=0.5）

<table>
<tr><th>Anchor bbox</th><th>Cross-image grounded target bbox</th><th>Matched target bbox</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_000_photograph_image_000_enlarging_umbilical_nodule_f01.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/grounding/location_00003.png" width="300"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f01.png" width="300"></td></tr>
</table>

- **Anchor Lingshu caption：** The umbilicus contains a 2 cm diameter, smooth, rounded, red nodule. The surrounding skin appears normal.
- **Target Lingshu caption：** The image shows a cross-sectional view of the abdomen. Within the boxed region, there appears to be an area of increased density or opacity, which could potentially indicate the presence of an abnormality such as a mass, lesion, or other pathological process. The surrounding tissues appear relatively normal in appearance. Further evaluation and correlation with clinical information would be necessary to determine the significance of this finding.

### Partial Support

#### Partial 1: `study_000_photograph_image_000_enlarging_umbilical_nodule_f01` → `study_002_ct_image_001_axial_c_portal_venous_phase`

- **Query：** `location_00004`
- **Returned target bbox：** `[347, 236, 486, 377]`
- **Maximum IoU：** 0.316（低于 threshold=0.5）

<table>
<tr><th>Anchor bbox</th><th>Cross-image grounded target bbox</th><th>Closest existing target bbox</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_000_photograph_image_000_enlarging_umbilical_nodule_f01.png" width="320"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/grounding/location_00004.png" width="320"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f02.png" width="320"></td></tr>
</table>

#### Partial 2: `study_002_ct_image_000_axial_non_contrast_f02` → `study_002_ct_image_001_axial_c_portal_venous_phase`

- **Query：** `location_00006`
- **Returned target bbox：** `[280, 310, 440, 500]`
- **Maximum IoU：** 0.182（低于 threshold=0.5）

<table>
<tr><th>Anchor bbox</th><th>Cross-image grounded target bbox</th><th>Closest existing target bbox</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f02.png" width="320"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/grounding/location_00006.png" width="320"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f01.png" width="320"></td></tr>
</table>

#### Partial 3: `study_002_ct_image_000_axial_non_contrast_f03` → `study_002_ct_image_001_axial_c_portal_venous_phase`

- **Query：** `location_00007`
- **Returned target bbox：** `[625, 262, 775, 400]`
- **Maximum IoU：** 0.153（低于 threshold=0.5）

<table>
<tr><th>Anchor bbox</th><th>Cross-image grounded target bbox</th><th>Closest existing target bbox</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_000_axial_non_contrast_f03.png" width="320"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/grounding/location_00007.png" width="320"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_002_ct_image_001_axial_c_portal_venous_phase_f03.png" width="320"></td></tr>
</table>

### Not Support

#### Not support 1: `study_000_photograph_image_000_enlarging_umbilical_nodule_f01` → `study_001_ultrasound_image_000_missing`

- **Query：** `location_00001`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_000_photograph_image_000_enlarging_umbilical_nodule_f01.png" width="340"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/images/study_001_ultrasound_image_000_missing.jpeg" width="340"></td></tr>
</table>

#### Not support 2: `study_000_photograph_image_000_enlarging_umbilical_nodule_f01` → `study_001_ultrasound_image_001_missing`

- **Query：** `location_00002`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/sister-mary-joseph-nodule-7/nodes/study_000_photograph_image_000_enlarging_umbilical_nodule_f01.png" width="340"></td><td><img src="../assets_step3/sister-mary-joseph-nodule-7/images/study_001_ultrasound_image_001_missing.jpeg" width="340"></td></tr>
</table>
