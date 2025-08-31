#!/usr/bin/env python
"""
Script to start the MLflow server for the marketing workflow project.
"""

import subprocess
import sys
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from mlflow_utils.config import get_mlflow_server_command

def start_mlflow_server():
    """Start the MLflow server."""
    try:
        print("Starting MLflow server...")
        print(f"Tracking URI: http://localhost:5001")
        print(f"Artifact Store: {project_root}/mlflow/mlflow_artifacts/artifacts")
        print("Press Ctrl+C to stop the server")
        
        # Start the server
        subprocess.run(get_mlflow_server_command())
        
    except KeyboardInterrupt:
        print("\nMLflow server stopped.")
    except Exception as e:
        print(f"Error starting MLflow server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_mlflow_server()
