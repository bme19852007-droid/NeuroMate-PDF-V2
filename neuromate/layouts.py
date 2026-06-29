# =========================================================
# NeuroMate Layout System
# Version 2.0
# =========================================================

from reportlab.platypus import PageBreak


class NeuroMateLayouts:

    def __init__(self, components):

        self.components = components

    # =====================================================
    # COVER
    # =====================================================

    def cover(
        self,
        title,
        subtitle="",
        description=""
    ):

        elements = []

        elements.extend(

            self.components.cover_block(
                title,
                subtitle,
                description
            )

        )

        elements.append(PageBreak())

        return elements

    # =====================================================
    # QUOTE
    # =====================================================

    def quote(self, text):

        elements = []

        elements.extend(

            self.components.quote_block(text)

        )

        elements.append(PageBreak())

        return elements

    # =====================================================
    # SECTION
    # =====================================================

    def section(
        self,
        title,
        content
    ):

        elements = []

        elements.extend(

            self.components.section_block(
                title,
                content
            )

        )

        elements.append(PageBreak())

        return elements

    # =====================================================
    # INFO CARD
    # =====================================================

    def info(
        self,
        title,
        content
    ):

        return self.components.info_box(
            title,
            content
        )

    # =====================================================
    # CHARACTER CARD
    # =====================================================

    def character(
        self,
        name,
        role,
        description
    ):

        return self.components.character_card(
            name,
            role,
            description
        )