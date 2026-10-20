# Pushes the homework project to https://github.com/loveaskaeva/selenium-homework
# Run: cd into the selenium-homework folder and execute: .\push_to_github.ps1

$ErrorActionPreference = "Continue"
$RepoUrl = "https://github.com/loveaskaeva/selenium-homework.git"
$Branch = "main"
$Message = "Homework: Selenium intro - saucedemo purchase test with fixtures and multi-browser"

Set-Location -Path $PSScriptRoot

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: git is not installed. Install it from https://git-scm.com/ and run again." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path ".git")) {
    git init -q -b $Branch
}

$remotes = git remote
if ($remotes -contains "origin") {
    git remote set-url origin $RepoUrl
} else {
    git remote add origin $RepoUrl
}

git add -A
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git -c user.name="loveaskaeva" -c user.email="gusevmat005@gmail.com" commit -q -m $Message
    Write-Host "Commit created."
} else {
    Write-Host "No changes to commit."
}

git push -u origin $Branch
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: push failed. Check your GitHub access (login or token)." -ForegroundColor Red
    exit 1
}

Write-Host "Done: https://github.com/loveaskaeva/selenium-homework" -ForegroundColor Green
