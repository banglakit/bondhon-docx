import bondhon
from docx import Document


def handle_paragraph(from_encoding: str, to_encoding: str, p):
    inline = p.runs
    for i in range(len(inline)):
        inline[i].text = bondhon.convert(from_encoding, to_encoding, inline[i].text)


def handle_table(from_encoding, to_encoding, table):
    for row in table.rows:
        for cell in row.cells:
            convert_document(from_encoding, to_encoding, cell)


def convert_document(from_encoding: str, to_encoding: str, document: Document):
    print(document)
    for p in document.paragraphs:
        handle_paragraph(from_encoding, to_encoding, p)

    for table in document.tables:
        handle_table(from_encoding, to_encoding, table)
