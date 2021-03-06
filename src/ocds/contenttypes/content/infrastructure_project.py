# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from collective import dexteritytextindexer
# from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from zope import schema
from zope.interface import implementer


from ocds.contenttypes import _


class IInfrastructureProject(model.Schema):
    """ Marker interface and Dexterity Python Schema for InfrastructureProject
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('infrastructure_project.xml')

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
                title=_(u'Title'),
                description=_(u'''
                The title of the project.
                '''),
                required=True,
                )
    dexteritytextindexer.searchable('description')
    description = schema.Text(
                title=_(u'Description'),
                description=_(u'''
                A description of this project. This should usually be no
                longer than a single paragraph.
                '''),
                required=False,
                )

    id_reference = schema.TextLine(
                title=_(u'Identifier or Reference'),
                description=_(u'''
                A unique identifier or reference number for this
                infrastructure project.
                '''
                              ),
                required=False,
                )

    # status
    # https://standard.open-contracting.org/infrastructure/latest/en/reference/codelists/#projectstatus

    directives.widget(project_status=SelectFieldWidget)
    project_status = schema.Choice(
        title=_(u'Project Status'),
        description=_(u'''
        The current phase or status of this project
        '''),

        required=False,
        vocabulary='ocds.ProjectStatus',
        )

    # Project Period as fieldset

    # startDate
    project_startDate = schema.Date(
        title=_(u'Start Date'),
        description=_(u'''
        The start date for the period. When known, a precise start date
        must always be provided.
        '''),
        required=False,)

    # endDate
    project_endDate = schema.Date(
        title=_(u'End Date'),
        description=_(u'''
        The end date for the period. When known, a precise end date must
        always be provided.
        '''),
        required=False,)

    # period_maxExtentDate

    project_maxExtentDate = schema.Date(
            title=_(u'Maximum extent'),
            description=_(u'''
            The period cannot be extended beyond this date. This field
            is optional, and can be used to express the maximum
            available data for extension or renewal of this period.
            '''),
            required=False,)

    # period_durationInDays
    # Implemented as view

    # Project Sector
    # https://standard.open-contracting.org/infrastructure/latest/en/reference/codelists/#projectsector

    directives.widget(project_sector=SelectFieldWidget)
    project_sector = schema.Choice(
        title=_(u'Project Sector'),
        required=False,
        vocabulary='ocds.sector',
        )

    purpose = schema.Text(
            title=_(u'Project purpose'),
            description=_(u'The socioeconomic purpose of this project'),
            required=False,
            )

    # additionalClassifications

    # project_type


    directives.widget(project_sector=SelectFieldWidget)
    project_sector = schema.Choice(
        title=_(u'Project Sector'),
        required=False,
        vocabulary='ocds.sector',
        )
    directives.widget(project_type=SelectFieldWidget)
    project_type = schema.Choice(
        title=_(u'Project Type'),
        required=False,
        vocabulary='ocds.projecttypes',
        )

    # AssetLifeTime
    # assetLifeTime_start_date
    # assetLifeTime_end_date
    # assetLifeTime_maxExtentDate
    # assetLifeTime_durationInDays

    # Asset startDate
    assetLifetime_startDate = schema.Date(
        title=_(u'Asset Start Date'),
        description=_(u'''
        The start date for the asset. When known, a precise start date
        must always be provided.
        '''),
        required=False,)

    # Asset endDate
    assetLifetime_endDate = schema.Date(
        title=_(u'Asset End Date'),
        description=_(u'''
        The end date for the period. When known, a precise asset end
        date must always be provided.
        '''),
        required=False,)

    # Asset period_maxExtentDate

    assetLifetime_maxExtentDate = schema.Date(
            title=_(u'Asset Maximum extent'),
            description=_(u'''
            The period cannot be extended beyond this date. This field
            is optional, and can be used to express the maximum
            available data for extension or renewal of this period.
            '''),
            required=False,
            )

    fieldset('Asset Lifetime',
             fields=['assetLifetime_startDate',
                     'assetLifetime_endDate',
                     'assetLifetime_maxExtentDate',
                     ])

    # locations

    # budget

    budget_amount = schema.Decimal(
            title=_(u'Budget Amount'),
            description=_(u'''
            The projected costs or allocated budget for
            the project'''),
            required=False,
            )

    # budget_currency
    directives.widget(budget_currency=SelectFieldWidget)
    budget_currency = schema.Choice(
            title=u'Budget Currency',
            description=u'Currency of the budget amount',
            required=False,
            vocabulary='collective.vocabularies.iso.currencies',
            )

    budget_approvalDate = schema.Date(
            title=_(u'Budget Approval Date'),
            description=_(u'''
            The date on which the project budget was approved. Where
            documentary evidence for this exists, it may be included
            amongst the project documents with the documentType set to
            ‘budgetApproval’.
            '''),
            required=False,
            )

    # budget_breakdown
    # implemented as content type

    # Parties
    # Implemented as a Behaviour

    # Contracting Processes
    # Implemented as content type

    # completion_endDate

    completion_endDate = schema.Date(
        title=_(u'Completion Date'),
        description=_(u'''
        The actual completion date for the project (compare with the
        endDate in project period.
            '''),
        required=False,
        )

    completion_endDate_details = RichText(
        title=_(u'Completion End Date Details'),
        description=_(u'''
        Details related to the endDate. This may be a justification for
        the contract’s completion date being different than in the
        original contract.
        '''),

        required=False,
        )

    # completion_endDateDetails
    completion_finalValue_amount = schema.Decimal(
            title=_(u'Final Value'),
            description=_(u'The total cost of this project at completion.'),
            required=False,
            )

    directives.widget(completion_finalValue_currency=SelectFieldWidget)
    completion_finalValue_currency = schema.Choice(
            title=u'Final  Currency',
            description=u'Currency of the budget amount',
            required=False,
            vocabulary='collective.vocabularies.iso.currencies',
            )

    completion_finalValue_details = RichText(
        title=_(u'Final value details'),
        description=_(u'''
        Details related to the final value. This may be a justification
        for the completed project’s value being different than in the
        original or latest revised budget.
        '''),
        required=False,
        )

    completion_finalScope = schema.Text(
        title=_(u'Final Scope'),
        description=_(u'''
        A short description of the final scope of the project at
        completion.
        '''),
        required=False,
        )

    completion_finalScopeDetails = RichText(
        title=_(u'Final scope details'),
        description=_(u'''
        A reason, explanation or justification for any variation between
        the anticipated scope (compare to the projectScope document) and
        the final scope at completion. If appropriate, additional
        details may be included in the documents section, with a title
        indicating that these documents will describe and differences
        between the planned and completed scope of work.
        '''),
        required=False,
        )

    fieldset('Completion', fields=[
        'completion_endDate',
        'completion_endDate_details',
        'completion_finalValue_amount',
        'completion_finalValue_currency',
        'completion_finalValue_details',
        'completion_finalScope',
        'completion_finalScopeDetails',
        ]
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

@implementer(IInfrastructureProject)
class InfrastructureProject(Container):
    """
    """
