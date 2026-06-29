# =========================================================
# NeuroMate Utilities
# Version 2.0
# =========================================================

import arabic_reshaper
from bidi.algorithm import get_display


def fix_text(text):
    """
    Prepare Arabic text for ReportLab rendering.
    English text is returned unchanged.
    """

    if text is None:
        return ""

    text = str(text)

    try:
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)

    except Exception:
        return text