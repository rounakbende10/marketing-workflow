# MLflow Utilities

This directory contains all MLflow-related files and utilities for the marketing workflow project.

## Structure

```
mlflow_utils/
├── __init__.py              # Package initialization
├── config.py               # MLflow configuration settings
├── utils.py                # Utility functions for MLflow operations
├── start_server.py         # Script to start MLflow server
├── test_setup.py           # Test script for MLflow setup
├── mlflow_artifacts/       # MLflow artifacts and database
│   ├── artifacts/          # Stored artifacts
│   └── mlflow.db          # SQLite database
├── mlflow_experiment_data.json    # Experiment data
├── mlflow_experiment_report.md    # Experiment reports
├── mlflow_monitor.py       # MLflow monitoring utilities
├── metrics_dashboard.py    # Metrics dashboard
├── metrics_analyzer.py     # Metrics analysis utilities
└── metrics_dashboard_report.json  # Metrics reports
```

## Usage

### Starting the MLflow Server

```bash
# From project root
python mlflow_utils/start_server.py

# Or directly with mlflow command
mlflow server --backend-store-uri sqlite:///mlflow_utils/mlflow_artifacts/mlflow.db --default-artifact-root mlflow_utils/mlflow_artifacts/artifacts --host 0.0.0.0 --port 5001
```

### Using MLflow in Code

```python
from mlflow_utils import setup_mlflow, log_parameters_safe, log_metrics_safe, log_metrics_files_safe

# Setup MLflow
setup_mlflow()

# Log parameters safely
log_parameters_safe({"param1": "value1"})

# Log metrics safely
log_metrics_safe({"metric1": 0.95})

# Log metrics files safely
log_metrics_files_safe()
```

## Configuration

All MLflow settings are centralized in `config.py`:

- **Tracking URI**: `http://localhost:5001`
- **Experiment Name**: `ai-ml-research-scientist-marketing`
- **Database**: SQLite at `mlflow/mlflow_artifacts/mlflow.db`
- **Artifacts**: Stored in `mlflow/mlflow_artifacts/artifacts`

## Benefits of This Organization

1. **Centralized Configuration**: All MLflow settings in one place
2. **Reusable Utilities**: Safe logging functions with error handling
3. **Clean Separation**: MLflow files separated from main code
4. **Easy Maintenance**: Clear structure for updates and modifications
5. **Consistent Logging**: Standardized approach across the project
