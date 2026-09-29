import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas

PAGE_WIDTH, PAGE_HEIGHT = A4
FIG_DIR = r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\docs_figures"
OUTPUT_PDF = r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\Smart_City_Management_Simulator_Black_Book.pdf"

class AcademicNumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas that dynamically counts total pages and writes
    running headers and footers according to academic standards.
    """
    frontmatter_offset = 9

    def __init__(self, *args, **kwargs):
        super(AcademicNumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super(AcademicNumberedCanvas, self).showPage()
        super(AcademicNumberedCanvas, self).save()

    def draw_header_footer(self, page_count):
        # Suppress header and footer on cover page (page 1)
        if self._pageNumber == 1:
            return

        # Certificate page (page 2): Draw exact official double border and suppress standard running header/footer
        if self._pageNumber == 2:
            self.saveState()
            self.setStrokeColor(colors.black)
            # Outer thicker border
            self.setLineWidth(1.8)
            self.rect(26, 26, PAGE_WIDTH - 52, PAGE_HEIGHT - 52)
            # Inner thinner border
            self.setLineWidth(0.8)
            self.rect(30, 30, PAGE_WIDTH - 60, PAGE_HEIGHT - 60)
            self.restoreState()
            return

        self.saveState()
        
        # Header (Pages 3+)
        self.setFont("Times-Bold", 8)
        self.setFillColor(colors.HexColor("#334155"))
        self.drawString(54, PAGE_HEIGHT - 38, "Smart City Management Simulator - Professional Black Book")
        self.setFont("Times-Roman", 8)
        self.drawRightString(PAGE_WIDTH - 54, PAGE_HEIGHT - 38, "University of Mumbai | B.Sc Computer Science")
        
        self.setStrokeColor(colors.HexColor("#94a3b8"))
        self.setLineWidth(0.6)
        self.line(54, PAGE_HEIGHT - 44, PAGE_WIDTH - 54, PAGE_HEIGHT - 44)

        # Footer (Pages 3+)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 46, PAGE_WIDTH - 54, 46)

        self.setFont("Times-Roman", 8)
        self.setFillColor(colors.HexColor("#475569"))
        self.drawString(54, 32, "D.G. Ruparel College of Arts, Science and Commerce | Dept. of Computer Science")
        
        # Helper for Roman numerals
        def to_roman(num):
            val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            syb = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
            roman_num = ""
            i = 0
            while num > 0:
                for _ in range(num // val[i]):
                    roman_num += syb[i]
                    num -= val[i]
                i += 1
            return roman_num

        # Page numbering: Bottom center
        if self._pageNumber > self.frontmatter_offset:
            main_page = self._pageNumber - self.frontmatter_offset
            self.setFont("Times-Bold", 9.5)
            self.setFillColor(colors.HexColor("#0f172a"))
            self.drawCentredString(PAGE_WIDTH / 2.0, 32, str(main_page))
        elif self._pageNumber >= 3:
            roman_page = to_roman(self._pageNumber)
            self.setFont("Times-Bold", 9.5)
            self.setFillColor(colors.HexColor("#475569"))
            self.drawCentredString(PAGE_WIDTH / 2.0, 32, roman_page)

        self.restoreState()

print("Canvas helper ready.")
