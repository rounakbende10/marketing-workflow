# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN_FRONTEND=noninteractive

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv for dependency management
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install Python dependencies using uv
RUN uv sync --frozen

# Copy application code
COPY . .

# Install the project in development mode
RUN pip install -e .

# Create necessary directories
RUN mkdir -p mlflow_utils/mlflow_artifacts/artifacts \
    && mkdir -p resources/drafts \
    && mkdir -p resources/images \
    && mkdir -p resources/optimized_reports

# Set permissions
RUN chmod -R 755 mlflow_utils/mlflow_artifacts/ \
    && chmod -R 755 resources/

# Expose ports
EXPOSE 5001 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5001/health || exit 1

# Default command
CMD ["python", "mlflow_utils/start_server.py"]
