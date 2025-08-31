# MLflow Setup Guide for AI/ML Research Scientist Marketing Workflow

This guide explains how to set up and use MLflow for experiment tracking in the AI/ML Research Scientist Marketing Workflow system, including Docker deployment options.

## 🚀 Quick Setup

### Option 1: Local Setup
```bash
# Install dependencies using uv
uv sync

# Or install manually
pip install mlflow crewai python-dotenv

# Start MLflow tracking server
python mlflow_utils/start_server.py

# Run the system
run_crew
```

### Option 2: Docker Setup (Recommended)
```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build and run manually
docker build -t marketing-workflow .
docker run -p 5001:5001 -p 8000:8000 marketing-workflow
```

## 🐳 Docker Setup

### Prerequisites
- Docker and Docker Compose installed
- OpenAI API key
- Serper API key

### Quick Docker Start
```bash
# Clone and setup
git clone <repository-url>
cd marketing-workflow

# Create environment file
cp .env.example .env
# Edit .env with your API keys

# Start with Docker Compose
docker-compose up -d

# Access services
# MLflow UI: http://localhost:5001
# Application: http://localhost:8000
```

### Docker Configuration
The project includes:
- `Dockerfile` - Main application container
- `docker-compose.yml` - Multi-service orchestration
- `docker/` - Docker-related scripts and configurations

### Docker Services
1. **mlflow-server** - MLflow tracking server
2. **marketing-workflow** - Main application
3. **redis** - Caching and session storage (optional)

## 📊 MLflow Features

### Experiment Tracking
- **Automatic Logging**: All CrewAI runs are automatically logged
- **Parameter Tracking**: Input parameters and configuration are tracked
- **Metrics Logging**: Performance metrics and execution statistics
- **Artifact Management**: Generated content and visualizations are stored

### Tracked Metrics
- **Execution Performance**: Task completion times and success rates
- **Content Generation**: Number of posts, blogs, and visualizations created
- **Quality Metrics**: Content length, technical depth, and engagement potential
- **Resource Usage**: API calls, processing time, and artifact generation

### Artifacts Logged
- Generated markdown files (research analysis, posts, blogs)
- Technical visualizations and diagrams
- Configuration files and parameters
- Experiment reports and summaries

## 🏗️ Project Structure

```
marketing-workflow/
├── src/marketing/           # Main application code
├── mlflow_utils/           # MLflow integration
│   ├── config.py           # MLflow configuration
│   ├── utils.py            # MLflow utility functions
│   ├── start_server.py     # MLflow server startup
│   ├── test_setup.py       # MLflow connection test
│   └── mlflow_artifacts/   # MLflow database and artifacts
├── docker/                 # Docker configurations
│   ├── Dockerfile          # Main application Dockerfile
│   ├── docker-compose.yml  # Multi-service orchestration
│   └── scripts/            # Docker utility scripts
├── resources/              # Generated content and resources
└── pyproject.toml          # Project configuration
```

## 🔧 Configuration

### Environment Variables
```bash
# Required API keys
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key

# MLflow configuration
MLFLOW_TRACKING_URI=http://localhost:5001
MLFLOW_EXPERIMENT_NAME=ai-ml-research-scientist-marketing

# Docker configuration (optional)
DOCKER_MLFLOW_PORT=5001
DOCKER_APP_PORT=8000
```

### MLflow Configuration
The system uses centralized configuration in `mlflow_utils/config.py`:

```python
# MLflow settings
MLFLOW_TRACKING_URI = "http://localhost:5001"
MLFLOW_EXPERIMENT_NAME = "ai-ml-research-scientist-marketing"
MLFLOW_BACKEND_STORE_URI = "sqlite:///mlflow_utils/mlflow_artifacts/mlflow.db"
MLFLOW_ARTIFACT_ROOT = "mlflow_utils/mlflow_artifacts/artifacts"
MLFLOW_HOST = "0.0.0.0"
MLFLOW_PORT = 5001
```

