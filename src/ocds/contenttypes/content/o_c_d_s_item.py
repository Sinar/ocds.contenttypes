# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from collective import dexteritytextindexer
from zope import schema
from zope.interface import implementer


from ocds.contenttypes import _


class IOCDSItem(model.Schema):
    """ Marker interface and Dexterity Python Schema for OCDSItem
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('o_c_d_s_item.xml')
    
    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
                title=_(u'Title'),
                description=_(u'''
                Name of item associted with tender, award or contract
                '''),
                required=True,
                )
    dexteritytextindexer.searchable('description')
    description = schema.Text(
                title=_(u'Description'),
                description=_(u'''
                A description of the goods, services to be provided.
                '''),
                required=False,
                )

    # Classificaiton 
    # TODO
    
    # Quantity

    quantity = schema.Float(
            title=_(u'Quantity'),
            description=_(u'The number of units to be provided.'),
            required=False,
            )

    unit = schema.TextLine(
            title=_(u'Unit'),
            description=_(u'''
            A description of the unit in which the supplies, services or
            works are provided (e.g. hours, kilograms) and the
            unit-price.
            '''),
            required=False,
            )

    # Unit

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(IOCDSItem)
class OCDSItem(Container):
    """
    """
