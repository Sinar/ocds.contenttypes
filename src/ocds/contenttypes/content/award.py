# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.vocabularies.catalog import CatalogSource
from zope import schema
from collective import dexteritytextindexer
from zope.interface import implementer

from ocds.contenttypes import _


class IAward(model.Schema):
    """ Marker interface and Dexterity Python Schema for Award
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('award.xml')

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
                title=_(u'Title'),
                description=_(u'''
                Award title
                '''),
                required=True,
                )
    dexteritytextindexer.searchable('description')
    description = schema.Text(
                title=_(u'Description'),
                description=_(u'''
                Award description
                '''),
                required=False,
                )

    # Award Status

    directives.widget(award_status=SelectFieldWidget)
    award_status = schema.List(
                title=_(u'Award Status'),
                description=_(u'''
                The current status of the award
                '''),

                default=[],
                value_type=schema.Choice(
                    vocabulary='ocds.AwardStatus'
                    ),
                required=False,
                )

    # Award date
    award_date = schema.Date(
        title=_(u'Award Date'),
        description=_(u'''
        The date of the contract award. This is usually the date on
        which a decision to award was made.
        '''),
        required=False,)

    # Value

    award_amount = schema.Float(
            title=_(u'Contract value'),
            description=_(u'''
            The total value of this award. In the case of a framework
            contract this may be the total estimated lifetime value, or
            maximum value, of the agreement. There may be more than one
            award per procurement. A negative value indicates that the
            award may involve payments from the supplier to the buyer
            (commonly used in concession contracts).
                '''),
            required=False,
            )

    directives.widget(award_currency=SelectFieldWidget)
    award_currency = schema.Choice(
            title=u'Contract Value Currency',
            description=u'Currency of the contract amount',
            required=False,
            vocabulary='collective.vocabularies.iso.currencies',
            )

    # Suppliers

    directives.widget('suppliers',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basepath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )
    suppliers = RelationList(
            title=u'Suppliers',
            description=_(u'''
            Entities awarded or contracted to provide goods, works or
            services.
            '''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type='Organization'),
                ),
            required=False,
            )


    # Items Awarded

    # Contract period
    
    # startDate
    contractPeriod_startDate = schema.Date(
        title=_(u'Contract Start Date'),
        description=_(u'''
        The start date for the period. When known, a precise start date
        must always be provided.
        '''),
        required=False,)

    # endDate
    contractPeriod_endDate = schema.Date(
        title=_(u'Contract End Date'),
        description=_(u'''
        The end date for the period. When known, a precise end date must
        always be provided.
        '''),
        required=False,)

    # period_maxExtentDate
    contractPeriod_maxExtentDate = schema.Date(
            title=_(u'Contract Maximum extent'),
            description=_(u'''
            The period cannot be extended beyond this date. This field
            is optional, and can be used to express the maximum
            available data for extension or renewal of this period.
            '''),
            required=False,)

    # Documents (as OCDS Documents)

    # Amendment implemented as versioning

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


@implementer(IAward)
class Award(Container):
    """
    """
