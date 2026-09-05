# Morgagni hernia

[返回 Step 3 总览](../README_STEP3_VISUALIZATION.md)

- **Case ID：** `morgagni-hernia-8`
- **Case URL：** [https://radiopaedia.org/cases/morgagni-hernia-8?lang=us](https://radiopaedia.org/cases/morgagni-hernia-8?lang=us)
- **验证模型：** Qwen3-VL-8B
- **图像 / Step 2 findings：** 5 / 1
- **定位结果：** strong 0；partial 1；not support 2；parse error 0
- **Strong bbox relations：** 0
- **原始 JSON：** [case_evidence.json](../assets_step3/morgagni-hernia-8/case_evidence.json)

**Overlay 图例：** 红框为跨图新定位；绿框为 IoU >= 0.5 的已有 bbox；黄框为未达到阈值的已有 bbox。

## Step 2 Finding Nodes

### Finding 1: `study_000_x_ray_image_001_lateral_f01`

<img src="../assets_step3/morgagni-hernia-8/nodes/study_000_x_ray_image_001_lateral_f01.png" width="420">

- **Modality / subcategory：** X-ray / Lateral
- **bbox_2d：** `[150, 100, 700, 900]`
- **Lingshu caption：** The lungs are clear bilaterally. Specifically, no evidence of focal consolidation, pneumothorax, or pleural effusion. Cardiomediastinal silhouette is unremarkable. Visualized osseous structures of the thorax are without acute abnormality.

## Directed Cross-image Validation

### Anchor 1: `study_000_x_ray_image_001_lateral_f01`

<img src="../assets_step3/morgagni-hernia-8/nodes/study_000_x_ray_image_001_lateral_f01.png" width="420">

**Anchor Lingshu caption：** The lungs are clear bilaterally. Specifically, no evidence of focal consolidation, pneumothorax, or pleural effusion. Cardiomediastinal silhouette is unremarkable. Visualized osseous structures of the thorax are without acute abnormality.

#### location_00001: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/morgagni-hernia-8/nodes/study_000_x_ray_image_001_lateral_f01.png" width="300"></td><td><img src="../assets_step3/morgagni-hernia-8/images/study_001_ct_image_000_axial_non_contrast.jpeg" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_000_axial_non_contrast`; CT; Axial non-contrast
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

#### location_00002: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th></tr>
<tr><td><img src="../assets_step3/morgagni-hernia-8/nodes/study_000_x_ray_image_001_lateral_f01.png" width="300"></td><td><img src="../assets_step3/morgagni-hernia-8/grounding/location_00002.png" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_001_sagittal_non_contrast`; CT; Sagittal non-contrast
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[136, 109, 458, 768]`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00003: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/morgagni-hernia-8/nodes/study_000_x_ray_image_001_lateral_f01.png" width="300"></td><td><img src="../assets_step3/morgagni-hernia-8/images/study_001_ct_image_002_coronal_non_contrast.jpeg" width="300"></td></tr>
</table>

- **Target：** `study_001_ct_image_002_coronal_non_contrast`; CT; Coronal non-contrast
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

## Dynamically Skipped Anchors

None.

## Case-level Location Validation Summary / 病例级定位验证总结

- **Strong support：** 0 个 bbox-to-bbox 关系
- **Partial support：** 1 个 bbox-to-image 关系
- **Not support：** 2 个 bbox-to-image 关系

### Strong Support

该病例没有 strong-support bbox 对应关系。

### Partial Support

#### Partial 1: `study_000_x_ray_image_001_lateral_f01` → `study_001_ct_image_001_sagittal_non_contrast`

- **Query：** `location_00002`
- **Returned target bbox：** `[136, 109, 458, 768]`
- **Maximum IoU：** n/a（低于 threshold=0.5）

<table>
<tr><th>Anchor bbox</th><th>Cross-image grounded target bbox</th></tr>
<tr><td><img src="../assets_step3/morgagni-hernia-8/nodes/study_000_x_ray_image_001_lateral_f01.png" width="320"></td><td><img src="../assets_step3/morgagni-hernia-8/grounding/location_00002.png" width="320"></td></tr>
</table>

### Not Support

#### Not support 1: `study_000_x_ray_image_001_lateral_f01` → `study_001_ct_image_000_axial_non_contrast`

- **Query：** `location_00001`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/morgagni-hernia-8/nodes/study_000_x_ray_image_001_lateral_f01.png" width="340"></td><td><img src="../assets_step3/morgagni-hernia-8/images/study_001_ct_image_000_axial_non_contrast.jpeg" width="340"></td></tr>
</table>

#### Not support 2: `study_000_x_ray_image_001_lateral_f01` → `study_001_ct_image_002_coronal_non_contrast`

- **Query：** `location_00003`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/morgagni-hernia-8/nodes/study_000_x_ray_image_001_lateral_f01.png" width="340"></td><td><img src="../assets_step3/morgagni-hernia-8/images/study_001_ct_image_002_coronal_non_contrast.jpeg" width="340"></td></tr>
</table>
