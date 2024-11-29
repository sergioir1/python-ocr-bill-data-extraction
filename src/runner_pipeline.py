from ocr.ocr_engine import OCREngine
from annotator.annotator_engine import AnnotatorEngine
#from core.logger import logger

import logging
logger = logging.getLogger(__name__)


class RunnerPipeline:

    def run(self, pathname):
        logger.info("ARRANCANDO SCRIPT")
        text = OCREngine().run(pathname)
        annotator_dict = AnnotatorEngine().run(text)

        return annotator_dict
