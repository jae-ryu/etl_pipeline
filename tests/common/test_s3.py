"""Test S3BucketConnectorMethods"""
import os
import unittest
import boto3
from moto import mock_s3
from etl_src.common.s3 import S3BucketConnector

# in unittest, we create classes
class TestS3BucketConnectorMethods(unittest.TestCase):
    """
    Testing the S3BucketConnector class
    """

    # method to initialize the test
    def setUp(self):
        """
        Setting up the environment
        """
        # mocking S3 connection start
        self.mock_s3 = mock_s3()
        self.mock_s3.start()
        # define class args to submit to S3BucketConnector
        self.s3_access_key = "AWS_ACCESS_KEY_ID"
        self.s3_secret_key = "AWS_SECRET_ACCESS_KEY"
        self.s3_endpoint_url = "https://s3.eu-central-1.amazonaws.com"
        self.s3_bucket_name = "test-bucket"
        # create s3 access keys as env variables
        os.environ[self.s3_access_key] = "KEY1"
        os.environ[self.s3_secret_key] = "KEY2"
        # create bucket on mocked s3
        self.s3 = boto3.resource(service_name="s3", endpoint_url=self.s3_endpoint_url)
        self.s3.create_bucket(
            Bucket=self.s3_bucket_name,
            CreateBucketConfiguration={"LocationConstraint": "eu-central-1"},
        )
        self.s3_bucket = self.s3.Bucket(self.s3_bucket_name)
        # create testing instance
        self.s3_bucket_connector = S3BucketConnector(
            self.s3_access_key,
            self.s3_secret_key,
            self.s3_endpoint_url,
            self.s3_bucket_name,
        )

    def tearDown(self):
        """
        Executing after unittests
        """
        # mocking s3 connection stop
        self.mock_s3.stop()

    def test_list_files_prefix_ok(self):
        """
        Tests list_files_in_prefix method for getting 2 files keys
        as listed on the mocked s3 bucket
        """
        # Expected ersults
        prefix_exp = "prefix/"
        key1_exp = f"{prefix_exp}test1.csv"
        key2_exp = f"{prefix_exp}test2.csv"
        # Test init for this test
        csv_content = """col1,col2
        valA,valB"""
        self.s3_bucket.put_object(Body=csv_content, Key=key1_exp)
        self.s3_bucket.put_object(Body=csv_content, Key=key2_exp)
        # Method execution
        list_result = self.s3_bucket_conn.list_files_in_prefix(prefix_exp)
        # Tests after method execution
        self.assertEqual(len(list_result), 2)
        self.assertIn(key1_exp, list_result)
        self.assertIn(key2_exp, list_result)
        # Cleanup after tests
        self.s3_bucket.delete_object(
            Delete={"Objects": [{"Key": key1_exp}, {"Key": key2_exp}]}
        )

    def test_list_files_in_prefix_wrong_prefix(self):
        """
        Tests list_files_in_prefix in case of wrong/nonexistent prefix
        """
        pass


if __name__ == "__main__":
    unittest.main()
