# Gastric band induced megaesophagus presenting as a neck mass

[返回 Step 3 总览](../README_STEP3_VISUALIZATION.md)

- **Case ID：** `gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass`
- **Case URL：** [https://radiopaedia.org/cases/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass?lang=us](https://radiopaedia.org/cases/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass?lang=us)
- **验证模型：** Qwen3-VL-8B
- **图像 / Step 2 findings：** 6 / 5
- **定位结果：** strong 0；partial 3；not support 8；parse error 0
- **Strong bbox relations：** 0
- **原始 JSON：** [case_evidence.json](../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/case_evidence.json)

**Overlay 图例：** 红框为跨图新定位；绿框为 IoU >= 0.5 的已有 bbox；黄框为未达到阈值的已有 bbox。

## Step 2 Finding Nodes

### Finding 1: `study_000_ultrasound_image_000_missing_f01`

<img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_000_ultrasound_image_000_missing_f01.png" width="420">

- **Modality / subcategory：** Ultrasound / missing
- **bbox_2d：** `[100, 100, 900, 900]`
- **Lingshu caption：** The image shows a transverse view of the neck. The boxed region appears to be located in the left side of the neck. Within this region, there is a hypoechoic area that could represent a lymph node or other soft tissue structure. The borders of this area are somewhat irregular, which may indicate an abnormality. Surrounding tissues appear relatively homogeneous without obvious signs of inflammation or other abnormalities.

### Finding 2: `study_001_ct_image_000_axial_non_contrast_f01`

<img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_000_axial_non_contrast_f01.png" width="420">

- **Modality / subcategory：** CT / Axial non-contrast
- **bbox_2d：** `[439, 412, 556, 520]`
- **Lingshu caption：** The red box is located in the midline at the level of the trachea. Within this area there is a large amount of air present in the soft tissues of the neck. There is also extensive subcutaneous emphysema throughout the chest wall bilaterally.

### Finding 3: `study_001_ct_image_001_coronal_non_contrast_f01`

<img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_001_coronal_non_contrast_f01.png" width="420">

- **Modality / subcategory：** CT / Coronal non-contrast
- **bbox_2d：** `[396, 298, 511, 524]`
- **Lingshu caption：** The right upper lobe demonstrates a large area of consolidation with air bronchograms. There is also a small amount of peribronchial cuffing. The left lung is clear. The cardiomediastinal silhouette is unremarkable. No pleural effusions or pneumothorax.

### Finding 4: `study_001_ct_image_002_oblique_non_contrast_f01`

<img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_002_oblique_non_contrast_f01.png" width="420">

- **Modality / subcategory：** CT / Oblique non-contrast
- **bbox_2d：** `[359, 175, 521, 488]`
- **Lingshu caption：** The oblique non-contrast CT image shows a marked region in the upper thoracic area, specifically involving the trachea and surrounding structures. Within this region, there appears to be a significant narrowing of the tracheal lumen, which could indicate stenosis. The tracheal walls seem thickened, and there is evidence of irregularity in the tracheal contour. Adjacent to the trachea, there is a noticeable mass-like structure that may be causing compression or displacement of the trachea. This mass appears to have heterogeneous density, suggesting possible involvement of soft tissue or other pathological processes. The surrounding mediastinal structures, including the esophagus and major blood vessels, do not show obvious abnormalities in this view. The lung fields appear clear without any evident consolidation, effusion, or masses. The bony structures, including the vertebrae and ribs, are intact without signs of fractures or lesions.

### Finding 5: `study_002_fluoroscopy_image_000_missing_f01`

<img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_002_fluoroscopy_image_000_missing_f01.png" width="420">

- **Modality / subcategory：** Fluoroscopy / missing
- **bbox_2d：** `[286, 1, 571, 500]`
- **Lingshu caption：** The esophagus is mildly dilated with a tapered narrowing at the gastroesophageal junction. There is no evidence of retained contrast in the esophagus 15 minutes after ingestion.

## Directed Cross-image Validation

### Anchor 1: `study_000_ultrasound_image_000_missing_f01`

<img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_000_ultrasound_image_000_missing_f01.png" width="420">

**Anchor Lingshu caption：** The image shows a transverse view of the neck. The boxed region appears to be located in the left side of the neck. Within this region, there is a hypoechoic area that could represent a lymph node or other soft tissue structure. The borders of this area are somewhat irregular, which may indicate an abnormality. Surrounding tissues appear relatively homogeneous without obvious signs of inflammation or other abnormalities.

#### location_00001: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th></tr>
<tr><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_000_ultrasound_image_000_missing_f01.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/grounding/location_00001.png" width="300"></td></tr>
</table>

- **Target：** `study_000_ultrasound_image_001_missing`; Ultrasound; missing
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[100, 100, 800, 900]`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00002: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_ct_image_000_axial_non_contrast_f01</th></tr>
<tr><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_000_ultrasound_image_000_missing_f01.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/images/study_001_ct_image_000_axial_non_contrast.jpeg" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_000_axial_non_contrast_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_000_axial_non_contrast`; CT; Axial non-contrast
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_000_axial_non_contrast_f01`; `[439, 412, 556, 520]` | n/a | n/a | The red box is located in the midline at the level of the trachea. Within this area there is a large amount of air present in the soft tissues of the neck. There is also extensive subcutaneous emphysema throughout the chest wall bilaterally. |

#### location_00003: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_ct_image_001_coronal_non_contrast_f01</th></tr>
<tr><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_000_ultrasound_image_000_missing_f01.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/images/study_001_ct_image_001_coronal_non_contrast.jpeg" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_001_coronal_non_contrast_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_coronal_non_contrast`; CT; Coronal non-contrast
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_coronal_non_contrast_f01`; `[396, 298, 511, 524]` | n/a | n/a | The right upper lobe demonstrates a large area of consolidation with air bronchograms. There is also a small amount of peribronchial cuffing. The left lung is clear. The cardiomediastinal silhouette is unremarkable. No pleural effusions or pneumothorax. |

#### location_00004: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_ct_image_002_oblique_non_contrast_f01</th></tr>
<tr><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_000_ultrasound_image_000_missing_f01.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/images/study_001_ct_image_002_oblique_non_contrast.jpeg" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_002_oblique_non_contrast_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_002_oblique_non_contrast`; CT; Oblique non-contrast
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_002_oblique_non_contrast_f01`; `[359, 175, 521, 488]` | n/a | n/a | The oblique non-contrast CT image shows a marked region in the upper thoracic area, specifically involving the trachea and surrounding structures. Within this region, there appears to be a significant narrowing of the tracheal lumen, which could indicate stenosis. The tracheal walls seem thickened, and there is evidence of irregularity in the tracheal contour. Adjacent to the trachea, there is a noticeable mass-like structure that may be causing compression or displacement of the trachea. This mass appears to have heterogeneous density, suggesting possible involvement of soft tissue or other pathological processes. The surrounding mediastinal structures, including the esophagus and major blood vessels, do not show obvious abnormalities in this view. The lung fields appear clear without any evident consolidation, effusion, or masses. The bony structures, including the vertebrae and ribs, are intact without signs of fractures or lesions. |

#### location_00005: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_fluoroscopy_image_000_missing_f01</th></tr>
<tr><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_000_ultrasound_image_000_missing_f01.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/images/study_002_fluoroscopy_image_000_missing.jpeg" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_002_fluoroscopy_image_000_missing_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_fluoroscopy_image_000_missing`; Fluoroscopy; missing
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_fluoroscopy_image_000_missing_f01`; `[286, 1, 571, 500]` | n/a | n/a | The esophagus is mildly dilated with a tapered narrowing at the gastroesophageal junction. There is no evidence of retained contrast in the esophagus 15 minutes after ingestion. |

### Anchor 2: `study_001_ct_image_000_axial_non_contrast_f01`

<img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_000_axial_non_contrast_f01.png" width="420">

**Anchor Lingshu caption：** The red box is located in the midline at the level of the trachea. Within this area there is a large amount of air present in the soft tissues of the neck. There is also extensive subcutaneous emphysema throughout the chest wall bilaterally.

#### location_00006: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_ct_image_001_coronal_non_contrast_f01</th></tr>
<tr><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_000_axial_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/images/study_001_ct_image_001_coronal_non_contrast.jpeg" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_001_coronal_non_contrast_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_coronal_non_contrast`; CT; Coronal non-contrast
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_coronal_non_contrast_f01`; `[396, 298, 511, 524]` | n/a | n/a | The right upper lobe demonstrates a large area of consolidation with air bronchograms. There is also a small amount of peribronchial cuffing. The left lung is clear. The cardiomediastinal silhouette is unremarkable. No pleural effusions or pneumothorax. |

#### location_00007: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_002_oblique_non_contrast_f01</th></tr>
<tr><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_000_axial_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/grounding/location_00007.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_002_oblique_non_contrast_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_002_oblique_non_contrast`; CT; Oblique non-contrast
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[350, 220, 550, 380]`
- **Maximum IoU：** 0.458; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_002_oblique_non_contrast_f01`; `[359, 175, 521, 488]` | 0.458 | no | The oblique non-contrast CT image shows a marked region in the upper thoracic area, specifically involving the trachea and surrounding structures. Within this region, there appears to be a significant narrowing of the tracheal lumen, which could indicate stenosis. The tracheal walls seem thickened, and there is evidence of irregularity in the tracheal contour. Adjacent to the trachea, there is a noticeable mass-like structure that may be causing compression or displacement of the trachea. This mass appears to have heterogeneous density, suggesting possible involvement of soft tissue or other pathological processes. The surrounding mediastinal structures, including the esophagus and major blood vessels, do not show obvious abnormalities in this view. The lung fields appear clear without any evident consolidation, effusion, or masses. The bony structures, including the vertebrae and ribs, are intact without signs of fractures or lesions. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00008: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_fluoroscopy_image_000_missing_f01</th></tr>
<tr><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_000_axial_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/images/study_002_fluoroscopy_image_000_missing.jpeg" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_002_fluoroscopy_image_000_missing_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_fluoroscopy_image_000_missing`; Fluoroscopy; missing
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_fluoroscopy_image_000_missing_f01`; `[286, 1, 571, 500]` | n/a | n/a | The esophagus is mildly dilated with a tapered narrowing at the gastroesophageal junction. There is no evidence of retained contrast in the esophagus 15 minutes after ingestion. |

### Anchor 3: `study_001_ct_image_001_coronal_non_contrast_f01`

<img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_001_coronal_non_contrast_f01.png" width="420">

**Anchor Lingshu caption：** The right upper lobe demonstrates a large area of consolidation with air bronchograms. There is also a small amount of peribronchial cuffing. The left lung is clear. The cardiomediastinal silhouette is unremarkable. No pleural effusions or pneumothorax.

#### location_00009: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_002_oblique_non_contrast_f01</th></tr>
<tr><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_001_coronal_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/grounding/location_00009.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_002_oblique_non_contrast_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_002_oblique_non_contrast`; CT; Oblique non-contrast
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[275, 140, 475, 390]`
- **Maximum IoU：** 0.328; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_002_oblique_non_contrast_f01`; `[359, 175, 521, 488]` | 0.328 | no | The oblique non-contrast CT image shows a marked region in the upper thoracic area, specifically involving the trachea and surrounding structures. Within this region, there appears to be a significant narrowing of the tracheal lumen, which could indicate stenosis. The tracheal walls seem thickened, and there is evidence of irregularity in the tracheal contour. Adjacent to the trachea, there is a noticeable mass-like structure that may be causing compression or displacement of the trachea. This mass appears to have heterogeneous density, suggesting possible involvement of soft tissue or other pathological processes. The surrounding mediastinal structures, including the esophagus and major blood vessels, do not show obvious abnormalities in this view. The lung fields appear clear without any evident consolidation, effusion, or masses. The bony structures, including the vertebrae and ribs, are intact without signs of fractures or lesions. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00010: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_fluoroscopy_image_000_missing_f01</th></tr>
<tr><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_001_coronal_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/images/study_002_fluoroscopy_image_000_missing.jpeg" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_002_fluoroscopy_image_000_missing_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_fluoroscopy_image_000_missing`; Fluoroscopy; missing
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_fluoroscopy_image_000_missing_f01`; `[286, 1, 571, 500]` | n/a | n/a | The esophagus is mildly dilated with a tapered narrowing at the gastroesophageal junction. There is no evidence of retained contrast in the esophagus 15 minutes after ingestion. |

### Anchor 4: `study_001_ct_image_002_oblique_non_contrast_f01`

<img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_002_oblique_non_contrast_f01.png" width="420">

**Anchor Lingshu caption：** The oblique non-contrast CT image shows a marked region in the upper thoracic area, specifically involving the trachea and surrounding structures. Within this region, there appears to be a significant narrowing of the tracheal lumen, which could indicate stenosis. The tracheal walls seem thickened, and there is evidence of irregularity in the tracheal contour. Adjacent to the trachea, there is a noticeable mass-like structure that may be causing compression or displacement of the trachea. This mass appears to have heterogeneous density, suggesting possible involvement of soft tissue or other pathological processes. The surrounding mediastinal structures, including the esophagus and major blood vessels, do not show obvious abnormalities in this view. The lung fields appear clear without any evident consolidation, effusion, or masses. The bony structures, including the vertebrae and ribs, are intact without signs of fractures or lesions.

#### location_00011: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_fluoroscopy_image_000_missing_f01</th></tr>
<tr><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_001_ct_image_002_oblique_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/images/study_002_fluoroscopy_image_000_missing.jpeg" width="300"></td><td><img src="../assets_step3/gastric-band-induced-megaoesophagus-presenting-as-a-neck-mass/nodes/study_002_fluoroscopy_image_000_missing_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_fluoroscopy_image_000_missing`; Fluoroscopy; missing
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_fluoroscopy_image_000_missing_f01`; `[286, 1, 571, 500]` | n/a | n/a | The esophagus is mildly dilated with a tapered narrowing at the gastroesophageal junction. There is no evidence of retained contrast in the esophagus 15 minutes after ingestion. |

## Dynamically Skipped Anchors

None.
