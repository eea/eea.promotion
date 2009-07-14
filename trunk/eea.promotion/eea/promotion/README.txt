eea.promotion
=============

Product for making promotions visible on the EEA frontpage and themespages.
Any content type you have marked as IPromotable will get a 'create promotion'
item in the action menu.

The product intends to be separate from the other EEA products, but rely on
vocabularies provided by EEAContentTypes and eea.themecentre.

Other code related to this product:

  - Products.EEAContentTypes.promotion
  - Products.EEAContentTypes.browser.frontpage.getPromotions
  - eea.themecentre.browser.portlets.promotion

There's an adapter from old ExternalPromotions to IPromotions in:

  - Products.EEAContentTypes.promotion


What's this catalog.FrontpageSectionIndex?
------------------------------------------

In order to make RichTopics from each promotion category on the frontpage, we
needed some way to find those promotions using a catalog query. The problem is
that in Plone 2 it's somewhat complicated to add custom attributes.

In order to index the frontpage category of the promototions (including old
ones from EEAContentTypes), we needed to create a simple view
(eea.promotion.FrontpageIndex). However, catalog doesn't traverse views, so
we also needed to create a Python script inside a skin layer that returned
this value.
