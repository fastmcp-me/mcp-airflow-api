# Example Queries for MCP Airflow API

## DAG Management with Pagination

### Basic DAG Listing
```
Query: "List all DAGs"
Tool: list_dags()
Result: Returns first 100 DAGs with pagination metadata
```

### Paginated DAG Browsing
```
Query: "Show me the next 100 DAGs"
Tool: list_dags(limit=100, offset=100)
Result: Returns DAGs 101-200 with pagination info
```

### Large Environment Handling
```
Query: "Get all DAGs at once for analysis"
Tool: list_dags(limit=1000)
Result: Returns up to 1000 DAGs in one call
```

### Complete DAG Inventory
```
Query: "I need all DAGs in the system regardless of count"
Tool: list_all_dags_paginated()
Result: Automatically fetches all DAGs using multiple API calls
```

### Custom Page Sizes
```
Query: "Show me 50 DAGs per page starting from position 200"  
Tool: list_dags(limit=50, offset=200)
Result: Returns DAGs 201-250 with pagination details
```

### Understanding Pagination Response

When you call `list_dags()`, you get:
- `dags`: Array of DAG objects
- `total_entries`: Total number of DAGs in Airflow
- `limit`: Number requested
- `offset`: Starting position
- `returned_count`: Actual number returned
- `has_more_pages`: Boolean - are there more DAGs?
- `next_offset`: Use this for the next page
- `pagination_info`: 
  - `current_page`: Current page number
  - `total_pages`: Total pages available
  - `remaining_count`: How many DAGs are left

### Efficient Pagination Strategies

**Exploration (Recommended)**:
1. `list_dags()` → See first 100 DAGs
2. Check `has_more_pages` → If true, more DAGs exist  
3. `list_dags(limit=100, offset=100)` → Get next 100
4. Repeat as needed

**Analysis (For large datasets)**:
1. `list_all_dags_paginated(page_size=200)` → Get all DAGs automatically
2. Analyze complete dataset

**Targeted (For specific ranges)**:
1. `list_dags(limit=50, offset=150)` → Get DAGs 151-200
2. Use for jumping to specific sections

## Running and Failed DAGs

```
Query: "Show me all currently running DAGs"
Tool: running_dags()
```

```
Query: "What DAGs have failed recently?"
Tool: failed_dags()  
```

## DAG Operations

```
Query: "Trigger the analytics_daily DAG"
Tool: trigger_dag("analytics_daily")
```

```
Query: "Pause the data_pipeline DAG"
Tool: pause_dag("data_pipeline")
```

## Health and Monitoring

```
Query: "Check if Airflow is healthy"
Tool: get_health()
```

```
Query: "What version of Airflow is running?"
Tool: get_version()
```
