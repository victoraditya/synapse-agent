#!/bin/bash

# Ensure script exits on error
set -e

if [ -z "$PROJECT_ID" ]; then
    echo "ERROR: PROJECT_ID environment variable is not set."
    echo "Please set it: export PROJECT_ID='your-gcp-project-id'"
    exit 1
fi

echo "===================================================="
echo "🚀 Triggering Project Synapse Deployment"
echo "Project: $PROJECT_ID"
echo "===================================================="

# Submit the build to Google Cloud Build
echo "Starting Cloud Build process..."
gcloud builds submit --config cloudbuild.yaml .

echo ""
echo "✅ Deployment pipeline triggered successfully."
echo "Check your Cloud Run dashboard for the active Service URL."
