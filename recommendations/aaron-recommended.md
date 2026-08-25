# Aarons empfohlene OSINT-Ressourcen

Diese Seite ist bewusst von den Daten des offiziellen OSINT Frameworks getrennt. Sie enthält eine persönliche Auswahl empfohlener Ressourcen und kann unabhängig vom Upstream-Dataset weiterentwickelt werden.

> **Status:** Ausgangsbasis. Jede Ressource sollte regelmäßig erneut geprüft werden, bevor sie als aktuell und einsatzbereit betrachtet wird.

## Identität und Benutzernamen

| Ressource | URL | Hauptzweck | Hinweise |
|---|---|---|---|
| WhatsMyName | https://whatsmyname.app/ | Suche nach Benutzernamen | Schnelle plattformübergreifende Suche |
| Sherlock | https://github.com/sherlock-project/sherlock | Suche nach Benutzernamen | Lokales CLI; direkte Anfragen an Zielplattformen |
| Namechk | https://namechk.com/ | Benutzername- und Domainprüfung | Geeignet für eine erste Zuordnung |
| Keybase | https://keybase.io/ | Identitäts- und Schlüsselzuordnung | Öffentliche kryptografische Identitätsdaten |
| Sylva Identity Discovery | https://sylva.pfeister.dev/ | Identitätssuche | Geeignet für weitere Recherchezweige aus bekannten Kennungen |

## E-Mail und Identitätszuordnung

| Ressource | URL | Hauptzweck | Hinweise |
|---|---|---|---|
| Hunter | https://hunter.io/ | Recherche geschäftlicher E-Mail-Adressen | Suche nach Domain und Namen; Dienstbeschränkungen beachten |
| OSINT Industries | https://www.osint.industries/ | Kontenzuordnung | Ergebnisse als Recherchehinweise behandeln und verifizieren |
| theHarvester | https://github.com/laramies/theHarvester | Passive Datensammlung | Domains, E-Mail-Adressen, Subdomains und URLs aus öffentlichen Quellen |
| GHunt | https://github.com/mxrch/GHunt | Google-Konto-OSINT | Aktuelle Kompatibilität und OPSEC beachten |

## Web, Domains und Infrastruktur

| Ressource | URL | Hauptzweck | Hinweise |
|---|---|---|---|
| OSINT Framework | https://osintframework.com/ | Ressourcen finden | Zentrale Upstream-Quelle dieses Projekts |
| SecurityTrails | https://securitytrails.com/ | DNS- und Domaininformationen | Historische DNS- und Infrastrukturinformationen |
| crt.sh | https://crt.sh/ | Certificate Transparency | Suche nach Hostnamen anhand von Zertifikaten |
| Shodan | https://www.shodan.io/ | Öffentlich erreichbare Dienste | Nur für rechtmäßige Recherche und Analyse verwenden |
| Censys | https://search.censys.io/ | Internet-Infrastruktur | Suche nach Zertifikaten, Hosts und Diensten |

## GitHub und Code-Recherche

| Ressource | URL | Hauptzweck | Hinweise |
|---|---|---|---|
| GitHub | https://github.com/ | Recherche öffentlicher Repositories und Quelltexte | Öffentliche Repositories und Versionshistorie durchsuchen |
| GitFive | https://github.com/mxrch/GitFive | Untersuchung von GitHub-Profilen | Zuordnung öffentlich verfügbarer GitHub-Artefakte |

## Methodik

Eine Empfehlung ist kein Untersuchungsergebnis. Wichtige Feststellungen sollten mit unabhängigen Quellen überprüft werden. Zeitstempel, URLs und relevanter Kontext sollten nachvollziehbar dokumentiert werden.

Empfohlener Ablauf:

1. **Fragestellung definieren.**
2. **Mit der am wenigsten eingreifenden öffentlichen Quelle beginnen.**
3. **Zunächst Kennungen erfassen, nicht Schlussfolgerungen.**
4. **Nur auf bestätigten Kennungen weiterrecherchieren.**
5. **Ergebnisse mit unabhängigen Quellen abgleichen.**
6. **Zeitstempel und Herkunft dokumentieren.**
7. **Unsicherheiten ausdrücklich kennzeichnen.**
8. **Recherche beenden, sobald die Fragestellung beantwortet ist.**
