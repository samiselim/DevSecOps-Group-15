1. Triggers:
- pull_request to main (runs validation checks)
- push to main (triggers build and deployment)

2. Jobs:
- lint-and-test (runs in parallel with security-scan)
- security-scan (runs in parallel with lint-and-test)
- build-and-push (waits for test & security jobs)
- deploy-staging (waits for build-and-push)
- deploy-production (waits for deploy-staging)

3. Steps for Test Job:
1. Checkout code (actions/checkout)
2. Setup Python environment (actions/setup-python)
3. Cache pip dependencies
4. Install dependencies (pip install -r requirements.txt)
5. Run code linter (flake8 / black)
6. Run unit tests (pytest)

4. Artifact:
- Tagged Docker Image (e.g., gha-calculator:latest or gha-calculator:<commit-sha>)

5. Environments:
- Staging: Automated deployment after push to main
- Production: Manual approval required before deployment

6. Fail Fast Job:
- lint-and-test: Runs first because it is the fastest job and catches code issues early before wasting compute time/resources on build and deployment jobs.