"""
A sample to demonstrate analyzing with Azure Content Understanding Python SDK.

Requirements:
    - Python 3.9 or later

Setup:
    Follow the steps in the url below to configure your Microsoft Foundry resource and model deployments:
    https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/contentunderstanding/azure-ai-contentunderstanding#configuring-microsoft-foundry-resource


Usage:
    1. Navigate to the directory containing this file:
       cd path/to/the/directory/containing/this/file    # In your terminal

    2. Run the script:
       uv run python test_cv_parsing.py
"""

import sys
import json

from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisResult
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import AzureError
import os


def main() -> None:
    # Insert the following configurations.
    # 1) AZURE_CONTENT_UNDERSTANDING_ENDPOINT - the endpoint to your Content Understanding resource.
    endpoint = os.environ["CONTENTUNDERSTANDING_ENDPOINT"]

    # 2) CONTENT_UNDERSTANDING_KEY - your Content Understanding API key (optional if using DefaultAzureCredential).
    # key = "{{CONTENT_UNDERSTANDING_KEY}}"
    key = os.environ["CONTENTUNDERSTANDING_KEY"]

    # ANALYZER_ID - the ID of the analyzer to use.
    analyzer_id = "cv_parser_test"

    # API_VERSION - the API version to use.
    api_version = "2025-11-01"

    # Set up Content Understanding client.
    credential = AzureKeyCredential(key)
    client = ContentUnderstandingClient(endpoint=endpoint, credential=credential, api_version=api_version)

    # [START analyze]
    print(f"Analyzing with {analyzer_id} analyzer...")

    try:
        path_to_sample_document = "./examples/pdf/職務経歴書(サンプル).pdf"
        with open(path_to_sample_document, "rb") as f:
            poller = client.begin_analyze_binary(
                analyzer_id=analyzer_id,
                binary_input=f
            )
        result: AnalysisResult = poller.result()
    except AzureError as err:
        print(f"[Azure Error]: {err.message}")
        sys.exit(1)
    except Exception as ex:
        print(f"[Unexpected Error]: {ex}")
        sys.exit(1)
    # [END analyze]

    # [START output_result]
    print("=" * 50)
    print("Analysis result:")
    print("=" * 50 + "\n")

    max_display_lines = 50
    result_str = json.dumps(result.as_dict(), indent=2)
    ret_lines = result_str.splitlines()

    if len(ret_lines) > max_display_lines:
        print("\n".join(ret_lines[:max_display_lines]))
        print(f"\n {len(ret_lines) - max_display_lines} more lines to be displayed...\n")
    else:
        print(result_str)
    # [END output_result]


if __name__ == "__main__":
    main()