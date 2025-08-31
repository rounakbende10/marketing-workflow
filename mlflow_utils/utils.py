#!/usr/bin/env python
"""
Utility functions for MLflow operations in the marketing workflow project.
"""

import mlflow
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

from .config import (
    MLFLOW_TRACKING_URI, 
    MLFLOW_EXPERIMENT_NAME, 
    ARTIFACT_PATHS, 
    DIRECTORY_PATHS,
    METRICS_FILES,
    DEFAULT_RUN_NAME
)

def setup_mlflow():
    """Setup MLflow tracking and experiment."""
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)

def log_parameters_safe(params: Dict[str, Any]):
    """Safely log parameters to MLflow."""
    try:
        mlflow.log_params(params)
    except Exception as e:
        print(f"Warning: MLflow parameter logging failed: {e}")

def log_metrics_safe(metrics: Dict[str, Any]):
    """Safely log metrics to MLflow."""
    try:
        for key, value in metrics.items():
            mlflow.log_metric(key, value)
    except Exception as e:
        print(f"Warning: MLflow metrics logging failed: {e}")

def log_artifacts_safe(artifact_paths: List[str] = None):
    """Safely log artifacts to MLflow."""
    if artifact_paths is None:
        artifact_paths = ARTIFACT_PATHS
    
    for artifact_path in artifact_paths:
        if os.path.exists(artifact_path):
            try:
                mlflow.log_artifact(artifact_path)
            except Exception as e:
                print(f"Warning: Could not log artifact {artifact_path}: {e}")

def log_directories_safe(directory_paths: List[str] = None):
    """Safely log directories to MLflow."""
    if directory_paths is None:
        directory_paths = DIRECTORY_PATHS
    
    for dir_path in directory_paths:
        if os.path.exists(dir_path):
            try:
                mlflow.log_artifact(dir_path)
            except Exception as e:
                print(f"Warning: Could not log directory {dir_path}: {e}")

def log_metrics_files_safe(metrics_files: List[str] = None):
    """Safely log metrics files to MLflow."""
    if metrics_files is None:
        metrics_files = METRICS_FILES
    
    for metrics_file in metrics_files:
        if os.path.exists(metrics_file):
            try:
                mlflow.log_artifact(metrics_file)
            except Exception as e:
                print(f"Warning: Could not log metrics file {metrics_file}: {e}")

def create_run_context(run_name: str = None):
    """Create a context manager for MLflow runs."""
    if run_name is None:
        run_name = DEFAULT_RUN_NAME
    
    return mlflow.start_run(run_name=run_name)

def get_experiment_info():
    """Get information about the current experiment."""
    experiment = mlflow.get_experiment_by_name(MLFLOW_EXPERIMENT_NAME)
    if experiment:
        return {
            "experiment_id": experiment.experiment_id,
            "name": experiment.name,
            "artifact_location": experiment.artifact_location
        }
    return None
