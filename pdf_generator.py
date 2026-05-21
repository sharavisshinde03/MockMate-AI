from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(feedback, filename="feedback.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    paragraphs = feedback.split("\n")

    for para in paragraphs:

        elements.append(
            Paragraph(para, styles['BodyText'])
        )

        elements.append(
            Spacer(1, 12)
        )

    doc.build(elements)

    return filename