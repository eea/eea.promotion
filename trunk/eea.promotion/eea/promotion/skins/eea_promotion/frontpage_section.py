## Script (Python) "frontpage_section"
##title=Testing
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath

return context.restrictedTraverse('@@frontpage_category')()
