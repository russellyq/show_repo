#!/usr/bin/env python3
"""Export Step 3 location, size, and caption validation as GitHub Markdown."""

from __future__ import annotations

import argparse
import filecmp
import html
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
TRANSLATIONS_FILE = SCRIPT_DIR / "step3_caption_translations.json"
DEFAULT_SOURCE_ROOT = (
    SCRIPT_DIR.parent / "ours_method" / "cases_qwen3vl_8b"
)
STATUS_LABELS = {
    "strong_support": "STRONG SUPPORT",
    "partial_support": "PARTIAL SUPPORT",
    "not_support": "NOT SUPPORT",
    "parse_error": "PARSE ERROR",
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source_root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--output_root", type=Path, default=SCRIPT_DIR)
    parser.add_argument("--model_label", default="Qwen3-VL-8B")
    parser.add_argument("--overwrite_assets", action="store_true")
    return parser.parse_args()


def safe_name(value):
    return re.sub(r"[^A-Za-z0-9._-]+", "_", str(value)).strip("_") or "item"


def escaped(value):
    return html.escape(str(value if value is not None else "unknown"))


def compact(value):
    text = str(value if value is not None else "unknown").strip()
    return escaped(" ".join(text.split())).replace("|", "&#124;")


def load_translations(path=TRANSLATIONS_FILE):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Caption translation file not found: {path}")
    record = json.loads(path.read_text(encoding="utf-8"))
    return {
        "original": record.get("original") or {},
        "reground": record.get("reground") or {},
    }


def translated(translations, kind, case_id, item_id):
    key = f"{case_id}::{item_id}"
    value = (translations.get(kind) or {}).get(key)
    return compact(value) if value else "[缺少人工翻译]"


def copy_asset(source, destination):
    source = Path(source).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.is_file() or not filecmp.cmp(
        source, destination, shallow=False
    ):
        shutil.copy2(source, destination)
    return destination


def copy_image(source, directory, stem):
    source = Path(source).expanduser().resolve()
    suffix = source.suffix.lower() if source.suffix else ".png"
    return copy_asset(source, directory / f"{safe_name(stem)}{suffix}")


def relpath(path, page_dir):
    return Path(path).resolve().relative_to(page_dir.parent.resolve()).as_posix()


def image_tag(path, page_dir, width=420):
    return f'<img src="../{relpath(path, page_dir)}" width="{width}">'


def status_label(status):
    return STATUS_LABELS.get(status, str(status).upper().replace("_", " "))


def node_map(record):
    return {item["node_id"]: item for item in record.get("nodes") or []}


def image_map(record):
    return {item["image_id"]: item for item in record.get("images") or []}


def support_counts(record):
    return Counter(
        item.get("location_validation", {}).get("status", "unknown")
        for item in record.get("cross_image_grounding") or []
    )


def pair_validation_id(status, relation_or_query_id):
    prefix = "strong" if status == "strong_support" else "partial"
    return f"{prefix}__{relation_or_query_id}"


def validation_value(validation, key):
    value = validation.get(key)
    allowed_values = (
        {"consistent", "partially", "inconsistent"}
        if key == "qualitative_validation"
        else {"consistent", "inconsistent"}
    )
    if value not in allowed_values:
        raise ValueError(
            f"Invalid {key} for {validation.get('pair_id')}: {value!r}"
        )
    return value


def render_validation_lines(validation):
    return [
        f"- **Quantitative size validation / 定量大小一致性：** "
        f"`{validation_value(validation, 'quantitative_validation')}`",
        f"- **Qualitative caption validation / 定性语义一致性：** "
        f"`{validation_value(validation, 'qualitative_validation')}`",
    ]


def render_validation_table(pair_ids, pair_validations):
    lines = [
        "| Validation pair | Quantitative size / 定量 | Qualitative caption / 定性 |",
        "|---|---|---|",
    ]
    for pair_id in pair_ids:
        validation = pair_validations[pair_id]
        lines.append(
            f"| `{escaped(pair_id)}` | "
            f"`{validation_value(validation, 'quantitative_validation')}` | "
            f"`{validation_value(validation, 'qualitative_validation')}` |"
        )
    return lines


def render_iou_table(location, target_node_ids, nodes, translations, case_id):
    comparisons = {
        item.get("target_node_id"): item
        for item in location.get("existing_bbox_comparisons") or []
    }
    if not target_node_ids:
        return ["The target image has no existing Step 2 bbox."]
    lines = [
        "| Existing target bbox | IoU | Strong match | Lingshu caption | 中文翻译 |",
        "|---|---:|---|---|---|",
    ]
    for node_id in target_node_ids:
        item = comparisons.get(node_id) or {}
        node = nodes.get(node_id) or {}
        iou = item.get("iou")
        iou_text = "n/a" if iou is None else f"{float(iou):.3f}"
        match_text = (
            "n/a" if iou is None else ("yes" if item.get("strong_match") else "no")
        )
        lines.append(
            f"| `{escaped(node_id)}`; `{escaped(node.get('bbox_2d'))}` | "
            f"{iou_text} | "
            f"{match_text} | "
            f"{compact(node.get('lingshu_caption'))} | "
            f"{translated(translations, 'original', case_id, node_id)} |"
        )
    return lines


def render_case_location_summary(
    record,
    nodes,
    original_assets,
    node_assets,
    query_assets,
    reground_records,
    reground_assets,
    pair_validations,
    translations,
    page_dir,
):
    queries = record.get("cross_image_grounding") or []
    query_by_id = {item["query_id"]: item for item in queries}
    strong_relations = record.get("strong_support_relations") or []
    partial_queries = [
        item
        for item in queries
        if (item.get("location_validation") or {}).get("status")
        == "partial_support"
    ]
    not_support_queries = [
        item
        for item in queries
        if (item.get("location_validation") or {}).get("status") == "not_support"
    ]
    lines = [
        "## Case-level Location Validation Summary / 病例级定位验证总结",
        "",
        f"- **Strong support：** {len(strong_relations)} 个 bbox-to-bbox 关系",
        f"- **Partial support：** {len(partial_queries)} 个 bbox-to-image 关系",
        f"- **Not support：** {len(not_support_queries)} 个 bbox-to-image 关系",
        "",
        "### Strong Support",
        "",
    ]
    if not strong_relations:
        lines.extend(["该病例没有 strong-support bbox 对应关系。", ""])
    for index, relation in enumerate(strong_relations, 1):
        anchor_id = (relation.get("anchor") or {}).get("node_id")
        target_id = (relation.get("target") or {}).get("node_id")
        query_id = relation.get("source_query_id")
        query = query_by_id.get(query_id) or {}
        target_image_id = (query.get("target_image") or {}).get("image_id")
        cross_asset = query_assets.get(query_id)
        if cross_asset is None and target_image_id:
            cross_asset = original_assets.get(target_image_id)
        headers = ["Anchor bbox", "Cross-image grounded target bbox", "Matched target bbox"]
        cells = [
            image_tag(node_assets[anchor_id], page_dir, 300),
            image_tag(cross_asset, page_dir, 300),
            image_tag(node_assets[target_id], page_dir, 300),
        ]
        iou = relation.get("iou")
        iou_text = "n/a" if iou is None else f"{float(iou):.3f}"
        pair_id = pair_validation_id("strong_support", relation.get("relation_id"))
        lines.extend(
            [
                f"#### Strong {index}: `{escaped(anchor_id)}` ↔ `{escaped(target_id)}`",
                "",
                f"- **Relation / query：** `{escaped(relation.get('relation_id'))}` / `{escaped(query_id)}`",
                f"- **IoU：** {iou_text}（threshold=0.5）",
                "",
                "<table>",
                "<tr>" + "".join(f"<th>{item}</th>" for item in headers) + "</tr>",
                "<tr>" + "".join(f"<td>{item}</td>" for item in cells) + "</tr>",
                "</table>",
                "",
                f"- **Anchor Lingshu caption：** {compact((nodes.get(anchor_id) or {}).get('lingshu_caption'))}",
                f"- **Anchor caption 中文翻译：** {translated(translations, 'original', record['case_id'], anchor_id)}",
                f"- **Target Lingshu caption：** {compact((nodes.get(target_id) or {}).get('lingshu_caption'))}",
                f"- **Target caption 中文翻译：** {translated(translations, 'original', record['case_id'], target_id)}",
                *render_validation_lines(pair_validations[pair_id]),
                "",
            ]
        )

    lines.extend(["### Partial Support", ""])
    if not partial_queries:
        lines.extend(["该病例没有 partial-support 查询。", ""])
    for index, query in enumerate(partial_queries, 1):
        location = query.get("location_validation") or {}
        anchor_id = (query.get("anchor") or {}).get("node_id")
        target = query.get("target_image") or {}
        target_image_id = target.get("image_id")
        cross_asset = query_assets.get(query["query_id"], original_assets[target_image_id])
        comparisons = location.get("existing_bbox_comparisons") or []
        best = max(
            comparisons,
            key=lambda item: float(item.get("iou") or 0.0),
            default=None,
        )
        reground_record = reground_records.get(query["query_id"]) or {}
        headers = [
            "Anchor bbox",
            "Cross-image grounding and IoU overlay",
            "B image with the single re-grounded bbox given to Lingshu",
        ]
        cells = [
            image_tag(node_assets[anchor_id], page_dir, 320),
            image_tag(cross_asset, page_dir, 320),
            image_tag(reground_assets[query["query_id"]], page_dir, 320),
        ]
        if best and best.get("target_node_id") in node_assets:
            headers.append("Closest existing target bbox")
            cells.append(
                image_tag(node_assets[best["target_node_id"]], page_dir, 320)
            )
        max_iou = location.get("max_iou")
        max_iou_text = "n/a" if max_iou is None else f"{float(max_iou):.3f}"
        pair_id = pair_validation_id("partial_support", query.get("query_id"))
        lines.extend(
            [
                f"#### Partial {index}: `{escaped(anchor_id)}` → `{escaped(target_image_id)}`",
                "",
                f"- **Query：** `{escaped(query.get('query_id'))}`",
                f"- **Returned target bbox：** `{escaped(location.get('target_bbox_2d'))}`",
                f"- **Maximum IoU：** {max_iou_text}（低于 threshold=0.5）",
                "",
                "<table>",
                "<tr>" + "".join(f"<th>{item}</th>" for item in headers) + "</tr>",
                "<tr>" + "".join(f"<td>{item}</td>" for item in cells) + "</tr>",
                "</table>",
                "",
                f"- **A 端原始 Lingshu caption：** {compact((nodes.get(anchor_id) or {}).get('lingshu_caption'))}",
                f"- **A 端 caption 中文翻译：** {translated(translations, 'original', record['case_id'], anchor_id)}",
                f"- **B 端 re-ground Lingshu caption：** {compact(reground_record.get('caption'))}",
                f"- **B 端 re-ground caption 中文翻译：** {translated(translations, 'reground', record['case_id'], query['query_id'])}",
                *render_validation_lines(pair_validations[pair_id]),
                "",
            ]
        )

    lines.extend(["### Not Support", ""])
    if not not_support_queries:
        lines.extend(["该病例没有 not-support 查询。", ""])
    for index, query in enumerate(not_support_queries, 1):
        anchor_id = (query.get("anchor") or {}).get("node_id")
        target_image_id = (query.get("target_image") or {}).get("image_id")
        lines.extend(
            [
                f"#### Not support {index}: `{escaped(anchor_id)}` → `{escaped(target_image_id)}`",
                "",
                f"- **Query：** `{escaped(query.get('query_id'))}`",
                "- **Result：** 目标图返回 `null`，未定位到对应区域。",
                "",
                "<table>",
                "<tr><th>Anchor bbox</th><th>Target original image</th></tr>",
                "<tr>"
                f"<td>{image_tag(node_assets[anchor_id], page_dir, 340)}</td>"
                f"<td>{image_tag(original_assets[target_image_id], page_dir, 340)}</td>"
                "</tr>",
                "</table>",
                "",
                f"- **A 端原始 Lingshu caption：** {compact((nodes.get(anchor_id) or {}).get('lingshu_caption'))}",
                f"- **A 端 caption 中文翻译：** {translated(translations, 'original', record['case_id'], anchor_id)}",
                "- **B 端 re-ground caption：** 不适用；目标图返回 `null`，没有生成 re-ground bbox。",
                "- **定量 / 定性验证：** 不适用；仅对 strong-support 和 partial-support pair 执行。",
                "",
            ]
        )
    return lines


def render_case(
    record,
    output_root,
    assets_root,
    pages_root,
    model_label,
    translations,
):
    case_id = record["case_id"]
    case_assets = assets_root / safe_name(case_id)
    page_path = pages_root / f"{safe_name(case_id)}.md"
    nodes = node_map(record)
    images = image_map(record)

    original_assets = {}
    for image_id, image in images.items():
        original_assets[image_id] = copy_image(
            image["original_image_path"],
            case_assets / "images",
            image_id,
        )
    node_assets = {}
    for node_id, node in nodes.items():
        node_assets[node_id] = copy_image(
            node["bbox_image_path"],
            case_assets / "nodes",
            node_id,
        )
    query_assets = {}
    for query in record.get("cross_image_grounding") or []:
        overlay = (query.get("location_validation") or {}).get("cross_image_overlay")
        if overlay and overlay.get("path"):
            query_assets[query["query_id"]] = copy_image(
                overlay["path"],
                case_assets / "grounding",
                query["query_id"],
            )
    case_root = Path(record["source_step_2"]["path"]).parents[2]
    reground_path = case_root / "step_3_reground" / "case_evidence.json"
    if not reground_path.is_file():
        raise FileNotFoundError(f"Step 3 re-ground evidence not found: {reground_path}")
    reground_evidence = json.loads(reground_path.read_text(encoding="utf-8"))
    reground_records = {
        item["query_id"]: item
        for item in reground_evidence.get("partial_support_reground_captions") or []
    }
    reground_assets = {}
    for query_id, item in reground_records.items():
        bbox_path = (item.get("regrounded_region") or {}).get("bbox_image_path")
        if bbox_path:
            reground_assets[query_id] = copy_image(
                bbox_path,
                case_assets / "reground",
                query_id,
            )
    partial_ids = {
        item["query_id"]
        for item in record.get("cross_image_grounding") or []
        if (item.get("location_validation") or {}).get("status")
        == "partial_support"
    }
    missing_reground = sorted(partial_ids - set(reground_records))
    missing_assets = sorted(partial_ids - set(reground_assets))
    if missing_reground or missing_assets:
        raise ValueError(
            f"Incomplete re-ground output for {case_id}: "
            f"records={missing_reground}, assets={missing_assets}"
        )
    validation_path = case_root / "step_3_validation" / "case_evidence.json"
    if not validation_path.is_file():
        raise FileNotFoundError(
            f"Step 3 quantitative/qualitative validation not found: {validation_path}"
        )
    validation_evidence = json.loads(validation_path.read_text(encoding="utf-8"))
    pair_validations = {
        item["pair_id"]: item for item in validation_evidence.get("validations") or []
    }
    expected_pair_ids = {
        pair_validation_id("strong_support", item.get("relation_id"))
        for item in record.get("strong_support_relations") or []
    }
    expected_pair_ids.update(
        pair_validation_id("partial_support", item.get("query_id"))
        for item in record.get("cross_image_grounding") or []
        if (item.get("location_validation") or {}).get("status")
        == "partial_support"
    )
    missing_validations = sorted(expected_pair_ids - set(pair_validations))
    if missing_validations:
        raise ValueError(
            f"Incomplete quantitative/qualitative validation for {case_id}: "
            f"{missing_validations}"
        )
    for pair_id in expected_pair_ids:
        validation_value(pair_validations[pair_id], "quantitative_validation")
        validation_value(pair_validations[pair_id], "qualitative_validation")
    raw_json = copy_asset(
        Path(record["source_step_2"]["path"]).parents[2]
        / "step_3"
        / "case_evidence.json",
        case_assets / "case_evidence.json",
    )
    validation_json = copy_asset(
        validation_path,
        case_assets / "step_3_validation_case_evidence.json",
    )

    counts = support_counts(record)
    summary = record.get("processing_summary") or {}
    lines = [
        f"# {escaped(record.get('case_title') or case_id)}",
        "",
        "[返回 Step 3 总览](../README_STEP3_VISUALIZATION.md)",
        "",
        f"- **Case ID：** `{escaped(case_id)}`",
        f"- **Case URL：** [{escaped(record.get('case_url'))}]({escaped(record.get('case_url'))})",
        f"- **验证模型：** {escaped(model_label)}",
        f"- **图像 / Step 2 findings：** {summary.get('image_count', 0)} / {summary.get('node_count', 0)}",
        f"- **定位结果：** strong {counts['strong_support']}；partial {counts['partial_support']}；not support {counts['not_support']}；parse error {counts['parse_error']}",
        f"- **Strong bbox relations：** {summary.get('strong_relation_count', 0)}",
        f"- **原始 JSON：** [case_evidence.json](../{relpath(raw_json, pages_root)})",
        f"- **定量/定性验证 JSON：** [step_3_validation_case_evidence.json](../{relpath(validation_json, pages_root)})",
        "",
        "**Overlay 图例：** 红框为跨图新定位；绿框为 IoU >= 0.5 的已有 bbox；黄框为未达到阈值的已有 bbox。",
        "",
        "## Step 2 Finding Nodes",
        "",
    ]
    if not nodes:
        lines.extend(
            [
                "该病例的 Step 1/2 没有产生 bbox finding，因此 Step 3 没有可作为 anchor 的区域。",
                "",
                "| Original images |",
                "|---|",
            ]
        )
        for image_id in images:
            lines.append(f"| {image_tag(original_assets[image_id], pages_root, 360)} |")
    else:
        for index, node in enumerate(nodes.values(), 1):
            examination = (node.get("image") or {}).get("examination") or {}
            lines.extend(
                [
                    f"### Finding {index}: `{escaped(node['node_id'])}`",
                    "",
                    image_tag(node_assets[node["node_id"]], pages_root, 420),
                    "",
                    f"- **Modality / subcategory：** {escaped(examination.get('modality'))} / {escaped(examination.get('subcategory'))}",
                    f"- **bbox_2d：** `{escaped(node.get('bbox_2d'))}`",
                    f"- **Lingshu caption：** {compact(node.get('lingshu_caption'))}",
                    f"- **中文翻译：** {translated(translations, 'original', case_id, node['node_id'])}",
                    "",
                ]
            )

    lines.extend(["## Directed Cross-image Validation", ""])
    queries_by_anchor = defaultdict(list)
    for query in record.get("cross_image_grounding") or []:
        queries_by_anchor[query["anchor"]["node_id"]].append(query)
    if not queries_by_anchor:
        lines.extend(["没有可执行的跨图定位查询。", ""])
    for anchor_index, (anchor_id, queries) in enumerate(queries_by_anchor.items(), 1):
        anchor = nodes[anchor_id]
        lines.extend(
            [
                f"### Anchor {anchor_index}: `{escaped(anchor_id)}`",
                "",
                image_tag(node_assets[anchor_id], pages_root, 420),
                "",
                f"**Anchor Lingshu caption：** {compact(anchor.get('lingshu_caption'))}",
                f"**Anchor caption 中文翻译：** {translated(translations, 'original', case_id, anchor_id)}",
                "",
            ]
        )
        for query in queries:
            location = query.get("location_validation") or {}
            status = location.get("status", "unknown")
            target_id = query["target_image"]["image_id"]
            target_meta = query["target_image"].get("examination") or {}
            target_asset = query_assets.get(query["query_id"], original_assets[target_id])
            target_node_ids = query["target_image"].get("existing_node_ids") or []
            max_iou = location.get("max_iou")
            iou_text = "n/a" if max_iou is None else f"{float(max_iou):.3f}"
            visual_headers = ["Anchor original bbox"]
            visual_cells = [image_tag(node_assets[anchor_id], pages_root, 300)]
            if location.get("target_found"):
                visual_headers.append("Cross-image grounded target bbox")
            else:
                visual_headers.append("Target original image; model returned null")
            visual_cells.append(image_tag(target_asset, pages_root, 300))
            for target_node_id in target_node_ids:
                visual_headers.append(f"Existing target bbox: {escaped(target_node_id)}")
                visual_cells.append(
                    image_tag(node_assets[target_node_id], pages_root, 300)
                )
            lines.extend(
                [
                    f"#### {escaped(query['query_id'])}: {status_label(status)}",
                    "",
                    "<table>",
                    "<tr>" + "".join(f"<th>{item}</th>" for item in visual_headers) + "</tr>",
                    "<tr>" + "".join(f"<td>{item}</td>" for item in visual_cells) + "</tr>",
                    "</table>",
                    "",
                    f"- **Target：** `{escaped(target_id)}`; {escaped(target_meta.get('modality'))}; {escaped(target_meta.get('subcategory'))}",
                    f"- **Relation：** `{escaped(location.get('support_type'))}` / `{escaped(status)}`",
                    f"- **Returned target bbox：** `{escaped(location.get('target_bbox_2d'))}`",
                    f"- **Maximum IoU：** {iou_text}; threshold=0.5",
                    f"- **Strong relation IDs：** `{escaped(query.get('strong_relation_ids') or [])}`",
                    "",
                    "**IoU matching：**",
                    "",
                    *render_iou_table(
                        location,
                        target_node_ids,
                        nodes,
                        translations,
                        case_id,
                    ),
                    "",
                ]
            )
            if status == "partial_support":
                reground_record = reground_records[query["query_id"]]
                lines.extend(
                    [
                        "**B 图单红框（Lingshu 实际输入）：**",
                        "",
                        image_tag(reground_assets[query["query_id"]], pages_root, 420),
                        "",
                        f"**Re-ground Lingshu caption：** {compact(reground_record.get('caption'))}",
                        f"**Re-ground caption 中文翻译：** {translated(translations, 'reground', case_id, query['query_id'])}",
                        "",
                    ]
                )
            if status == "strong_support":
                pair_ids = [
                    pair_validation_id("strong_support", relation_id)
                    for relation_id in query.get("strong_relation_ids") or []
                ]
                lines.extend(
                    [
                        "**Quantitative / qualitative validation：**",
                        "",
                        *render_validation_table(pair_ids, pair_validations),
                        "",
                    ]
                )
            elif status == "partial_support":
                pair_id = pair_validation_id(
                    "partial_support", query.get("query_id")
                )
                lines.extend(
                    [
                        "**Quantitative / qualitative validation：**",
                        "",
                        *render_validation_table([pair_id], pair_validations),
                        "",
                    ]
                )
    skipped = record.get("skipped_anchor_nodes") or []
    lines.extend(["## Dynamically Skipped Anchors", ""])
    if not skipped:
        lines.extend(["None.", ""])
    else:
        lines.extend(
            [
                "| Anchor node | Reused strong relations | Skipped target images |",
                "|---|---|---|",
            ]
        )
        for item in skipped:
            lines.append(
                f"| `{escaped(item.get('anchor_node_id'))}` | "
                f"`{escaped(item.get('reused_strong_relation_ids'))}` | "
                f"`{escaped(item.get('skipped_target_image_ids'))}` |"
            )
        lines.append("")

    lines.extend(
        render_case_location_summary(
            record,
            nodes,
            original_assets,
            node_assets,
            query_assets,
            reground_records,
            reground_assets,
            pair_validations,
            translations,
            pages_root,
        )
    )

    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return {
        "case_id": case_id,
        "case_title": record.get("case_title") or case_id,
        "page_path": page_path,
        "summary": summary,
        "counts": counts,
        "validations": list(pair_validations.values()),
    }


def render_index(case_rows, output_root, model_label):
    totals = Counter()
    for row in case_rows:
        totals.update(row["counts"])
    query_total = sum(
        row["summary"].get("executed_or_reused_query_count", 0) for row in case_rows
    )
    validations = [
        validation
        for row in case_rows
        for validation in row.get("validations") or []
    ]

    def percentage(value):
        return 0.0 if query_total == 0 else value / query_total * 100

    def validation_count(support_status, validation_key, value):
        return sum(
            item.get("support_status") == support_status
            and item.get(validation_key) == value
            for item in validations
        )

    lines = [
        "# Step 3 Cross-image Validation 可视化",
        "",
        "[返回主 README](README.md)",
        "",
        f"本页展示 **{escaped(model_label)}** 当前已完成的 Step 3 结果：Step 2 bbox、Lingshu caption、跨图目标定位、IoU 匹配、strong/partial/not support 定位支持关系，以及 strong/partial pair 的定量大小与定性语义一致性。",
        "",
        "**关系定义：**",
        "",
        "- `STRONG SUPPORT`：跨图返回框与目标图已有 bbox 的 IoU >= 0.5，属于 bbox-to-bbox。",
        "- `PARTIAL SUPPORT`：目标图找到了新框，但没有已有 bbox 达到阈值，属于 bbox-to-image。",
        "- `NOT SUPPORT`：目标图返回 `null`，属于 bbox-to-image。",
        "",
        "**Caption 来源：**",
        "",
        "- `STRONG SUPPORT`：展示 A、B 两端已有 bbox 的原始 Step 2 Lingshu caption。",
        "- `PARTIAL SUPPORT`：展示 A 端已有 bbox 的原始 Step 2 Lingshu caption，以及 B 端跨图 re-ground bbox 重新送入 Lingshu 后得到的 caption。",
        "- `NOT SUPPORT`：展示 A 端原始 Step 2 Lingshu caption；由于目标图返回 `null`，B 端没有 bbox，也没有 re-ground caption。",
        "- 中文内容为对模型原始 caption 的逐条忠实翻译，仅用于对照阅读，不修正模型可能存在的医学错误。",
        "",
        "**定量 / 定性验证：**",
        "",
        "- 定量验证使用两张带 bbox 的图像及对应 Lingshu caption，输出 `consistent` 或 `inconsistent`。",
        "- 定性验证只使用两条 Lingshu caption 判断语义兼容性，输出 `consistent`、`partially` 或 `inconsistent`。",
        "- 仅 strong-support 与 partial-support pair 接受这两项验证；not-support 不执行。",
        "",
        "**Overlay 图例：** 红框为跨图新定位；绿框为达到阈值的已有 bbox；黄框为未达到阈值的已有 bbox。",
        "",
        "## Overall Summary",
        "",
        f"共 **{len(case_rows)}** 个病例、**{query_total}** 条实际执行或复用的定向跨图查询。当前目录中未发现 Qwen3-VL-32B 的完整 Step 3 case evidence，因此本次只展示 8B 结果。",
        "",
        "| Status | Count | Percentage |",
        "|---|---:|---:|",
        f"| Strong support | {totals['strong_support']} | {percentage(totals['strong_support']):.2f}% |",
        f"| Partial support | {totals['partial_support']} | {percentage(totals['partial_support']):.2f}% |",
        f"| Not support | {totals['not_support']} | {percentage(totals['not_support']):.2f}% |",
        f"| Parse error | {totals['parse_error']} | {percentage(totals['parse_error']):.2f}% |",
        "",
        "### Quantitative and Qualitative Validation",
        "",
        f"共 **{len(validations)}** 个 strong/partial pair 完成定量与定性验证。",
        "",
        "| Location relation | Pairs | Quantitative consistent | Quantitative inconsistent | Qualitative consistent | Qualitative partially | Qualitative inconsistent |",
        "|---|---:|---:|---:|---:|---:|---:|",
        f"| Strong support | {sum(item.get('support_status') == 'strong_support' for item in validations)} | {validation_count('strong_support', 'quantitative_validation', 'consistent')} | {validation_count('strong_support', 'quantitative_validation', 'inconsistent')} | {validation_count('strong_support', 'qualitative_validation', 'consistent')} | {validation_count('strong_support', 'qualitative_validation', 'partially')} | {validation_count('strong_support', 'qualitative_validation', 'inconsistent')} |",
        f"| Partial support | {sum(item.get('support_status') == 'partial_support' for item in validations)} | {validation_count('partial_support', 'quantitative_validation', 'consistent')} | {validation_count('partial_support', 'quantitative_validation', 'inconsistent')} | {validation_count('partial_support', 'qualitative_validation', 'consistent')} | {validation_count('partial_support', 'qualitative_validation', 'partially')} | {validation_count('partial_support', 'qualitative_validation', 'inconsistent')} |",
        f"| **Total** | **{len(validations)}** | **{sum(item.get('quantitative_validation') == 'consistent' for item in validations)}** | **{sum(item.get('quantitative_validation') == 'inconsistent' for item in validations)}** | **{sum(item.get('qualitative_validation') == 'consistent' for item in validations)}** | **{sum(item.get('qualitative_validation') == 'partially' for item in validations)}** | **{sum(item.get('qualitative_validation') == 'inconsistent' for item in validations)}** |",
        "",
        "## Cases",
        "",
        "| Case | Images | Findings | Queries | Strong | Partial | Not support | Strong relations | Skipped |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in case_rows:
        summary = row["summary"]
        counts = row["counts"]
        page = row["page_path"].relative_to(output_root).as_posix()
        lines.append(
            f"| [{escaped(row['case_title'])}]({page}) (`{escaped(row['case_id'])}`) | "
            f"{summary.get('image_count', 0)} | {summary.get('node_count', 0)} | "
            f"{summary.get('executed_or_reused_query_count', 0)} | "
            f"{counts['strong_support']} | {counts['partial_support']} | "
            f"{counts['not_support']} | {summary.get('strong_relation_count', 0)} | "
            f"{summary.get('dynamic_skipped_query_count', 0)} |"
        )
    (output_root / "README_STEP3_VISUALIZATION.md").write_text(
        "\n".join(lines).rstrip() + "\n", encoding="utf-8"
    )


def main():
    args = parse_args()
    source_root = args.source_root.expanduser().resolve()
    output_root = args.output_root.expanduser().resolve()
    assets_root = output_root / "assets_step3"
    pages_root = output_root / "step3_cases"
    if args.overwrite_assets:
        shutil.rmtree(assets_root, ignore_errors=True)
        shutil.rmtree(pages_root, ignore_errors=True)
    assets_root.mkdir(parents=True, exist_ok=True)
    pages_root.mkdir(parents=True, exist_ok=True)
    translations = load_translations()

    evidence_paths = sorted(source_root.glob("*/step_3/case_evidence.json"))
    if not evidence_paths:
        raise FileNotFoundError(f"No Step 3 case evidence found under {source_root}")
    case_rows = []
    for path in evidence_paths:
        record = json.loads(path.read_text(encoding="utf-8"))
        case_rows.append(
            render_case(
                record,
                output_root,
                assets_root,
                pages_root,
                args.model_label,
                translations,
            )
        )
    render_index(case_rows, output_root, args.model_label)
    print(
        f"[step-3-viz] cases={len(case_rows)} "
        f"index={output_root / 'README_STEP3_VISUALIZATION.md'} "
        f"assets={assets_root}"
    )


if __name__ == "__main__":
    main()
