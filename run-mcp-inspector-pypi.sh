#!/bin/bash

# (NOTE) 로컬 개발 소스로 기동됨.

npx -y @modelcontextprotocol/inspector \
	-e AIRFLOW_API_URL='http://localhost:38080/api/v1' \
	-e AIRFLOW_API_USERNAME='airflow' \
	-e AIRFLOW_API_PASSWORD='airflow' \
	-e AIRFLOW_LOG_LEVEL='INFO' \
	-- uvx mcp-airflow-api
