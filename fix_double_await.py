#!/usr/bin/env python3
"""
Script to fix double await issues.
"""

def fix_double_await():
    """Fix double await issues."""
    
    # Read the file
    with open('/root/Workspace-RL8/MCP-Airflow-API/src/mcp_airflow_api/airflow_api.py', 'r') as f:
        content = f.read()
    
    # Fix double await
    content = content.replace('await await ', 'await ')
    
    # Write back the modified content
    with open('/root/Workspace-RL8/MCP-Airflow-API/src/mcp_airflow_api/airflow_api.py', 'w') as f:
        f.write(content)
    
    print("Double await fix complete!")

if __name__ == "__main__":
    fix_double_await()
