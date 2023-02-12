import PyPDF2
from fpdf import FPDF

# Converts pdf into text. Make sure the pdf is in the project folder.
def extract(ans):
    fileName = input('What is the pdf file name? (No need to add .pdf): ')
    pdfFile = open(f'{fileName}.pdf', 'rb')
    pdf = PyPDF2.PdfReader(pdfFile)

    for page in range(len(pdf.pages)):
        text = pdf.pages[page].extract_text()
        print(text)

# Creates a new pdf which allows you to type or add images.
def create(ans):
    fpdf = FPDF()
    fpdf.add_page()
    fpdf.set_font('Arial', size=12)
    text = input('Write down text: ')
    fpdf.text(10, 10, txt= str(text))
    image = input('Do you want to add an image? (Y/N): ').upper().strip()
    if image == 'Y':
        imgName = input('Image file name: ').lower().strip()
        fpdf.image(f'{imgName}.pdf', 10, 10)
    else:
        pass

    pdfName = input('Name your pdf:').lower().strip()
    fpdf.output(f'{pdfName}.pdf')

while True:
    navigate = input('Would you like to create a new pdf or extract old one into text? (create/extract): ').lower().strip()
    if navigate == 'extract':
        try:
            extract(navigate)
            break
        except FileNotFoundError:
            print('Make sure file is typed correctly or inside project folder. Re-enter information.')
            break
    elif navigate == 'create':
        create(navigate)
        break
    else:
        pass
