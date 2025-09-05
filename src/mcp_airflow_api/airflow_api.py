"""
Dynamic MCP server that loads API version-specific tools based on AIRFLOW_API_VERSION.

- Airflow API v1 Documents: https://airflow.apache.org/docs/apache-airflow/2.0.0/stable-rest-api-ref.html
- Airflow API v2 Documents: https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html
"""
import argparse
import asyncio
import logging
from typing import Any, Dict, List, Optional
from fastmcp import FastMCP
import os

from .functions import get_api_version

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def create_mcp_server():
    """Create and configure MCP server based on API version."""
    api_version = get_api_version()
    mcp = FastMCP("mcp-airflow-api")
    
    logger.info(f"Initializing MCP server for Airflow API {api_version}")
    
    if api_version == "v1":
        logger.info("Loading Airflow API v1 tools (Airflow 2.x)")
        from .tools import v1_tools
        v1_tools.register_tools(mcp)
    elif api_version == "v2":
        logger.info("Loading Airflow API v2 tools (Airflow 3.0+)")
        from .tools import v2_tools
        v2_tools.register_tools(mcp)
    else:
        raise ValueError(f"Unsupported API version: {api_version}. Use 'v1' or 'v2'")
    
    logger.info(f"MCP server initialized with API version {api_version}")
    return mcp

# Create the MCP server instance
mcp = create_mcp_server()

def main(argv: Optional[List[str]] = None):
    """Entrypoint for MCP Airflow API server.

    Supports optional CLI arguments (e.g. --log-level DEBUG) while remaining
    backward-compatible with stdio launcher expectations.
    """
    parser = argparse.ArgumentParser(prog="mcp-airflow-api", description="MCP Airflow API Server")
    parser.add_argument(
        "--log-level",
        dest="log_level",
        help="Logging level override (DEBUG, INFO, WARNING, ERROR, CRITICAL). Overrides AIRFLOW_LOG_LEVEL env if provided.",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )
    parser.add_argument(
        "--type",
        dest="transport_type",
        help="Transport type (stdio or streamable-http). Default: stdio",
        choices=["stdio", "streamable-http"],
    )
    parser.add_argument(
        "--host",
        dest="host",
        help="Host address for streamable-http transport. Default: 127.0.0.1",
    )
    parser.add_argument(
        "--port",
        dest="port",
        type=int,
        help="Port number for streamable-http transport. Default: 8000",
    )
    # Allow future extension without breaking unknown args usage
    args = parser.parse_args(argv)

    # Determine log level: CLI arg > environment variable > default
    log_level = args.log_level or os.getenv("AIRFLOW_LOG_LEVEL", "INFO")
    
    # Set logging level
    logging.getLogger().setLevel(log_level)
    logger.setLevel(log_level)
    logging.getLogger("aiohttp.client").setLevel("WARNING")  # reduce noise at DEBUG
    
    if args.log_level:
        logger.info("Log level set via CLI to %s", args.log_level)
    elif os.getenv("AIRFLOW_LOG_LEVEL"):
        logger.info("Log level set via environment variable to %s", log_level)
    else:
        logger.info("Using default log level: %s", log_level)

    # 우선순위: 실행옵션 > 환경변수 > 기본값
    # Transport type 결정
    transport_type = args.transport_type or os.getenv("FASTMCP_TYPE", "stdio")
    
    # Host 결정
    host = args.host or os.getenv("FASTMCP_HOST", "127.0.0.1")
    
    # Port 결정 (간결하게)
    port = args.port or int(os.getenv("FASTMCP_PORT", 8000))
    
    # Transport 모드에 따른 실행
    if transport_type == "streamable-http":
        logger.info(f"Starting streamable-http server on {host}:{port}")
        mcp.run(transport="streamable-http", host=host, port=port)
    else:
        logger.info("Starting stdio transport for local usage")
        mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
