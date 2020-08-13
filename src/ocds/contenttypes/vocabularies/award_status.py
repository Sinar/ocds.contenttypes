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
class AwardStatus(object):
    """
    """

    def __call__(self, context):
        # An award moves through multiple states. Releases over time can update
        # the status of an award.
        # https://standard.open-contracting.org/latest/en/schema/codelists/#award-status

        items = [
            VocabItem(u'pending', _(u'Pending')),
            VocabItem(u'active', _(u'Active')),
            VocabItem(u'cancelled', _(u'Cancelled')),
            VocabItem(u'uncessfull', _(u'Unsuccessful')),
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


AwardStatusFactory = AwardStatus()
