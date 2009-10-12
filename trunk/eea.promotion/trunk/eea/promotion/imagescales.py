# -*- coding: utf-8 -*-

from valentine.imagescales.browser.base import BaseImageLink
from elementtree import ElementTree as ET


class ImageLink(BaseImageLink):
    """ImageLink for items in the promotion side bar

    The markup mimics the template markup that was before. It's highly coupled
    with the logic of promotion.js.dtml.

    See #2118.
    """

    @property
    def short_title(self):
        utitle = self.title.decode('utf-8')
        maxlen = 30
        if len(utitle) > maxlen:
            delimiter = u' — ' # note: long dash sign
            if delimiter in utitle:
                return utitle.split(delimiter)[0].strip()
            return utitle[:maxlen] + u'...'
        return utitle

    def link(self, imgtag):
        utitle = self.short_title # short_title already returns unicode
        udesc = self.desc.decode('utf-8')

        a1 = ET.Element('a')
        a1.set('title', udesc)
        a1.set('class', ' '.join(self.classnames + ['portletHeader']))
        a1.set('href', self.url)
        a1.text = utitle

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
        a3.set('title', udesc or 'description not available')
        a3.append(img)

        return ''.join(ET.tostring(i, 'utf-8') for i in (a1, a2, a3))


class VideoImageLink(ImageLink):

    def __init__(self, context, request):
        super(VideoImageLink, self).__init__(context, request)
        self.classnames.append('thickbox')
