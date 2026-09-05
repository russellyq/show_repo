# Jugulotympanic paraganglioma

[返回 Step 3 总览](../README_STEP3_VISUALIZATION.md)

- **Case ID：** `jugulotympanic-paraganglioma-9`
- **Case URL：** [https://radiopaedia.org/cases/jugulotympanic-paraganglioma-9?lang=us](https://radiopaedia.org/cases/jugulotympanic-paraganglioma-9?lang=us)
- **验证模型：** Qwen3-VL-8B
- **图像 / Step 2 findings：** 4 / 5
- **定位结果：** strong 0；partial 1；not support 8；parse error 0
- **Strong bbox relations：** 0
- **原始 JSON：** [case_evidence.json](../assets_step3/jugulotympanic-paraganglioma-9/case_evidence.json)

**Overlay 图例：** 红框为跨图新定位；绿框为 IoU >= 0.5 的已有 bbox；黄框为未达到阈值的已有 bbox。

## Step 2 Finding Nodes

### Finding 1: `study_000_ct_image_000_axial_bone_window_f01`

<img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f01.png" width="420">

- **Modality / subcategory：** CT / Axial bone window
- **bbox_2d：** `[84, 488, 384, 740]`
- **Lingshu caption：** The right mastoid air cells appear opacified compared to the left side. The right middle ear cavity also appears opacified. There is no definite bony erosion.

### Finding 2: `study_000_ct_image_000_axial_bone_window_f02`

<img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f02.png" width="420">

- **Modality / subcategory：** CT / Axial bone window
- **bbox_2d：** `[718, 544, 924, 738]`
- **Lingshu caption：** The left mastoid air cells appear opacified. The left middle ear cavity also appears opacified. There is no definite bony erosion.

### Finding 3: `study_001_mri_image_000_axial_t1_c_fat_sat_f01`

<img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_000_axial_t1_c_fat_sat_f01.png" width="420">

- **Modality / subcategory：** MRI / Axial T1 C+ fat sat
- **bbox_2d：** `[612, 452, 767, 575]`
- **Lingshu caption：** The left internal auditory canal demonstrates a small enhancing mass. The right internal auditory canal appears normal. The cerebellum, medulla, and pons appear normal. There is no evidence of hydrocephalus.

### Finding 4: `study_001_mri_image_001_coronal_t1_c_f01`

<img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_001_coronal_t1_c_f01.png" width="420">

- **Modality / subcategory：** MRI / Coronal T1 C+
- **bbox_2d：** `[645, 250, 815, 410]`
- **Lingshu caption：** The left carotid artery is enlarged and tortuous. There is a large mass centered at the bifurcation of the left carotid artery. The mass is heterogeneous and contains areas of high signal intensity. The mass extends into the left internal carotid artery and external carotid artery. The mass also extends posteriorly to the left vertebral artery.

### Finding 5: `study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01`

<img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01.png" width="420">

- **Modality / subcategory：** DSA (angiography) / Lateral External carotid artery
- **bbox_2d：** `[530, 120, 784, 520]`
- **Lingshu caption：** The lateral view of the left external carotid artery shows a complex network of vessels with a prominent area of irregularity and possible vascular malformation or abnormal branching within the boxed region. The vessels appear tortuous and there is a notable concentration of contrast material suggesting increased vascularity or potential arteriovenous shunting. The surrounding vasculature appears less dense, providing a stark contrast to the highlighted area.

## Directed Cross-image Validation

### Anchor 1: `study_000_ct_image_000_axial_bone_window_f01`

<img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f01.png" width="420">

**Anchor Lingshu caption：** The right mastoid air cells appear opacified compared to the left side. The right middle ear cavity also appears opacified. There is no definite bony erosion.

#### location_00001: PARTIAL SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Cross-image grounded target bbox</th><th>Existing target bbox: study_001_mri_image_000_axial_t1_c_fat_sat_f01</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f01.png" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/grounding/location_00001.png" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_000_axial_t1_c_fat_sat_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_mri_image_000_axial_t1_c_fat_sat`; MRI; Axial T1 C+ fat sat
- **Relation：** `bbox_to_image` / `partial_support`
- **Returned target bbox：** `[87, 442, 375, 656]`
- **Maximum IoU：** 0.000; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_mri_image_000_axial_t1_c_fat_sat_f01`; `[612, 452, 767, 575]` | 0.000 | no | The left internal auditory canal demonstrates a small enhancing mass. The right internal auditory canal appears normal. The cerebellum, medulla, and pons appear normal. There is no evidence of hydrocephalus. |

**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.

#### location_00002: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_mri_image_001_coronal_t1_c_f01</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f01.png" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_001_mri_image_001_coronal_t1_c.jpeg" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_001_coronal_t1_c_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_mri_image_001_coronal_t1_c`; MRI; Coronal T1 C+
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_mri_image_001_coronal_t1_c_f01`; `[645, 250, 815, 410]` | n/a | n/a | The left carotid artery is enlarged and tortuous. There is a large mass centered at the bifurcation of the left carotid artery. The mass is heterogeneous and contains areas of high signal intensity. The mass extends into the left internal carotid artery and external carotid artery. The mass also extends posteriorly to the left vertebral artery. |

#### location_00003: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f01.png" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_002_dsa_angiography_image_000_lateral_external_carotid_artery.jpeg" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_000_lateral_external_carotid_artery`; DSA (angiography); Lateral External carotid artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01`; `[530, 120, 784, 520]` | n/a | n/a | The lateral view of the left external carotid artery shows a complex network of vessels with a prominent area of irregularity and possible vascular malformation or abnormal branching within the boxed region. The vessels appear tortuous and there is a notable concentration of contrast material suggesting increased vascularity or potential arteriovenous shunting. The surrounding vasculature appears less dense, providing a stark contrast to the highlighted area. |

### Anchor 2: `study_000_ct_image_000_axial_bone_window_f02`

<img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f02.png" width="420">

**Anchor Lingshu caption：** The left mastoid air cells appear opacified. The left middle ear cavity also appears opacified. There is no definite bony erosion.

#### location_00004: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_mri_image_000_axial_t1_c_fat_sat_f01</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f02.png" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_001_mri_image_000_axial_t1_c_fat_sat.jpeg" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_000_axial_t1_c_fat_sat_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_mri_image_000_axial_t1_c_fat_sat`; MRI; Axial T1 C+ fat sat
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_mri_image_000_axial_t1_c_fat_sat_f01`; `[612, 452, 767, 575]` | n/a | n/a | The left internal auditory canal demonstrates a small enhancing mass. The right internal auditory canal appears normal. The cerebellum, medulla, and pons appear normal. There is no evidence of hydrocephalus. |

#### location_00005: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_mri_image_001_coronal_t1_c_f01</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f02.png" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_001_mri_image_001_coronal_t1_c.jpeg" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_001_coronal_t1_c_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_mri_image_001_coronal_t1_c`; MRI; Coronal T1 C+
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_mri_image_001_coronal_t1_c_f01`; `[645, 250, 815, 410]` | n/a | n/a | The left carotid artery is enlarged and tortuous. There is a large mass centered at the bifurcation of the left carotid artery. The mass is heterogeneous and contains areas of high signal intensity. The mass extends into the left internal carotid artery and external carotid artery. The mass also extends posteriorly to the left vertebral artery. |

#### location_00006: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f02.png" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_002_dsa_angiography_image_000_lateral_external_carotid_artery.jpeg" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_000_lateral_external_carotid_artery`; DSA (angiography); Lateral External carotid artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01`; `[530, 120, 784, 520]` | n/a | n/a | The lateral view of the left external carotid artery shows a complex network of vessels with a prominent area of irregularity and possible vascular malformation or abnormal branching within the boxed region. The vessels appear tortuous and there is a notable concentration of contrast material suggesting increased vascularity or potential arteriovenous shunting. The surrounding vasculature appears less dense, providing a stark contrast to the highlighted area. |

### Anchor 3: `study_001_mri_image_000_axial_t1_c_fat_sat_f01`

<img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_000_axial_t1_c_fat_sat_f01.png" width="420">

**Anchor Lingshu caption：** The left internal auditory canal demonstrates a small enhancing mass. The right internal auditory canal appears normal. The cerebellum, medulla, and pons appear normal. There is no evidence of hydrocephalus.

#### location_00007: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_001_mri_image_001_coronal_t1_c_f01</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_000_axial_t1_c_fat_sat_f01.png" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_001_mri_image_001_coronal_t1_c.jpeg" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_001_coronal_t1_c_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_001_mri_image_001_coronal_t1_c`; MRI; Coronal T1 C+
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_001_mri_image_001_coronal_t1_c_f01`; `[645, 250, 815, 410]` | n/a | n/a | The left carotid artery is enlarged and tortuous. There is a large mass centered at the bifurcation of the left carotid artery. The mass is heterogeneous and contains areas of high signal intensity. The mass extends into the left internal carotid artery and external carotid artery. The mass also extends posteriorly to the left vertebral artery. |

#### location_00008: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_000_axial_t1_c_fat_sat_f01.png" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_002_dsa_angiography_image_000_lateral_external_carotid_artery.jpeg" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_000_lateral_external_carotid_artery`; DSA (angiography); Lateral External carotid artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01`; `[530, 120, 784, 520]` | n/a | n/a | The lateral view of the left external carotid artery shows a complex network of vessels with a prominent area of irregularity and possible vascular malformation or abnormal branching within the boxed region. The vessels appear tortuous and there is a notable concentration of contrast material suggesting increased vascularity or potential arteriovenous shunting. The surrounding vasculature appears less dense, providing a stark contrast to the highlighted area. |

### Anchor 4: `study_001_mri_image_001_coronal_t1_c_f01`

<img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_001_coronal_t1_c_f01.png" width="420">

**Anchor Lingshu caption：** The left carotid artery is enlarged and tortuous. There is a large mass centered at the bifurcation of the left carotid artery. The mass is heterogeneous and contains areas of high signal intensity. The mass extends into the left internal carotid artery and external carotid artery. The mass also extends posteriorly to the left vertebral artery.

#### location_00009: NOT SUPPORT

<table>
<tr><th>Anchor original bbox</th><th>Target original image; model returned null</th><th>Existing target bbox: study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_001_coronal_t1_c_f01.png" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_002_dsa_angiography_image_000_lateral_external_carotid_artery.jpeg" width="300"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01.png" width="300"></td></tr>
</table>

- **Target：** `study_002_dsa_angiography_image_000_lateral_external_carotid_artery`; DSA (angiography); Lateral External carotid artery
- **Relation：** `bbox_to_image` / `not_support`
- **Returned target bbox：** `unknown`
- **Maximum IoU：** n/a; threshold=0.5
- **Strong relation IDs：** `[]`

**IoU matching：**

| Existing target bbox | IoU | Strong match | Lingshu caption |
|---|---:|---|---|
| `study_002_dsa_angiography_image_000_lateral_external_carotid_artery_f01`; `[530, 120, 784, 520]` | n/a | n/a | The lateral view of the left external carotid artery shows a complex network of vessels with a prominent area of irregularity and possible vascular malformation or abnormal branching within the boxed region. The vessels appear tortuous and there is a notable concentration of contrast material suggesting increased vascularity or potential arteriovenous shunting. The surrounding vasculature appears less dense, providing a stark contrast to the highlighted area. |

## Dynamically Skipped Anchors

None.

## Case-level Location Validation Summary / 病例级定位验证总结

- **Strong support：** 0 个 bbox-to-bbox 关系
- **Partial support：** 1 个 bbox-to-image 关系
- **Not support：** 8 个 bbox-to-image 关系

### Strong Support

该病例没有 strong-support bbox 对应关系。

### Partial Support

#### Partial 1: `study_000_ct_image_000_axial_bone_window_f01` → `study_001_mri_image_000_axial_t1_c_fat_sat`

- **Query：** `location_00001`
- **Returned target bbox：** `[87, 442, 375, 656]`
- **Maximum IoU：** 0.000（低于 threshold=0.5）

<table>
<tr><th>Anchor bbox</th><th>Cross-image grounded target bbox</th><th>Closest existing target bbox</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f01.png" width="320"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/grounding/location_00001.png" width="320"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_000_axial_t1_c_fat_sat_f01.png" width="320"></td></tr>
</table>

### Not Support

#### Not support 1: `study_000_ct_image_000_axial_bone_window_f01` → `study_001_mri_image_001_coronal_t1_c`

- **Query：** `location_00002`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f01.png" width="340"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_001_mri_image_001_coronal_t1_c.jpeg" width="340"></td></tr>
</table>

#### Not support 2: `study_000_ct_image_000_axial_bone_window_f01` → `study_002_dsa_angiography_image_000_lateral_external_carotid_artery`

- **Query：** `location_00003`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f01.png" width="340"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_002_dsa_angiography_image_000_lateral_external_carotid_artery.jpeg" width="340"></td></tr>
</table>

#### Not support 3: `study_000_ct_image_000_axial_bone_window_f02` → `study_001_mri_image_000_axial_t1_c_fat_sat`

- **Query：** `location_00004`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f02.png" width="340"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_001_mri_image_000_axial_t1_c_fat_sat.jpeg" width="340"></td></tr>
</table>

#### Not support 4: `study_000_ct_image_000_axial_bone_window_f02` → `study_001_mri_image_001_coronal_t1_c`

- **Query：** `location_00005`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f02.png" width="340"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_001_mri_image_001_coronal_t1_c.jpeg" width="340"></td></tr>
</table>

#### Not support 5: `study_000_ct_image_000_axial_bone_window_f02` → `study_002_dsa_angiography_image_000_lateral_external_carotid_artery`

- **Query：** `location_00006`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_000_ct_image_000_axial_bone_window_f02.png" width="340"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_002_dsa_angiography_image_000_lateral_external_carotid_artery.jpeg" width="340"></td></tr>
</table>

#### Not support 6: `study_001_mri_image_000_axial_t1_c_fat_sat_f01` → `study_001_mri_image_001_coronal_t1_c`

- **Query：** `location_00007`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_000_axial_t1_c_fat_sat_f01.png" width="340"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_001_mri_image_001_coronal_t1_c.jpeg" width="340"></td></tr>
</table>

#### Not support 7: `study_001_mri_image_000_axial_t1_c_fat_sat_f01` → `study_002_dsa_angiography_image_000_lateral_external_carotid_artery`

- **Query：** `location_00008`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_000_axial_t1_c_fat_sat_f01.png" width="340"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_002_dsa_angiography_image_000_lateral_external_carotid_artery.jpeg" width="340"></td></tr>
</table>

#### Not support 8: `study_001_mri_image_001_coronal_t1_c_f01` → `study_002_dsa_angiography_image_000_lateral_external_carotid_artery`

- **Query：** `location_00009`
- **Result：** 目标图返回 `null`，未定位到对应区域。

<table>
<tr><th>Anchor bbox</th><th>Target original image</th></tr>
<tr><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/nodes/study_001_mri_image_001_coronal_t1_c_f01.png" width="340"></td><td><img src="../assets_step3/jugulotympanic-paraganglioma-9/images/study_002_dsa_angiography_image_000_lateral_external_carotid_artery.jpeg" width="340"></td></tr>
</table>
