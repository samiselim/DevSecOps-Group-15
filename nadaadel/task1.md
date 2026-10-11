# 1-Triggers
- Pull requests to main: Run tests and code quality checks.
- Pushes to main: Run tests, build the Docker image, and deploy if approved.

# 2-Jobs
- Test: Run tests and check code quality.
- Build: Build the Docker image after tests pass.
- Deploy to Staging: Deploy the image after the build succeeds.
- Deploy to Production: Deploy the image after manual approval.

# 3-Steps
1. Check out the repository code.
2. Set up Python.
3. Install dependencies.
4. Run tests.
5. Run code quality checks.

# 4-Artifact
The Docker image of the Python web API.

# 5-Environments
- Development: Test changes during development.
- Staging: Test the application before production.
- Production: Deploy the final version after human approval.

# 6-Fail Fast
The test job should run first because it detects errors early and prevents wasting time building or deploying broken code.