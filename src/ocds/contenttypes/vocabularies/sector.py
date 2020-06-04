# -*- coding: utf-8 -*-

# from plone import api
from ocds.contenttypes import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class Sector(object):
    """
    """

    def __call__(self, context):

        items = [
            VocabItem(u'education', _(u'Education')),
            VocabItem(u'health', _(u'Health')),
            VocabItem(u'energy', _(u'Energy')),
            VocabItem(u'communications', _(u'Communications')),
            VocabItem(u'waterAndWaste', _(u'Water and waste')),
            VocabItem(u'governance', _(u'Governance')),
            VocabItem(u'economy', _(u'Economy')),
            VocabItem(u'cultureSportsAndRecreation', 
                      _(u'Culture, sports and recreation')),
            VocabItem(u'transport', _(u'Transport')),
            VocabItem(u'transport.air', _(u'Air transport')),
            VocabItem(u'transport.water', _(u'Water traansport')),
            VocabItem(u'transport.rail', _(u'Transport rail')),
            VocabItem(u'transport.road', _(u'Transport road')),
            VocabItem(u'transport.urban', _(u'Transport urban')),
            VocabItem(u'socialHousing', _(u'Social housing')),
            ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


SectorFactory = Sector()
