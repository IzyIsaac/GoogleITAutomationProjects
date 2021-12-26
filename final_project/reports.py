#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, data):
    content = []
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,20)
    content.append(report_title)
    content.append(empty_line)
    for item in data:
        content.append(Paragraph(f'name: {item["name"]}', styles["BodyText"]))
        content.append(Paragraph(f'weight: {item["weight"]} lbs', styles["BodyText"]))
        content.append(empty_line)
    report.build(content)