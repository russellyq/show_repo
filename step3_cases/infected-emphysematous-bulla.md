# Infected emphysematous bulla

[返回 Step 3 总览](../README_STEP3_VISUALIZATION.md)

- **Case ID：** `infected-emphysematous-bulla`
- **Case URL：** [https://radiopaedia.org/cases/infected-emphysematous-bulla?lang=us](https://radiopaedia.org/cases/infected-emphysematous-bulla?lang=us)
- **验证模型：** Qwen3-VL-8B
- **图像 / Step 2 findings：** 4 / 4
- **定位结果：** strong 2；partial 1；not support 3；parse error 0
- **Strong bbox relations：** 2
- **原始 JSON：** [case_evidence.json](../assets_step3/infected-emphysematous-bulla/case_evidence.json)

**Overlay 图例：** 红框为跨图新定位；绿框为 IoU >= 0.5 的已有 bbox；黄框为未达到阈值的已有 bbox。

## Step 2 Finding Nodes

### Finding 1: `study_000_x_ray_image_000_frontal_f01`

<img src="../assets_step3/infected-emphysematous-bulla/nodes/study_000_x_ray_image_000_frontal_f01.png" width="420">

- **Modality / subcategory：** X-ray / Frontal
- **bbox_2d：** `[175, 408, 362, 530]`
- **Lingshu caption：** The lungs are hyperinflated. There is a 1.5 cm rounded opacity projecting over the right mid lung zone. No pleural effusion or pneumothorax is seen. The cardiac and mediastinal silhouettes are unremarkable.

### Finding 2: `study_000_x_ray_image_001_lateral_f01`

<img src="../assets_step3/infected-emphysematous-bulla/nodes/study_000_x_ray_image_001_lateral_f01.png" width="420">

- **Modality / subcategory：** X-ray / Lateral
- **bbox_2d：** `[436, 362, 639, 538]`
- **Lingshu caption：** The heart size is enlarged. The aorta is tortuous. There is a calcified lesion overlying the cardiac silhouette. This could represent a calcified lymph node or other calcification.

### Finding 3: `study_001_ct_image_000_axial_lung_window_f01`

<img src="../assets_step3/infected-emphysematous-bulla/nodes/study_001_ct_image_000_axial_lung_window_f01.png" width="420">

- **Modality / subcategory：** CT / Axial lung window
- **bbox_2d：** `[185, 552, 444, 721]`
- **Lingshu caption：** The right lower lobe contains a large cystic structure with thin walls. The remainder of the lungs are clear without focal consolidation, pleural effusion, or pneumothorax. The cardiomediastinal silhouette is normal.

### Finding 4: `study_001_ct_image_001_coronal_lung_window_f01`

<img src="../assets_step3/infected-emphysematous-bulla/nodes/study_001_ct_image_001_coronal_lung_window_f01.png" width="420">

- **Modality / subcategory：** CT / Coronal lung window
- **bbox_2d：** `[210, 256, 464, 444]`
- **Lingshu caption：** The lungs are hyperinflated. There is a large cavitary lesion in the right upper lobe with thick irregular walls. The remainder of the lungs demonstrate emphysematous changes. No pleural effusions are seen.

## Directed Cross-image Validation

### Anchor 1: `study_000_x_ray_image_000_frontal_f01`

<img src="../assets_step3/infected-emphysematous-bulla/nodes/study_000_x_ray_image_000_frontal_f01.png" width="420">

**Anchor Lingshu caption：** The lungs are hyperinflated. There is a 1.5 cm rounded opacity projecting over the right mid lung zone. No pleural effusion or pneumothorax is seen. The cardiac and mediastinal silhouettes are unremarkable.

#### location_00001: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_000_x_ray_image_001_lateral_f01</th></tr>
<tr><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_000_x_ray_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/grounding/location_00001.png" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_000_x_ray_image_001_lateral_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_000_x_ray_image_001_lateral`; X-ray; Lateral
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[236, 328, 460, 555]`
- **Maximum IoU：** 0.051; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_000_x_ray_image_001_lateral_f01`; `[436, 362, 639, 538]` | 0.051 | no | The heart size is enlarged. The aorta is tortuous. There is a calcified lesion overlying the cardiac silhouette. This could represent a calcified lymph node or other calcification. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00002: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_ct_image_000_axial_lung_window_f01</th></tr>
<tr><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_000_x_ray_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/images/study_001_ct_image_000_axial_lung_window.jpg" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_001_ct_image_000_axial_lung_window_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_000_axial_lung_window`; CT; Axial lung window
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_000_axial_lung_window_f01`; `[185, 552, 444, 721]` | n/a | n/a | The right lower lobe contains a large cystic structure with thin walls. The remainder of the lungs are clear without focal consolidation, pleural effusion, or pneumothorax. The cardiomediastinal silhouette is normal. |

#### location_00003: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_ct_image_001_coronal_lung_window_f01</th></tr>
<tr><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_000_x_ray_image_000_frontal_f01.png" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/images/study_001_ct_image_001_coronal_lung_window.jpg" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_001_ct_image_001_coronal_lung_window_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_coronal_lung_window`; CT; Coronal lung window
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_coronal_lung_window_f01`; `[210, 256, 464, 444]` | n/a | n/a | The lungs are hyperinflated. There is a large cavitary lesion in the right upper lobe with thick irregular walls. The remainder of the lungs demonstrate emphysematous changes. No pleural effusions are seen. |

### Anchor 2: `study_000_x_ray_image_001_lateral_f01`

<img src="../assets_step3/infected-emphysematous-bulla/nodes/study_000_x_ray_image_001_lateral_f01.png" width="420">

**Anchor Lingshu caption：** The heart size is enlarged. The aorta is tortuous. There is a calcified lesion overlying the cardiac silhouette. This could represent a calcified lymph node or other calcification.

#### location_00004: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_ct_image_000_axial_lung_window_f01</th></tr>
<tr><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_000_x_ray_image_001_lateral_f01.png" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/images/study_001_ct_image_000_axial_lung_window.jpg" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_001_ct_image_000_axial_lung_window_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_000_axial_lung_window`; CT; Axial lung window
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_000_axial_lung_window_f01`; `[185, 552, 444, 721]` | n/a | n/a | The right lower lobe contains a large cystic structure with thin walls. The remainder of the lungs are clear without focal consolidation, pleural effusion, or pneumothorax. The cardiomediastinal silhouette is normal. |

#### location_00005: STRONG SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_001_coronal_lung_window_f01</th></tr>
<tr><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_000_x_ray_image_001_lateral_f01.png" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/grounding/location_00005.png" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_001_ct_image_001_coronal_lung_window_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_coronal_lung_window`; CT; Coronal lung window
- **Relation：** `bbox_to_bbox` / `strong_support`
- **Returned target bbox：** `[234, 192, 440, 462]`
- **Maximum IoU：** 0.595; threshold=0.5
- **Strong relation IDs：** `[&#x27;strong_location_00005_01&#x27;]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_coronal_lung_window_f01`; `[210, 256, 464, 444]` | 0.595 | yes | The lungs are hyperinflated. There is a large cavitary lesion in the right upper lobe with thick irregular walls. The remainder of the lungs demonstrate emphysematous changes. No pleural effusions are seen. |

### Anchor 3: `study_001_ct_image_000_axial_lung_window_f01`

<img src="../assets_step3/infected-emphysematous-bulla/nodes/study_001_ct_image_000_axial_lung_window_f01.png" width="420">

**Anchor Lingshu caption：** The right lower lobe contains a large cystic structure with thin walls. The remainder of the lungs are clear without focal consolidation, pleural effusion, or pneumothorax. The cardiomediastinal silhouette is normal.

#### location_00006: STRONG SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_ct_image_001_coronal_lung_window_f01</th></tr>
<tr><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_001_ct_image_000_axial_lung_window_f01.png" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/grounding/location_00006.png" width="300"></td><td><img src="../assets_step3/infected-emphysematous-bulla/nodes/study_001_ct_image_001_coronal_lung_window_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_coronal_lung_window`; CT; Coronal lung window
- **Relation：** `bbox_to_bbox` / `strong_support`
- **Returned target bbox：** `[220, 136, 430, 468]`
- **Maximum IoU：** 0.504; threshold=0.5
- **Strong relation IDs：** `[&#x27;strong_location_00006_01&#x27;]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_ct_image_001_coronal_lung_window_f01`; `[210, 256, 464, 444]` | 0.504 | yes | The lungs are hyperinflated. There is a large cavitary lesion in the right upper lobe with thick irregular walls. The remainder of the lungs demonstrate emphysematous changes. No pleural effusions are seen. |

## Dynamically Skipped Anchors

None.
