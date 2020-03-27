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

    # Parties
    # OCDS Party roles implemented as relationships

    dexteritytextindexer.searchable('notes')
    notes = RichText(
         title=_(u'Notes'),
         description=_(u'''
            Notes about this procurement process
            '''),
         required=False
     )

    # buyer

    directives.widget('buyer',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    buyer = RelationChoice(
            title=u'Buyer',
            description=_(u"""
            A buyer is an entity whose budget will be used to pay for
            goods, works or services related to a contract.
            """),
            source=CatalogSource(portal_type='Organization'),
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
    
    # tenderers

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

    # funder

    directives.widget('funders',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )


    funders = RelationList(
            title=u'Funders',
            description=_(u'''
            The funder is an entity providing money or finance for this
            contracting process.
            '''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type='Organization'),
                ),
            required=False,
            )

    # enquirer
    # payer
    # payee

    # reviewBody

    directives.widget('reviewBody',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    reviewBody = RelationChoice(
            title=u'Review Body',
            description=_(u'''
            A party responsible for the review of this procurement
            process. This party often has a role in any challenges made
            to the contract award.
            '''),
            source=CatalogSource(portal_type='Organization'),
            required=False,
            )

    # interestedParty

    directives.widget('interestedParties',
                      RelatedItemsFieldWidget,
                      pattern_options={
                        'basePath': '/',
                        'mode': 'auto',
                        'favourites': [],
                        }
                      )

    interestedParties = RelationList(
            title=u'Interested Parties',
            description=_(u'''
            Parties that has expressed an interest in the contracting
            process: for example, by purchasing tender documents or
            submitting clarification questions.
            '''),
            default=[],
            value_type=RelationChoice(
                source=CatalogSource(portal_type='Organization'),
                ),
            required=False,
            )
    
    # fieldset set the tabs on the edit form

    fieldset(
            'parties',
            label=_(u'Parties'),
            fields=[
                'buyer',
                'procuringEntity',
                'suppliers',
                'funders',
                'reviewBody',
                'interestedParties',
                ],
            )


@implementer(IOCDSRelease)
class OCDSRelease(Container):
    """
    """
