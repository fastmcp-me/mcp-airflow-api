# 🚀 MCP-Airflow-API: Revolutionary Open Source Tool for Managing Apache Airflow with Natural Language

[![Deploy to PyPI with tag](https://github.com/call518/MCP-Airflow-API/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/call518/MCP-Airflow-API/actions/workflows/pypi-publish.yml)
[![BuyMeACoffee](https://raw.githubusercontent.com/pachadotdev/buymeacoffee-badges/main/bmc-donate-yellow.svg)](https://www.buymeacoffee.com/call518)

Have you ever wondered how amazing it would be if you could manage your Apache Airflow workflows using natural language instead of complex REST API calls or web interface manipulations? **MCP-Airflow-API** is the revolutionary open-source project that makes this goal a reality.

![MCP-Airflow-API Screenshot](img/screenshot-000.png)

---

## 🎯 What is MCP-Airflow-API?

MCP-Airflow-API is an MCP server that leverages the **Model Context Protocol (MCP)** to transform Apache Airflow REST API operations into natural language tools. This project hides the complexity of API structures and enables intuitive management of Airflow clusters through natural language commands.

**Traditional approach (example):**
```bash
curl -X GET "http://localhost:8080/api/v1/dags?limit=100&offset=0" \
  -H "Authorization: Basic YWlyZmxvdzphaXJmbG93"
```

**MCP-Airflow-API approach (natural language):**
> "Show me the currently running DAGs"

---

## 🚀 QuickStart: Get started in 5 minutes

### 1. Environment Setup

```bash
git clone https://github.com/call518/MCP-Airflow-API.git
cd MCP-Airflow-API

### Check and modify .env file
cp .env.example .env

### Airflow API Configuration
AIRFLOW_API_URL=http://host.docker.internal:38080/api/v1
AIRFLOW_API_USERNAME=airflow
AIRFLOW_API_PASSWORD=changeme!@34
```

### 2. Start Demo Containers

```bash
# Start all containers
docker-compose up -d
```

### 3. Access to OpenWebUI

http://localhost:3002/

- The list of MCP tool features provided by `swagger` can be found in the MCPO API Docs URL.
  - e.g: `http://localhost:8002/docs`

### 4. Registering the Tool in OpenWebUI

1. logging in to OpenWebUI with an admin account
1. go to "Settings" → "Tools" from the top menu.
1. Enter the `airflow-api` Tool address (e.g., `http://localhost:8002/airflow-api`) to connect MCP Tools.
1. Setup Ollama or OpenAI.

---

## 🌟 Key Features

1. **Natural Language Queries**  
   No need to learn complex API syntax. Just ask as you would naturally speak:
   - "What DAGs are currently running?"
   - "Show me the failed tasks"
   - "Find DAGs containing ETL"

2. **Comprehensive Monitoring Capabilities**  
   Real-time cluster status monitoring:
   - Cluster health monitoring
   - DAG status and performance analysis
   - Task execution log tracking
   - XCom data management

3. **43 Powerful MCP Tools**  
   Covers almost all Airflow API functionality:
   - DAG management (trigger, pause, resume)
   - Task instance monitoring
   - Pool and variable management
   - Connection configuration
   - Configuration queries
   - Event log analysis

4. **Large Environment Optimization**  
   Efficiently handles large environments with 1000+ DAGs:
   - Smart pagination support
   - Advanced filtering options
   - Batch processing capabilities

---

## 🛠️ Technical Advantages

- **Leveraging Model Context Protocol (MCP)**  
  MCP is an open standard for secure connections between AI applications and data sources, providing:
  - Standardized interface
  - Secure data access
  - Scalable architecture

- **Support for Two Connection Modes**
  - `stdio` mode: Traditional approach for local environments
  - `streamable-http` mode: Docker-based remote deployment

- **Complete Docker Support**  
  Full Docker Compose setup with 3 separate services:
  - **Open WebUI**: Web interface (port `3002`)
  - **MCP Server**: Airflow API tools (port `8080`)
  - **MCPO Proxy**: REST API endpoint provider (port `8002`)

---

## 🚀 Real Usage Examples

### DAG Management
```python
# List all currently running DAGs
list_dags(limit=50, is_active=True)

# Search for DAGs containing specific keywords
list_dags(id_contains="etl", name_contains="daily")

# Trigger DAG immediately
trigger_dag("my_etl_pipeline")
```

### Task Monitoring
```python
# Query failed task instances
list_task_instances_all(state="failed", limit=20)

# Check logs for specific task
get_task_instance_logs(
    dag_id="my_dag", 
    dag_run_id="run_123", 
    task_id="extract_data"
)
```

### Performance Analysis
```python
# DAG execution time statistics
dag_run_duration("my_etl_pipeline", limit=50)

# Task-level performance analysis
dag_task_duration("my_etl_pipeline", "latest_run")
```

---

## 📊 Real-World Use Cases

![Capacity Management for Operations Teams](img/screenshot-001.png)
---
![Capacity Management for Operations Teams](img/screenshot-002.png)
---
![Capacity Management for Operations Teams](img/screenshot-003.png)
---
![Capacity Management for Operations Teams](img/screenshot-004.png)
---
![Capacity Management for Operations Teams](img/screenshot-005.png)
---
![Capacity Management for Operations Teams](img/screenshot-006.png)
---
![Capacity Management for Operations Teams](img/screenshot-007.png)
---
![Capacity Management for Operations Teams](img/screenshot-008.png)
---
![Capacity Management for Operations Teams](img/screenshot-009.png)
---
![Capacity Management for Operations Teams](img/screenshot-010.png)
---
![Capacity Management for Operations Teams](img/screenshot-011.png)

---

## 🔧 Easy Installation and Setup

### Simple Installation via PyPI
```bash
uvx --python 3.11 mcp-airflow-api
```

### One-Click Deployment with Docker Compose (example)
```yaml
version: '3.8'
services:
  mcp-server:
    build: 
      context: .
      dockerfile: Dockerfile.MCP-Server
    environment:
      - FASTMCP_PORT=8080
      - AIRFLOW_API_URL=http://your-airflow:8080/api/v1
      - AIRFLOW_API_USERNAME=airflow
      - AIRFLOW_API_PASSWORD=your-password
```

### MCP Configuration File (example)
```json
{
  "mcpServers": {
    "airflow-api": {
      "command": "uvx",
      "args": ["--python", "3.11", "mcp-airflow-api"],
      "env": {
        "AIRFLOW_API_URL": "http://localhost:8080/api/v1",
        "AIRFLOW_API_USERNAME": "airflow",
        "AIRFLOW_API_PASSWORD": "airflow"
      }
    }
  }
}
```

---

## 🌈 Future-Ready Architecture

- Scalable design and modular structure for easy addition of new features  
- Standards-compliant protocol for integration with other tools  
- Cloud-native operations and LLM-ready interface  
- Context-aware query processing and automated workflow management capabilities

---

## 🎯 Who Is This Tool For?

- **Data Engineers** — Reduce debugging time, improve productivity, minimize learning curve  
- **DevOps Engineers** — Automate infrastructure monitoring, reduce incident response time  
- **System Administrators** — User-friendly management without complex APIs, real-time cluster status monitoring

---

## 🚀 Open Source Contribution and Community

**Repository:** https://github.com/call518/MCP-Airflow-API

**How to Contribute**
- Bug reports and feature suggestions
- Documentation improvements
- Code contributions

Please consider starring the project if you find it useful.

---

## 🔮 Conclusion

MCP-Airflow-API changes the paradigm of data engineering and workflow management:  
No need to memorize REST API calls — just ask in natural language:

> "Show me the status of currently running ETL jobs."

---

## 🏷️ Tags
`#Apache-Airflow #MCP #ModelContextProtocol #DataEngineering #DevOps #WorkflowAutomation #NaturalLanguage #OpenSource #Python #Docker #AI-Integration`

---

## 📚 Example Queries & Use Cases

This section provides comprehensive examples of how to use MCP-Airflow-API tools with natural language queries.

### Basic DAG Operations
- **list_dags**: "List all DAGs with limit 10 in a table format." → Returns up to 10 DAGs
- **list_dags**: "List all DAGs a table format." → Returns up to All DAGs (WARN: Need High Tokens)
- **list_dags**: "Show next page of DAGs." → Use offset for pagination
- **list_dags**: "List DAGs 21-40." → `list_dags(limit=20, offset=20)`
- **list_dags**: "Filter DAGs whose ID contains 'tutorial'." → `list_dags(id_contains="etl")`
- **list_dags**: "Filter DAGs whose display name contains 'tutorial'." → `list_dags(name_contains="daily")`
- **get_dags_detailed_batch**: "Get detailed information for all DAGs with execution status." → `get_dags_detailed_batch(fetch_all=True)`
- **get_dags_detailed_batch**: "Get details for active, unpaused DAGs with recent runs." → `get_dags_detailed_batch(is_active=True, is_paused=False)`
- **get_dags_detailed_batch**: "Get detailed info for DAGs containing 'example' with run history." → `get_dags_detailed_batch(id_contains="example", limit=50)`
- **running_dags**: "Show running DAGs."
- **failed_dags**: "Show failed DAGs."
- **trigger_dag**: "Trigger DAG 'example_complex'."
- **pause_dag**: "Pause DAG 'example_complex' in a table format."
- **unpause_dag**: "Unpause DAG 'example_complex' in a table format."

### Cluster Management & Health
- **get_health**: "Check Airflow cluster health."
- **get_version**: "Get Airflow version information."

### Pool Management
- **list_pools**: "List all pools."
- **list_pools**: "Show pool usage statistics."
- **get_pool**: "Get details for pool 'default_pool'."
- **get_pool**: "Check pool utilization."

### Variable Management
- **list_variables**: "List all variables."
- **list_variables**: "Show all Airflow variables with their values."
- **get_variable**: "Get variable 'database_url'."
- **get_variable**: "Show the value of variable 'api_key'."

### Task Instance Management
- **list_task_instances_all**: "List all task instances for DAG 'example_complex'."
- **list_task_instances_all**: "Show running task instances."
- **list_task_instances_all**: "Show task instances filtered by pool 'default_pool'."
- **list_task_instances_all**: "List task instances with duration greater than 300 seconds."
- **list_task_instances_all**: "Show failed task instances from last week."
- **list_task_instances_all**: "List failed task instances from yesterday."
- **list_task_instances_all**: "Show task instances that started after 9 AM today."
- **list_task_instances_all**: "List task instances from the last 3 days with state 'failed'."
- **get_task_instance_details**: "Get details for task 'data_processing' in DAG 'example_complex' run 'scheduled__xxxxx'."
- **list_task_instances_batch**: "List failed task instances from last month."
- **list_task_instances_batch**: "Show task instances in batch for multiple DAGs from this week."
- **get_task_instance_extra_links**: "Get extra links for task 'data_processing' in latest run."
- **get_task_instance_logs**: "Retrieve logs for task 'create_entry_gcs' try number 2 of DAG 'example_complex'."

### XCom Management
- **list_xcom_entries**: "List XCom entries for task 'data_processing' in DAG 'example_complex' run 'scheduled__xxxxx'."
- **list_xcom_entries**: "Show all XCom entries for task 'data_processing' in latest run."
- **get_xcom_entry**: "Get XCom entry with key 'result' for task 'data_processing' in specific run."
- **get_xcom_entry**: "Retrieve XCom value for key 'processed_count' from task 'data_processing'."

### Configuration Management
- **get_config**: "Show all Airflow configuration sections and options." → Returns complete config or 403 if expose_config=False
- **list_config_sections**: "List all configuration sections with summary information."
- **get_config_section**: "Get all settings in 'core' section." → `get_config_section("core")`
- **get_config_section**: "Show webserver configuration options." → `get_config_section("webserver")`
- **search_config_options**: "Find all database-related configuration options." → `search_config_options("database")`
- **search_config_options**: "Search for timeout settings in configuration." → `search_config_options("timeout")`

**Important**: Configuration tools require `expose_config = True` in airflow.cfg `[webserver]` section. Even admin users get 403 errors if this is disabled.

### DAG Analysis & Monitoring
- **get_dag**: "Get details for DAG 'example_complex'."
- **get_dags_detailed_batch**: "Get comprehensive details for all DAGs with execution history." → `get_dags_detailed_batch(fetch_all=True)`
- **get_dags_detailed_batch**: "Get details for active DAGs with latest run information." → `get_dags_detailed_batch(is_active=True)`
- **get_dags_detailed_batch**: "Get detailed info for ETL DAGs with recent execution data." → `get_dags_detailed_batch(id_contains="etl")`

**Note**: `get_dags_detailed_batch` returns each DAG with both configuration details (from `get_dag()`) and a `latest_dag_run` field containing the most recent execution information (run_id, state, execution_date, start_date, end_date, etc.).

- **dag_graph**: "Show task graph for DAG 'example_complex'."
- **list_tasks**: "List all tasks in DAG 'example_complex'."
- **dag_code**: "Get source code for DAG 'example_complex'."
- **list_event_logs**: "List event logs for DAG 'example_complex'."
- **list_event_logs**: "Show event logs with ID from yesterday for all DAGs."
- **get_event_log**: "Get event log entry with ID 12345."
- **all_dag_event_summary**: "Show event count summary for all DAGs."
- **list_import_errors**: "List import errors with ID."
- **get_import_error**: "Get import error with ID 67890."
- **all_dag_import_summary**: "Show import error summary for all DAGs."
- **dag_run_duration**: "Get run duration stats for DAG 'example_complex'."
- **dag_task_duration**: "Show latest run of DAG 'example_complex'."
- **dag_task_duration**: "Show task durations for latest run of 'manual__xxxxx'."
- **dag_calendar**: "Get calendar info for DAG 'example_complex' from last month."
- **dag_calendar**: "Show DAG schedule for 'example_complex' from this week."

### Date Calculation Examples

Tools automatically base relative date calculations on the server's current date/time:

| User Input | Calculation Method | Example Format |
|------------|-------------------|----------------|
| "yesterday" | current_date - 1 day | YYYY-MM-DD (1 day before current) |
| "last week" | current_date - 7 days to current_date - 1 day | YYYY-MM-DD to YYYY-MM-DD (7 days range) |
| "last 3 days" | current_date - 3 days to current_date | YYYY-MM-DD to YYYY-MM-DD (3 days range) |
| "this morning" | current_date 00:00 to 12:00 | YYYY-MM-DDTHH:mm:ssZ format |

The server always uses its current date/time for these calculations.

---

## Contributing

🤝 **Got ideas? Found bugs? Want to add cool features?**

We're always excited to welcome new contributors! Whether you're fixing a typo, adding a new monitoring tool, or improving documentation - every contribution makes this project better.

**Ways to contribute:**
- 🐛 Report issues or bugs
- 💡 Suggest new PostgreSQL monitoring features
- 📝 Improve documentation 
- 🚀 Submit pull requests
- ⭐ Star the repo if you find it useful!

**Pro tip:** The codebase is designed to be super friendly for adding new tools. Check out the existing `@mcp.tool()` functions in `airflow_api.py`.

---

## License
Freely use, modify, and distribute under the **MIT License**.
