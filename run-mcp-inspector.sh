#!/bin/bash

# (NOTE) 로컬 소스가 아닌 Pypi에 배포된  패키지로 기동됨.

npx -y @modelcontextprotocol/inspector \
	-e AIRFLOW_API_URL='http://localhost:8080/api/v1' \
	-e AIRFLOW_API_USER='airflow' \
	-e AIRFLOW_API_PASSWORD='airflow' \
	-- uvx mcp-airflow-api
