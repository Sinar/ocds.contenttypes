# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


class DocumentTypeViewlet(ViewletBase):

    def documenttype_title(self, value):

        factory = getUtility(IVocabularyFactory,
                             'ocds.DocumentType')

        vocabulary = factory(self)

        term = vocabulary.getTerm(value)

        return term.title

    def render(self):
        return super(DocumentTypeViewlet, self).render()
