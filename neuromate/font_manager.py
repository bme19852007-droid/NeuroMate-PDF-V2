# =========================================================
# NeuroMate Font Manager
# Version 2.0
# =========================================================

import os
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from neuromate.config import (
    FONTS_DIR,
    FONT_REGULAR,
    FONT_BOLD,
    FONT_SEMIBOLD,
)


class FontManager:

    @staticmethod
    def register():

        try:

            regular = os.path.join(
                FONTS_DIR,
                "Cairo-Regular.ttf"
            )

            bold = os.path.join(
                FONTS_DIR,
                "Cairo-Bold.ttf"
            )

            semibold = os.path.join(
                FONTS_DIR,
                "Cairo-SemiBold.ttf"
            )

            if os.path.exists(regular):
                pdfmetrics.registerFont(
                    TTFont(
                        "Cairo-Regular",
                        regular
                    )
                )

            if os.path.exists(bold):
                pdfmetrics.registerFont(
                    TTFont(
                        "Cairo-Bold",
                        bold
                    )
                )

            if os.path.exists(semibold):
                pdfmetrics.registerFont(
                    TTFont(
                        "Cairo-SemiBold",
                        semibold
                    )
                )

            # Register Font Family

            addMapping(
                "Cairo",
                0,
                0,
                "Cairo-Regular"
            )

            addMapping(
                "Cairo",
                1,
                0,
                "Cairo-Bold"
            )

            addMapping(
                "Cairo",
                0,
                1,
                "Cairo-Regular"
            )

            addMapping(
                "Cairo",
                1,
                1,
                "Cairo-Bold"
            )

            print("✓ Cairo fonts loaded")

            return {
                "regular": "Cairo-Regular",
                "bold": "Cairo-Bold",
                "semibold": "Cairo-SemiBold",
            }

        except Exception:

            print("⚠ Cairo fonts not found -> Using Helvetica")

            return {
                "regular": FONT_REGULAR,
                "bold": FONT_BOLD,
                "semibold": FONT_SEMIBOLD,
            }