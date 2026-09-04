# Insulinoma

[返回 Step 3 总览](../README_STEP3_VISUALIZATION.md)

- **Case ID：** `insulinoma-3`
- **Case URL：** [https://radiopaedia.org/cases/insulinoma-3?lang=us](https://radiopaedia.org/cases/insulinoma-3?lang=us)
- **验证模型：** Qwen3-VL-8B
- **图像 / Step 2 findings：** 8 / 5
- **定位结果：** strong 0；partial 3；not support 20；parse error 0
- **Strong bbox relations：** 0
- **原始 JSON：** [case_evidence.json](../assets_step3/insulinoma-3/case_evidence.json)

**Overlay 图例：** 红框为跨图新定位；绿框为 IoU >= 0.5 的已有 bbox；黄框为未达到阈值的已有 bbox。

## Step 2 Finding Nodes

### Finding 1: `study_000_ct_image_000_axial_non_contrast_f01`

<img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_000_axial_non_contrast_f01.png" width="420">

- **Modality / subcategory：** CT / Axial non-contrast
- **bbox_2d：** `[240, 180, 760, 460]`
- **Lingshu caption：** The liver is enlarged and contains multiple hypodense lesions. The largest lesion measures approximately 3.5 cm and is located in segment 4. There is also a smaller lesion measuring approximately 1.5 cm in segment 2.

### Finding 2: `study_000_ct_image_001_axial_c_arterial_phase_f01`

<img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_001_axial_c_arterial_phase_f01.png" width="420">

- **Modality / subcategory：** CT / Axial C+ arterial phase
- **bbox_2d：** `[300, 300, 700, 600]`
- **Lingshu caption：** The liver is enlarged and contains multiple hypodense lesions. The largest lesion measures 2.5 cm and is located in segment 4. There is also a smaller lesion measuring 1.3 cm in segment 8. These lesions demonstrate peripheral enhancement on the arterial phase.

### Finding 3: `study_001_mri_image_000_axial_t2_fat_sat_f01`

<img src="../assets_step3/insulinoma-3/nodes/study_001_mri_image_000_axial_t2_fat_sat_f01.png" width="420">

- **Modality / subcategory：** MRI / Axial T2 fat sat
- **bbox_2d：** `[375, 150, 725, 500]`
- **Lingshu caption：** The liver is enlarged and demonstrates diffuse abnormal signal intensity, which is heterogeneous. The spleen is also enlarged. There is a small amount of fluid in the right upper quadrant.

### Finding 4: `study_002_dsa_angiography_image_000_splenic_artery_f01`

<img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_000_splenic_artery_f01.png" width="420">

- **Modality / subcategory：** DSA (angiography) / Splenic artery
- **bbox_2d：** `[320, 380, 680, 580]`
- **Lingshu caption：** The splenic artery is visualized on this angiogram. There is a focal area of narrowing followed by dilation in the proximal portion of the splenic artery. The remainder of the splenic artery appears to have normal caliber.

### Finding 5: `study_002_dsa_angiography_image_001_hepatic_artery_f01`

<img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_001_hepatic_artery_f01.png" width="420">

- **Modality / subcategory：** DSA (angiography) / Hepatic artery
- **bbox_2d：** `[220, 250, 650, 580]`
- **Lingshu caption：** The image shows a hepatic artery with a clear branching pattern. Within the boxed region, there appears to be a focal area of irregularity or narrowing along one of the arterial branches. This could potentially represent a stenosis or other vascular abnormality affecting the hepatic arterial supply. The surrounding vasculature appears otherwise unremarkable.

## Directed Cross-image Validation

### Anchor 1: `study_000_ct_image_000_axial_non_contrast_f01`

<img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_000_axial_non_contrast_f01.png" width="420">

**Anchor Lingshu caption：** The liver is enlarged and contains multiple hypodense lesions. The largest lesion measures approximately 3.5 cm and is located in segment 4. There is also a smaller lesion measuring approximately 1.5 cm in segment 2.

#### location_00001: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_000_ct_image_001_axial_c_arterial_phase_f01</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_000_axial_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/grounding/location_00001.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_001_axial_c_arterial_phase_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_000_ct_image_001_axial_c_arterial_phase`; CT; Axial C+ arterial phase
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[200, 100, 700, 400]`
- **Maximum IoU：** 0.179; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_000_ct_image_001_axial_c_arterial_phase_f01`; `[300, 300, 700, 600]` | 0.179 | no | The liver is enlarged and contains multiple hypodense lesions. The largest lesion measures 2.5 cm and is located in segment 4. There is also a smaller lesion measuring 1.3 cm in segment 8. These lesions demonstrate peripheral enhancement on the arterial phase. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00002: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_mri_image_000_axial_t2_fat_sat_f01</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_000_axial_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/grounding/location_00002.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/nodes/study_001_mri_image_000_axial_t2_fat_sat_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_mri_image_000_axial_t2_fat_sat`; MRI; Axial T2 fat sat
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[320, 260, 680, 580]`
- **Maximum IoU：** 0.447; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_mri_image_000_axial_t2_fat_sat_f01`; `[375, 150, 725, 500]` | 0.447 | no | The liver is enlarged and demonstrates diffuse abnormal signal intensity, which is heterogeneous. The spleen is also enlarged. There is a small amount of fluid in the right upper quadrant. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00003: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_000_axial_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_001_mri_image_001_coronal_t2_fat_sat.jpg" width="300"></td></tr>
</table>

- **Target：** `study_001_mri_image_001_coronal_t2_fat_sat`; MRI; Coronal T2 fat sat
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

#### location_00004: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_dsa_angiography_image_000_splenic_artery_f01</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_000_axial_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_000_splenic_artery.jpg" width="300"></td><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_000_splenic_artery_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_000_splenic_artery`; DSA (angiography); Splenic artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_dsa_angiography_image_000_splenic_artery_f01`; `[320, 380, 680, 580]` | n/a | n/a | The splenic artery is visualized on this angiogram. There is a focal area of narrowing followed by dilation in the proximal portion of the splenic artery. The remainder of the splenic artery appears to have normal caliber. |

#### location_00005: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_dsa_angiography_image_001_hepatic_artery_f01</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_000_axial_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_001_hepatic_artery.jpg" width="300"></td><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_001_hepatic_artery_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_001_hepatic_artery`; DSA (angiography); Hepatic artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_dsa_angiography_image_001_hepatic_artery_f01`; `[220, 250, 650, 580]` | n/a | n/a | The image shows a hepatic artery with a clear branching pattern. Within the boxed region, there appears to be a focal area of irregularity or narrowing along one of the arterial branches. This could potentially represent a stenosis or other vascular abnormality affecting the hepatic arterial supply. The surrounding vasculature appears otherwise unremarkable. |

#### location_00006: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_000_axial_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_002_superior_mesenteric_artery.jpg" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_002_superior_mesenteric_artery`; DSA (angiography); Superior mesenteric artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

#### location_00007: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_000_axial_non_contrast_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_003_right_hepatic_vein.jpg" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_003_right_hepatic_vein`; DSA (angiography); Right hepatic vein
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

### Anchor 2: `study_000_ct_image_001_axial_c_arterial_phase_f01`

<img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_001_axial_c_arterial_phase_f01.png" width="420">

**Anchor Lingshu caption：** The liver is enlarged and contains multiple hypodense lesions. The largest lesion measures 2.5 cm and is located in segment 4. There is also a smaller lesion measuring 1.3 cm in segment 8. These lesions demonstrate peripheral enhancement on the arterial phase.

#### location_00008: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_mri_image_000_axial_t2_fat_sat_f01</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_001_axial_c_arterial_phase_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/grounding/location_00008.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/nodes/study_001_mri_image_000_axial_t2_fat_sat_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_mri_image_000_axial_t2_fat_sat`; MRI; Axial T2 fat sat
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[350, 300, 650, 550]`
- **Maximum IoU：** 0.394; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_mri_image_000_axial_t2_fat_sat_f01`; `[375, 150, 725, 500]` | 0.394 | no | The liver is enlarged and demonstrates diffuse abnormal signal intensity, which is heterogeneous. The spleen is also enlarged. There is a small amount of fluid in the right upper quadrant. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00009: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_001_axial_c_arterial_phase_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_001_mri_image_001_coronal_t2_fat_sat.jpg" width="300"></td></tr>
</table>

- **Target：** `study_001_mri_image_001_coronal_t2_fat_sat`; MRI; Coronal T2 fat sat
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

#### location_00010: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_dsa_angiography_image_000_splenic_artery_f01</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_001_axial_c_arterial_phase_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_000_splenic_artery.jpg" width="300"></td><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_000_splenic_artery_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_000_splenic_artery`; DSA (angiography); Splenic artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_dsa_angiography_image_000_splenic_artery_f01`; `[320, 380, 680, 580]` | n/a | n/a | The splenic artery is visualized on this angiogram. There is a focal area of narrowing followed by dilation in the proximal portion of the splenic artery. The remainder of the splenic artery appears to have normal caliber. |

#### location_00011: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_dsa_angiography_image_001_hepatic_artery_f01</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_001_axial_c_arterial_phase_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_001_hepatic_artery.jpg" width="300"></td><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_001_hepatic_artery_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_001_hepatic_artery`; DSA (angiography); Hepatic artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_dsa_angiography_image_001_hepatic_artery_f01`; `[220, 250, 650, 580]` | n/a | n/a | The image shows a hepatic artery with a clear branching pattern. Within the boxed region, there appears to be a focal area of irregularity or narrowing along one of the arterial branches. This could potentially represent a stenosis or other vascular abnormality affecting the hepatic arterial supply. The surrounding vasculature appears otherwise unremarkable. |

#### location_00012: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_001_axial_c_arterial_phase_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_002_superior_mesenteric_artery.jpg" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_002_superior_mesenteric_artery`; DSA (angiography); Superior mesenteric artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

#### location_00013: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_000_ct_image_001_axial_c_arterial_phase_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_003_right_hepatic_vein.jpg" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_003_right_hepatic_vein`; DSA (angiography); Right hepatic vein
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

### Anchor 3: `study_001_mri_image_000_axial_t2_fat_sat_f01`

<img src="../assets_step3/insulinoma-3/nodes/study_001_mri_image_000_axial_t2_fat_sat_f01.png" width="420">

**Anchor Lingshu caption：** The liver is enlarged and demonstrates diffuse abnormal signal intensity, which is heterogeneous. The spleen is also enlarged. There is a small amount of fluid in the right upper quadrant.

#### location_00014: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_001_mri_image_000_axial_t2_fat_sat_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_001_mri_image_001_coronal_t2_fat_sat.jpg" width="300"></td></tr>
</table>

- **Target：** `study_001_mri_image_001_coronal_t2_fat_sat`; MRI; Coronal T2 fat sat
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

#### location_00015: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_dsa_angiography_image_000_splenic_artery_f01</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_001_mri_image_000_axial_t2_fat_sat_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_000_splenic_artery.jpg" width="300"></td><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_000_splenic_artery_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_000_splenic_artery`; DSA (angiography); Splenic artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_dsa_angiography_image_000_splenic_artery_f01`; `[320, 380, 680, 580]` | n/a | n/a | The splenic artery is visualized on this angiogram. There is a focal area of narrowing followed by dilation in the proximal portion of the splenic artery. The remainder of the splenic artery appears to have normal caliber. |

#### location_00016: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_dsa_angiography_image_001_hepatic_artery_f01</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_001_mri_image_000_axial_t2_fat_sat_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_001_hepatic_artery.jpg" width="300"></td><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_001_hepatic_artery_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_001_hepatic_artery`; DSA (angiography); Hepatic artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_dsa_angiography_image_001_hepatic_artery_f01`; `[220, 250, 650, 580]` | n/a | n/a | The image shows a hepatic artery with a clear branching pattern. Within the boxed region, there appears to be a focal area of irregularity or narrowing along one of the arterial branches. This could potentially represent a stenosis or other vascular abnormality affecting the hepatic arterial supply. The surrounding vasculature appears otherwise unremarkable. |

#### location_00017: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_001_mri_image_000_axial_t2_fat_sat_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_002_superior_mesenteric_artery.jpg" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_002_superior_mesenteric_artery`; DSA (angiography); Superior mesenteric artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

#### location_00018: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_001_mri_image_000_axial_t2_fat_sat_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_003_right_hepatic_vein.jpg" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_003_right_hepatic_vein`; DSA (angiography); Right hepatic vein
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

### Anchor 4: `study_002_dsa_angiography_image_000_splenic_artery_f01`

<img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_000_splenic_artery_f01.png" width="420">

**Anchor Lingshu caption：** The splenic artery is visualized on this angiogram. There is a focal area of narrowing followed by dilation in the proximal portion of the splenic artery. The remainder of the splenic artery appears to have normal caliber.

#### location_00019: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_dsa_angiography_image_001_hepatic_artery_f01</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_000_splenic_artery_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_001_hepatic_artery.jpg" width="300"></td><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_001_hepatic_artery_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_001_hepatic_artery`; DSA (angiography); Hepatic artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_dsa_angiography_image_001_hepatic_artery_f01`; `[220, 250, 650, 580]` | n/a | n/a | The image shows a hepatic artery with a clear branching pattern. Within the boxed region, there appears to be a focal area of irregularity or narrowing along one of the arterial branches. This could potentially represent a stenosis or other vascular abnormality affecting the hepatic arterial supply. The surrounding vasculature appears otherwise unremarkable. |

#### location_00020: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_000_splenic_artery_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_002_superior_mesenteric_artery.jpg" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_002_superior_mesenteric_artery`; DSA (angiography); Superior mesenteric artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

#### location_00021: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_000_splenic_artery_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_003_right_hepatic_vein.jpg" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_003_right_hepatic_vein`; DSA (angiography); Right hepatic vein
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

### Anchor 5: `study_002_dsa_angiography_image_001_hepatic_artery_f01`

<img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_001_hepatic_artery_f01.png" width="420">

**Anchor Lingshu caption：** The image shows a hepatic artery with a clear branching pattern. Within the boxed region, there appears to be a focal area of irregularity or narrowing along one of the arterial branches. This could potentially represent a stenosis or other vascular abnormality affecting the hepatic arterial supply. The surrounding vasculature appears otherwise unremarkable.

#### location_00022: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_001_hepatic_artery_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_002_superior_mesenteric_artery.jpg" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_002_superior_mesenteric_artery`; DSA (angiography); Superior mesenteric artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

#### location_00023: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th></tr>
<tr><td><img src="../assets_step3/insulinoma-3/nodes/study_002_dsa_angiography_image_001_hepatic_artery_f01.png" width="300"></td><td><img src="../assets_step3/insulinoma-3/images/study_002_dsa_angiography_image_003_right_hepatic_vein.jpg" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_003_right_hepatic_vein`; DSA (angiography); Right hepatic vein
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

The target image has no existing Step 2 bbox.

## Dynamically Skipped Anchors

None.
