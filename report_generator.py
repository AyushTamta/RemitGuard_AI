from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER


def generate_report(data, filename):

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("RemitGuard AI Risk Report", styles['Heading1']))
    story.append(Spacer(1, 12))

    for key, value in data.items():
        story.append(
            Paragraph(f"{key}: {value}", styles['Normal'])
        )
        story.append(Spacer(1, 6))

    doc = SimpleDocTemplate(filename, pagesize=LETTER)
    doc.build(story)

    return filename