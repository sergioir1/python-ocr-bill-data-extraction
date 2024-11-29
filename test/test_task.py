from unittest import TestCase
from glob import glob

from src.runner_pipeline import RunnerPipeline

PATH_TEST_CASES = "C:/Users/sergi/PycharmProjects/FastAPIProject/data/processed/*.pdf"

class TestTask(TestCase):

    def test_task(self):
        files = glob(PATH_TEST_CASES)
        for file in files:
            result = RunnerPipeline().run(file)
            print(result)