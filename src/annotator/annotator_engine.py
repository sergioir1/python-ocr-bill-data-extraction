import re

from config import cfg
from annotator.anotators import annotators

import logging
logger = logging.getLogger(__name__)

_AVAILABLE = "ON"

class AnnotatorEngine:

    def extract_regex(self, text: str, annotators_process):
        result = {}
        for regex in annotators_process:
            pattern = re.compile(regex["regex"])
            matches = pattern.findall(text)

            # Extraer el grupo deseado
            result[regex["name"]] = [match[regex["precedence"] - 1] for match in matches]

            return result

    def process_annotators(self, text):
        """with open(pathname, "r", encoding="utf-8") as f:
            text = f.read()"""
        annotators_process = annotators.get("luz", None)
        extractions = self.extract_regex(text, annotators_process)
        return extractions


    def run(self, text):
        if cfg.get('ANNOTATOR.AVAILABLE') == _AVAILABLE:
            extractions = self.process_annotators(text)
        return extractions