import PyPDF2

from config import cfg

import logging
logger = logging.getLogger(__name__)

_AVAILABLE = "ON"

class OCREngine():

    def pdf_to_txt(self, pathname):
        with open(pathname, "rb") as archivo_pdf:
            pdf_reader = PyPDF2.PdfReader(archivo_pdf)
            text = ""
            for i, page in enumerate(pdf_reader.pages):
                text += f"\n\n--- PAGE_{i+1} ---\n\n"
                text += page.extract_text()
        return text

    def run(self, pathname):
        text = ""
        if cfg.get('OCR.TEXT_LAYER.AVAILABLE') == _AVAILABLE:
            logger.info("PDF TO TXT OCR ON")
            text = self.pdf_to_txt(pathname)
        return text
