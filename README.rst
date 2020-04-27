.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=================
ocds.contenttypes
=================

Open Contracting Data Standard Compliant Plone content types.

This add-on is for tracking procurements and contracts, and uses
popolo.contenttypes to provide links and info on persons and
orgnizations for transparency and reporting purposes.

It is not meant to be a complete implementation of OCDS, but will be
able to export OCDS compliant data.

Features
--------

- OCDS Relesae with Parties linked to popolo.contenttypes
- OCDS Planning, Tender, Bids, Award, Contract, Implementation and
  Amendment content types at basic level.
- OC4IDS Infrastructure Project Tracking

Examples
--------

This add-on can be seen in action at the following sites:
- https://politikus.sinarproject.org
- https://hivos.sinarproject.org


Documentation
-------------

TODO

Translations
------------

TODO

Installation
------------

Install ocds.contenttypes by adding it to your buildout::

    [buildout]

    ...

    eggs =
        ocds.contenttypes


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/ocds.contenttypes/issues
- Source Code: https://github.com/collective/ocds.contenttypes
- Documentation: TODO


Support
-------

If you are having issues, please let us know.

License
-------

The project is licensed under the GPLv2.

Credits
-------

This project is supported by Hivos East Africa, Nation Media Group.
Indirectly via IDRC, Alternatives, (Montreal) and the kind individual
contributors to Sinar Project.

Also this project would not be possible without the contributors to
the Open Contracting Data Standard
