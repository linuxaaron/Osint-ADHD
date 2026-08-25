#!/usr/bin/env python3
"""Synchronisiert das offizielle OSINT Framework mit OSINT ADHD.

Es wird ausschließlich die kanonische arf.json geladen. Daraus werden die
Rohdaten, ein vollständiger Link-Index und einzelne kategorisierte Markdown-
Dateien erzeugt. Externe Ressourcen werden nicht automatisch aufgerufen.
"""

from __future__ import annotations

import json
import pathlib
import re
import urllib.request
from collections import defaultdict
from typing import Any, Iterator

UPSTREAM_URL = (
    "https://raw.githubusercontent.com/lockfale/OSINT-Framework/"
    "master/public/arf.json"
)
ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
CATEGORY_DIR = ROOT / "categories"
JSON_OUT = DATA_DIR / "osint-framework.json"
MD_OUT = DATA_DIR / "osint-framework-links.md"


def fetch_json() -> dict[str, Any]:
    request = urllib.request.Request(
        UPSTREAM_URL,
        headers={"User-Agent": "OSINT-ADHD-Upstream-Sync/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)

    if not isinstance(payload, dict) or payload.get("type") != "folder":
        raise ValueError("Unerwartete Struktur des Upstream-Datensatzes")
    return payload


def walk(node: dict[str, Any], parents: tuple[str, ...] = ()) -> Iterator[tuple[tuple[str, ...], dict[str, Any]]]:
    name = str(node.get("name", "Unbenannt"))
    current = parents + (name,)

    if node.get("type") == "url" and node.get("url"):
        yield current, node
        return

    for child in node.get("children", []):
        if isinstance(child, dict):
            yield from walk(child, current)


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9äöüß]+", "-", value)
    value = value.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return value.strip("-") or "allgemein"


def category_name(path: tuple[str, ...]) -> str:
    return " / ".join(path[1:-1]) if len(path) > 2 else "Allgemein"


def render_records(title: str, records: list[tuple[tuple[str, ...], dict[str, Any]]]) -> str:
    lines = [
        f"# {title}",
        "",
        "> Automatisch aus dem offiziellen OSINT Framework erzeugt. Nicht manuell bearbeiten.",
        "> Die Namen und Beschreibungen der externen Ressourcen bleiben im Original, damit keine Bedeutungen verfälscht werden.",
        "",
        f"**Anzahl Ressourcen:** {len(records)}",
        "",
    ]

    for path, item in records:
        name = str(item.get("name", path[-1]))
        url = str(item["url"])
        lines.append(f"## {name}")
        lines.append("")
        lines.append(f"- **URL:** {url}")
        lines.append(f"- **Kategorie:** {category_name(path)}")
        if item.get("description"):
            lines.append(f"- **Beschreibung:** {item['description']}")
        if item.get("status"):
            lines.append(f"- **Status:** {item['status']}")
        if item.get("pricing"):
            lines.append(f"- **Kosten:** {item['pricing']}")
        if item.get("registration") is not None:
            lines.append(f"- **Registrierung:** {item['registration']}")
        if item.get("api") is not None:
            lines.append(f"- **API:** {item['api']}")
        lines.append("")

    return "\n".join(lines)


def generate_indexes(dataset: dict[str, Any]) -> int:
    records = list(walk(dataset))
    records.sort(key=lambda item: (item[0], str(item[1].get("url", ""))))

    lines = [
        "# OSINT Framework — vollständige Linkliste",
        "",
        "> Automatisch aus dem offiziellen OSINT Framework erzeugt. Nicht manuell bearbeiten.",
        "> Quelle: https://github.com/lockfale/OSINT-Framework/blob/master/public/arf.json",
        "",
        f"**Erfasste Ressourcen:** {len(records)}",
        "",
        "## Alle Ressourcen",
        "",
    ]

    grouped: dict[str, list[tuple[tuple[str, ...], dict[str, Any]]]] = defaultdict(list)
    for path, item in records:
        grouped[category_name(path)].append((path, item))
        name = str(item.get("name", path[-1]))
        url = str(item["url"])
        lines.append(f"- **{name}** — `{category_name(path)}` — {url}")

    lines.extend([
        "",
        "## Herkunft",
        "",
        "Diese Datei wird aus dem offiziellen Upstream-Datensatz erzeugt. Die verlinkten Drittanbieter-Ressourcen unterliegen ihren eigenen Nutzungsbedingungen.",
        "",
    ])
    MD_OUT.write_text("\n".join(lines), encoding="utf-8")

    CATEGORY_DIR.mkdir(parents=True, exist_ok=True)
    for category, category_records in grouped.items():
        filename = f"{slugify(category)}.md"
        (CATEGORY_DIR / filename).write_text(
            render_records(category, category_records), encoding="utf-8"
        )

    return len(records)


def main() -> None:
    dataset = fetch_json()
    records = list(walk(dataset))
    if not records:
        raise ValueError("Der Upstream-Datensatz enthält keine URL-Ressourcen")

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(
        json.dumps(dataset, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    count = generate_indexes(dataset)
    print(f"{count} URL-Ressourcen aus dem OSINT Framework synchronisiert")


if __name__ == "__main__":
    main()
