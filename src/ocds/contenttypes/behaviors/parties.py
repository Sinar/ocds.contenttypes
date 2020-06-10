# -*- coding: utf-8 -*-

from ocds.contenttypes import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from plone.supermodel.directives import fieldset
from collective import dexteritytextindexer
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.vocabularies.catalog import CatalogSource


class IPartiesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IParties(model.Schema):
    """
    """

    # Parties
    # OCDS Party roles implemented as relationships

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
            Entity responsible for contract administration
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
                'tenderers',
                'funders',
                'reviewBody',
                'interestedParties',
                ],
            )


@implementer(IParties)
@adapter(IPartiesMarker)
class Parties(object):
    def __init__(self, context):
        self.context = context

    @property
    def buyer(self):
        if safe_hasattr(self.context, 'buyer'):
            return self.context.buyer
        return None

    @buyer.setter
    def buyer(self, value):
        self.context.buyer = value

    @property
    def procuringEntity(self):
        if safe_hasattr(self.context, 'procuringEntity'):
            return self.context.procuringEntity
        return None

    @procuringEntity.setter
    def procuringEntity(self, value):
        self.context.procuringEntity = value

    @property
    def suppliers(self):
        if safe_hasattr(self.context, 'suppliers'):
            return self.context.suppliers
        return None

    @suppliers.setter
    def suppliers(self, value):
        self.context.suppliers = value

    @property
    def suppliers(self):
        if safe_hasattr(self.context, 'suppliers'):
            return self.context.suppliers
        return None

    @suppliers.setter
    def suppliers(self, value):
        self.context.suppliers = value

    @property
    def tenderers(self):
        if safe_hasattr(self.context, 'tenderers'):
            return self.context.tenderers
        return None

    @tenderers.setter
    def tenderers(self, value):
        self.context.tenderers = value

    @property
    def funders(self):
        if safe_hasattr(self.context, 'funders'):
            return self.context.funders
        return None

    @funders.setter
    def funders(self, value):
        self.context.funders = value

    @property
    def reviewBody(self):
        if safe_hasattr(self.context, 'reviewBody'):
            return self.context.reviewBody
        return None

    @reviewBody.setter
    def reviewBody(self, value):
        self.context.reviewBody = value

    @property
    def reviewBody(self):
        if safe_hasattr(self.context, 'reviewBody'):
            return self.context.reviewBody
        return None

    @reviewBody.setter
    def reviewBody(self, value):
        self.context.reviewBody = value

    @property
    def interestedParties(self):
        if safe_hasattr(self.context, 'interestedParties'):
            return self.context.interestedParties
        return None

    @interestedParties.setter
    def interestedParties(self, value):
        self.context.interestedParties = value
