# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


from ocds.contenttypes import _


class IInfrastructureProject(model.Schema):
    """ Marker interface and Dexterity Python Schema for InfrastructureProject
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('infrastructure_project.xml')

    title = schema.TextLine(
                title=_(u'Title'),
                description=_(u'''
                The title of the project.
                '''),
                required=True,
                )

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

    # Project Period as fieldset
    # period_start_date
    # period_end_date
    # period_maxExtentDate
    # period_durationInDays

    # Project Sector
    # https://standard.open-contracting.org/infrastructure/latest/en/reference/codelists/#projectsector

    purpose = schema.Text(
            title=_(u'Project purpose'),
            description=_(u'The socioeconomic purpose of this project'),
            required=False,
            )

    # additionalClassifications

    # project_type

    project_type = schema.Choice(
        title=_(u'Project Type'),
        required=False,
        vocabulary='ocds.contenttypes.projecttypes',
        )

    # AssetLifeTime
    # assetLifeTime_start_date
    # assetLifeTime_end_date
    # assetLifeTime_maxExtentDate
    # assetLifeTime_durationInDays

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
    # budget_breakdown
   

    # Parties
    # Implemented as a Behaviour 

    #completion_endDate
    #completion_endDateDetails

    completion_finalValue_amount = schema.Decimal(
            title=_(u'Final Value'),
            description=_(u'The total cost of this project at completion.'),
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

@implementer(IInfrastructureProject)
class InfrastructureProject(Container):
    """
    """
