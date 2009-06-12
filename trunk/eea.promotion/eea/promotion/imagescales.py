from valentine.imagescales.browser.base import BaseImageLink
from elementtree import ElementTree as ET


class ImageLink(BaseImageLink):
    """ImageLink for items in the promotion side bar


    The markup mimics the template markup that was before. It's highly coupled
    with the logic of promotion.js.dtml.

    See #2118.
    """

    def link(self, imgtag):
        a1 = ET.Element('a')
        a1.set('title', self.desc)
        a1.set('class', ' '.join(self.classnames + ['portletHeader']))
        a1.set('href', self.url)
        a1.text = self.title

        br = ET.SubElement(a1, 'br')
        br.set('clear', 'all')

        img = ET.XML(imgtag)

        # This anchor is just to be read by showImage in promotion.js.dtml
        a2 = ET.Element('a')
        a2.set('style', 'display: none')
        a2.set('href', img.get('src'))

        a3 = ET.Element('a')
        a3.set('href', self.url)
        a3.set('class', ' '.join(self.classnames))
        a3.set('title', self.desc or 'description not available')
        a3.append(img)

        return ET.tostring(a1) + ET.tostring(a2) + ET.tostring(a3)


class VideoImageLink(ImageLink):

    def __init__(self, context, request):
        super(VideoImageLink, self).__init__(context, request)
        self.classnames.append('thickbox')
