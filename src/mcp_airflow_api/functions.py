"""
Airflow MCP auxiliary utility functions definition file
"""
import os
import requests

def airflow_request(method, url, **kwargs):
    token = os.getenv("AIRFLOW_API_TOKEN")
    headers = kwargs.pop("headers", {})
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return requests.request(method, url, headers=headers, **kwargs)
