1. Triggers

Pull requests to main run tests and security checks.

Pushes to main trigger tests, build, and deployment.

2. Jobs

Test: Run Python tests.

Security: Check for vulnerabilities.

Build: Build the Docker image.

Publish: Push the image to a container registry.

Deploy: Deploy to staging, then production.

Tests and security checks can run in parallel. Build waits for the required checks to pass. Deployment waits for the image to be published.

3. Test Steps

Check out the repository.

Set up Python.

Install dependencies.

Run tests.

4. Artifact

The Docker image is the deployable artifact. Tag it with the Git commit SHA.

5. Environments

Staging: Deploy automatically after successful checks.

Production: Deploy after staging validation and human approval.

6. Fail Fast

Run tests early. If tests fail, stop the pipeline to avoid wasting time building or deploying broken code.