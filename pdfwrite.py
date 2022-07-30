from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
import PyPDF2


width, height = landscape(A4)

def pdfwrite(filename, data):
    n = len(data)
    len_per_char = 15.94
    line_len = 582-290
    margin_left = (line_len - (len_per_char*n))//2 
    c = canvas.Canvas(filename, pagesize=landscape(A4))
    c.setFont("Helvetica", 24)
    c.drawString(298+margin_left, 248, data)
    c.showPage()
    c.save()



def create_cert(name):
    pdfwrite("temp.pdf", name.upper())


    with open('temp.pdf', 'rb') as f:
        named = PyPDF2.PdfFileReader(f)

        with open('cert_template.pdf', 'rb') as cert:

            cert = PyPDF2.PdfFileReader(cert)

            named = named.getPage(0)

            cert = cert.getPage(0)

            cert.mergePage(named)

            pdf_writer = PyPDF2.PdfFileWriter()

            pdf_writer.addPage(cert)

            with open('Cert.pdf', 'wb') as new_file:

                pdf_writer.write(new_file)
    return 'Cert.pdf'

