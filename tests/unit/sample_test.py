import unittest
import tempfile
import os
import shutil
from cicd_template_new.jobs.sample.entrypoint import SampleJob
from pyspark.sql import SparkSession

class SampleJobUnitTest(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory().name
        self.spark = SparkSession.builder.master("local[1]").getOrCreate()
        self.test_config = {
            "output_format": "parquet",
            "output_path": os.path.join(self.test_dir, "output")
        }
        self.job = SampleJob(spark=self.spark, init_conf=self.test_config)


    def test_sample(self):

        self.job.launch()

        output_count = (
            self.spark
                .read
                .format(self.test_config["output_format"])
                .load(self.test_config["output_path"])
                .count()
        )

        self.assertGreater(output_count, 0)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

if __name__ == "__main__":
    unittest.main()
