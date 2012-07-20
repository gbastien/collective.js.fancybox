from Acquisition import aq_base

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView

class IncludeFancybox(BrowserView):
    """This check if a particular fancybox js has to be activated or not...
    """

    def isOnFor(self, use_on):
        """
          Return True if the fancybox behaviour is activated in portal_registry for given 'use_on'
        """
        if use_on == 'use_on_newsitem':
            if not self.context.portal_type == 'News Item':
                return False
        elif use_on =='use_on_text':
            if not hasattr(aq_base(self.context), 'CookedBody'):
                return False
        
        registry = getToolByName(self.context, 'portal_registry')
        if registry.get('collective.js.fancybox.example.controlpanel.IFancyboxSettings.%s' % use_on):
            return True
        return False