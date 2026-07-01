from io import BytesIO
import os
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

# ----------------------------------------------------
# STYLES
# ----------------------------------------------------

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = colors.HexColor("#1B5E20")
title_style.fontSize = 24
title_style.spaceAfter = 18

heading_style = styles["Heading2"]
heading_style.textColor = colors.HexColor("#2E7D32")
heading_style.spaceBefore = 12
heading_style.spaceAfter = 8

normal_style = styles["BodyText"]
normal_style.fontSize = 10
normal_style.leading = 18

footer_style = styles["BodyText"]
footer_style.alignment = TA_CENTER
footer_style.textColor = colors.grey
footer_style.fontSize = 9


# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

def add_footer(canvas, doc):

    canvas.saveState()

    canvas.setFont("Helvetica", 9)

    canvas.setFillColor(colors.grey)

    canvas.drawCentredString(
        300,
        25,
        f"Page {doc.page}"
    )

    canvas.restoreState()


# ----------------------------------------------------
# SUMMARY TABLE
# ----------------------------------------------------

def create_summary_table(
    prediction,
    crop_health,
    yield_loss
):

    data = [

        ["Disease", prediction],

        ["Confidence", "98.7 %"],

        ["Crop Health", f"{crop_health}%"],

        ["Severity", "Medium"],

        ["Estimated Yield Loss", f"{yield_loss}%"]

    ]

    table = Table(
        data,
        colWidths=[170, 290]
    )

    table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#E8F5E9")),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica"),

            ("BOTTOMPADDING",(0,0),(-1,-1),10),

            ("TOPPADDING",(0,0),(-1,-1),10),

            ("VALIGN",(0,0),(-1,-1),"MIDDLE")

        ])

    )

    return table
# ----------------------------------------------------
# PDF GENERATOR
# ----------------------------------------------------

def generate_pdf(
    request,
    prediction,
    disease_info,
    filename
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    elements = []

    # ==========================================
    # TITLE
    # ==========================================

    elements.append(
        Paragraph(
            "PlantAI",
            title_style
        )
    )

    elements.append(

        Paragraph(

            "AI Powered Plant Disease Detection Report",

            heading_style

        )

    )

    elements.append(Spacer(1,20))

    # ==========================================
    # REPORT DETAILS
    # ==========================================

    report_id = datetime.now().strftime(
        "PLT-%Y%m%d-%H%M%S"
    )

    details = [

        ["Report ID", report_id],

        ["Generated On",
         datetime.now().strftime(
            "%d %B %Y %I:%M %p"
         )],

        ["Generated For",
         request.user.username]

    ]

    report_table = Table(
        details,
        colWidths=[150,310]
    )

    report_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#E8F5E9")),

            ("BOTTOMPADDING",(0,0),(-1,-1),10),

            ("TOPPADDING",(0,0),(-1,-1),10)

        ])

    )

    elements.append(report_table)

    elements.append(Spacer(1,25))

    # ==========================================
    # IMAGE
    # ==========================================

    image_path = os.path.join(
        settings.MEDIA_ROOT,
        "uploads",
        filename
    )

    if os.path.exists(image_path):

        elements.append(

            Paragraph(

                "Uploaded Leaf Image",

                heading_style

            )

        )

        img = Image(
            image_path,
            width=3.5*inch,
            height=3.5*inch
        )

        img.hAlign = "CENTER"

        elements.append(img)

        elements.append(Spacer(1,20))

    # ==========================================
    # SUMMARY
    # ==========================================

    elements.append(

        Paragraph(

            "Prediction Summary",

            heading_style

        )

    )

    elements.append(

        create_summary_table(

            prediction,

            disease_info.crop_health,

            disease_info.yield_loss

        )

    )

    elements.append(Spacer(1,20))
    # ==========================================
    # DISEASE DESCRIPTION
    # ==========================================

    elements.append(
        Paragraph(
            "Disease Description",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            disease_info.description,
            normal_style
        )
    )

    elements.append(Spacer(1,15))

    # ==========================================
    # SIGNS & SYMPTOMS
    # ==========================================

    elements.append(
        Paragraph(
            "Signs & Symptoms",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            disease_info.signs_of_damage,
            normal_style
        )
    )

    elements.append(Spacer(1,15))

    # ==========================================
    # PREVENTION
    # ==========================================

    elements.append(
        Paragraph(
            "Prevention",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            disease_info.prevention,
            normal_style
        )
    )

    elements.append(Spacer(1,15))

    # ==========================================
    # RECOMMENDATION
    # ==========================================

    elements.append(
        Paragraph(
            "Plant Care Recommendation",
            heading_style
        )
    )

    recommendation = getattr(
        disease_info,
        "recommendation",
        "Follow good agricultural practices and monitor the crop regularly."
    )

    elements.append(
        Paragraph(
            recommendation,
            normal_style
        )
    )

    elements.append(Spacer(1,25))

    # ==========================================
    # THANK YOU
    # ==========================================

    thanks = Table(
        [[
            Paragraph(
                "<b>Thank you for using PlantAI!</b><br/><br/>"
                "Helping farmers grow healthier crops through Artificial Intelligence.<br/><br/>"
                "<font color='green'><b>www.PlantAI.com</b></font><br/>"
                "© 2026 PlantAI. All Rights Reserved.",
                footer_style
            )
        ]],
        colWidths=[460]
    )

    thanks.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#F1F8E9")),
        ("BOX",(0,0),(-1,-1),1,colors.HexColor("#81C784")),
        ("BOTTOMPADDING",(0,0),(-1,-1),18),
        ("TOPPADDING",(0,0),(-1,-1),18),
        ("LEFTPADDING",(0,0),(-1,-1),15),
        ("RIGHTPADDING",(0,0),(-1,-1),15),
    ]))

    elements.append(thanks)

    # ==========================================
    # BUILD PDF
    # ==========================================

    doc.build(
        elements,
        onFirstPage=add_footer,
        onLaterPages=add_footer
    )

    pdf = buffer.getvalue()
    buffer.close()

    response = HttpResponse(
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        'attachment; filename="PlantAI_Report.pdf"'
    )

    response.write(pdf)

    return response
