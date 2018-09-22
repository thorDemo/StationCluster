from PIL import Image, ImageDraw, ImageFont
from random import choice
import os
from peewee import *
from Tools.lib.DomainConf import DomainConf


class ImgTool:

    def __init__(self):
        self.project_path = os.path.dirname(os.path.abspath(__file__))
        self.font_path = os.path.dirname(os.path.abspath(__file__)) + '/font'
        self.static_path = os.path.dirname(os.path.abspath(__file__)) + '/static'

    def create_logo(self, url, name):
        logo = ['banner-s-3.png', 'banner-s-4.png', 'banner-s-5.png', 'banner-s-6.png', 'banner-s-7.png']
        img = '%s/static/%s' % (self.project_path, choice(logo))
        # get an image
        base = Image.open(img).convert('RGBA')
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new('RGBA', base.size, (0,0,0,0))
        # get a font
        # fnt = ImageFont.truetype('/System/Library/Fonts/Hiragino Sans GB.ttc', 40)
        fnt = ImageFont.truetype('%s/Adilla and Rita.ttf' % self.font_path, 100)
        # get a drawing context
        d = ImageDraw.Draw(txt)
        d.text((10, 30), text="%s >" % name, font=fnt, fill=(100,100,100,200))
        d.text((10,10), text=url, font=fnt, fill=(100,100,100,200))
        out = Image.alpha_composite(base, txt)
        out.save('%s/logo/%s.png' % (self.project_path, url))

    def create_ico(self, url, name):
        ico = self.static_path + '/jianshu.ico'
        print(ico)
        base = Image.open(ico).convert('RGBA')
        txt = Image.new('RGBA', base.size, (0,0,0,0))
        fnt1 = ImageFont.truetype('%s/Hiragino Sans GB.ttc' % self.font_path, 40)
        fnt2 = ImageFont.truetype('%s/Adilla and Rita.ttf' % self.font_path, 90)
        d = ImageDraw.Draw(txt)
        temp = url.split('.')[1]
        d.text((20,20), text=name[0:4], font=fnt1, fill=(220,118,97))
        d.text((20,40), text=url[-10:], font=fnt2, fill=(220,118,97))
        out = Image.alpha_composite(base, txt)
        out.save('%s/logo/%s.png' % (self.project_path, temp))


if __name__ == '__main__':
    img = ImgTool()
    domain = DomainConf.filter(DomainConf.domain != '')
    print(domain)
    for line in domain:
        img.create_ico(line.domain, line.index_title)
