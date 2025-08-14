from fpdf import FPDF




def main():
    name = input('Name: ')
    newpdf = FPDF()
    newpdf.add_page()
    newpdf.set_margin(0)
    newpdf.set_auto_page_break(False)
    newpdf.image('shirtificate.png', 5, 70, 200)
    newpdf.set_font("helvetica", '', 50)
    newpdf.text(50, 40, 'CS50 Shirtificate' )
    newpdf.set_font("helvetica", '', 25)
    newpdf.set_text_color(255,255,255)
    newpdf.text(59, 135, name + " took CS50")
    newpdf.output('shirtificate.pdf')


if __name__ == "__main__":
    main()
