import PyPDF2

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        raise RuntimeError(f"Failed to read the PDF file: {e}")

def convert_images_to_pdf(image_paths, output_pdf_path):
    """Convert a list of image files to a single PDF."""
    from PIL import Image
    from fpdf import FPDF

    try:
        pdf = FPDF()
        for image_path in image_paths:
            image = Image.open(image_path)
            image = image.convert('RGB')
            temp_path = "temp_image.jpg"
            image.save(temp_path)
            pdf.add_page()
            pdf.image(temp_path, x=10, y=10, w=180)
        pdf.output(output_pdf_path)
    except Exception as e:
        raise RuntimeError(f"Failed to convert images to PDF: {e}")
