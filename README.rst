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

.. image:: https://sinarproject.org/media/hivos_logo-1.png/@@images/7485dd1c-7b0c-47a7-a940-d7966445764f.png
    :alt: Hivos Logo
.. image:: https://sinarproject.org/media/partner-logos/copy_of_od4d.png/@@images/a9c51168-cbba-4ee1-9978-bd7c43136657.png
    :alt: Open Data for Development Logo

This project is funded and supported by Hivos East Africa, and
indirectly via International Development Research Centre (IDRC) Canada.

This project would not be possible without Open Contracting Data
Standards https://standard.open-contracting.org/latest/en developed by
the Open Contracting Partnership https://www.open-contracting.org/
