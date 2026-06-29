# =========================================================
# NeuroMate Configuration
# Version 2.0
# =========================================================

import os

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4

# =========================================================
# PROJECT PATHS
# =========================================================

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

IMAGES_DIR = os.path.join(ASSETS_DIR, "images")

FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")

OUTPUT_DIR = os.path.join(ROOT_DIR, "output")

# =========================================================
# PAGE SETTINGS
# =========================================================

PAGE_SIZE = A4

PAGE_WIDTH, PAGE_HEIGHT = PAGE_SIZE

LEFT_MARGIN = 50
RIGHT_MARGIN = 50

TOP_MARGIN = 50
BOTTOM_MARGIN = 50

# =========================================================
# FONT DEFAULTS
# =========================================================

FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_SEMIBOLD = "Helvetica-Bold"

# =========================================================
# COLORS
# =========================================================

BLACK = HexColor("#05070A")

WHITE = HexColor("#F5F5F5")

BLUE = HexColor("#00C8FF")

SILVER = HexColor("#AEB8C4")

GOLD = HexColor("#D4AF37")

LIGHT_BLUE = HexColor("#56D6FF")

DARK_PANEL = HexColor("#0D1117")

DIVIDER = HexColor("#2B3642")

# =========================================================
# FILES
# =========================================================

LOGO_FILE = os.path.join(
    IMAGES_DIR,
    "logo.png"
)

COVER_FILE = os.path.join(
    IMAGES_DIR,
    "cover_bg.jpg"
)