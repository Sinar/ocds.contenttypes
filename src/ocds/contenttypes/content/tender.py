# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
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


class ITender(model.Schema):
    """ Marker interface and Dexterity Python Schema for Tender
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('tender.xml')

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
                title=_(u'Title'),
                description=_(u'''
                A title for this tender. This will often be used by
                applications as a headline to attract interest, and to
                help analysts understand the nature of this procurement.
                '''),
                required=True,
                )
    dexteritytextindexer.searchable('description')
    description = schema.Text(
                title=_(u'Description'),
                description=_(u'''
                A summary description of the tender. This complements
                any structured information provided using the items
                array. Descriptions should be short and easy to read.
                Avoid using ALL CAPS.
                '''),
                required=False,
                )

    # procuringEntity
    directives.widget('procuringEntity',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    procuringEntity = RelationChoice(
            title=u'Procuring Entity',
            description=_(u'''
            The entity managing the procurement. This can be different
            from the buyer who pays for, or uses, the items being
            procured.
            '''),
            source=CatalogSource(portal_type='Organization'),
            required=False,
            )

    # Items

    # Value

    tender_value = schema.Float(
            title=_(u'Tender value'),
            description=_(u'''
            The total upper estimated value of the procurement. a
            negative value indicates that the contracting process may
            involve payments from the supplier to the buyer (commonly
            used in concession contracts).
                '''),
            required=False,
            )

    directives.widget(tender_value_currency=SelectFieldWidget)
    tender_value_currency = schema.Choice(
            title=u'Tender Value Currency',
            description=u'Currency of the tender amount',
            required=False,
            vocabulary='collective.vocabularies.iso.currencies',
            )

    tender_minValue = schema.Float(
            title=_(u'Tender Minumum Value'),
            description=_(u'''
            The minimum estimated value of the procurement. A negative
            value indicates that the contracting process may involve
            payments from the supplier to the buyer (commonly used in
                concession contracts).
                '''),
            required=False,
            )

    directives.widget(tender_minValue_currency=SelectFieldWidget)
    tender_minValue_currency = schema.Choice(
            title=u'Tender Value Currency',
            description=u'Currency of the minimum tender value',
            required=False,
            vocabulary='collective.vocabularies.iso.currencies',
            )

    # Procurement Method

    directives.widget(procurementMethod=SelectFieldWidget)
    procurementMethod = schema.Choice(
        title=_(u'Procurement Method'),
        description=_(u'''
        The procurement method
        '''),
        required=False,
        vocabulary='ocds.Method',
        )

    dexteritytextindexer.searchable('procurementMethodDetails')
    procurementMethodDetails = RichText(
        title=_(u'Procurement method details'),
        description=_(u'''
        Additional detail on the procurement method used. This field
        should be used to record an agreed list of procurement process
        types, such as: International Competitive Bidding, National
        Competitive Bidding, Donor Procurement Rules, Framework or
        Direct Award.
        '''),

        required=False,
        )

    dexteritytextindexer.searchable('procurementMethodRationale')
    procurementMethodRationale = RichText(
        title=_(u'Procurement method rationale'),
        description=_(u'''
        Rationale for the chosen procurement method. This is especially
        important to provide a justification in the case of limited
        tenders or direct awards.
        '''),
        required=False,
        )

    directives.widget(mainProcurementCategory=SelectFieldWidget)
    mainProcurementCategory = schema.Choice(
        title=_(u'Main procurement category'),
        description=_(u'''
        The primary category describing the main object of this
        contracting process.
        '''),
        required=False,
        vocabulary='ocds.ProjectCategory',
        )

    directives.widget(mainProcurementCategory=SelectFieldWidget)
    mainProcurementCategory = schema.Choice(
        title=_(u'Main procurement category'),
        description=_(u'''
        The primary category describing the main object of this
        contracting process
        '''),
        required=False,
        vocabulary='ocds.ProcurementCategory',
        )

    directives.widget(awardCriteria=SelectFieldWidget)
    awardCriteria = schema.Choice(
        title=_(u'Award criteria'),
        description=_(u'''
        The award criteria for the procurement
        '''),
        required=False,
        vocabulary='ocds.AwardCriteria',
        )

    dexteritytextindexer.searchable('awardCriteriaDetails')
    awardCriteriaDetails = RichText(
        title=_(u'Award criteria details'),
        description=_(u'''
        Any detailed or further information on the award or selection criteria.
        '''),
        required=False,
        )

    directives.widget(submissionMethod=SelectFieldWidget)
    submissionMethod = schema.Choice(
        title=_(u'Submission method'),
        description=_(u'''
        The methods by which bids are submitted
        '''),
        required=False,
        vocabulary='ocds.submissionMethod',
        )

    dexteritytextindexer.searchable('submissionMethodDetails')
    awardCriteriaDetails = RichText(
        title=_(u'Submission method details'),
        description=_(u'''
        Any detailed or further information on the submission method. This can
        include the address, e-mail address or online service to which bids are
        submitted, and any special requirements to be followed for submissions.
        '''),
        required=False,
        )

    # Tender Period

    # startDate
    tenderPeriod_startDate = schema.Date(
        title=_(u'Tender Start Date'),
        description=_(u'''
        The start date for the period. When known, a precise start date
        must always be provided.
        '''),
        required=False,)

    # endDate
    tenderPeriod_endDate = schema.Date(
        title=_(u'Tender End Date'),
        description=_(u'''
        The end date for the period. When known, a precise end date must
        always be provided.
        '''),
        required=False,)

    # period_maxExtentDate
    tenderPeriod_maxExtentDate = schema.Date(
            title=_(u'Tender Maximum extent'),
            description=_(u'''
            The period cannot be extended beyond this date. This field
            is optional, and can be used to express the maximum
            available data for extension or renewal of this period.
            '''),
            required=False,)

    # Enquiry Period

    # startDate
    enquiryPeriod_startDate = schema.Date(
        title=_(u'Enquiry Start Date'),
        description=_(u'''
        The start date for the period. When known, a precise start date
        must always be provided.
        '''),
        required=False,)

    # endDate
    enquiryPeriod_endDate = schema.Date(
        title=_(u'Enquiry End Date'),
        description=_(u'''
        The end date for the period. When known, a precise end date must
        always be provided.
        '''),
        required=False,)

    # period_maxExtentDate
    enquiryPeriod_maxExtentDate = schema.Date(
            title=_(u'Enquiry Maximum extent'),
            description=_(u'''
            The period cannot be extended beyond this date. This field
            is optional, and can be used to express the maximum
            available data for extension or renewal of this period.
            '''),
            required=False,)

    # Has Enquiries
    hasEnquiries = schema.Bool(
            title=_(u'Has enquiries?'),
            description=_(u'''
            Check if true.
            '''),
            required=False,)

    dexteritytextindexer.searchable('elegibilityCriteria')
    elegibilityCriteria = RichText(
        title=_(u'Elegibility Criteria'),
        description=_(u'''
        A description of any eligibility criteria for potential suppliers.
        '''),
        required=False,
        )

    # Evaluation Award Period

    # startDate
    awardPeriod_start = schema.Date(
        title=_(u'Enquiry Start Date'),
        description=_(u'''
        The start date for the period. When known, a precise start date
        must always be provided.
        '''),
        required=False,)

    # endDate
    awardPeriod_endDate = schema.Date(
        title=_(u'Enquiry End Date'),
        description=_(u'''
        The end date for the period. When known, a precise end date must
        always be provided.
        '''),
        required=False,)

    # period_maxExtentDate
    awardPeriod_maxExtentDate = schema.Date(
            title=_(u'Enquiry Maximum extent'),
            description=_(u'''
            The period cannot be extended beyond this date. This field
            is optional, and can be used to express the maximum
            available data for extension or renewal of this period.
            '''),
            required=False,)

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

    # Number of tenderers
    numberOfTenderers = schema.Int(
            title=_(u'Number of tenderers'),
            description=_(u'''
            The number of parties who submit a bid.
            '''),
            required=False,)

    # Tenderers
    directives.widget('tenderers',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    tenderers = RelationList(
            title=u'Tenderers',
            description=_(u'''
            All entities who submit a tender.
            '''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type='Organization'),
                ),
            required=False,
            )


    # not implemented for now
    
#    directives.widget(additionalProcurementCategory=SelectFieldWidget)
#    additionalProcurementCategory = schema.Choice(
#        title=_(u'Main procurement category'),
#        description=_(u'''
#        The primary category describing the main object of this
#        contracting process.
#        '''),
#        required=False,
#        vocabulary='ocds.AdditionalProjectCategory',
#        )



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


@implementer(ITender)
class Tender(Container):
    """
    """
