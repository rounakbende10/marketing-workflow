# AI/ML Research Scientist Marketing Workflow

A comprehensive AI-powered marketing workflow system that uses CrewAI to automate content creation, research analysis, and LinkedIn marketing for AI/ML Research Scientists. The system leverages multiple AI agents to conduct deep technical analysis, generate engaging content, and track performance using MLflow.

## 🎯 Project Overview

This system is designed to help AI/ML Research Scientists:
- **Automate content creation** for LinkedIn marketing and thought leadership
- **Conduct comprehensive research** on trending AI/ML topics
- **Generate technical blog posts** and LinkedIn content
- **Track performance metrics** using MLflow experiment tracking
- **Optimize content strategy** based on data-driven insights

## 🏗️ System Architecture

### CrewAI Agent Workflow
The system uses 5 specialized AI agents working together:

1. **AI/ML Research Scientist** - Conducts deep technical analysis and research
2. **Research Content Creator** - Creates comprehensive research content
3. **Research Blog Writer** - Writes detailed technical blog posts
4. **Content Optimizer** - Optimizes content for SEO and engagement
5. **Content Summarizer** - Creates executive summaries and key insights

### Key Components
- **CrewAI Framework** - Orchestrates AI agents and tasks
- **MLflow Integration** - Tracks experiments and performance metrics
- **Custom Tools** - LinkedIn analysis, research tools, and content optimization
- **DALL-E Integration** - Generates technical visualizations and diagrams

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- OpenAI API key
- Serper API key (for web search)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd marketing-workflow

# Install dependencies using uv
uv sync

# Set up environment variables
cp .env.example .env
# Add your API keys to .env file
```

### Running the System

#### Option 1: Using CrewAI CLI
```bash
# Install the project in development mode
pip install -e .

# Run the crew
run_crew
```

#### Option 2: Using uv
```bash
# Run with uv
uv run run_crew
```

#### Option 3: Direct Python execution
```bash
# Run the main script
python src/marketing/main.py
```

### MLflow Setup
```bash
# Start MLflow tracking server
python mlflow_utils/start_server.py

# Access MLflow UI
open http://localhost:5001
```

## 📊 What the System Does

### 1. Research & Analysis
- **Identifies trending AI/ML topics** using web search and analysis
- **Conducts deep technical research** on selected topics
- **Analyzes performance benchmarks** and architectural comparisons
- **Evaluates implementation complexity** and practical applications

### 2. Content Generation
- **Creates LinkedIn posts** (8-12 posts) with technical insights
- **Writes research blog posts** (3-5 comprehensive articles)
- **Generates technical visualizations** using DALL-E
- **Produces executive summaries** and key insights

### 3. Content Optimization
- **SEO optimization** for better discoverability
- **Engagement optimization** for LinkedIn performance
- **Technical depth assessment** for target audience
- **Hashtag optimization** for maximum reach

### 4. Performance Tracking
- **MLflow experiment tracking** for all runs
- **Metrics logging** (execution time, content quality, engagement potential)
- **Artifact management** (generated content, visualizations)
- **Performance analytics** and reporting

## 📁 Project Structure

```
marketing-workflow/
├── src/marketing/           # Main application code
│   ├── crew.py             # CrewAI agents and tasks definition
│   ├── main.py             # Main execution script
│   ├── config/             # Configuration files
│   │   ├── agents.yaml     # Agent configurations
│   │   └── tasks.yaml      # Task definitions
│   └── tools/              # Custom tools
│       └── custom_tool.py  # LinkedIn analysis, research tools
├── mlflow_utils/           # MLflow integration
│   ├── config.py           # MLflow configuration
│   ├── utils.py            # MLflow utility functions
│   ├── start_server.py     # MLflow server startup
│   └── mlflow_artifacts/   # MLflow database and artifacts
├── resources/              # Generated content and resources
│   ├── drafts/             # Draft content
│   ├── images/             # Generated visualizations
│   └── optimized_reports/  # Optimized content reports
├── knowledge/              # Knowledge base and preferences
├── tests/                  # Test files
└── pyproject.toml          # Project configuration
```

## 🛠️ Configuration

### Environment Variables
Create a `.env` file with:
```bash
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

### Agent Configuration
Modify `src/marketing/config/agents.yaml` to customize:
- Agent roles and responsibilities
- Tool assignments
- Reasoning capabilities
- Rate limits and iteration limits

