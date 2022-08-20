import os, platform, subprocess
from io import BytesIO
from datetime import datetime
from dateutil import relativedelta
import tempfile
import sys

from PySide6.QtWidgets import QApplication, QMainWindow,QHeaderView
from uic.form_input import Ui_MainWindow

from num2words import num2words
from jinja2 import Template
import imgkit
from PIL import Image


class FormApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.info_default = {
            'paper_id':"1",

            'pay_date_day': '1',
            'pay_date_month': '0',
            'pay_date_year': '2022',

            'price': '0',
            'person_name':'',
            'address':'',
            'phone':'',
            'person_id':'',
            'kefil_name':'',
            'kefil_id':'',

            'mod_date_day': '1',
            'mod_date_month': '0',
            'mod_date_year': '2022',

            'amount': '1'
        }

        self.info = self.info_default
        
        self.ui.date_day.textChanged.connect(self.genHandler('pay_date_day'))
        self.ui.date_month.currentIndexChanged.connect(self.genHandler('pay_date_month'))
        self.ui.date_year.textChanged.connect(self.genHandler('pay_date_year'))

        self.ui.edit_price.textChanged.connect(self.genHandler('price'))
        self.ui.edit_name.textChanged.connect(self.genHandler('person_name'))
        self.ui.edit_address.textChanged.connect(self.genHandler('address'))
        self.ui.edit_phone.textChanged.connect(self.genHandler('phone'))
        self.ui.edit_id.textChanged.connect(self.genHandler('person_id'))
        self.ui.edit_name_kefil.textChanged.connect(self.genHandler('kefil_name')) 
        self.ui.edit_kefil_id.textChanged.connect(self.genHandler('kefil_id'))

        self.ui.date_day_2.textChanged.connect(self.genHandler('mod_date_day'))
        self.ui.date_month_2.currentIndexChanged.connect(self.genHandler('mod_date_month'))
        self.ui.date_year_2.textChanged.connect(self.genHandler('mod_date_year'))      

        self.ui.edit_amount.textChanged.connect(self.genHandler('amount'))

        self.ui.button_prepare.clicked.connect(self.button_prepare_clicked)
        self.ui.button_reset.clicked.connect(self.resetForm)

    def resetForm(self):
        self.ui.date_day.setText('1')
        self.ui.date_month.setCurrentIndex(0)
        self.ui.date_year.setText('2022')
        self.ui.edit_price.setText('0')
        self.ui.edit_name.setText('')
        self.ui.edit_address.setPlainText('')
        self.ui.edit_phone.setText('')
        self.ui.edit_id.setText('')
        self.ui.edit_name_kefil.setText('')
        self.ui.edit_kefil_id.setText('')
        self.ui.date_day_2.setText('1')
        self.ui.date_month_2.setCurrentIndex(0)
        self.ui.date_year_2.setText('2022')

        self.info = self.info_default


    def genHandler(self,id):

        if id == 'address':
            def handler():
                self.info[id] = self.ui.edit_address.toPlainText()
            return handler

        else:
            def handler(value):
                self.info[id] = str(value)

            return handler

        


    def _formatDate(self,d,m,y):
        return f"{str(d).zfill(2)}/{str(m).zfill(2)}/{y}"

    def _formatDateLong(self,d,m,y):
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
        self.info['pay_date'] = self._formatDate(self.info['pay_date_day'],int(self.info['pay_date_month'])+1,self.info['pay_date_year'])
        self.info['mod_date'] = self._formatDate(self.info['mod_date_day'],int(self.info['mod_date_month'])+1,self.info['mod_date_year'])

        self.info["pay_date_long"] = self._formatDateLong(self.info['pay_date_day'],int(self.info['pay_date_month']),self.info['pay_date_year'])

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



    def button_prepare_clicked(self):

        self._formatFinalInfo()
        bimgs = self._prepareImages()
        pages = self._concatImages(bimgs)
        pdf_filename = self._pages2PDF(pages)
        self._openPDF(pdf_filename)

        self.resetForm()




if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = FormApp()
    window.show()

    sys.exit(app.exec())