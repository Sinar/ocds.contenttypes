# -*- coding: utf-8 -*-

from ocds.contenttypes import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from plone.supermodel.directives import fieldset
from collective import dexteritytextindexer
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.vocabularies.catalog import CatalogSource



class IRelatedOCDSReleasesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IRelatedOCDSReleases(model.Schema):
    """
    """

    # related OCDS releases or procurement process

    directives.widget('related_releases',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    related_releases = RelationList(
            title=u'Related Procurement or Contracting Process',
            description=_(u'''
            '''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type='OCDS Release'),
                ),
            required=False,
            )

@implementer(IRelatedOCDSReleases)
@adapter(IRelatedOCDSReleasesMarker)
class RelatedOCDSReleases(object):
    def __init__(self, context):
        self.context = context

    @property
    def related_releases(self):
        if safe_hasattr(self.context, 'related_releases'):
            return self.context.related_releases
        return None

    @related_releases.setter
    def related_releases(self, value):
        self.context.related_releases = value
