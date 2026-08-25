#!/usr/bin/env python3
"""Sync the official OSINT Framework dataset into OSINT ADHD.

The script intentionally performs no third-party crawling. It downloads only the
canonical upstream JSON file, validates it, preserves the upstream structure and
generates a flat Markdown navigation index for humans.
"""

from __future__ import annotations

import json
import pathlib
import urllib.request
from typing import Any

UPSTREAM_URL = (
    "https://raw.githubusercontent.com/lockfale/OSINT-Framework/"
    "master/public/arf.json"
)
ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
JSON_OUT = DATA_DIR / "osint-framework.json"
MD_OUT = DATA_DIR / "osint-framework-links.md"


def fetch_json() -> dict[str, Any]:
    request = urllib.request.Request(
        UPSTREAM_URL,
        headers={"User-Agent": "OSINT-ADHD-Upstream-Sync/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)

    if not isinstance(payload, dict):
        raise ValueError("Upstream dataset root must be a JSON object")
    if payload.get("type") != "folder":
        raise ValueError("Unexpected upstream dataset type")
    return payload


def walk(node: dict[str, Any], parents: tuple[str, ...] = ()):
    name = str(node.get("name", "Unnamed"))
    current = parents + (name,)

    if node.get("type") == "url" and node.get("url"):
        yield current, node
        return

    for child in node.get("children", []):
        if isinstance(child, dict):
            yield from walk(child, current)


def markdown_index(dataset: dict[str, Any]) -> str:
    records = list(walk(dataset))
    records.sort(key=lambda item: (item[0], str(item[1].get("url", ""))))

    lines = [
        "# OSINT Framework — generated URL index",
        "",
        "> Generated from the official OSINT Framework dataset. Do not edit manually.",
        "> Source: https://github.com/lockfale/OSINT-Framework/blob/master/public/arf.json",
        "",
        f"**Indexed resources:** {len(records)}",
        "",
        "## Resources",
        "",
    ]

    for path, item in records:
        category = " / ".join(path[1:-1]) if len(path) > 2 else "General"
        name = str(item.get("name", path[-1]))
        url = str(item["url"])
        lines.append(f"- **{name}** — `{category}` — {url}")

    lines.extend([
        "",
        "## Provenance",
        "",
        "This file is generated from upstream data. Third-party resources remain subject to their own terms.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    dataset = fetch_json()
    records = list(walk(dataset))
    if not records:
        raise ValueError("Upstream dataset contains no URL records")

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(
        json.dumps(dataset, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    MD_OUT.write_text(markdown_index(dataset), encoding="utf-8")
    print(f"Synced {len(records)} URL records from OSINT Framework")


if __name__ == "__main__":
    main()
