from zope import interface
from zope import schema

class IFancyboxSettings(interface.Interface):
    
    use_on_newsitem = schema.Bool(title=u"Use on 'News item'",
                       description=u"Activate the Fancybox on 'News Item' selected image",
                       required=False,default=False)
    
    use_on_text = schema.Bool(title=u"Use on elements having a 'text' attribute",
                         description=u"Activate the 'fancybox' class useable on content_types having a 'text' attribute",required=False,default=False)

    use_on_leadimage = schema.Bool(title=u"Use on elements having a 'leadImage'",
                         description=u"Activate the Fancybox on elements having a 'leadImage'.  This require collective.leadimage to be installed",required=False,default=False)