### Task Configuration
Modify `src/marketing/config/tasks.yaml` to customize:
- Task descriptions and requirements
- Expected outputs
- Quality criteria
- Dependencies between tasks

## 📈 Output Files

### Generated Content
- `research_blogs.md` - Comprehensive technical blog posts
- `research_linkedin_posts.md` - LinkedIn posts with technical insights
- `optimized_research_content.md` - SEO-optimized content
- `resources/drafts/` - Individual content files
- `resources/images/` - Generated visualizations

### MLflow Artifacts
- `mlflow_utils/mlflow_artifacts/` - Experiment data and artifacts
- `mlflow_experiment_data.json` - Exported experiment data
- `mlflow_experiment_report.md` - Detailed experiment reports

### Metrics and Analytics
- `metrics_dashboard_report.json` - Performance metrics
- `metrics_analyzer.py` - Metrics calculation and analysis
- `metrics_dashboard.py` - Interactive metrics dashboard

## 🔧 Customization

### Adding New Agents
1. Define agent in `src/marketing/config/agents.yaml`
2. Add agent creation in `src/marketing/crew.py`
3. Assign tools and configure parameters

### Adding New Tools
1. Create tool in `src/marketing/tools/custom_tool.py`
2. Register tool with agents in `src/marketing/crew.py`
3. Update agent configurations

### Modifying Tasks
1. Edit task definitions in `src/marketing/config/tasks.yaml`
2. Update task assignments in `src/marketing/crew.py`
3. Adjust task dependencies and requirements

## 📊 MLflow Integration

### Experiment Tracking
- **Automatic logging** of all CrewAI executions
- **Parameter tracking** for input configurations
- **Metrics logging** for performance analysis
- **Artifact management** for generated content

### Tracked Metrics
- **Content Generation**: Posts, blogs, visualizations created
- **Quality Metrics**: Technical depth, engagement potential
- **Performance Metrics**: Execution time, API calls, success rates
- **Business Impact**: Career advancement potential, networking opportunities

### MLflow UI Features
- **Experiment Dashboard**: View all runs and experiments
- **Metrics Comparison**: Compare performance across runs
- **Artifact Browser**: Access generated content and visualizations
- **Parameter Analysis**: Analyze impact of different configurations

## 🎯 Use Cases

### For AI/ML Research Scientists
- **Automate LinkedIn content creation** for thought leadership
- **Generate technical blog posts** for publication
- **Track content performance** and engagement metrics
- **Optimize content strategy** based on data insights

### For Content Creators
- **Scale content production** with AI assistance
- **Maintain technical accuracy** with specialized agents
- **Optimize for engagement** using data-driven insights
- **Track content performance** over time

### For Marketing Teams
- **Automate technical content creation** for AI/ML audiences
- **Generate thought leadership content** for senior professionals
- **Track campaign performance** using MLflow analytics
- **Optimize content strategy** based on metrics

## 🔍 Troubleshooting

### Common Issues

#### CrewAI Reasoning Errors
```bash
# Check CrewAI version
python -c "import crewai; print(crewai.__version__)"

# Downgrade if needed
pip install crewai==0.165.1
```

#### MLflow Server Issues
```bash
# Check if server is running
ps aux | grep mlflow

# Restart server
python mlflow_utils/start_server.py
```

#### API Rate Limiting
- Increase `max_rpm` in agent configurations
- Add delays between requests
- Check API key validity and credits

### Debug Mode
```bash
# Enable verbose logging
export CREWAI_VERBOSE=1

# Run with debug output
python src/marketing/main.py
```

## 📞 Support

For issues and questions:
1. Check the troubleshooting section above
2. Review configuration files in `src/marketing/config/`
3. Check MLflow logs for experiment tracking issues
4. Verify API keys and rate limits

## 🎉 Ready to Use

Your AI/ML Research Scientist Marketing Workflow is now ready! The system will:

1. **Automate content creation** for LinkedIn and blogs
2. **Conduct deep technical research** on trending topics
3. **Generate engaging visualizations** using DALL-E
4. **Track performance metrics** using MLflow
5. **Optimize content strategy** based on data insights

**Start the MLflow server and run your first crew to begin automating your content creation!** 🚀
