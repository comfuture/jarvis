import os
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app

app: FastAPI = get_fast_api_app(
    agent_dir="agents",
    session_db_url="sqlite:///./sessions.db",
    allow_origins=["http://localhost", "http://localhost:8080", "*"],
    web=True,
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
