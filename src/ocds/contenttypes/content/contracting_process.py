# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from collective import dexteritytextindexer
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from zope import schema
from zope.interface import implementer
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.vocabularies.catalog import CatalogSource

from ocds.contenttypes import _


class IContractingProcess(model.Schema):
    """ Marker interface and Dexterity Python Schema for ContractingProcess
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('contracting_process.xml')

    # Infrastructure Project
    directives.widget('InfrastructureProject',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    InfrastructureProject = RelationChoice(
            title=u'Infrasructure Project',
            description=_(u'''
            Infrastructure Project this contract is part of
            '''),
            source=CatalogSource(portal_type='Infrastructure Project'),
            required=False,
            )

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

    directives.widget(project_nature=SelectFieldWidget)
    project_nature = schema.List(
                title=_(u'Nature'),
                description=_(u'''
                Whether this contracting process relates to the design,
                construction and/or supervision of the project, from the
                contractNature codelist. More than one value may be
                provided if the contract is for both design and
                construction, or both design and supervision, etc.
                '''),

                default=[],
                value_type=schema.Choice(
                    vocabulary='ocds.ContractNature'
                    ),
                required=False,
                )

    directives.widget(project_status=SelectFieldWidget)
    project_status = schema.Choice(
        title=_(u'Project Status'),
        description=_(u'''
        The current phase or status of this project
        '''),

        required=False,
        vocabulary='ocds.ProjectStatus',
        )

    # Tender Process

    directives.widget(procurementMethod=SelectFieldWidget)
    procurementMethod = schema.Choice(
        title=_(u'Procurement Method'),
        description=_(u'''
        '''),
        required=False,
        vocabulary='ocds.Method',
        )

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

    costEstimate_amount = schema.Decimal(
            title=_(u'Cost estimate'),
            description=_(u'Amount as a number'),
            required=False,
            )

    directives.widget(costEstimate_currency=SelectFieldWidget)
    costEstimate_currency = schema.Choice(
            title=u'Cost Estimate Currency',
            description=u'Currency of the estimate amount',
            required=False,
            vocabulary='collective.vocabularies.iso.currencies',
            )

    numberOfTenderers = schema.Int(
            title=_(u'Number of tenderers'),
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

    # suppliers
    directives.widget('suppliers',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    # administrativeEntity
    directives.widget('administrativeEntity',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    administrativeEntity = RelationChoice(
            title=u'Administrative Entity',
            description=_(u'''
            The name and identifier of the entity responsible for
            contract administration if this is different from the
            procuring entity.administrativeEntity
            '''),
            source=CatalogSource(portal_type='Organization'),
            required=False,
            )

    # suppliers
    directives.widget('suppliers',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
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

    contractValue_amount = schema.Decimal(
            title=_(u'Contract value'),
            description=_(u'The initial value of the contract'),
            required=False,
            )

    directives.widget(contractValue_currency=SelectFieldWidget)
    contractValue_currency = schema.Choice(
            title=u'Contract Value Currency',
            description=u'Currency of the contract amount',
            required=False,
            vocabulary='collective.vocabularies.iso.currencies',
            )

    # startDate
    contractPeriod_startDate = schema.Date(
        title=_(u'Start Date'),
        description=_(u'''
        The start date for the period. When known, a precise start date
        must always be provided.
        '''),
        required=False,)

    # endDate
    contractPeriod_endDate = schema.Date(
        title=_(u'End Date'),
        description=_(u'''
        The end date for the period. When known, a precise end date must
        always be provided.
        '''),
        required=False,)

    # period_maxExtentDate
    contractPeriod_maxExtentDate = schema.Date(
            title=_(u'Maximum extent'),
            description=_(u'''
            The period cannot be extended beyond this date. This field
            is optional, and can be used to express the maximum
            available data for extension or renewal of this period.
            '''),
            required=False,)

    finalValue_amount = schema.Decimal(
            title=_(u'Final value'),
            description=_(u'''
            This should be provided when the contracting process is
            complete. This may be derived from the sum of
            contract.implementation.transactions values in linked OCDS
            data where available. In other cases, it may need to be
            identified and entered manually based on other project
            documentation.
            '''),
            required=False,
            )

    directives.widget(finalValue_currency=SelectFieldWidget)
    finalValue_currency = schema.Choice(
            title=u'Final Contract Value Currency',
            description=u'Currency of the final contract amount',
            required=False,
            vocabulary='collective.vocabularies.iso.currencies',
            )

    # Modification implemented as content type

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
