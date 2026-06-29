# =========================================================
# NeuroMate Style System
# Version 2.0
# =========================================================

from reportlab.lib.enums import (
    TA_CENTER,
    TA_RIGHT,
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)

from neuromate.config import (
    BLUE,
    WHITE,
    SILVER,
    GOLD,
)

from neuromate.font_manager import FontManager


class NeuroMateStyles:

    def __init__(self):

        self.styles = getSampleStyleSheet()

        fonts = FontManager.register()

        self.font_regular = fonts["regular"]
        self.font_bold = fonts["bold"]
        self.font_semibold = fonts["semibold"]

    # =====================================================
    # Main Cover Title
    # =====================================================

    def title(self):

        return ParagraphStyle(

            "Title",

            parent=self.styles["Heading1"],

            fontName=self.font_bold,

            fontSize=34,

            leading=40,

            alignment=TA_CENTER,

            textColor=WHITE,

            spaceAfter=18,

        )

    # =====================================================
    # Subtitle
    # =====================================================

    def subtitle(self):

        return ParagraphStyle(

            "Subtitle",

            parent=self.styles["Heading2"],

            fontName=self.font_semibold,

            fontSize=18,

            leading=24,

            alignment=TA_CENTER,

            textColor=SILVER,

            spaceAfter=12,

        )

    # =====================================================
    # Section Title
    # =====================================================

    def section_title(self):

        return ParagraphStyle(

            "SectionTitle",

            parent=self.styles["Heading2"],

            fontName=self.font_bold,

            fontSize=22,

            leading=28,

            alignment=TA_RIGHT,

            textColor=BLUE,

            spaceAfter=16,

        )

    # =====================================================
    # Body
    # =====================================================

    def body(self):

        return ParagraphStyle(

            "Body",

            parent=self.styles["BodyText"],

            fontName=self.font_regular,

            fontSize=12,

            leading=22,

            alignment=TA_RIGHT,

            textColor=WHITE,

            spaceAfter=10,

        )

    # =====================================================
    # Quote
    # =====================================================

    def quote(self):

        return ParagraphStyle(

            "Quote",

            parent=self.styles["BodyText"],

            fontName=self.font_semibold,

            fontSize=16,

            leading=28,

            alignment=TA_CENTER,

            textColor=SILVER,

            italic=True,

            spaceAfter=20,

        )

    # =====================================================
    # Highlight
    # =====================================================

    def highlight(self):

        return ParagraphStyle(

            "Highlight",

            parent=self.styles["BodyText"],

            fontName=self.font_bold,

            fontSize=14,

            leading=22,

            alignment=TA_RIGHT,

            textColor=GOLD,

            spaceAfter=10,

        )