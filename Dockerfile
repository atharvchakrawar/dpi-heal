# Project DPI-Heal Dockerfile for BharatAgentic / aiKart Submission
FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Expose Gateway & Simulator port
EXPOSE 8000

# Run DPI-Heal Gateway Server with 24/7 Autopilot Swarm
CMD ["python", "main.py", "--serve", "--host", "0.0.0.0", "--port", "8000"]
