#!/bin/bash
# Cloud Readiness Accelerator - GitHub Publication Script
# Execute this script to publish the framework to GitHub

echo "=========================================="
echo "Cloud Readiness Accelerator"
echo "GitHub Publication Script"
echo "=========================================="
echo ""

# Step 1: Create local directory
echo "Step 1: Creating local repository directory..."
mkdir -p Cloud-Readiness-acceleartor
cd Cloud-Readiness-acceleartor

# Step 2: Initialize git
echo "Step 2: Initializing git repository..."
git init

# Step 3: Add remote
echo "Step 3: Adding GitHub remote..."
git remote add origin https://github.com/upendra-29003/Cloud-Readiness-acceleartor.git

# Step 4: Verify remote
echo "Step 4: Verifying remote..."
git remote -v

# Step 5: Create GitHub directories
echo "Step 5: Creating GitHub configuration directories..."
mkdir -p .github/workflows
mkdir -p .github/ISSUE_TEMPLATE

# Step 6: Copy files (you need to copy files manually or use the copy commands below)
echo "Step 6: Files should be copied from deployment folder"
echo "        Copy all files from 'Cloud Readiness acceleartor/' to 'Cloud-Readiness-acceleartor/'"
echo ""
echo "        On Windows (PowerShell):"
echo "        Copy-Item -Path 'Cloud Readiness acceleartor\*' -Destination 'Cloud-Readiness-acceleartor\' -Recurse -Force"
echo ""
echo "        On macOS/Linux:"
echo "        cp -r 'Cloud Readiness acceleartor'/* Cloud-Readiness-acceleartor/"
echo ""
read -p "Press Enter after copying files..."

# Step 7: Configure git user (if not already configured)
echo "Step 7: Configuring git user..."
echo "Enter your name (or press Enter to skip if already configured):"
read git_name
if [ ! -z "$git_name" ]; then
    git config --global user.name "$git_name"
fi

echo "Enter your email (or press Enter to skip if already configured):"
read git_email
if [ ! -z "$git_email" ]; then
    git config --global user.email "$git_email"
fi

# Step 8: Add all files
echo "Step 8: Adding all files to git..."
git add .

# Step 9: Verify files are staged
echo "Step 9: Verifying files are staged..."
git status

# Step 10: Create initial commit
echo "Step 10: Creating initial commit..."
git commit -m "Initial commit: Cloud Readiness Accelerator v1.0

- Complete assessment framework with 4-phase methodology
- 24+ reusable templates for discovery, scoring, business case, risk, governance, and reporting
- 12+ comprehensive guides for phases, integration, customization, and QA
- Multi-cloud evaluation support (AWS, Azure, Google Cloud)
- Business case development with TCO and ROI analysis
- Risk and compliance assessment framework
- Migration planning and wave sequencing
- Enterprise governance and stakeholder management
- GitHub workflows for CI/CD and release management
- Issue templates for bug reports, feature requests, and questions
- Complete documentation and getting started guides
- MIT License for open-source distribution"

# Step 11: Push to GitHub
echo "Step 11: Pushing to GitHub..."
echo "Note: You may be prompted for GitHub credentials"
git push -u origin main

# Step 12: Verify push
echo "Step 12: Verifying push..."
echo "Repository URL: https://github.com/upendra-29003/Cloud-Readiness-acceleartor"
echo ""
echo "=========================================="
echo "✅ GitHub Publication Complete!"
echo "=========================================="
echo ""
echo "Next Steps:"
echo "1. Go to: https://github.com/upendra-29003/Cloud-Readiness-acceleartor/settings"
echo "2. Enable: Discussions, Issues, Projects, Wiki"
echo "3. Add topics: cloud, readiness, assessment, migration, aws, azure, gcp"
echo "4. Create release v1.0.0"
echo ""
