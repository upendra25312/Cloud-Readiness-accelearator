@echo off
REM Cloud Readiness Accelerator - GitHub Publication Script (Windows)
REM Execute this script to publish the framework to GitHub

echo ==========================================
echo Cloud Readiness Accelerator
echo GitHub Publication Script (Windows)
echo ==========================================
echo.

REM Step 1: Create local directory
echo Step 1: Creating local repository directory...
mkdir Cloud-Readiness-acceleartor
cd Cloud-Readiness-acceleartor

REM Step 2: Initialize git
echo Step 2: Initializing git repository...
git init

REM Step 3: Add remote
echo Step 3: Adding GitHub remote...
git remote add origin https://github.com/upendra-29003/Cloud-Readiness-acceleartor.git

REM Step 4: Verify remote
echo Step 4: Verifying remote...
git remote -v

REM Step 5: Create GitHub directories
echo Step 5: Creating GitHub configuration directories...
mkdir .github\workflows
mkdir .github\ISSUE_TEMPLATE

REM Step 6: Copy files
echo Step 6: Files should be copied from deployment folder
echo.
echo Copy all files from 'Cloud Readiness acceleartor\' to 'Cloud-Readiness-acceleartor\'
echo.
echo Using PowerShell:
echo Copy-Item -Path "Cloud Readiness acceleartor\*" -Destination "Cloud-Readiness-acceleartor\" -Recurse -Force
echo.
pause

REM Step 7: Configure git user (if not already configured)
echo Step 7: Configuring git user...
set /p git_name="Enter your name (or press Enter to skip): "
if not "%git_name%"=="" (
    git config --global user.name "%git_name%"
)

set /p git_email="Enter your email (or press Enter to skip): "
if not "%git_email%"=="" (
    git config --global user.email "%git_email%"
)

REM Step 8: Add all files
echo Step 8: Adding all files to git...
git add .

REM Step 9: Verify files are staged
echo Step 9: Verifying files are staged...
git status

REM Step 10: Create initial commit
echo Step 10: Creating initial commit...
git commit -m "Initial commit: Cloud Readiness Accelerator v1.0"

REM Step 11: Push to GitHub
echo Step 11: Pushing to GitHub...
echo Note: You may be prompted for GitHub credentials
git push -u origin main

REM Step 12: Verify push
echo Step 12: Verifying push...
echo Repository URL: https://github.com/upendra-29003/Cloud-Readiness-acceleartor
echo.
echo ==========================================
echo ✅ GitHub Publication Complete!
echo ==========================================
echo.
echo Next Steps:
echo 1. Go to: https://github.com/upendra-29003/Cloud-Readiness-acceleartor/settings
echo 2. Enable: Discussions, Issues, Projects, Wiki
echo 3. Add topics: cloud, readiness, assessment, migration, aws, azure, gcp
echo 4. Create release v1.0.0
echo.
pause