### Docker Configuration
```yaml
# docker-compose.yml
version: '3.8'
services:
  mlflow-server:
    build: .
    ports:
      - "5001:5001"
    volumes:
      - ./mlflow_utils/mlflow_artifacts:/app/mlflow_utils/mlflow_artifacts
    environment:
      - MLFLOW_TRACKING_URI=http://localhost:5001
    command: python mlflow_utils/start_server.py

  marketing-workflow:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - mlflow-server
    environment:
      - MLFLOW_TRACKING_URI=http://mlflow-server:5001
    volumes:
      - ./resources:/app/resources
      - ./mlflow_utils/mlflow_artifacts:/app/mlflow_utils/mlflow_artifacts
```

## 📈 Monitoring and Analysis

### View Experiments
```bash
# Local setup
open http://localhost:5001

# Docker setup
open http://localhost:5001
```

### Generate Reports
```bash
# Local setup
python mlflow_utils/mlflow_monitor.py

# Docker setup
docker exec marketing-workflow python mlflow_utils/mlflow_monitor.py
```

### Monitor Experiments
```python
from mlflow_utils.mlflow_monitor import CrewAIMLflowMonitor

# Create monitor instance
monitor = CrewAIMLflowMonitor()

# Get experiment summary
summary = monitor.get_experiment_summary()
print(summary)

# Export data
monitor.export_experiment_data("my_experiment_data.json")

# Create report
monitor.create_experiment_report("my_experiment_report.md")
```

## 🎯 Use Cases

### Experiment Comparison
- Compare different CrewAI configurations
- Analyze performance across multiple runs
- Track improvements over time
- Identify optimal parameters

### Performance Analysis
- Monitor execution times
- Track resource usage
- Analyze content quality metrics
- Optimize system performance

### Content Management
- Version control for generated content
- Track content evolution
- Manage different content strategies
- Archive successful experiments

## 🔍 MLflow UI Features

### Dashboard
- **Experiment Overview**: View all experiments and runs
- **Metrics Comparison**: Compare metrics across runs
- **Parameter Analysis**: Analyze parameter impact on results
- **Artifact Browser**: Browse generated content and visualizations

### Run Details
- **Parameters**: View input parameters and configuration
- **Metrics**: Track performance metrics over time
- **Artifacts**: Download and view generated content
- **Tags**: Organize and categorize runs

### Experiment Management
- **Run Comparison**: Side-by-side comparison of runs
- **Search and Filter**: Find specific runs and experiments
- **Export Data**: Export experiment data for analysis
- **Delete Runs**: Clean up old experiments

## 🛠️ Advanced Configuration

### Custom Metrics
```python
from mlflow_utils import log_metrics_safe

# Log custom metrics
log_metrics_safe({
    "content_quality_score": 0.85,
    "technical_depth_score": 0.92,
    "engagement_potential": 0.78
})
```

### Custom Artifacts
```python
from mlflow_utils import log_artifacts_safe

# Log custom artifacts
log_artifacts_safe("custom_analysis.json")
log_artifacts_safe("performance_report.pdf")
log_artifacts_safe("visualization_package.zip")
```

### Custom Parameters
```python
from mlflow_utils import log_parameters_safe

# Log custom parameters
log_parameters_safe({
    "experiment_type": "deep_technical_analysis",
    "llm_topic": "mixture_of_experts",
    "content_focus": "performance_benchmarking"
})
```

## 📊 Reporting and Analytics

### Experiment Reports
- **Summary Statistics**: Overview of experiment performance
- **Trend Analysis**: Performance trends over time
- **Parameter Impact**: Analysis of parameter effects
- **Recommendations**: Optimization suggestions

### Data Export
- **JSON Export**: Structured data for analysis
- **CSV Export**: Tabular data for spreadsheets
- **Markdown Reports**: Human-readable reports
- **API Access**: Programmatic access to data

### Metrics Dashboard
```bash
# Local setup
python mlflow_utils/metrics_dashboard.py
python mlflow_utils/metrics_analyzer.py

# Docker setup
docker exec marketing-workflow python mlflow_utils/metrics_dashboard.py
docker exec marketing-workflow python mlflow_utils/metrics_analyzer.py
```

