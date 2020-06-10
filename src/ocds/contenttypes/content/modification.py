# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
from plone.app.z3cform.widget import SelectFieldWidget
# from z3c.form.browser.radio import RadioFieldWidget
from collective import dexteritytextindexer
from zope import schema
from zope.interface import implementer
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from z3c.relationfield.schema import RelationChoice
# from z3c.relationfield.schema import RelationList
from plone.app.vocabularies.catalog import CatalogSource


from ocds.contenttypes import _


class IModification(model.Schema):
    """ Marker interface and Dexterity Python Schema for Modification
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('modification.xml')

    # contractingProcess
    directives.widget('contractingProcess',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    contractingProcess = RelationChoice(
            title=u'Contracting Process',
            description=_(u'''
            The Contracting Process this modification refers to
            '''),
            source=CatalogSource(portal_type='Contracting Process'),
            required=False,
            )

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
                title=_(u'Title'),
                description=_(u'''
                Modification title
                '''),
                required=True,
                )
    dexteritytextindexer.searchable('description')
    description = schema.Text(
                title=_(u'Description'),
                description=_(u'''
                Details of the modification.
                '''),
                required=False,
                )

    rationale = RichText(
         title=_(u'Rationale'),
         description=_(u'''
         A summary of the reasons which have led to this modification to
         the originally planned scope, period or value.
         '''),
         required=False
    )

    directives.widget(modificationType=SelectFieldWidget)
    modificationType = schema.List(
        title=_(u'Type'),
        description=_(u'''
         Indicates whether the modification relates to the duration,
         value, scope or other aspect of the contract.
        '''),
        default=[],
        value_type=schema.Choice(
            vocabulary='ocds.ModificationType',
            ),
        required=False,
        )

    # OCDS Release ID (not used yet)

    oldContractValue = schema.Decimal(
            title=_(u'Old Contract Value'),
            description=_(u'''
            Contract value before the modification, taking into account
            any prior modifications.
            '''),
            required=False,
            )

    directives.widget(oldContractValue_currency=SelectFieldWidget)
    oldContractValue_currency = schema.Choice(
            title=u'Old Contract Value Currency',
            description=u'Currency of the old contract value',
            required=False,
            vocabulary='collective.vocabularies.iso.currencies',
            )

    newContractValue = schema.Decimal(
            title=_(u'New Contract Value'),
            description=_(u'''
            Contract value after the modification, taking into account
            any prior modifications.
            '''),
            required=False,
            )

    directives.widget(newContractValue_currency=SelectFieldWidget)
    newContractValue_currency = schema.Choice(
            title=u'New Contract Value Currency',
            description=u'Currency of the new contract value',
            required=False,
            vocabulary='collective.vocabularies.iso.currencies',
            )

    # startDate
    oldContractPeriod_startDate = schema.Date(
        title=_(u'Old Start Date'),
        description=_(u'''
        The start date for the period. When known, a precise start date
        must always be provided.
        '''),
        required=False,)

    # endDate
    oldContractPeriod_endDate = schema.Date(
        title=_(u'Old End Date'),
        description=_(u'''
        The end date for the period. When known, a precise end date must
        always be provided.
        '''),
        required=False,)

    # period_maxExtentDate
    oldContractPeriod_maxExtentDate = schema.Date(
            title=_(u'Old Maximum extent'),
            description=_(u'''
            The period cannot be extended beyond this date. This field
            is optional, and can be used to express the maximum
            available data for extension or renewal of this period.
            '''),
            required=False,)

    # startDate
    newContractPeriod_startDate = schema.Date(
        title=_(u'New Start Date'),
        description=_(u'''
        The start date for the period. When known, a precise start date
        must always be provided.
        '''),
        required=False,)

    # endDate
    newContractPeriod_endDate = schema.Date(
        title=_(u'New End Date'),
        description=_(u'''
        The end date for the period. When known, a precise end date must
        always be provided.
        '''),
        required=False,)

    # period_maxExtentDate
    newContractPeriod_maxExtentDate = schema.Date(
            title=_(u'New Maximum extent'),
            description=_(u'''
            The period cannot be extended beyond this date. This field
            is optional, and can be used to express the maximum
            available data for extension or renewal of this period.
            '''),
            required=False,)


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


@implementer(IModification)
class Modification(Container):
    """
    """
