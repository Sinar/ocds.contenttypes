# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.app.vocabularies.catalog import CatalogSource
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.supermodel.directives import fieldset
from collective import dexteritytextindexer

# from z3c.form.browser.radio import RadioFieldWidget
# from zope import schema
from zope.interface import implementer
from ocds.contenttypes import _


class IOCDSRelease(model.Schema):
    """ Marker interface and Dexterity Python Schema for OCDSRelease
    """

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    dexteritytextindexer.searchable('notes')
    notes = RichText(
         title=_(u'Notes'),
         description=_(u'''
            Notes about this procurement process
            '''),
         required=False
     )


@implementer(IOCDSRelease)
class OCDSRelease(Container):
    """
    """
