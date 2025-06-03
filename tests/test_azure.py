

import pytest
from providers.azure import AzureProvider

class DummyCredentials:
    def get(self, key, default=None):
        return "dummy_value"

def test_azure_command_execution(monkeypatch):
    credentials = DummyCredentials()
    azure_provider = AzureProvider(credentials)

    def mock_run_command(command):
        assert "az" in command
        return "Simulated Azure command output"

    azure_provider.run_command = mock_run_command

    result = azure_provider.run_command("az account show")
    assert result == "Simulated Azure command output"