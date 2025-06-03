import unittest
from providers.gcp import GCPProvider

class TestGCPProvider(unittest.TestCase):
    def setUp(self):
        self.credentials = {
            "GOOGLE_APPLICATION_CREDENTIALS": "fake-path-to-creds.json"
        }
        self.provider = GCPProvider(self.credentials)

    def test_run_command_success(self):
        output = self.provider.run_command("echo GCP Test")
        self.assertIn("GCP Test", output)

    def test_run_command_failure(self):
        output = self.provider.run_command("false")
        self.assertIn("Error executing GCP command", output)

if __name__ == '__main__':
    unittest.main()
