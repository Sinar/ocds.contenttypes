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


class IRelatedAwardsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IRelatedAwards(model.Schema):
    """
    """

    # awards

    directives.widget('related_awards',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    related_awards = RelationList(
            title=u'Related Contract Awards',
            description=_(u'''
            Related Contract Awards
            '''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type='Award'),
                ),
            required=False,
            )


@implementer(IRelatedAwards)
@adapter(IRelatedAwardsMarker)
class RelatedAwards(object):
    def __init__(self, context):
        self.context = context

    @property
    def related_awards(self):
        if safe_hasattr(self.context, 'related_awards'):
            return self.context.related_awards
        return None

    @related_awards.setter
    def related_awards(self, value):
        self.context.related_awards = value
