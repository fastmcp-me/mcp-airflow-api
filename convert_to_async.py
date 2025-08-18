#!/usr/bin/env python3
"""
Script to convert all MCP tools to async functions and add await to airflow_request calls.
"""
import re

def convert_mcp_tools_to_async():
    """Convert all MCP tools to async and add await to airflow_request calls."""
    
    # Read the file
    with open('/root/Workspace-RL8/MCP-Airflow-API/src/mcp_airflow_api/airflow_api.py', 'r') as f:
        content = f.read()
    
    # Pattern to find @mcp.tool() followed by def function
    pattern = r'(@mcp\.tool\(\))\s*\n\s*(def\s+(\w+)\s*\([^)]*\)\s*->[^:]*:)'
    
    def replace_function(match):
        decorator = match.group(1)
        function_def = match.group(2)
        function_name = match.group(3)
        
        # Skip if already async
        if 'async def' in function_def:
            return match.group(0)
        
        # Convert def to async def
        async_function_def = function_def.replace('def ', 'async def ', 1)
        return f"{decorator}\n{async_function_def}"
    
    # Apply the replacement
    content = re.sub(pattern, replace_function, content, flags=re.MULTILINE)
    
    # Add await to airflow_request calls
    content = re.sub(r'\bairflow_request\(', 'await airflow_request(', content)
    
    # Add await to list_dags_internal calls
    content = re.sub(r'\blist_dags_internal\(', 'await list_dags_internal(', content)
    
    # Add await to get_dag_detailed_info calls  
    content = re.sub(r'\bget_dag_detailed_info\(', 'await get_dag_detailed_info(', content)
    
    # Write back the modified content
    with open('/root/Workspace-RL8/MCP-Airflow-API/src/mcp_airflow_api/airflow_api.py', 'w') as f:
        f.write(content)
    
    print("Conversion complete!")

if __name__ == "__main__":
    convert_mcp_tools_to_async()