## 🔧 Troubleshooting

### Local Setup Issues

#### MLflow Server Not Starting
```bash
# Check if port 5001 is available
lsof -i :5001

# Use different port
python mlflow_utils/start_server.py --port 5002
```

#### Connection Errors
```bash
# Check MLflow server status
curl http://localhost:5001/health

# Restart MLflow server
python mlflow_utils/start_server.py
```

#### Permission Issues
```bash
# Fix directory permissions
chmod -R 755 mlflow_utils/mlflow_artifacts/

# Create directories with proper permissions
mkdir -p mlflow_utils/mlflow_artifacts/artifacts
```

#### Database Migration Issues
```bash
# If you encounter database migration errors, reset the database
rm -f mlflow_utils/mlflow_artifacts/mlflow.db

# Restart the server to create a fresh database
python mlflow_utils/start_server.py
```

### Docker Setup Issues

#### Container Not Starting
```bash
# Check container logs
docker logs marketing-workflow

# Check container status
docker ps -a

# Restart containers
docker-compose restart
```

#### Port Conflicts
```bash
# Check port usage
lsof -i :5001
lsof -i :8000

# Use different ports in docker-compose.yml
ports:
  - "5002:5001"  # Map host port 5002 to container port 5001
```

#### Volume Mount Issues
```bash
# Check volume permissions
ls -la mlflow_utils/mlflow_artifacts/

# Fix permissions
chmod -R 755 mlflow_utils/mlflow_artifacts/
```

#### Network Issues
```bash
# Check Docker network
docker network ls

# Inspect network
docker network inspect marketing-workflow_default
```

### Debug Mode
```bash
# Local debug
export CREWAI_VERBOSE=1
python src/marketing/main.py

# Docker debug
docker run -it --env CREWAI_VERBOSE=1 marketing-workflow python src/marketing/main.py
```

## 📈 Tracked Metrics

### Content Generation Metrics
- **LinkedIn Posts Generated**: Number of LinkedIn posts created
- **Research Blogs Generated**: Number of research blog articles
- **Technical Visualizations Created**: Number of AI-generated diagrams and charts
- **Content Length Analysis**: Word counts and average lengths
- **Content Completeness**: Assessment of content coverage and depth

### Quality Metrics
- **Technical Depth Score**: Measurement of technical complexity and sophistication
- **Research Credibility Score**: Academic and research credibility assessment
- **Innovation Tracking Score**: Coverage of latest innovations and trends
- **Practical Applicability Score**: Real-world application potential
- **Content Completeness Score**: Overall content quality and completeness

### Performance Metrics
- **Execution Time**: System performance and processing speed
- **API Calls Made**: Resource usage and efficiency tracking
- **Content Length Words**: Comprehensive content volume analysis
- **Visualization Quality Score**: DALL-E generated image quality assessment
- **System Reliability**: Success rates and error tracking

### Business Impact Metrics
- **Target Audience Relevance**: Alignment with senior research scientist roles
- **Thought Leadership Potential**: Demonstration of expertise and authority
- **Networking Opportunity Score**: LinkedIn engagement and networking potential
- **Career Advancement Potential**: Job search and career growth impact
- **Professional Branding Score**: Personal brand development effectiveness

## 🎉 Ready to Use

Your MLflow integration is now ready! The system will automatically:

1. **Track all CrewAI executions** with comprehensive metrics
2. **Log generated content** as artifacts for version control
3. **Monitor performance** and provide optimization insights
4. **Generate reports** for analysis and comparison
5. **Provide web interface** for experiment management

### Quick Start Commands

**Local Setup:**
```bash
# Start MLflow server
python mlflow_utils/start_server.py

# Run your crew
run_crew

# View results in MLflow UI
open http://localhost:5001
```

**Docker Setup:**
```bash
# Start all services
docker-compose up -d

# Run your crew
docker exec marketing-workflow run_crew

# View results in MLflow UI
open http://localhost:5001
```

**Start the MLflow server and run your experiments!** 🚀
