

import importlib

PROVIDERS = {
    "aws": "providers.aws",
    "azure": "providers.azure",
    "gcp": "providers.gcp",
    "oracle": "providers.oracle",
    "alibaba": "providers.alibaba",
}

def load_provider(provider_key):
    if provider_key not in PROVIDERS:
        raise ValueError(f"Unsupported provider: {provider_key}")
    module_path = PROVIDERS[provider_key]
    return importlib.import_module(module_path)