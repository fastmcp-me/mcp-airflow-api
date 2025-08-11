def main():
    pass


if __name__ == "__main__":
    """
    MCP server entry point
    """
    import os
    from fastapi import FastAPI
    from src.mcp_airflow_api.airflow_api import router as airflow_router


    app = FastAPI(title="MCP Airflow API Server")
    app.include_router(airflow_router, prefix="/airflow")

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
