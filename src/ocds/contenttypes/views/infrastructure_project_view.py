# -*- coding: utf-8 -*-

from ocds.contenttypes import _
from plone.dexterity.browser.view import DefaultView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class InfrastructureProjectView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('infrastructure_project_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(InfrastructureProjectView, self).__call__()
