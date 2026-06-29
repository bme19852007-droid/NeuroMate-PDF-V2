# =========================================================
# NeuroMate Components System
# Version 2.0
# =========================================================

from reportlab.platypus import (
    Paragraph,
    Spacer,
)

from neuromate.utils import fix_text


class NeuroMateComponents:

    def __init__(self, styles):

        self.styles = styles

    # =====================================================
    # COVER BLOCK
    # =====================================================

    def cover_block(
        self,
        title,
        subtitle="",
        description=""
    ):

        elements = []

        elements.append(
            Spacer(1, 180)
        )

        elements.append(

            Paragraph(
                fix_text(title),
                self.styles.title()
            )

        )

        if subtitle:

            elements.append(
                Spacer(1, 16)
            )

            elements.append(

                Paragraph(
                    fix_text(subtitle),
                    self.styles.subtitle()
                )

            )

        if description:

            elements.append(
                Spacer(1, 28)
            )

            elements.append(

                Paragraph(
                    fix_text(description),
                    self.styles.body()
                )

            )

        return elements
    # =====================================================
    # QUOTE BLOCK
    # =====================================================

    def quote_block(self, text):

        elements = []

        elements.append(
            Spacer(1, 220)
        )

        elements.append(

            Paragraph(
                f'“{fix_text(text)}”',
                self.styles.quote()
            )

        )

        elements.append(
            Spacer(1, 40)
        )

        return elements

    # =====================================================
    # SECTION BLOCK
    # =====================================================

    def section_block(
        self,
        title,
        content
    ):

        elements = []

        elements.append(

            Paragraph(
                fix_text(title),
                self.styles.section_title()
            )

        )

        elements.append(
            Spacer(1, 12)
        )

        for line in str(content).split("\n"):

            line = line.strip()

            if not line:
                continue

            elements.append(

                Paragraph(
                    fix_text(line),
                    self.styles.body()
                )

            )

            elements.append(
                Spacer(1, 8)
            )

        elements.append(
            Spacer(1, 20)
        )

        return elements
# =====================================================
# INFO BOX
# =====================================================

def info_box(
    self,
    title,
    content
):

    elements = []

    elements.append(

        Paragraph(
            fix_text(title),
            self.styles.highlight()
        )

    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(

        Paragraph(
            fix_text(content),
            self.styles.body()
        )

    )

    elements.append(
        Spacer(1, 24)
    )

    return elements
    # =====================================================
    # CHARACTER CARD
    # =====================================================

    def character_card(
        self,
        name,
        role,
        description
    ):

        elements = []

        elements.append(

            Paragraph(
                fix_text(name),
                self.styles.section_title()
            )

        )

        elements.append(

            Paragraph(
                fix_text(role),
                self.styles.highlight()
            )

        )

        elements.append(
            Spacer(1, 10)
        )

        elements.append(

            Paragraph(
                fix_text(description),
                self.styles.body()
            )

        )

        elements.append(
            Spacer(1, 24)
        )

        return elements


