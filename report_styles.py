import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import TableStyle

PAGE_WIDTH, PAGE_HEIGHT = A4
PRINTABLE_WIDTH = PAGE_WIDTH - 108 # 487.28 pt

def get_academic_styles():
    styles = getSampleStyleSheet()
    
    # Custom Palette
    NAVY = colors.HexColor("#0f2942")
    SLATE = colors.HexColor("#1e293b")
    MUTED = colors.HexColor("#475569")
    LIGHT_BG = colors.HexColor("#f8fafc")
    BORDER_COLOR = colors.HexColor("#cbd5e1")
    CODE_BG = colors.HexColor("#f1f5f9")
    
    # Document Title (Cover Page)
    styles.add(ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=22,
        leading=28,
        alignment=1, # Centered
        textColor=colors.black,
        spaceAfter=15
    ))
    
    styles.add(ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=16,
        alignment=1,
        textColor=colors.black,
        spaceAfter=25
    ))
    
    styles.add(ParagraphStyle(
        'CoverAuthor',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=13,
        leading=18,
        alignment=1,
        textColor=colors.black
    ))
    
    styles.add(ParagraphStyle(
        'CoverDetails',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11,
        leading=15,
        alignment=1,
        textColor=colors.black
    ))

    # Chapter Header (16 pt, Times New Roman Bold, Centered)
    styles.add(ParagraphStyle(
        'ChapterHeading',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=16,
        leading=22,
        alignment=1, # Centered
        textColor=NAVY,
        spaceBefore=10,
        spaceAfter=12,
        keepWithNext=True
    ))

    # Section Level 1 (14 pt, Times New Roman Bold)
    styles.add(ParagraphStyle(
        'SecHeading1',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=14,
        leading=18,
        textColor=NAVY,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    ))

    # Section Level 2 (14 pt, Times New Roman Bold)
    styles.add(ParagraphStyle(
        'SecHeading2',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=14,
        leading=18,
        textColor=SLATE,
        spaceBefore=12,
        spaceAfter=4,
        keepWithNext=True
    ))
    
    # Section Level 3 (14 pt, Times New Roman Bold)
    styles.add(ParagraphStyle(
        'SecHeading3',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=14,
        leading=18,
        textColor=SLATE,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    ))

    # Body Paragraph (12 pt, Times New Roman, Justified)
    styles['Normal'].fontName = 'Times-Roman'
    styles['Normal'].fontSize = 12
    styles['Normal'].leading = 16.5
    styles['Normal'].textColor = colors.HexColor("#0f172a")
    styles['Normal'].spaceAfter = 6
    styles['Normal'].alignment = 4 # Justified

    styles.add(ParagraphStyle(
        'AcademicBody',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=16.5,
        alignment=4 # Justified
    ))

    # Bullet / List
    styles.add(ParagraphStyle(
        'AcademicBullet',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=16.5,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3,
        alignment=4
    ))

    # Code Snippet
    styles.add(ParagraphStyle(
        'CodeSnippet',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=9.8,
        textColor=colors.HexColor("#0f172a"),
        alignment=0 # Left
    ))

    # Caption (Figures & Tables)
    styles.add(ParagraphStyle(
        'FigCaption',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=10,
        leading=13.5,
        alignment=1, # Center
        textColor=MUTED,
        spaceBefore=5,
        spaceAfter=10
    ))

    # Callout / Alert Box Text
    styles.add(ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#1e3a8a"),
        alignment=4
    ))

    # Table Cell Styles
    styles.add(ParagraphStyle(
        'TableHead',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=9,
        leading=11.5,
        textColor=colors.white,
        alignment=0
    ))
    
    styles.add(ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#1e293b"),
        alignment=0,
        spaceAfter=0
    ))

    styles.add(ParagraphStyle(
        'TableCellBold',
        parent=styles['TableCell'],
        fontName='Times-Bold',
        fontSize=8.5,
        leading=11
    ))

    styles.add(ParagraphStyle(
        'TableRightBold',
        parent=styles['TableCell'],
        fontName='Times-Bold',
        fontSize=8.5,
        leading=11,
        alignment=2
    ))

    return styles

def get_standard_table_style():
    return TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e3a8a")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ])
