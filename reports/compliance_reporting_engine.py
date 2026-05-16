import uuid

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import LETTER


def generate_report(data):

    filename = "remitguard_report.pdf"

    styles = getSampleStyleSheet()

    story = []

    case_id = str(uuid.uuid4())[:8].upper()

    story.append(
        Paragraph(
            "RemitGuard AI Compliance Investigation Report",
            styles['Heading1']
        )
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(
            f"Case ID: {case_id}",
            styles['Normal']
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"Risk Level: {data['risk_level']}",
            styles['Heading2']
        )
    )

    story.append(
        Paragraph(
            f"Risk Score: {data['risk_score']}/100",
            styles['Normal']
        )
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(
            "Behavioral Risk Indicators",
            styles['Heading2']
        )
    )

    for flag in data['behavioral_flags']:

        story.append(
            Paragraph(
                f"• {flag}",
                styles['Normal']
            )
        )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(
            "AI Investigation Summary",
            styles['Heading2']
        )
    )

    story.append(
        Paragraph(
            data['summary'],
            styles['Normal']
        )
    )

    doc = SimpleDocTemplate(
        filename,
        pagesize=LETTER
    )

    doc.build(story)

    return filename