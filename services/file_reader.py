import fitz  # PyMuPDF

import fitz  # PyMuPDF

def read_math_pdf_text(pdf_path="data/Maths_Sec_2025-26.pdf") -> str:
    """
    Reads and extracts plain text from a class 9 or class 10 mathematics syllabus PDF.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted plain text content from the PDF.

    Raises:
        FileNotFoundError: If the file path is invalid.
    """
    try:
        with fitz.open(pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text.strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")


def read_science_pdf_text(pdf_path="data/Science_Sec_2025-26.pdf") -> str:
    """
    🔬 Tool: Science Syllabus Reader

    Reads and extracts text from a science syllabus PDF (typically class 9 or 10 combined).

    

    Returns:
        str: Extracted plain text content from the PDF.

    Raises:
        FileNotFoundError: If the file path is invalid.
    """
    try:
        with fitz.open(pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return f"🔬 class 9th and 10th Science Syllabus:\n\n{text.strip()}"
    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")



