# Username / Specific Sites

> Automatisch aus dem offiziellen OSINT Framework erzeugt. Nicht manuell bearbeiten.
> Die Namen und Beschreibungen der externen Ressourcen bleiben im Original, damit keine Bedeutungen verfälscht werden.

**Anzahl Ressourcen:** 7

## Amazon Usernames (M)

- **URL:** https://www.google.com/search?q=site:amazon.com+%3Cusername%3E
- **Kategorie:** Username / Specific Sites
- **Beschreibung:** Google dork that searches Amazon.com for pages associated with a specific username, surfacing public profiles, wishlists, and reviews.
- **Status:** live
- **Kosten:** free
- **Registrierung:** False
- **API:** False

## Github User (M)

- **URL:** https://api.github.com/users/%3Cusername%3E/events/public
- **Kategorie:** Username / Specific Sites
- **Beschreibung:** Queries the GitHub public Events API to retrieve a user's recent public activity, including pushes, pull requests, issues, and other repository events.
- **Status:** live
- **Kosten:** free
- **Registrierung:** False
- **API:** True

## Keybase

- **URL:** https://keybase.io/
- **Kategorie:** Username / Specific Sites
- **Beschreibung:** Platform for cryptographic identity verification, linking social media accounts, PGP keys, and cryptocurrency addresses to a single profile. Acquired by Zoom in 2020 but still operational.
- **Status:** live
- **Kosten:** free
- **Registrierung:** False
- **API:** True

## MIT PGP Key Server

- **URL:** https://pgp.mit.edu/
- **Kategorie:** Username / Specific Sites
- **Beschreibung:** MIT PGP Public Key Server for searching, submitting, and removing PGP public keys. Look up keys by name, email, or key ID to find associated cryptographic identities.
- **Status:** live
- **Kosten:** free
- **Registrierung:** False
- **API:** True

## ProtonMail Domains (M)

- **URL:** https://api.protonmail.ch/pks/lookup?op=index&search=<email_address>
- **Kategorie:** Username / Specific Sites
- **Beschreibung:** Queries ProtonMail's HKP key server with a full email address to check for a PGP public key. Useful for identifying ProtonMail users on custom domains.
- **Status:** live
- **Kosten:** free
- **Registrierung:** False
- **API:** True

## ProtonMail users (M)

- **URL:** https://api.protonmail.ch/pks/lookup?op=index&search=<username>@protonmail.com
- **Kategorie:** Username / Specific Sites
- **Beschreibung:** Queries ProtonMail's HKP-compatible PGP key server to look up the public key for a ProtonMail username. A successful response confirms the account exists.
- **Status:** live
- **Kosten:** free
- **Registrierung:** False
- **API:** True

## Tinder Usernames (M)

- **URL:** https://www.gotinder.com/@%3Cusername%3E
- **Kategorie:** Username / Specific Sites
- **Beschreibung:** Accesses a Tinder user's public web profile via their username. The gotinder.com domain redirects to tinder.com.
- **Status:** live
- **Kosten:** free
- **Registrierung:** False
- **API:** False
