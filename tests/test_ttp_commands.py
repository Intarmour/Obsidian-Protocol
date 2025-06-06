

import os
import pytest
import yaml

TTP_FOLDER = "ttps"
SCENARIO_FOLDER = "scenarios"

def collect_yaml_files(folder):
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".yaml")
    ]

@pytest.mark.parametrize("yaml_path", collect_yaml_files(TTP_FOLDER))
def test_ttp_yaml_structure(yaml_path):
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)
    
    assert "name" in data, f"'name' key missing in {yaml_path}"
    assert "description" in data, f"'description' key missing in {yaml_path}"
    assert "mitre_technique" in data, f"'mitre_technique' key missing in {yaml_path}"
    assert "stage" in data, f"'stage' key missing in {yaml_path}"
    assert "steps" in data and isinstance(data["steps"], list), f"'steps' must be a list in {yaml_path}"
    
    for step in data["steps"]:
        assert "action" in step, f"Missing 'action' in one of the steps in {yaml_path}"
        assert "description" in step, f"Missing 'description' in one of the steps in {yaml_path}"

@pytest.mark.parametrize("yaml_path", collect_yaml_files(SCENARIO_FOLDER))
def test_scenario_yaml_structure(yaml_path):
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)

    assert "name" in data, f"'name' key missing in {yaml_path}"
    assert "description" in data, f"'description' key missing in {yaml_path}"
    assert "sequence" in data and isinstance(data["sequence"], list), f"'sequence' must be a list in {yaml_path}"

    for step in data["sequence"]:
        assert "ttp" in step, f"Missing 'ttp' reference in scenario step in {yaml_path}"