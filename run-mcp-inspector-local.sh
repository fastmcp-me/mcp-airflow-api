#!/bin/bash

# (NOTE) 로컬 개발 소스로 기동됨 (uv run 사용).

# 현재 스크립트 위치로 이동하여 올바른 작업 디렉토리 설정
cd "$(dirname "$0")"

npx -y @modelcontextprotocol/inspector \
	-e AIRFLOW_API_URL='http://localhost:38080/api/v1' \
	-e AIRFLOW_API_USERNAME='airflow' \
	-e AIRFLOW_API_PASSWORD='airflow' \
	-e AIRFLOW_LOG_LEVEL='INFO' \
	-e PYTHONPATH='./src' \
	-- uv run python -m mcp_airflow_api.airflow_api
