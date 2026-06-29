# =========================================================
# NeuroMate PDF Engine
# Version 2.0
# =========================================================

import os

from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.platypus import SimpleDocTemplate

from neuromate.config import (
    PAGE_SIZE,
    PAGE_WIDTH,
    PAGE_HEIGHT,
    LEFT_MARGIN,
    RIGHT_MARGIN,
    TOP_MARGIN,
    BOTTOM_MARGIN,
    OUTPUT_DIR,
    LOGO_FILE,
    COVER_FILE,
    BLUE,
    SILVER,
)

from neuromate.styles import NeuroMateStyles
from neuromate.components import NeuroMateComponents
from neuromate.layouts import NeuroMateLayouts


class NeuroMatePDF:

    def __init__(self, output_path=OUTPUT_DIR):

        self.output_path = output_path

        os.makedirs(
            self.output_path,
            exist_ok=True
        )

        self.styles = NeuroMateStyles()

        self.components = NeuroMateComponents(
            self.styles
        )

        self.layouts = NeuroMateLayouts(
            self.components
        )

        self.story = []

        self.doc = None

        self.file_path = os.path.join(
            self.output_path,
            "temp.pdf"
        )
    # =====================================================
    # CREATE DOCUMENT
    # =====================================================

    def create_document(self):

        self.doc = SimpleDocTemplate(

            self.file_path,

            pagesize=PAGE_SIZE,

            leftMargin=LEFT_MARGIN,

            rightMargin=RIGHT_MARGIN,

            topMargin=TOP_MARGIN,

            bottomMargin=BOTTOM_MARGIN,

        )

    # =====================================================
    # ADD COVER
    # =====================================================

    def add_cover(
        self,
        title,
        subtitle="",
        description=""
    ):

        self.story.extend(

            self.layouts.cover(
                title,
                subtitle,
                description
            )

        )

    # =====================================================
    # ADD QUOTE
    # =====================================================

    def add_quote(
        self,
        text
    ):

        self.story.extend(

            self.layouts.quote(text)

        )

    # =====================================================
    # ADD SECTION
    # =====================================================

    def add_section(
        self,
        title,
        content
    ):

        self.story.extend(

            self.layouts.section(
                title,
                content
            )

        )
    # =====================================================
    # DRAW COVER
    # =====================================================

    def draw_cover(self, canvas, doc):

        canvas.saveState()

        # ---------- Cover Background ----------

        if os.path.exists(COVER_FILE):

            try:

                canvas.drawImage(

                    ImageReader(COVER_FILE),

                    0,

                    0,

                    width=PAGE_WIDTH,

                    height=PAGE_HEIGHT,

                    preserveAspectRatio=False,

                    mask="auto"

                )

            except Exception:

                canvas.setFillColor(
                    HexColor("#05070A")
                )

                canvas.rect(
                    0,
                    0,
                    PAGE_WIDTH,
                    PAGE_HEIGHT,
                    fill=1,
                    stroke=0
                )

        else:

            canvas.setFillColor(
                HexColor("#05070A")
            )

            canvas.rect(
                0,
                0,
                PAGE_WIDTH,
                PAGE_HEIGHT,
                fill=1,
                stroke=0
            )

        # ---------- Large Logo ----------

        if os.path.exists(LOGO_FILE):

            try:

                logo_size = 120

                canvas.drawImage(

                    ImageReader(LOGO_FILE),

                    (PAGE_WIDTH - logo_size) / 2,

                    PAGE_HEIGHT - 220,

                    width=logo_size,

                    height=logo_size,

                    mask="auto",

                    preserveAspectRatio=True

                )

            except Exception:

                pass

        canvas.restoreState()

    # =====================================================
    # DRAW NORMAL PAGE
    # =====================================================

    def draw_page(self, canvas, doc):

        canvas.saveState()

        canvas.setFillColor(
            HexColor("#0D1117")
        )

        canvas.rect(

            0,

            0,

            PAGE_WIDTH,

            PAGE_HEIGHT,

            fill=1,

            stroke=0

        )

        # ---------- Header ----------

        canvas.setFillColor(BLUE)

        canvas.setFont("Helvetica-Bold", 11)

        canvas.drawString(

            LEFT_MARGIN,

            PAGE_HEIGHT - 28,

            "NEUROMATE"

        )

        # ---------- Divider ----------

        canvas.setStrokeColor(SILVER)

        canvas.setLineWidth(0.5)

        canvas.line(

            LEFT_MARGIN,

            PAGE_HEIGHT - 36,

            PAGE_WIDTH - RIGHT_MARGIN,

            PAGE_HEIGHT - 36

        )

        # ---------- Footer ----------

        canvas.setFillColor(SILVER)

        canvas.setFont("Helvetica", 9)

        canvas.drawRightString(

            PAGE_WIDTH - RIGHT_MARGIN,

            22,

            f"Page {canvas.getPageNumber()}"

        )

        canvas.restoreState()
    # =====================================================
    # SAVE PDF
    # =====================================================

    def save(self, filename="NeuroMate.pdf"):

        if self.doc is None:
            self.create_document()

        output_file = os.path.join(
            self.output_path,
            filename
        )

        self.doc.build(

            self.story,

            onFirstPage=self.draw_cover,

            onLaterPages=self.draw_page,

        )

        if os.path.exists(output_file):

            os.remove(output_file)

        os.replace(

            self.file_path,

            output_file

        )

        return output_file