# CI/CD Pipeline Design - gha-calculator

## 1. Triggers
* Push to `main` branch: Triggers full pipeline.
* Pull Request (PR) to `main`: Triggers CI checks (Lint & Tests).

## 2. Jobs
* Code Quality & Unit Tests (Run in parallel).
* Docker Build & Push (Waits for tests).
* Deploy to Staging & Production (Sequential).

## 3. Test Job Steps
1. Checkout code.
2. Set up Python.
3. Install dependencies.
4. Run tests (`pytest`).

## 4. Artifact
* Single deployable Docker Image.

## 5. Environments
* Staging: Automatic.
* Production: Manual Approval required.

## 6. Fail Fast
* Run Linting and Unit Tests first to fail early and save build time/resources.
