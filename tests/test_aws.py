

import unittest
from providers.aws import AWSProvider

class TestAWSProvider(unittest.TestCase):
    def setUp(self):
        self.credentials = {
            "AWS_ACCESS_KEY_ID": "dummy_access_key",
            "AWS_SECRET_ACCESS_KEY": "dummy_secret_key",
            "AWS_REGION": "us-east-1"
        }
        self.provider = AWSProvider(self.credentials)

    def test_initialization(self):
        self.assertEqual(self.provider.credentials["AWS_ACCESS_KEY_ID"], "dummy_access_key")
        self.assertEqual(self.provider.credentials["AWS_SECRET_ACCESS_KEY"], "dummy_secret_key")
        self.assertEqual(self.provider.credentials["AWS_REGION"], "us-east-1")

    def test_run_command_mock(self):
        # Note: This test does not actually call AWS CLI to avoid dependency on real AWS credentials
        try:
            output = self.provider.run_command("echo AWS test successful")
            self.assertIn("AWS test successful", output)
        except Exception as e:
            self.fail(f"run_command raised an exception unexpectedly: {e}")

if __name__ == "__main__":
    unittest.main()