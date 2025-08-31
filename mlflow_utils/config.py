#!/usr/bin/env python
"""
MLflow configuration for the marketing workflow project.
"""

import os
from pathlib import Path

# MLflow Configuration
MLFLOW_TRACKING_URI = "http://localhost:5001"
MLFLOW_EXPERIMENT_NAME = "ai-ml-research-scientist-marketing"

# Database and Artifacts Configuration
PROJECT_ROOT = Path(__file__).parent.parent
MLFLOW_BACKEND_STORE_URI = f"sqlite:///{PROJECT_ROOT}/mlflow_utils/mlflow_artifacts/mlflow.db"
MLFLOW_ARTIFACT_ROOT = f"{PROJECT_ROOT}/mlflow_utils/mlflow_artifacts/artifacts"

# Server Configuration
MLFLOW_HOST = "0.0.0.0"
MLFLOW_PORT = 5001

# Experiment Settings
DEFAULT_RUN_NAME = "crewai_deep_technical_analysis"

# Artifact Paths
ARTIFACT_PATHS = [
    "research_market_analysis.md",
    "research_strategy.md", 
    "research_content_calendar.md",
    "research_linkedin_posts.md",
    "research_blogs.md",
    "optimized_research_content.md"
]

# Metrics Files
METRICS_FILES = [
    "metrics_dashboard_report.json",
    "metrics_analyzer.py",
    "metrics_dashboard.py"
]

# Directory Paths
DIRECTORY_PATHS = [
    "resources/drafts", 
    "resources/images"
]

def get_mlflow_server_command():
    """Get the command to start MLflow server."""
    return [
        "mlflow", "server",
        "--backend-store-uri", MLFLOW_BACKEND_STORE_URI,
        "--default-artifact-root", MLFLOW_ARTIFACT_ROOT,
        "--host", MLFLOW_HOST,
        "--port", str(MLFLOW_PORT)
    ]
