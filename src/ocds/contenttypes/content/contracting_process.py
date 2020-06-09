# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from collective import dexteritytextindexer
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


from ocds.contenttypes import _


class IContractingProcess(model.Schema):
    """ Marker interface and Dexterity Python Schema for ContractingProcess
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('contracting_process.xml')

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
                title=_(u'Title'),
                description=_(u'''
                The formal name of this contracting process. Once set,
                this should not normally by changed.
                '''),
                required=True,
                )
    dexteritytextindexer.searchable('description')
    description = schema.Text(
                title=_(u'Description'),
                description=_(u'''
                The description should summarise the purpose of this
                contract and the scope of work to be undertaken.
                '''),
                required=False,
                )

    ExternalReference = schema.TextLine(
                title=_(u'External Reference'),
                description=_(u'''
                If this contracting process is identified by some
                external reference number it may be recorded here.
                '''),
                required=False,
                )


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


@implementer(IContractingProcess)
class ContractingProcess(Container):
    """
    """
