#!/bin/bash
set -euo pipefail

# (NOTE) PyPI에서 설치된 패키지로 기동됨.

# 현재 스크립트 위치로 이동하여 올바른 작업 디렉토리 설정
cd "$(dirname "$0")"

npx -y @modelcontextprotocol/inspector \
	-e AIRFLOW_API_BASE_URL='http://localhost:38080/api' \
	-e AIRFLOW_API_VERSION='v1' \
	-e AIRFLOW_API_USERNAME='airflow' \
	-e AIRFLOW_API_PASSWORD='airflow' \
	-e MCP_LOG_LEVEL='INFO' \
	-- mcp-airflow-api
