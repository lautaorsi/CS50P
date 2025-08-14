from fpdf import FPDF
from datetime import datetime
import os



def diploma(name):
    img_dir =os.getcwd()
    duck = img_dir + '\\csduck.png'
    diploma = img_dir + '\\diploma.png'
    pre_date = datetime.now()
    post_date = f'{pre_date.day}/{pre_date.month}/{pre_date.year}'
    newpdf = FPDF()
    newpdf.add_page()
    newpdf.image(diploma, 5, 70, 200)
    newpdf.image(duck, 137, 164, 25)
    newpdf.set_font("times", '', 20)
    newpdf.set_text_color(255,255,255)
    newpdf.text(85, 123, 'CS50 Python')
    newpdf.set_font("Courier", '', 19)
    newpdf.set_text_color(254,236,200)
    newpdf.text(82, 143, name)
    newpdf.set_font("times", '', 15)
    newpdf.text(52, 188, post_date)
    newpdf.output('diploma.pdf')

