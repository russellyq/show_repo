# Aspergilloma

[返回 Step 3 总览](../README_STEP3_VISUALIZATION.md)

- **Case ID：** `aspergilloma-1`
- **Case URL：** [https://radiopaedia.org/cases/aspergilloma-1?lang=us](https://radiopaedia.org/cases/aspergilloma-1?lang=us)
- **验证模型：** Qwen3-VL-8B
- **图像 / Step 2 findings：** 4 / 7
- **定位结果：** strong 2；partial 5；not support 5；parse error 0
- **Strong bbox relations：** 2
- **原始 JSON：** [case_evidence.json](../assets_step3/aspergilloma-1/case_evidence.json)

**Overlay 图例：** 红框为跨图新定位；绿框为 IoU >= 0.5 的已有 bbox；黄框为未达到阈值的已有 bbox。

## Step 2 Finding Nodes

### Finding 1: `study_000_x_ray_image_000_frontal_f01`

<img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f01.png" width="420">

- **Modality / subcategory：** X-ray / Frontal
- **bbox_2d：** `[70, 124, 502, 809]`
- **Lingshu caption：** The lungs are hyperinflated. There is diffuse interstitial thickening bilaterally. The heart size is normal. No pneumothorax or pleural effusion seen.

### Finding 2: `study_000_x_ray_image_000_frontal_f02`

<img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f02.png" width="420">

- **Modality / subcategory：** X-ray / Frontal
- **bbox_2d：** `[587, 124, 952, 824]`
- **Lingshu caption：** The lungs are hyperinflated. There is diffuse interstitial thickening bilaterally. The heart size is normal. No pneumothorax or pleural effusion seen.

### Finding 3: `study_000_x_ray_image_000_frontal_f03`

<img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f03.png" width="420">

- **Modality / subcategory：** X-ray / Frontal
- **bbox_2d：** `[424, 500, 699, 905]`
- **Lingshu caption：** The heart size is enlarged. The mediastinal contours are prominent. There is increased opacity throughout both lungs with more pronounced opacities in the lower lobes bilaterally.

### Finding 4: `study_001_x_ray_image_000_missing_f01`

<img src="../assets_step3/aspergilloma-1/nodes/study_001_x_ray_image_000_missing_f01.png" width="420">

- **Modality / subcategory：** X-ray / missing
- **bbox_2d：** `[0, 845, 274, 1000]`
- **Lingshu caption：** The image shows a chest x-ray with a red box highlighting a specific area. Within this region, there appears to be a foreign object, possibly a medical device or implant, which is not typically present in a normal chest x-ray. The surrounding lung fields appear relatively clear, without any obvious signs of consolidation, effusion, or pneumothorax. The heart size and mediastinal contours seem within normal limits. However, due to the presence of the foreign object, further evaluation may be necessary to determine its nature and potential implications.

### Finding 5: `study_002_ct_image_000_axial_lung_window_f01`

<img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f01.png" width="420">

- **Modality / subcategory：** CT / Axial lung window
- **bbox_2d：** `[200, 390, 500, 660]`
- **Lingshu caption：** The lungs are hyperinflated. There is a large area of consolidation in the right upper lobe. There is also a smaller area of consolidation in the left upper lobe. The mediastinal contours are normal.

### Finding 6: `study_002_ct_image_000_axial_lung_window_f02`

<img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f02.png" width="420">

- **Modality / subcategory：** CT / Axial lung window
- **bbox_2d：** `[641, 410, 826, 628]`
- **Lingshu caption：** The lungs are hyperinflated. There is a large area of consolidation in the left upper lobe. The right upper lobe also shows some areas of consolidation.

### Finding 7: `study_002_ct_image_001_oblique_lung_window_f01`

<img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_001_oblique_lung_window_f01.png" width="420">

- **Modality / subcategory：** CT / Oblique lung window
- **bbox_2d：** `[250, 100, 750, 800]`
- **Lingshu caption：** The lungs are hyperinflated. There is diffuse bronchiectasis and bronchial wall thickening. There is also diffuse ground glass opacity.

## Directed Cross-image Validation

### Anchor 1: `study_000_x_ray_image_000_frontal_f01`

<img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f01.png" width="420">

**Anchor Lingshu caption：** The lungs are hyperinflated. There is diffuse interstitial thickening bilaterally. The heart size is normal. No pneumothorax or pleural effusion seen.

#### location_00001: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_x_ray_image_000_missing_f01</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/grounding/location_00001.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_001_x_ray_image_000_missing_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_x_ray_image_000_missing`; X-ray; missing
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[0, 720, 342, 1000]`
- **Maximum IoU：** 0.443; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_x_ray_image_000_missing_f01`; `[0, 845, 274, 1000]` | 0.443 | no | The image shows a chest x-ray with a red box highlighting a specific area. Within this region, there appears to be a foreign object, possibly a medical device or implant, which is not typically present in a normal chest x-ray. The surrounding lung fields appear relatively clear, without any obvious signs of consolidation, effusion, or pneumothorax. The heart size and mediastinal contours seem within normal limits. However, due to the presence of the foreign object, further evaluation may be necessary to determine its nature and potential implications. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00002: STRONG SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_ct_image_000_axial_lung_window_f01</th><th>Existing target bbox: study_002_ct_image_000_axial_lung_window_f02</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/grounding/location_00002.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_000_axial_lung_window`; CT; Axial lung window
- **Relation：** `bbox_to_bbox` / `strong_support`
- **Returned target bbox：** `[180, 350, 465, 650]`
- **Maximum IoU：** 0.703; threshold=0.5
- **Strong relation IDs：** `[&#x27;strong_location_00002_01&#x27;]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_000_axial_lung_window_f01`; `[200, 390, 500, 660]` | 0.703 | yes | The lungs are hyperinflated. There is a large area of consolidation in the right upper lobe. There is also a smaller area of consolidation in the left upper lobe. The mediastinal contours are normal. |
| `study_002_ct_image_000_axial_lung_window_f02`; `[641, 410, 826, 628]` | 0.000 | no | The lungs are hyperinflated. There is a large area of consolidation in the left upper lobe. The right upper lobe also shows some areas of consolidation. |

#### location_00003: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_ct_image_001_oblique_lung_window_f01</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/grounding/location_00003.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_001_oblique_lung_window_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_001_oblique_lung_window`; CT; Oblique lung window
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[157, 157, 400, 850]`
- **Maximum IoU：** 0.224; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_001_oblique_lung_window_f01`; `[250, 100, 750, 800]` | 0.224 | no | The lungs are hyperinflated. There is diffuse bronchiectasis and bronchial wall thickening. There is also diffuse ground glass opacity. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

### Anchor 2: `study_000_x_ray_image_000_frontal_f02`

<img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f02.png" width="420">

**Anchor Lingshu caption：** The lungs are hyperinflated. There is diffuse interstitial thickening bilaterally. The heart size is normal. No pneumothorax or pleural effusion seen.

#### location_00004: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_x_ray_image_000_missing_f01</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f02.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/images/study_001_x_ray_image_000_missing.jpg" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_001_x_ray_image_000_missing_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_x_ray_image_000_missing`; X-ray; missing
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_x_ray_image_000_missing_f01`; `[0, 845, 274, 1000]` | n/a | n/a | The image shows a chest x-ray with a red box highlighting a specific area. Within this region, there appears to be a foreign object, possibly a medical device or implant, which is not typically present in a normal chest x-ray. The surrounding lung fields appear relatively clear, without any obvious signs of consolidation, effusion, or pneumothorax. The heart size and mediastinal contours seem within normal limits. However, due to the presence of the foreign object, further evaluation may be necessary to determine its nature and potential implications. |

#### location_00005: STRONG SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_ct_image_000_axial_lung_window_f01</th><th>Existing target bbox: study_002_ct_image_000_axial_lung_window_f02</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f02.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/grounding/location_00005.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_000_axial_lung_window`; CT; Axial lung window
- **Relation：** `bbox_to_bbox` / `strong_support`
- **Returned target bbox：** `[200, 350, 450, 650]`
- **Maximum IoU：** 0.714; threshold=0.5
- **Strong relation IDs：** `[&#x27;strong_location_00005_01&#x27;]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_000_axial_lung_window_f01`; `[200, 390, 500, 660]` | 0.714 | yes | The lungs are hyperinflated. There is a large area of consolidation in the right upper lobe. There is also a smaller area of consolidation in the left upper lobe. The mediastinal contours are normal. |
| `study_002_ct_image_000_axial_lung_window_f02`; `[641, 410, 826, 628]` | 0.000 | no | The lungs are hyperinflated. There is a large area of consolidation in the left upper lobe. The right upper lobe also shows some areas of consolidation. |

#### location_00006: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_ct_image_001_oblique_lung_window_f01</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f02.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/grounding/location_00006.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_001_oblique_lung_window_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_001_oblique_lung_window`; CT; Oblique lung window
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[187, 100, 480, 800]`
- **Maximum IoU：** 0.400; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_001_oblique_lung_window_f01`; `[250, 100, 750, 800]` | 0.400 | no | The lungs are hyperinflated. There is diffuse bronchiectasis and bronchial wall thickening. There is also diffuse ground glass opacity. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

### Anchor 3: `study_000_x_ray_image_000_frontal_f03`

<img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f03.png" width="420">

**Anchor Lingshu caption：** The heart size is enlarged. The mediastinal contours are prominent. There is increased opacity throughout both lungs with more pronounced opacities in the lower lobes bilaterally.

#### location_00007: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_x_ray_image_000_missing_f01</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f03.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/images/study_001_x_ray_image_000_missing.jpg" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_001_x_ray_image_000_missing_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_x_ray_image_000_missing`; X-ray; missing
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_x_ray_image_000_missing_f01`; `[0, 845, 274, 1000]` | n/a | n/a | The image shows a chest x-ray with a red box highlighting a specific area. Within this region, there appears to be a foreign object, possibly a medical device or implant, which is not typically present in a normal chest x-ray. The surrounding lung fields appear relatively clear, without any obvious signs of consolidation, effusion, or pneumothorax. The heart size and mediastinal contours seem within normal limits. However, due to the presence of the foreign object, further evaluation may be necessary to determine its nature and potential implications. |

#### location_00008: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_ct_image_000_axial_lung_window_f01</th><th>Existing target bbox: study_002_ct_image_000_axial_lung_window_f02</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f03.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/images/study_002_ct_image_000_axial_lung_window.jpg" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_000_axial_lung_window`; CT; Axial lung window
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_000_axial_lung_window_f01`; `[200, 390, 500, 660]` | n/a | n/a | The lungs are hyperinflated. There is a large area of consolidation in the right upper lobe. There is also a smaller area of consolidation in the left upper lobe. The mediastinal contours are normal. |
| `study_002_ct_image_000_axial_lung_window_f02`; `[641, 410, 826, 628]` | n/a | n/a | The lungs are hyperinflated. There is a large area of consolidation in the left upper lobe. The right upper lobe also shows some areas of consolidation. |

#### location_00009: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_ct_image_001_oblique_lung_window_f01</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_000_x_ray_image_000_frontal_f03.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/grounding/location_00009.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_001_oblique_lung_window_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_001_oblique_lung_window`; CT; Oblique lung window
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[184, 184, 548, 732]`
- **Maximum IoU：** 0.417; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_001_oblique_lung_window_f01`; `[250, 100, 750, 800]` | 0.417 | no | The lungs are hyperinflated. There is diffuse bronchiectasis and bronchial wall thickening. There is also diffuse ground glass opacity. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

### Anchor 4: `study_001_x_ray_image_000_missing_f01`

<img src="../assets_step3/aspergilloma-1/nodes/study_001_x_ray_image_000_missing_f01.png" width="420">

**Anchor Lingshu caption：** The image shows a chest x-ray with a red box highlighting a specific area. Within this region, there appears to be a foreign object, possibly a medical device or implant, which is not typically present in a normal chest x-ray. The surrounding lung fields appear relatively clear, without any obvious signs of consolidation, effusion, or pneumothorax. The heart size and mediastinal contours seem within normal limits. However, due to the presence of the foreign object, further evaluation may be necessary to determine its nature and potential implications.

#### location_00010: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_ct_image_000_axial_lung_window_f01</th><th>Existing target bbox: study_002_ct_image_000_axial_lung_window_f02</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_001_x_ray_image_000_missing_f01.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/images/study_002_ct_image_000_axial_lung_window.jpg" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f02.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_000_axial_lung_window`; CT; Axial lung window
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_000_axial_lung_window_f01`; `[200, 390, 500, 660]` | n/a | n/a | The lungs are hyperinflated. There is a large area of consolidation in the right upper lobe. There is also a smaller area of consolidation in the left upper lobe. The mediastinal contours are normal. |
| `study_002_ct_image_000_axial_lung_window_f02`; `[641, 410, 826, 628]` | n/a | n/a | The lungs are hyperinflated. There is a large area of consolidation in the left upper lobe. The right upper lobe also shows some areas of consolidation. |

#### location_00011: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_ct_image_001_oblique_lung_window_f01</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_001_x_ray_image_000_missing_f01.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/images/study_002_ct_image_001_oblique_lung_window.jpg" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_001_oblique_lung_window_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_001_oblique_lung_window`; CT; Oblique lung window
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_001_oblique_lung_window_f01`; `[250, 100, 750, 800]` | n/a | n/a | The lungs are hyperinflated. There is diffuse bronchiectasis and bronchial wall thickening. There is also diffuse ground glass opacity. |

### Anchor 5: `study_002_ct_image_000_axial_lung_window_f02`

<img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f02.png" width="420">

**Anchor Lingshu caption：** The lungs are hyperinflated. There is a large area of consolidation in the left upper lobe. The right upper lobe also shows some areas of consolidation.

#### location_00013: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_002_ct_image_001_oblique_lung_window_f01</th></tr>
<tr><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_000_axial_lung_window_f02.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/grounding/location_00013.png" width="300"></td><td><img src="../assets_step3/aspergilloma-1/nodes/study_002_ct_image_001_oblique_lung_window_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_ct_image_001_oblique_lung_window`; CT; Oblique lung window
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[462, 220, 710, 620]`
- **Maximum IoU：** 0.282; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_ct_image_001_oblique_lung_window_f01`; `[250, 100, 750, 800]` | 0.282 | no | The lungs are hyperinflated. There is diffuse bronchiectasis and bronchial wall thickening. There is also diffuse ground glass opacity. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

## Dynamically Skipped Anchors

| Anchor node | Reused strong relations | Skipped target images |
|---|---|---|
| `study_002_ct_image_000_axial_lung_window_f01` | `[&#x27;strong_location_00002_01&#x27;, &#x27;strong_location_00005_01&#x27;]` | `[&#x27;study_002_ct_image_001_oblique_lung_window&#x27;]` |
