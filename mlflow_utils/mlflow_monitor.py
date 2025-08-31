#!/usr/bin/env python3
"""
MLflow Monitoring and Experiment Tracking
Comprehensive monitoring script for CrewAI experiments and metrics tracking.
"""

import mlflow
import mlflow.tracking
from mlflow.tracking import MlflowClient
import pandas as pd
from datetime import datetime
import json
import os
from pathlib import Path

class CrewAIMLflowMonitor:
    """MLflow monitoring class for CrewAI experiments"""
    
    def __init__(self, tracking_uri="http://localhost:5001"):
        """Initialize MLflow monitor"""
        self.tracking_uri = tracking_uri
        mlflow.set_tracking_uri(tracking_uri)
        self.client = MlflowClient()
        self.experiment_name = "ai-ml-research-scientist-marketing"
        
        # Ensure experiment exists
        try:
            self.experiment = self.client.get_experiment_by_name(self.experiment_name)
            if self.experiment is None:
                self.experiment_id = self.client.create_experiment(self.experiment_name)
            else:
                self.experiment_id = self.experiment.experiment_id
        except Exception as e:
            print(f"Warning: Could not connect to MLflow server: {e}")
            self.experiment_id = None
    
    def log_crew_execution(self, run_name, inputs, outputs, metrics=None, artifacts=None):
        """Log a complete CrewAI execution"""
        if self.experiment_id is None:
            print("MLflow not available, skipping logging")
            return None
            
        with mlflow.start_run(experiment_id=self.experiment_id, run_name=run_name) as run:
            # Log parameters
            mlflow.log_params(inputs)
            
            # Log metrics
            if metrics:
                for key, value in metrics.items():
                    mlflow.log_metric(key, value)
            
            # Log execution metrics
            mlflow.log_metric("execution_timestamp", datetime.now().timestamp())
            mlflow.log_metric("total_inputs", len(inputs))
            mlflow.log_metric("total_outputs", len(outputs) if outputs else 0)
            
            # Log artifacts
            if artifacts:
                for artifact_path in artifacts:
                    if os.path.exists(artifact_path):
                        mlflow.log_artifact(artifact_path)
            
            # Log directories
            for dir_path in ["resources/drafts", "resources/images"]:
                if os.path.exists(dir_path):
                    mlflow.log_artifact(dir_path)
            
            return run.info.run_id
    
    def get_experiment_summary(self):
        """Get summary of all experiments"""
        if self.experiment_id is None:
            return "MLflow server not available"
            
        runs = self.client.search_runs(
            experiment_ids=[self.experiment_id],
            order_by=["attributes.start_time DESC"]
        )
        
        summary = {
            "total_runs": len(runs),
            "experiment_name": self.experiment_name,
            "runs": []
        }
        
        for run in runs:
            run_info = {
                "run_id": run.info.run_id,
                "run_name": run.data.tags.get("mlflow.runName", "Unknown"),
                "start_time": datetime.fromtimestamp(run.info.start_time / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                "status": run.info.status,
                "metrics": dict(run.data.metrics),
                "params": dict(run.data.params)
            }
            summary["runs"].append(run_info)
        
        return summary
    
    def export_experiment_data(self, output_file="mlflow_experiment_data.json"):
        """Export experiment data to JSON file"""
        summary = self.get_experiment_summary()
        
        with open(output_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"📊 Experiment data exported to {output_file}")
        return output_file
    
    def create_experiment_report(self, output_file="mlflow_experiment_report.md"):
        """Create a markdown report of experiments"""
        summary = self.get_experiment_summary()
        
        if isinstance(summary, str):
            report_content = f"# MLflow Experiment Report\n\n{summary}"
        else:
            report_content = f"""# MLflow Experiment Report

## Experiment Summary
- **Experiment Name**: {summary['experiment_name']}
- **Total Runs**: {summary['total_runs']}
- **Generated**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Recent Runs

"""
            
            for run in summary['runs'][:10]:  # Show last 10 runs
                report_content += f"""### {run['run_name']}
- **Run ID**: {run['run_id']}
- **Start Time**: {run['start_time']}
- **Status**: {run['status']}

#### Metrics
"""
                for metric, value in run['metrics'].items():
                    report_content += f"- {metric}: {value}\n"
                
                report_content += "\n#### Parameters\n"
                for param, value in run['params'].items():
                    report_content += f"- {param}: {value}\n"
                
                report_content += "\n---\n\n"
        
        with open(output_file, 'w') as f:
            f.write(report_content)
        
        print(f"📋 Experiment report created: {output_file}")
        return output_file

def main():
    """Main function for MLflow monitoring"""
    monitor = CrewAIMLflowMonitor()
    
    print("🔍 MLflow Experiment Monitor")
    print("=" * 50)
    
    # Get experiment summary
    summary = monitor.get_experiment_summary()
    print(f"📊 {summary}")
    
    # Export data
    monitor.export_experiment_data()
    monitor.create_experiment_report()
    
    print("\n✅ MLflow monitoring complete!")
    print("🌐 View experiments at: http://localhost:5001")

if __name__ == "__main__":
    main()
