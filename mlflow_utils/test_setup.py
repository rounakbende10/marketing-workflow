#!/usr/bin/env python
"""
Test script to verify MLflow setup and configuration.
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from mlflow_utils import setup_mlflow, get_experiment_info, log_parameters_safe, log_metrics_safe
import mlflow

def test_mlflow_setup():
    """Test MLflow setup and basic functionality."""
    print("Testing MLflow setup...")
    
    try:
        # Setup MLflow
        setup_mlflow()
        print("✅ MLflow setup successful")
        
        # Test experiment info
        experiment_info = get_experiment_info()
        if experiment_info:
            print(f"✅ Experiment found: {experiment_info['name']}")
        else:
            print("⚠️  No experiment found")
        
        # Test basic logging
        with mlflow.start_run(run_name="test_run"):
            log_parameters_safe({"test_param": "test_value"})
            log_metrics_safe({"test_metric": 0.95})
            print("✅ Basic logging successful")
        
        print("\n🎉 All MLflow tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ MLflow test failed: {e}")
        return False

if __name__ == "__main__":
    test_mlflow_setup()
