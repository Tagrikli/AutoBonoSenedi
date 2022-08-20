import os, platform, subprocess
from io import BytesIO
from datetime import datetime
from dateutil import relativedelta
import tempfile
import sys

from num2words import num2words
from jinja2 import Template
import imgkit
from PIL import Image


class FormHandler:
    def __init__(self):
        self.info = None
     

    def generate(self,data):
        self.info = data

        self._formatFinalInfo()
        bimgs = self._prepareImages()
        pages = self._concatImages(bimgs)
        pdf_filename = self._pages2PDF(pages)

        self._openPDF(pdf_filename)

        return pdf_filename



    def _formatDate(self,date):

        print(date)
        d = datetime.strptime(date,"%Y-%m-%d")
        return datetime.strftime(d, "%d/%m/%Y")

    def _formatDateLong(self,date):
        d,m,y = date.split('/')
        months = ['OCAK','ŞUBAT','MART','NİSAN','MAYIS','HAZİRAN','TEMMUZ','AĞUSTOS','EYLÜL','EKİM','KASIM','ARALIK']
        return f"{str(d).zfill(2)} {months[int(m)]} {y}"

    def _formatPriceLong(self,price):
        return num2words(int(price),lang='tr').upper()

    def _getNextPayDate(self,pay_date):

        current = datetime.strptime(pay_date,"%d/%m/%Y")
        next = current + relativedelta.relativedelta(months=1)
        next_ = datetime.strftime(next,"%d/%m/%Y")
        print(pay_date,next_)
        return next_

    def _formatFinalInfo(self):
        self.info['pay_date'] = self._formatDate(self.info['pay_date'])
        self.info['mod_date'] = self._formatDate(self.info['mod_date'])
        self.info["pay_date_long"] = self._formatDateLong(self.info['pay_date'])
        self.info['price_long'] = self._formatPriceLong(self.info['price'])


    def _prepareImages(self):
        current_pay_date = self.info['pay_date']
        bimgs = []
        for i in range(int(self.info['amount'])):
            bimg = self._createSinglePaper(i+1,current_pay_date)
            current_pay_date = self._getNextPayDate(current_pay_date)
            bimgs.append(bimg)

        return bimgs

    def _concatImages(self,bimgs):

        pages = []

        page_count = len(bimgs) // 3 if len(bimgs) % 3 == 0 else (len(bimgs) // 3) + 1
        
        for i in range(page_count):
            bimgs_ = bimgs[i*3:max(len(bimgs) % 3, (i+1)*3)]
            images = []
            for bimg in bimgs_:
                images.append(Image.open(bimg))
            
            width = images[0].width
            height = sum([img.height for img in images])

            dest = Image.new('RGB',(2480, 3508), (255, 255, 255))
            for index, image in enumerate(images):
                #image.thumbnail((2300,3000/3), Image.Resampling.LANCZOS)
                
                dest.paste(image,(190,100 + sum([img.height for img in images[0:index]])))

            pages.append(dest)

        return pages

    def _pages2PDF(self,pages):

        filename = tempfile.mktemp(suffix='.pdf')
        print(filename)
        pages[0].save(filename,save_all=True,append_images=pages[1:],quality=100)

        return filename

    def _openPDF(self,filepath):
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(filepath)
        else:                                   # linux variants
            subprocess.call(('xdg-open', filepath))


    def _createSinglePaper(self, id, pay_date):

        self.info_ = self.info

        self.info_['paper_id'] = str(id)
        self.info_['pay_date'] = pay_date

        template = Template(open('paper.html').read())
        pp = template.render(**self.info_)

        img = imgkit.from_string(pp,output_path=False)

        bimg = BytesIO(img)
        bimg.seek(0)

        return bimg

