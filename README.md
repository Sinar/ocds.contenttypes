# politikus.ocds

[OCDS](https://standard.open-contracting.org) content types for
[Plone](https://plone.org) 6.2: OCDS releases and items, tender, award,
contracting process, modification, infrastructure project, and OCDS
documents.

Part of the [Politikus](https://github.com/Sinar/politikus) project, a CMS
for investigative journalism built on open data standards (Popolo, OCDS,
BODS). Depends on
[politikus.popolo](https://github.com/Sinar/politikus.popolo) for the
party (person/organization) content types.

## Content types

- **OCDS Release** — a single OCDS release (planning, tender, award,
  contract, implementation)
- **OCDS Item** — a collection of OCDS releases
- **Tender** — a call for proposals, with status, method, procurement
  category, award criteria
- **Award** — an award granted in a tender, with status, value, supplier
- **Contracting Process** — a tender + award pair, with contract status
  and nature
- **Modification** — a modification of a contracting process
- **Infrastructure Project** — an infrastructure project, with status,
  sector, milestones
- **OCDS Document** — a document attached to any OCDS content type

## Installation

This add-on is developed as a source checkout inside the
[politikus buildout](https://github.com/Sinar/politikus) (mr.developer,
`branch=plone6`). Create a Plone site, then install `politikus.ocds` via
the Plone Add-ons screen (after `politikus.popolo`).

## Testing

The test suite runs with `zope.testrunner` against a Plone 6.2 egg set:

```shell
zope-testrunner --test-path src -s politikus.ocds \
    -t 'test_(behavior|ct|setup|view|viewlet|vocab)'
```

Robot tests (`tests/robot/*.robot`) need a browser and are excluded from
the fast loop.

Locale catalogs (`locales/`) are updated with the buildout's
`bin/i18n-extract` and `bin/i18n-compile` scripts; compiled `.mo` files
are committed.

## Credits

Generated from the [plonecli](https://github.com/plone/plonecli) `addon`
template (bobtemplates.plone), carrying over the content of the former
`ocds.contenttypes` package.
