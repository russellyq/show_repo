#!/usr/bin/env python3
"""Export Step 3 bbox, captions and validation records as GitHub Markdown."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
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


def copy_asset(source, destination):
    source = Path(source).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.is_file() or source.stat().st_size != destination.stat().st_size:
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


def validation_map(record):
    return {item["validation_id"]: item for item in record.get("validations") or []}


def node_map(record):
    return {item["node_id"]: item for item in record.get("nodes") or []}


def image_map(record):
    return {item["image_id"]: item for item in record.get("images") or []}


def support_counts(record):
    return Counter(
        item.get("location_validation", {}).get("status", "unknown")
        for item in record.get("cross_image_grounding") or []
    )


def render_validation_table(query, validations):
    rows = []
    for validation_id in query.get("validation_ids") or []:
        item = validations.get(validation_id)
        if not item:
            rows.append(
                f"| `{escaped(validation_id)}` | missing | missing validation record |"
            )
            continue
        quantity = item.get("quantification_validation") or {}
        quality = item.get("characterization_validation") or {}
        rows.append(
            "| Quantification | "
            f"`{escaped(quantity.get('status'))}` | {compact(quantity.get('reason'))} |"
        )
        rows.append(
            "| Characterization | "
            f"`{escaped(quality.get('status'))}` | {compact(quality.get('reason'))} |"
        )
    if not rows:
        rows.append(
            "| Quantification / characterization | not applicable | "
            "Target region was not found, so no downstream validation was run. |"
        )
    return [
        "| Validation | Status | Reason |",
        "|---|---|---|",
        *rows,
    ]


def render_iou_table(location, target_node_ids, nodes):
    comparisons = {
        item.get("target_node_id"): item
        for item in location.get("existing_bbox_comparisons") or []
    }
    if not target_node_ids:
        return ["The target image has no existing Step 2 bbox."]
    lines = [
        "| Existing target bbox | IoU | Strong match | Lingshu caption |",
        "|---|---:|---|---|",
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
            f"{compact(node.get('lingshu_caption'))} |"
        )
    return lines


def render_case(record, output_root, assets_root, pages_root, model_label):
    case_id = record["case_id"]
    case_assets = assets_root / safe_name(case_id)
    page_path = pages_root / f"{safe_name(case_id)}.md"
    nodes = node_map(record)
    images = image_map(record)
    validations = validation_map(record)

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
    raw_json = copy_asset(
        Path(record["source_step_2"]["path"]).parents[2]
        / "step_3"
        / "case_evidence.json",
        case_assets / "case_evidence.json",
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
                    *render_iou_table(location, target_node_ids, nodes),
                    "",
                ]
            )
            if status == "partial_support":
                lines.extend(
                    [
                        "**Target Lingshu caption：** unavailable. This is a newly re-grounded bbox and has not passed through Step 2 Lingshu captioning.",
                        "",
                    ]
                )
            lines.extend(
                [
                    "**Quantification / characterization：**",
                    "",
                    *render_validation_table(query, validations),
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

    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return {
        "case_id": case_id,
        "case_title": record.get("case_title") or case_id,
        "page_path": page_path,
        "summary": summary,
        "counts": counts,
    }


def render_index(case_rows, output_root, model_label):
    totals = Counter()
    for row in case_rows:
        totals.update(row["counts"])
    query_total = sum(
        row["summary"].get("executed_or_reused_query_count", 0) for row in case_rows
    )

    def percentage(value):
        return 0.0 if query_total == 0 else value / query_total * 100

    lines = [
        "# Step 3 Cross-image Validation 可视化",
        "",
        "[返回主 README](README.md)",
        "",
        f"本页展示 **{escaped(model_label)}** 的 Step 3 输出。每个病例子页包含 Step 2 bbox、Lingshu caption、跨图目标定位、IoU 匹配，以及定量和定性 validation。",
        "",
        "**关系定义：**",
        "",
        "- `STRONG SUPPORT`：跨图返回框与目标图已有 bbox 的 IoU >= 0.5，属于 bbox-to-bbox。",
        "- `PARTIAL SUPPORT`：目标图找到了新框，但没有已有 bbox 达到阈值，属于 bbox-to-image。",
        "- `NOT SUPPORT`：目标图返回 `null`，属于 bbox-to-image。",
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
