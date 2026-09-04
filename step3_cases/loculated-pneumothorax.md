# Loculated pneumothorax

[返回 Step 3 总览](../README_STEP3_VISUALIZATION.md)

- **Case ID：** `loculated-pneumothorax`
- **Case URL：** [https://radiopaedia.org/cases/loculated-pneumothorax?lang=us](https://radiopaedia.org/cases/loculated-pneumothorax?lang=us)
- **验证模型：** Qwen3-VL-8B
- **图像 / Step 2 findings：** 4 / 7
- **定位结果：** strong 1；partial 5；not support 4；parse error 0
- **Strong bbox relations：** 1
- **原始 JSON：** [case_evidence.json](../assets_step3/loculated-pneumothorax/case_evidence.json)

**Overlay 图例：** 红框为跨图新定位；绿框为 IoU >= 0.5 的已有 bbox；黄框为未达到阈值的已有 bbox。

## Step 2 Finding Nodes

### Finding 1: `study_000_x_ray_image_000_frontal_f01`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_000_x_ray_image_000_frontal_f01.png" width="420">

- **Modality / subcategory：** X-ray / Frontal
- **bbox_2d：** `[601, 469, 886, 919]`
- **Lingshu caption：** The lungs are hyperinflated. There is increased opacity in the left lower lung zone. The heart size is normal. The mediastinal contour is normal. There is no pneumothorax. There is no pleural effusion.

### Finding 2: `study_001_ct_image_000_coronal_lung_window_f01`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f01.png" width="420">

- **Modality / subcategory：** CT / Coronal lung window
- **bbox_2d：** `[101, 284, 427, 825]`
- **Lingshu caption：** The right lower lobe demonstrates a large area of consolidation with air bronchograms. There is also a moderate right pleural effusion. The left lung appears clear.

### Finding 3: `study_001_ct_image_000_coronal_lung_window_f02`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f02.png" width="420">

- **Modality / subcategory：** CT / Coronal lung window
- **bbox_2d：** `[180, 40, 498, 382]`
- **Lingshu caption：** The right upper lobe demonstrates a large cavitary lesion with surrounding consolidation. There is also a smaller cavitary lesion in the right lower lobe. The left lung appears clear.

### Finding 4: `study_001_ct_image_000_coronal_lung_window_f03`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f03.png" width="420">

- **Modality / subcategory：** CT / Coronal lung window
- **bbox_2d：** `[591, 95, 880, 875]`
- **Lingshu caption：** The left lung is well inflated with no areas of focal consolidation, pleural effusion, or pneumothorax identified. The pulmonary vasculature is within normal limits. There is no evidence of hilar lymphadenopathy.

### Finding 5: `study_001_ct_image_001_axial_lung_window_f01`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f01.png" width="420">

- **Modality / subcategory：** CT / Axial lung window
- **bbox_2d：** `[175, 226, 675, 656]`
- **Lingshu caption：** The right upper lobe demonstrates a large cavitary lesion with surrounding consolidation. There is also a smaller cavitary lesion in the left upper lobe. The remaining lung parenchyma appears relatively clear. No pleural effusions or pneumothorax are identified. The mediastinal structures appear unremarkable.

### Finding 6: `study_001_ct_image_001_axial_lung_window_f02`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f02.png" width="420">

- **Modality / subcategory：** CT / Axial lung window
- **bbox_2d：** `[588, 272, 937, 712]`
- **Lingshu caption：** The lungs are hyperinflated. There is a large right pneumothorax with collapse of the right lung. The left lung appears normal.

### Finding 7: `study_002_x_ray_image_000_frontal_f01`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_002_x_ray_image_000_frontal_f01.png" width="420">

- **Modality / subcategory：** X-ray / Frontal
- **bbox_2d：** `[125, 476, 382, 894]`
- **Lingshu caption：** The lungs are hyperinflated. There is increased opacity in the right lower lung zone. The heart size is normal. The mediastinal contour is normal. There is no pneumothorax. There is no pleural effusion.

## Directed Cross-image Validation

### Anchor 1: `study_000_x_ray_image_000_frontal_f01`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_000_x_ray_image_000_frontal_f01.png" width="420">

**Anchor Lingshu caption：** The lungs are hyperinflated. There is increased opacity in the left lower lung zone. The heart size is normal. The mediastinal contour is normal. There is no pneumothorax. There is no pleural effusion.

#### location_00001: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_000_coronal_lung_window_f01</th><th>Existing target bbox: study_001_ct_image_000_coronal_lung_window_f02</th><th>Existing target bbox: study_001_ct_image_000_coronal_lung_window_f03</th></tr>
<tr><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_000_x_ray_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/grounding/location_00001.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f02.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f03.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_000_coronal_lung_window`; CT; Coronal lung window
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[450, 475, 660, 850]`
- **Maximum IoU：** 0.092; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_000_coronal_lung_window_f01`; `[101, 284, 427, 825]` | 0.000 | no | The right lower lobe demonstrates a large area of consolidation with air bronchograms. There is also a moderate right pleural effusion. The left lung appears clear. |
| `study_001_ct_image_000_coronal_lung_window_f02`; `[180, 40, 498, 382]` | 0.000 | no | The right upper lobe demonstrates a large cavitary lesion with surrounding consolidation. There is also a smaller cavitary lesion in the right lower lobe. The left lung appears clear. |
| `study_001_ct_image_000_coronal_lung_window_f03`; `[591, 95, 880, 875]` | 0.092 | no | The left lung is well inflated with no areas of focal consolidation, pleural effusion, or pneumothorax identified. The pulmonary vasculature is within normal limits. There is no evidence of hilar lymphadenopathy. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00002: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_ct_image_001_axial_lung_window_f01</th><th>Existing target bbox: study_001_ct_image_001_axial_lung_window_f02</th></tr>
<tr><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_000_x_ray_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/images/study_001_ct_image_001_axial_lung_window.jpg" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_axial_lung_window`; CT; Axial lung window
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_axial_lung_window_f01`; `[175, 226, 675, 656]` | n/a | n/a | The right upper lobe demonstrates a large cavitary lesion with surrounding consolidation. There is also a smaller cavitary lesion in the left upper lobe. The remaining lung parenchyma appears relatively clear. No pleural effusions or pneumothorax are identified. The mediastinal structures appear unremarkable. |
| `study_001_ct_image_001_axial_lung_window_f02`; `[588, 272, 937, 712]` | n/a | n/a | The lungs are hyperinflated. There is a large right pneumothorax with collapse of the right lung. The left lung appears normal. |

#### location_00003: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_x_ray_image_000_frontal_f01</th></tr>
<tr><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_000_x_ray_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/grounding/location_00003.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_002_x_ray_image_000_frontal_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_x_ray_image_000_frontal`; X-ray; Frontal
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[586, 469, 866, 924]`
- **Maximum IoU：** 0.000; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_x_ray_image_000_frontal_f01`; `[125, 476, 382, 894]` | 0.000 | no | The lungs are hyperinflated. There is increased opacity in the right lower lung zone. The heart size is normal. The mediastinal contour is normal. There is no pneumothorax. There is no pleural effusion. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

### Anchor 2: `study_001_ct_image_000_coronal_lung_window_f01`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f01.png" width="420">

**Anchor Lingshu caption：** The right lower lobe demonstrates a large area of consolidation with air bronchograms. There is also a moderate right pleural effusion. The left lung appears clear.

#### location_00004: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_001_axial_lung_window_f01</th><th>Existing target bbox: study_001_ct_image_001_axial_lung_window_f02</th></tr>
<tr><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/grounding/location_00004.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_axial_lung_window`; CT; Axial lung window
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[175, 187, 490, 558]`
- **Maximum IoU：** 0.458; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_axial_lung_window_f01`; `[175, 226, 675, 656]` | 0.458 | no | The right upper lobe demonstrates a large cavitary lesion with surrounding consolidation. There is also a smaller cavitary lesion in the left upper lobe. The remaining lung parenchyma appears relatively clear. No pleural effusions or pneumothorax are identified. The mediastinal structures appear unremarkable. |
| `study_001_ct_image_001_axial_lung_window_f02`; `[588, 272, 937, 712]` | 0.000 | no | The lungs are hyperinflated. There is a large right pneumothorax with collapse of the right lung. The left lung appears normal. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00005: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_x_ray_image_000_frontal_f01</th></tr>
<tr><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/images/study_002_x_ray_image_000_frontal.jpg" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_002_x_ray_image_000_frontal_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_x_ray_image_000_frontal`; X-ray; Frontal
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_x_ray_image_000_frontal_f01`; `[125, 476, 382, 894]` | n/a | n/a | The lungs are hyperinflated. There is increased opacity in the right lower lung zone. The heart size is normal. The mediastinal contour is normal. There is no pneumothorax. There is no pleural effusion. |

### Anchor 3: `study_001_ct_image_000_coronal_lung_window_f02`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f02.png" width="420">

**Anchor Lingshu caption：** The right upper lobe demonstrates a large cavitary lesion with surrounding consolidation. There is also a smaller cavitary lesion in the right lower lobe. The left lung appears clear.

#### location_00006: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_001_axial_lung_window_f01</th><th>Existing target bbox: study_001_ct_image_001_axial_lung_window_f02</th></tr>
<tr><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f02.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/grounding/location_00006.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_axial_lung_window`; CT; Axial lung window
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[180, 134, 500, 450]`
- **Maximum IoU：** 0.293; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_axial_lung_window_f01`; `[175, 226, 675, 656]` | 0.293 | no | The right upper lobe demonstrates a large cavitary lesion with surrounding consolidation. There is also a smaller cavitary lesion in the left upper lobe. The remaining lung parenchyma appears relatively clear. No pleural effusions or pneumothorax are identified. The mediastinal structures appear unremarkable. |
| `study_001_ct_image_001_axial_lung_window_f02`; `[588, 272, 937, 712]` | 0.000 | no | The lungs are hyperinflated. There is a large right pneumothorax with collapse of the right lung. The left lung appears normal. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00007: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_x_ray_image_000_frontal_f01</th></tr>
<tr><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f02.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/images/study_002_x_ray_image_000_frontal.jpg" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_002_x_ray_image_000_frontal_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_x_ray_image_000_frontal`; X-ray; Frontal
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_x_ray_image_000_frontal_f01`; `[125, 476, 382, 894]` | n/a | n/a | The lungs are hyperinflated. There is increased opacity in the right lower lung zone. The heart size is normal. The mediastinal contour is normal. There is no pneumothorax. There is no pleural effusion. |

### Anchor 4: `study_001_ct_image_000_coronal_lung_window_f03`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f03.png" width="420">

**Anchor Lingshu caption：** The left lung is well inflated with no areas of focal consolidation, pleural effusion, or pneumothorax identified. The pulmonary vasculature is within normal limits. There is no evidence of hilar lymphadenopathy.

#### location_00008: STRONG SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_001_axial_lung_window_f01</th><th>Existing target bbox: study_001_ct_image_001_axial_lung_window_f02</th></tr>
<tr><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f03.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/grounding/location_00008.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_axial_lung_window`; CT; Axial lung window
- **Relation：** `bbox_to_bbox` / `strong_support`
- **Returned target bbox：** `[480, 300, 880, 700]`
- **Maximum IoU：** 0.594; threshold=0.5
- **Strong relation IDs：** `[&#x27;strong_location_00008_01&#x27;]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_axial_lung_window_f01`; `[175, 226, 675, 656]` | 0.227 | no | The right upper lobe demonstrates a large cavitary lesion with surrounding consolidation. There is also a smaller cavitary lesion in the left upper lobe. The remaining lung parenchyma appears relatively clear. No pleural effusions or pneumothorax are identified. The mediastinal structures appear unremarkable. |
| `study_001_ct_image_001_axial_lung_window_f02`; `[588, 272, 937, 712]` | 0.594 | yes | The lungs are hyperinflated. There is a large right pneumothorax with collapse of the right lung. The left lung appears normal. |

#### location_00009: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_x_ray_image_000_frontal_f01</th></tr>
<tr><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_000_coronal_lung_window_f03.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/grounding/location_00009.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_002_x_ray_image_000_frontal_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_x_ray_image_000_frontal`; X-ray; Frontal
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[574, 114, 876, 874]`
- **Maximum IoU：** 0.000; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_x_ray_image_000_frontal_f01`; `[125, 476, 382, 894]` | 0.000 | no | The lungs are hyperinflated. There is increased opacity in the right lower lung zone. The heart size is normal. The mediastinal contour is normal. There is no pneumothorax. There is no pleural effusion. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

### Anchor 5: `study_001_ct_image_001_axial_lung_window_f01`

<img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f01.png" width="420">

**Anchor Lingshu caption：** The right upper lobe demonstrates a large cavitary lesion with surrounding consolidation. There is also a smaller cavitary lesion in the left upper lobe. The remaining lung parenchyma appears relatively clear. No pleural effusions or pneumothorax are identified. The mediastinal structures appear unremarkable.

#### location_00010: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_x_ray_image_000_frontal_f01</th></tr>
<tr><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_001_ct_image_001_axial_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/images/study_002_x_ray_image_000_frontal.jpg" width="300"></td><td><img src="../assets_step3/loculated-pneumothorax/nodes/study_002_x_ray_image_000_frontal_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_x_ray_image_000_frontal`; X-ray; Frontal
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_x_ray_image_000_frontal_f01`; `[125, 476, 382, 894]` | n/a | n/a | The lungs are hyperinflated. There is increased opacity in the right lower lung zone. The heart size is normal. The mediastinal contour is normal. There is no pneumothorax. There is no pleural effusion. |

## Dynamically Skipped Anchors

| Anchor node | Reused strong relations | Skipped target images |
|---|---|---|
| `study_001_ct_image_001_axial_lung_window_f02` | `[&#x27;strong_location_00008_01&#x27;]` | `[&#x27;study_002_x_ray_image_000_frontal&#x27;]` |
