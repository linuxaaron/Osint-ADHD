# OSINT ADHD

> Professionelle, kuratierte Sammlung von OSINT-Ressourcen für webbasierte Recherchen.

**OSINT ADHD** ist eine strukturierte Sammlung öffentlich zugänglicher OSINT-Ressourcen, Recherchewerkzeuge, Suchmaschinen, Referenzmaterialien und Arbeitsabläufe. Als Datenquelle wird das offizielle **OSINT Framework** verwendet. Zusätzlich enthält das Projekt eine getrennte Ebene für persönliche Empfehlungen und eigene Hinweise.

[![OSINT Framework](https://img.shields.io/badge/Quelle-OSINT%20Framework-111827)](https://osintframework.com/)
[![Lizenz](https://img.shields.io/badge/Lizenz-MIT-blue.svg)](LICENSE)
[![Daten](https://img.shields.io/badge/Daten-automatisch%20synchronisiert-orange.svg)](sources/UPSTREAM.md)

---

## Projektziele

- OSINT-Ressourcen strukturiert, durchsuchbar und reproduzierbar erfassen.
- Das offizielle OSINT Framework eindeutig als externe Quelle kennzeichnen.
- Eine getrennte, persönlich kuratierte Sammlung empfohlener Ressourcen pflegen.
- Relevante Metadaten wie Kategorie, Preismodell, API-Verfügbarkeit und Registrierung dokumentieren, sofern diese zuverlässig verifizierbar sind.
- Rechtmäßige Recherche mit öffentlich zugänglichen Informationen unterstützen.
- Die Daten sowohl für Menschen als auch für automatisierte Verarbeitung nutzbar machen.

## Repository-Struktur

```text
.
├── README.md
├── LICENSE
├── THIRD-PARTY-NOTICES.md
├── sources/
│   ├── UPSTREAM.md
│   ├── schema.md
│   └── upstream-metadata.json
├── recommendations/
│   └── aaron-recommended.md
├── categories/
│   ├── username.md
│   ├── email.md
│   ├── domains-infrastructure.md
│   ├── social-media.md
│   ├── people.md
│   ├── images.md
│   ├── geolocation.md
│   ├── documents.md
│   ├── companies.md
│   ├── code-github.md
│   ├── search-engines.md
│   └── investigations.md
├── scripts/
│   └── sync_upstream.py
└── .github/workflows/
    └── sync-osint-framework.yml
```

## Offizielles OSINT Framework

Das zentrale Upstream-Projekt wird von `lockfale` gepflegt:

- Webseite: https://osintframework.com/
- Repository: https://github.com/lockfale/OSINT-Framework
- Strukturierte Daten: https://github.com/lockfale/OSINT-Framework/blob/master/public/arf.json

Das Upstream-Dataset enthält strukturierte Ressourceneinträge einschließlich URLs und Metadaten. Dieses Repository kennzeichnet die Quelle ausdrücklich und verwendet einen automatisierten Synchronisationsprozess.

## Persönliche Empfehlungen

Die persönlich empfohlenen Ressourcen befinden sich unter [`recommendations/aaron-recommended.md`](recommendations/aaron-recommended.md). Diese Sammlung bleibt bewusst von den Upstream-Daten getrennt.

## Verantwortungsvolle Nutzung

Dieses Repository ist ein Ressourcenverzeichnis und keine Berechtigung zur Durchführung einer Recherche. Die Aufnahme einer Ressource bedeutet nicht, dass deren Nutzung in einem bestimmten Fall rechtlich zulässig oder vom jeweiligen Zielsystem erlaubt ist.

OSINT-Ressourcen ausschließlich für rechtmäßige Recherchen, eigene Systeme und Daten oder Systeme und Daten verwenden, für die eine ausdrückliche Berechtigung besteht. Datenschutzrecht, Nutzungsbedingungen, Robots-Regeln, Rate Limits, Zugriffskontrollen und sonstige geltende Vorschriften beachten.

**Dieses Repository darf nicht dazu verwendet werden, Authentifizierung oder Zugriffskontrollen zu umgehen, nicht öffentliche Informationen unbefugt zu beschaffen, Rate Limits zu umgehen oder unbefugte Aktivitäten durchzuführen.**

Hinweise zu einzelnen Ressourcen können veralten. Vor dem Einsatz in einer tatsächlichen Recherche ist das aktuelle Verhalten des jeweiligen Anbieters zu prüfen.

## Datenqualität

Die Verfügbarkeit von Ressourcen ändert sich regelmäßig. Links können verschwinden, Domains können den Betreiber wechseln, APIs können kostenpflichtig werden und Projekte können eingestellt werden. Der Status einer Ressource ist deshalb als zeitabhängige Information zu verstehen und nicht als dauerhafte Garantie.

Nicht zuverlässig verifizierbare Angaben werden als unbekannt gekennzeichnet und nicht geraten.

## Beiträge

Beiträge sollten:

1. Nach Möglichkeit eine kanonische URL enthalten.
2. Die Funktion der Ressource sachlich beschreiben.
3. Keine unbelegten Aussagen über Genauigkeit, Anonymität oder Rechtmäßigkeit enthalten.
4. Bekannte Anforderungen an Registrierung, API und Kosten dokumentieren.
5. Persönliche Empfehlungen von den Upstream-Daten getrennt halten.
6. Niemals Zugangsdaten, private Daten, API-Schlüssel oder Untersuchungsziele einchecken.

## Lizenz

Eigener Code und eigene Dokumentation dieses Projekts werden unter der MIT-Lizenz veröffentlicht. Inhalte des externen OSINT Frameworks unterliegen den jeweiligen Lizenz- und Attribution-Bedingungen. Siehe [`THIRD-PARTY-NOTICES.md`](THIRD-PARTY-NOTICES.md).
