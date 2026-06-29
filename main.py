# =========================================================
# NeuroMate PDF Generator
# Main Entry Point
# Version 2.0
# =========================================================

from neuromate.pdf_engine import NeuroMatePDF


def main():

    print("=" * 50)
    print(" NeuroMate PDF Generator V2")
    print("=" * 50)

    pdf = NeuroMatePDF()

    pdf.create_document()

    # -----------------------------------------------------
    # Cover
    # -----------------------------------------------------

    pdf.add_cover(

        title="NEUROMATE",

        subtitle="THE BLACK MIND",

        description="A Cinematic Franchise Bible"

    )

    # -----------------------------------------------------
    # Quote
    # -----------------------------------------------------

    pdf.add_quote(

        "The world is not a board... it is a battlefield of minds."

    )

    # -----------------------------------------------------
    # Executive Summary
    # -----------------------------------------------------

    pdf.add_section(

        "EXECUTIVE SUMMARY",

        """
NeuroMate is a premium cinematic science-fiction franchise exploring
the hidden war between artificial intelligence and human consciousness.
        """

    )

    # -----------------------------------------------------
    # World Building
    # -----------------------------------------------------

    pdf.add_section(

        "WORLD BUILDING",

        """
Every decision is predicted.
Every move is monitored.
Every mind can be rewritten.
        """

    )

    output = pdf.save(
        "NeuroMate_Franchise_Bible.pdf"
    )

    print("\nPDF Created Successfully")
    print(output)


if __name__ == "__main__":
    main()