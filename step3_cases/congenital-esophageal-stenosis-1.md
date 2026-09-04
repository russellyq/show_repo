# Congenital esophageal stenosis

[返回 Step 3 总览](../README_STEP3_VISUALIZATION.md)

- **Case ID：** `congenital-esophageal-stenosis-1`
- **Case URL：** [https://radiopaedia.org/cases/congenital-esophageal-stenosis-1?lang=us](https://radiopaedia.org/cases/congenital-esophageal-stenosis-1?lang=us)
- **验证模型：** Qwen3-VL-8B
- **图像 / Step 2 findings：** 5 / 7
- **定位结果：** strong 0；partial 6；not support 9；parse error 0
- **Strong bbox relations：** 0
- **原始 JSON：** [case_evidence.json](../assets_step3/congenital-esophageal-stenosis-1/case_evidence.json)

**Overlay 图例：** 红框为跨图新定位；绿框为 IoU >= 0.5 的已有 bbox；黄框为未达到阈值的已有 bbox。

## Step 2 Finding Nodes

### Finding 1: `study_000_fluoroscopy_image_000_frontal_f01`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_000_frontal_f01.png" width="420">

- **Modality / subcategory：** Fluoroscopy / Frontal
- **bbox_2d：** `[175, 280, 280, 375]`
- **Lingshu caption：** The image shows a frontal view of the neck and upper chest area. There is a red box highlighting a specific region on the left side of the neck. Within this region, there appears to be an abnormality that could potentially indicate a pathological condition. The surrounding tissues and structures appear relatively normal, without any obvious signs of inflammation, swelling, or other abnormalities.

### Finding 2: `study_000_fluoroscopy_image_001_frontal_f01`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f01.png" width="420">

- **Modality / subcategory：** Fluoroscopy / Frontal
- **bbox_2d：** `[27, 27, 187, 236]`
- **Lingshu caption：** The image shows a frontal view of the chest with a red box highlighting an area of interest in the upper left quadrant. Within this region, there appears to be a radiopaque structure that could represent a foreign body or calcification. The surrounding lung fields appear clear without obvious signs of consolidation, effusion, or pneumothorax. The heart silhouette is visible and appears normal in size and shape. The diaphragm and costophrenic angles are also well-defined. No acute bony abnormalities are noted in the visible portions of the ribs and spine.

### Finding 3: `study_000_fluoroscopy_image_001_frontal_f02`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f02.png" width="420">

- **Modality / subcategory：** Fluoroscopy / Frontal
- **bbox_2d：** `[778, 314, 875, 424]`
- **Lingshu caption：** The image shows a frontal view of the chest with a red bounding box highlighting a specific area. Within this region, there appears to be a radiopaque object consistent with a foreign body, likely a coin, located in the upper esophagus. The surrounding structures, including the trachea and major bronchi, appear unremarkable. The lungs show no obvious signs of consolidation, effusion, or pneumothorax. The heart silhouette is normal in size and shape. There are no apparent fractures or dislocations of the ribs or clavicles.

### Finding 4: `study_000_fluoroscopy_image_001_frontal_f03`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f03.png" width="420">

- **Modality / subcategory：** Fluoroscopy / Frontal
- **bbox_2d：** `[845, 314, 942, 424]`
- **Lingshu caption：** The image shows a frontal view of the chest with a focus on the upper thoracic region. There is a marked area in the left upper quadrant of the image, which appears to be highlighted for further examination. Within this region, there is a noticeable opacity that could suggest the presence of an abnormality such as a mass or consolidation. The surrounding lung fields appear relatively clear, with no obvious signs of pleural effusion or pneumothorax. The heart silhouette is partially visible, and there are no apparent abnormalities in the mediastinum. The diaphragm and bony structures, including the ribs and spine, do not show any significant deviations from normal anatomy.

### Finding 5: `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01.png" width="420">

- **Modality / subcategory：** CT / Sagittal mediastinal window - with contrast
- **bbox_2d：** `[220, 360, 440, 680]`
- **Lingshu caption：** The red box is located in the anterior mediastinum. There is a large mass in this area which appears to be heterogeneous in density. The mass is displacing the heart posteriorly.

### Finding 6: `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02.png" width="420">

- **Modality / subcategory：** CT / Sagittal mediastinal window - with contrast
- **bbox_2d：** `[300, 480, 440, 640]`
- **Lingshu caption：** The image shows a sagittal view of the chest with a focus on the mediastinum. The boxed region highlights an area of interest that appears to have increased density compared to surrounding tissues. This could indicate a mass or lesion. The mediastinal structures, including the heart and major vessels, are visible, and there is no obvious displacement or compression of these structures. The lung fields appear clear without any significant abnormalities such as consolidation or effusion. The bony structures, including the vertebrae and ribs, are intact without signs of fracture or lytic lesions.

### Finding 7: `study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01.png" width="420">

- **Modality / subcategory：** Photograph / Upper digestive tract endoscopy.
- **bbox_2d：** `[427, 172, 731, 630]`
- **Lingshu caption：** The esophagus appears normal. The gastroesophageal junction is visible. The stomach is visible. There is a small amount of food debris present. The pylorus is visible.

## Directed Cross-image Validation

### Anchor 1: `study_000_fluoroscopy_image_000_frontal_f01`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_000_frontal_f01.png" width="420">

**Anchor Lingshu caption：** The image shows a frontal view of the neck and upper chest area. There is a red box highlighting a specific region on the left side of the neck. Within this region, there appears to be an abnormality that could potentially indicate a pathological condition. The surrounding tissues and structures appear relatively normal, without any obvious signs of inflammation, swelling, or other abnormalities.

#### location_00001: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_000_fluoroscopy_image_001_frontal_f01</th><th>Existing target bbox: study_000_fluoroscopy_image_001_frontal_f02</th><th>Existing target bbox: study_000_fluoroscopy_image_001_frontal_f03</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/grounding/location_00001.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f02.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f03.png" width="300"></td></tr>
</table>

- **Target：** `study_000_fluoroscopy_image_001_frontal`; Fluoroscopy; Frontal
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[150, 170, 250, 270]`
- **Maximum IoU：** 0.057; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_000_fluoroscopy_image_001_frontal_f01`; `[27, 27, 187, 236]` | 0.057 | no | The image shows a frontal view of the chest with a red box highlighting an area of interest in the upper left quadrant. Within this region, there appears to be a radiopaque structure that could represent a foreign body or calcification. The surrounding lung fields appear clear without obvious signs of consolidation, effusion, or pneumothorax. The heart silhouette is visible and appears normal in size and shape. The diaphragm and costophrenic angles are also well-defined. No acute bony abnormalities are noted in the visible portions of the ribs and spine. |
| `study_000_fluoroscopy_image_001_frontal_f02`; `[778, 314, 875, 424]` | 0.000 | no | The image shows a frontal view of the chest with a red bounding box highlighting a specific area. Within this region, there appears to be a radiopaque object consistent with a foreign body, likely a coin, located in the upper esophagus. The surrounding structures, including the trachea and major bronchi, appear unremarkable. The lungs show no obvious signs of consolidation, effusion, or pneumothorax. The heart silhouette is normal in size and shape. There are no apparent fractures or dislocations of the ribs or clavicles. |
| `study_000_fluoroscopy_image_001_frontal_f03`; `[845, 314, 942, 424]` | 0.000 | no | The image shows a frontal view of the chest with a focus on the upper thoracic region. There is a marked area in the left upper quadrant of the image, which appears to be highlighted for further examination. Within this region, there is a noticeable opacity that could suggest the presence of an abnormality such as a mass or consolidation. The surrounding lung fields appear relatively clear, with no obvious signs of pleural effusion or pneumothorax. The heart silhouette is partially visible, and there are no apparent abnormalities in the mediastinum. The diaphragm and bony structures, including the ribs and spine, do not show any significant deviations from normal anatomy. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification | `insufficient` | The source region has estimated size measurements, while the target region has unknown measurements, making reliable comparison impossible. |
| Characterization | `insufficient` | The target Lingshu caption is unknown, preventing semantic comparison using only the two Lingshu captions. |

#### location_00002: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/grounding/location_00002.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_000_coronal_lung_window`; CT; Coronal lung window
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[260, 180, 400, 320]`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification | `insufficient` | view, scale, or measurements do not permit a reliable comparison |
| Characterization | `insufficient` | Target Lingshu caption is unknown |

#### location_00003: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01</th><th>Existing target bbox: study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/grounding/location_00003.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast`; CT; Sagittal mediastinal window - with contrast
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[375, 120, 460, 280]`
- **Maximum IoU：** 0.000; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01`; `[220, 360, 440, 680]` | 0.000 | no | The red box is located in the anterior mediastinum. There is a large mass in this area which appears to be heterogeneous in density. The mass is displacing the heart posteriorly. |
| `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02`; `[300, 480, 440, 640]` | 0.000 | no | The image shows a sagittal view of the chest with a focus on the mediastinum. The boxed region highlights an area of interest that appears to have increased density compared to surrounding tissues. This could indicate a mass or lesion. The mediastinal structures, including the heart and major vessels, are visible, and there is no obvious displacement or compression of these structures. The lung fields appear clear without any significant abnormalities such as consolidation or effusion. The bony structures, including the vertebrae and ribs, are intact without signs of fracture or lytic lesions. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification | `insufficient` | The source region lacks explicit measurements, and the target region has unknown measurements, making reliable comparison impossible. |
| Characterization | `insufficient` | The target Lingshu caption is unknown, so semantic comparison cannot be performed. |

#### location_00004: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/images/study_002_photograph_image_000_upper_digestive_tract_endoscopy.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_photograph_image_000_upper_digestive_tract_endoscopy`; Photograph; Upper digestive tract endoscopy.
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01`; `[427, 172, 731, 630]` | n/a | n/a | The esophagus appears normal. The gastroesophageal junction is visible. The stomach is visible. There is a small amount of food debris present. The pylorus is visible. |

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification / characterization | not applicable | Target region was not found, so no downstream validation was run. |

### Anchor 2: `study_000_fluoroscopy_image_001_frontal_f01`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f01.png" width="420">

**Anchor Lingshu caption：** The image shows a frontal view of the chest with a red box highlighting an area of interest in the upper left quadrant. Within this region, there appears to be a radiopaque structure that could represent a foreign body or calcification. The surrounding lung fields appear clear without obvious signs of consolidation, effusion, or pneumothorax. The heart silhouette is visible and appears normal in size and shape. The diaphragm and costophrenic angles are also well-defined. No acute bony abnormalities are noted in the visible portions of the ribs and spine.

#### location_00005: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/images/study_001_ct_image_000_coronal_lung_window.jpeg" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_000_coronal_lung_window`; CT; Coronal lung window
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification / characterization | not applicable | Target region was not found, so no downstream validation was run. |

#### location_00006: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01</th><th>Existing target bbox: study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/grounding/location_00006.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast`; CT; Sagittal mediastinal window - with contrast
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[100, 20, 250, 200]`
- **Maximum IoU：** 0.000; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01`; `[220, 360, 440, 680]` | 0.000 | no | The red box is located in the anterior mediastinum. There is a large mass in this area which appears to be heterogeneous in density. The mass is displacing the heart posteriorly. |
| `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02`; `[300, 480, 440, 640]` | 0.000 | no | The image shows a sagittal view of the chest with a focus on the mediastinum. The boxed region highlights an area of interest that appears to have increased density compared to surrounding tissues. This could indicate a mass or lesion. The mediastinal structures, including the heart and major vessels, are visible, and there is no obvious displacement or compression of these structures. The lung fields appear clear without any significant abnormalities such as consolidation or effusion. The bony structures, including the vertebrae and ribs, are intact without signs of fracture or lytic lesions. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification | `insufficient` | view, scale, or measurements do not permit a reliable comparison |
| Characterization | `insufficient` | Target Lingshu caption is unknown |

#### location_00007: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/images/study_002_photograph_image_000_upper_digestive_tract_endoscopy.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_photograph_image_000_upper_digestive_tract_endoscopy`; Photograph; Upper digestive tract endoscopy.
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01`; `[427, 172, 731, 630]` | n/a | n/a | The esophagus appears normal. The gastroesophageal junction is visible. The stomach is visible. There is a small amount of food debris present. The pylorus is visible. |

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification / characterization | not applicable | Target region was not found, so no downstream validation was run. |

### Anchor 3: `study_000_fluoroscopy_image_001_frontal_f02`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f02.png" width="420">

**Anchor Lingshu caption：** The image shows a frontal view of the chest with a red bounding box highlighting a specific area. Within this region, there appears to be a radiopaque object consistent with a foreign body, likely a coin, located in the upper esophagus. The surrounding structures, including the trachea and major bronchi, appear unremarkable. The lungs show no obvious signs of consolidation, effusion, or pneumothorax. The heart silhouette is normal in size and shape. There are no apparent fractures or dislocations of the ribs or clavicles.

#### location_00008: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f02.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/images/study_001_ct_image_000_coronal_lung_window.jpeg" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_000_coronal_lung_window`; CT; Coronal lung window
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification / characterization | not applicable | Target region was not found, so no downstream validation was run. |

#### location_00009: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01</th><th>Existing target bbox: study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f02.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/grounding/location_00009.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast`; CT; Sagittal mediastinal window - with contrast
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[640, 140, 730, 230]`
- **Maximum IoU：** 0.000; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01`; `[220, 360, 440, 680]` | 0.000 | no | The red box is located in the anterior mediastinum. There is a large mass in this area which appears to be heterogeneous in density. The mass is displacing the heart posteriorly. |
| `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02`; `[300, 480, 440, 640]` | 0.000 | no | The image shows a sagittal view of the chest with a focus on the mediastinum. The boxed region highlights an area of interest that appears to have increased density compared to surrounding tissues. This could indicate a mass or lesion. The mediastinal structures, including the heart and major vessels, are visible, and there is no obvious displacement or compression of these structures. The lung fields appear clear without any significant abnormalities such as consolidation or effusion. The bony structures, including the vertebrae and ribs, are intact without signs of fracture or lytic lesions. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification | `insufficient` | view, scale, or measurements do not permit a reliable comparison |
| Characterization | `insufficient` | target Lingshu caption is unknown |

#### location_00010: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f02.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/images/study_002_photograph_image_000_upper_digestive_tract_endoscopy.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_photograph_image_000_upper_digestive_tract_endoscopy`; Photograph; Upper digestive tract endoscopy.
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01`; `[427, 172, 731, 630]` | n/a | n/a | The esophagus appears normal. The gastroesophageal junction is visible. The stomach is visible. There is a small amount of food debris present. The pylorus is visible. |

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification / characterization | not applicable | Target region was not found, so no downstream validation was run. |

### Anchor 4: `study_000_fluoroscopy_image_001_frontal_f03`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f03.png" width="420">

**Anchor Lingshu caption：** The image shows a frontal view of the chest with a focus on the upper thoracic region. There is a marked area in the left upper quadrant of the image, which appears to be highlighted for further examination. Within this region, there is a noticeable opacity that could suggest the presence of an abnormality such as a mass or consolidation. The surrounding lung fields appear relatively clear, with no obvious signs of pleural effusion or pneumothorax. The heart silhouette is partially visible, and there are no apparent abnormalities in the mediastinum. The diaphragm and bony structures, including the ribs and spine, do not show any significant deviations from normal anatomy.

#### location_00011: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f03.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/images/study_001_ct_image_000_coronal_lung_window.jpeg" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_000_coronal_lung_window`; CT; Coronal lung window
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification / characterization | not applicable | Target region was not found, so no downstream validation was run. |

#### location_00012: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01</th><th>Existing target bbox: study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f03.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/grounding/location_00012.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast`; CT; Sagittal mediastinal window - with contrast
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[675, 244, 764, 334]`
- **Maximum IoU：** 0.000; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01`; `[220, 360, 440, 680]` | 0.000 | no | The red box is located in the anterior mediastinum. There is a large mass in this area which appears to be heterogeneous in density. The mass is displacing the heart posteriorly. |
| `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02`; `[300, 480, 440, 640]` | 0.000 | no | The image shows a sagittal view of the chest with a focus on the mediastinum. The boxed region highlights an area of interest that appears to have increased density compared to surrounding tissues. This could indicate a mass or lesion. The mediastinal structures, including the heart and major vessels, are visible, and there is no obvious displacement or compression of these structures. The lung fields appear clear without any significant abnormalities such as consolidation or effusion. The bony structures, including the vertebrae and ribs, are intact without signs of fracture or lytic lesions. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification | `insufficient` | view, scale, or measurements do not permit a reliable comparison |
| Characterization | `insufficient` | Target Lingshu caption is unknown |

#### location_00013: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_000_fluoroscopy_image_001_frontal_f03.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/images/study_002_photograph_image_000_upper_digestive_tract_endoscopy.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_photograph_image_000_upper_digestive_tract_endoscopy`; Photograph; Upper digestive tract endoscopy.
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01`; `[427, 172, 731, 630]` | n/a | n/a | The esophagus appears normal. The gastroesophageal junction is visible. The stomach is visible. There is a small amount of food debris present. The pylorus is visible. |

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification / characterization | not applicable | Target region was not found, so no downstream validation was run. |

### Anchor 5: `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01.png" width="420">

**Anchor Lingshu caption：** The red box is located in the anterior mediastinum. There is a large mass in this area which appears to be heterogeneous in density. The mass is displacing the heart posteriorly.

#### location_00014: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f01.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/images/study_002_photograph_image_000_upper_digestive_tract_endoscopy.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_photograph_image_000_upper_digestive_tract_endoscopy`; Photograph; Upper digestive tract endoscopy.
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01`; `[427, 172, 731, 630]` | n/a | n/a | The esophagus appears normal. The gastroesophageal junction is visible. The stomach is visible. There is a small amount of food debris present. The pylorus is visible. |

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification / characterization | not applicable | Target region was not found, so no downstream validation was run. |

### Anchor 6: `study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02`

<img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02.png" width="420">

**Anchor Lingshu caption：** The image shows a sagittal view of the chest with a focus on the mediastinum. The boxed region highlights an area of interest that appears to have increased density compared to surrounding tissues. This could indicate a mass or lesion. The mediastinal structures, including the heart and major vessels, are visible, and there is no obvious displacement or compression of these structures. The lung fields appear clear without any significant abnormalities such as consolidation or effusion. The bony structures, including the vertebrae and ribs, are intact without signs of fracture or lytic lesions.

#### location_00015: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01</th></tr>
<tr><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_001_ct_image_001_sagittal_mediastinal_window_with_contrast_f02.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/images/study_002_photograph_image_000_upper_digestive_tract_endoscopy.png" width="300"></td><td><img src="../assets_step3/congenital-esophageal-stenosis-1/nodes/study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_photograph_image_000_upper_digestive_tract_endoscopy`; Photograph; Upper digestive tract endoscopy.
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_photograph_image_000_upper_digestive_tract_endoscopy_f01`; `[427, 172, 731, 630]` | n/a | n/a | The esophagus appears normal. The gastroesophageal junction is visible. The stomach is visible. There is a small amount of food debris present. The pylorus is visible. |

**Quantification / characterization：**

| Validation | Status | Reason |
|---|---|---|
| Quantification / characterization | not applicable | Target region was not found, so no downstream validation was run. |

## Dynamically Skipped Anchors

None.
