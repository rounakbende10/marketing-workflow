#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
import mlflow
import os
import time
from marketing.crew import Marketing
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Add project root to path for mlflow imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from mlflow_utils import setup_mlflow, log_parameters_safe, log_metrics_safe, log_artifacts_safe, log_directories_safe, log_metrics_files_safe, create_run_context

# Setup MLflow
setup_mlflow()

def run():
    """Run the AI/ML Research Scientist LinkedIn Marketing and Research Publication crew"""
    
    try:
        print("Starting AI/ML Research Scientist Marketing Workflow...")
        print(f"OpenAI API Key configured: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")
        print(f"Serper API Key configured: {'Yes' if os.getenv('SERPER_API_KEY') else 'No'}")
        
        # Start MLflow run
        with create_run_context():
            
            start_time = time.time()
            
            # Define inputs for the crew
            inputs = {
                "user_profession": "AI/ML Research Scientist",
                "target_industries": "Technology, Healthcare, Finance, Research Labs, AI Companies",
                "user_location": "United States (open to relocation)",
                "user_experience": "5+ years in AI/ML research and engineering with expertise in LLM architectures, performance analysis, and technical benchmarking",
                "user_projects": "InboxAI: Intelligent Email Assistant using LLMs - Deployed LangGraph, OpenAI/Llama3 LLMs, and Gmail/Outlook APIs for seamless real-time email retrieval and dynamic reply generation. Orchestrated ML workflows with Apache Airflow, leveraging Chroma DB vector embeddings for rapid semantic search across email data. Health Bot: Healthcare Assistant using LLMs - Constructed a Bi-RNN, GloVe, BERT pipeline for NLP-driven disease diagnosis, boosting precision in healthcare conversational AI tasks. Enhanced response accuracy through LoRA and RLHF, enabling advanced semantic interaction and nuanced dialogue with healthcare users.",
                "research_interests": "Advanced LLM architectures, Performance benchmarking and analysis, Transformer optimizations, Training methodologies, Efficiency improvements, Multimodal LLMs, RAG systems optimization, Technical implementation analysis, Comparative performance studies, Novel training techniques",
                "current_date": datetime.now().strftime("%Y-%m-%d"),
            }
            
            # Log parameters
            log_parameters_safe(inputs)
            
            # Create and run the crew
            print("Creating Marketing crew...")
            crew = Marketing()
            print("Starting crew execution...")
            result = crew.crew().kickoff(inputs)
            print("Crew execution completed!")
            
            # Calculate execution time
            execution_time = time.time() - start_time
            execution_time_minutes = execution_time / 60
            
            # Basic metrics logging
            metrics = {
                "total_tasks_completed": len(result.tasks) if hasattr(result, 'tasks') else 1,
                "run_timestamp": datetime.now().timestamp(),
                "execution_successful": 1,
                "execution_time_minutes": execution_time_minutes,
                "total_execution_time_seconds": execution_time
            }
            log_metrics_safe(metrics)
            
            # Log artifacts, directories, and metrics files
            log_artifacts_safe()
            log_directories_safe()
            log_metrics_files_safe()
            
            print("Workflow completed successfully!")
            return result
            
    except Exception as e:
        print(f"Error during workflow execution: {e}")
        # Log error metrics
        try:
            with create_run_context():
                log_metrics_safe({"execution_successful": 0, "error": str(e)})
        except:
            pass
        raise

if __name__ == "__main__":
    try:
        result = run()
        sys.exit(0)  # Exit with success code
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)  # Exit with error code
