# FichasTurhrock

import PyPDF2

//Existem várias bibliotecas em Python que permitem a criação de arquivos PDF programaticamente, como por exemplo PyPDF2, ReportLab e FPDF.

Um exemplo simples utilizando a biblioteca PyPDF2 seria:
# Cria um novo PDF
pdf = PyPDF2.PdfFileWriter()

# Adiciona uma nova página
page = pdf.addBlankPage(width=595, height=842)  # A4 (210mm x 297mm)

# Adiciona um texto na página
content = "Olá, mundo!"
text = PyPDF2.pdf.ContentStream(content.encode('utf-8'), pdf)
page.contents.add(text)

# Salva o PDF em disco
with open('arquivo.pdf', 'wb') as file:
    pdf.write(file)

//Para colocar informações em locais específicos de um PDF, é necessário utilizar uma biblioteca de edição de PDFs como o PyPDF2, ReportLab ou o pdfrw.

Com o PyPDF2, é possível editar arquivos PDF existentes e adicionar conteúdo em locais específicos. O exemplo a seguir demonstra como adicionar conteúdo em uma página existente em um local específico:

import PyPDF2

# Abre o arquivo PDF
with open('arquivo.pdf', 'rb') as file:
    pdf = PyPDF2.PdfFileReader(file)

    # Pega a primeira página
    page = pdf.getPage(0)

    # Cria um objeto texto
    text = PyPDF2.pdf.TextObject()
    text.setText("Informação a ser adicionada")
    text.setFillColorRGB(1, 0, 0)  # Define a cor do texto

    # Define a posição do texto na página
    x = 100
    y = 100
    text.x0 = x
    text.y0 = y

    # Adiciona o objeto texto na página
    page.mergeTranslatedPage(text)

    # Salva o PDF em disco
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('arquivo_editado.pdf', 'wb') as output:
        writer.write(output)


//Com a biblioteca ReportLab é possível criar arquivos PDFs a partir do zero e posicionar o conteúdo de forma precisa na página. O código abaixo é um exemplo de como criar um PDF a partir do zero e adicionar conteúdo em locais específicos:

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Cria um novo PDF
pdf = canvas.Canvas("arquivo.pdf")

# Adiciona um texto na posição (1 inch, 1 inch) da página
pdf.drawString(1 * inch, 1 * inch, "Texto a ser adicionado")

# Salva o PDF em disco
pdf.save()
