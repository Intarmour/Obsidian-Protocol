


import unittest
from unittest.mock import patch
from providers.oracle import OracleProvider

class TestOracleProvider(unittest.TestCase):
    def setUp(self):
        self.credentials = {
            "ORACLE_USER_OCID": "fake_user_ocid",
            "ORACLE_TENANCY_OCID": "fake_tenancy_ocid",
            "ORACLE_REGION": "us-phoenix-1",
            "ORACLE_FINGERPRINT": "fake_fingerprint",
            "ORACLE_PRIVATE_KEY_PATH": "/path/to/fake/private_key.pem"
        }
        self.provider = OracleProvider(self.credentials)

    @patch("subprocess.run")
    def test_run_command_success(self, mock_run):
        mock_run.return_value.stdout = "Command executed successfully"
        mock_run.return_value.returncode = 0

        output = self.provider.run_command("oci os ns get")
        self.assertIn("successfully", output)

    @patch("subprocess.run")
    def test_run_command_failure(self, mock_run):
        mock_run.side_effect = Exception("Failed to execute")

        output = self.provider.run_command("oci os ns get")
        self.assertIn("Error executing Oracle command", output)

if __name__ == "__main__":
    unittest.main()