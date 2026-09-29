import os
import sys
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable, Preformatted
)
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Custom Canvas to track page numbers and print running headers/footers
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_header_footer(self, page_count):
        if self._pageNumber == 1:
            return  # Suppress headers and footers on cover page

        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#475569"))

        # Running Header
        header_text = "Smart City Management Simulator — Professional Black Book"
        self.drawString(54, 11 * inch - 40, header_text)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(54, 11 * inch - 46, 8.5 * inch - 54, 11 * inch - 46)

        # Running Footer
        footer_text = "Dept. of Computer Science | D.G. Ruparel College of Arts, Science and Commerce"
        self.drawString(54, 42, footer_text)
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 54, 42, page_str)
        self.line(54, 52, 8.5 * inch - 54, 52)

        self.restoreState()

print("NumberedCanvas initialized successfully.")
