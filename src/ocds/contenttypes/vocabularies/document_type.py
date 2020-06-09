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
class DocumentType(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u'needsAssessment', _(u'Needs Assessment')),
            VocabItem(u'valueForMoneyAnalysis',
                      _(u'Value for money analysis')),
            VocabItem(u'technicalSpecifications',
                      _(u'Technical Specifications')),
            VocabItem(u'serviceDescription',
                      _(u'Service Description')),
            VocabItem(u'serviceDescription',
                      _(u'Service Description')),
            VocabItem(u'estimatedDemand',
                      _(u'Estimated Demand')),
            VocabItem(u'contractDraft',
                      _(u'Contract Draft')),
            VocabItem(u'contractSchedule',
                      _(u'Contract Schedule')),
            VocabItem(u'contractSigned',
                      _(u'Contract Signed')),
            VocabItem(u'feasibilityStudy',
                      _(u'Feasibility Study')),
            VocabItem(u'environmentalImpact',
                      _(u'Environmental Impact')),
            VocabItem(u'finalAudit',
                      _(u'Final Audit')),
            VocabItem(u'tenderNotice',
                      _(u'Tender Notice')),
            VocabItem(u'evaluationCommittee',
                      _(u'Evaluation Committee Details')),
            VocabItem(u'requestForQualification',
                      _(u'Request for Qualification')),
            VocabItem(u'evaluationCriteria',
                      _(u'Evaluation Criteria')),
            VocabItem(u'minutes',
                      _(u'Minutes')),
            VocabItem(u'shortlistedFirms',
                      _(u'Shortedlisted Firms')),
            VocabItem(u'registrationParameters',
                      _(u'registrationParameters')),
            VocabItem(u'evaluationReports',
                      _(u'Evaluation Reports')),
            VocabItem(u'contractGuarantees',
                      _(u'Guarantees')),
            VocabItem(u'defaultEvents',
                      _(u'Defaults')),
            VocabItem(u'defaultEvents',
                      _(u'Defaults')),
            VocabItem(u'termination',
                      _(u'Termination')),
            VocabItem(u'performanceReport',
                      _(u'Performance report')),
            VocabItem(u'awardNotice',
                      _(u'Award Notice')),
            VocabItem(u'contractNotice',
                      _(u'Contract Notice')),
            VocabItem(u'completionCertificate',
                      _(u'Completion certificate')),
            VocabItem(u'procurementPlan',
                      _(u'Procurement Plan')),
            VocabItem(u'biddingDocuments',
                      _(u'Bidding Documents')),
            VocabItem(u'contractArrangements',
                      _(u'Contract Arrangements')),
            VocabItem(u'physicalProgressReport',
                      _(u'Physical progress reports')),
            VocabItem(u'physicalProgressReport',
                      _(u'Physical progress reports')),
            VocabItem(u'financialProgressReport',
                      _(u'Financial progress reports')),
            VocabItem(u'hearingNotice',
                      _(u'Public Hearing Notice')),
            VocabItem(u'marketStudies',
                      _(u'Market Studies')),
            VocabItem(u'eligibilityCriteria',
                      _(u'Eligibility Criteria')),
            VocabItem(u'clarifications',
                      _(u'Clarifications to bidders questions')),
            VocabItem(u'assetAndLiabilityAssessment',
                      _(u'Assessment of governents\' assets and ' +
                          'liabilities')),
            VocabItem(u'riskProvisions',
                      _(u'''
                      Provisions for management of risks and liabilities
                      ''')),
            VocabItem(u'winningBid',
                      _(u'''
                      Wining Bid
                      ''')),
            VocabItem(u'complaints',
                      _(u'''
                      Complaints and decisions
                      ''')),
            VocabItem(u'contractAnnexe',
                      _(u'''
                      Annexes to the Contract
                      ''')),
            VocabItem(u'subContract',
                      _(u'''
                      Subcontracts
                      ''')),
            VocabItem(u'projectPlan',
                      _(u'''
                      Project Plan
                      ''')),
            VocabItem(u'billOfQuantity',
                      _(u'''
                      Bill Of Quantity
                      ''')),
            VocabItem(u'bidders',
                      _(u'''
                      Information on bidders
                      ''')),
            VocabItem(u'conflictOfInterest',
                      _(u'''
                      Conflict of Interest
                      ''')),
            VocabItem(u'debarments',
                      _(u'''
                      Debarments
                      ''')),
            VocabItem(u'illustration',
                      _(u'''
                      Illustrations
                      ''')),
            VocabItem(u'submissionDocuments',
                      _(u'''
                      Bid Submission Documents
                      ''')),
            VocabItem(u'contractSummary',
                      _(u'''
                      Contract Summary
                      ''')),
            VocabItem(u'cancellationDetails',
                      _(u'''
                      Cancellation Details
                      ''')),
            VocabItem(u'projectScope',
                      _(u'''
                      Project scope
                      ''')),
            VocabItem(u'landAndSettlementImpact',
                      _(u'''
                      Land and Settlement Impact
                      ''')),
            VocabItem(u'projectEvaluation',
                      _(u'''
                      Project evaluation
                      ''')),
            VocabItem(u'budgetApproval',
                      _(u'''
                      Budget approval 
                      ''')),
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


DocumentTypeFactory = DocumentType()
