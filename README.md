1. Triggers — What events should start the pipeline?
The pipeline should run on:
- Pull Requests targeting the main branch, to test and validate changes before merging.
- Pushes to the main branch, to test the merged code and build the Docker image.
- Optionally, manual triggers using workflow_dispatch for running the pipeline when needed. 
2. Jobs — What jobs do you create? Which can run in parallel?
I would create the following jobs:
- Test: Install dependencies and run automated tests.
- Build: Build the Docker image.
- Security Scan: Scan the source code or Docker image for vulnerabilities.
- Publish: Push the Docker image to a container registry.
- Deploy: Deploy the image to the target environment.
The Test and source-code Security Scan jobs can run in parallel. The Build job should wait for successful tests. Publishing should wait for the required checks and build to succeed. Deployment should wait for publishing.
3. Steps — List the test job steps in order
The test job should execute these steps in order:
1. Check out the repository using `actions/checkout`.
2. Set up the required Python version using `actions/setup-python`.
3. Install the project dependencies.
4. Run the automated tests.
5. Report the test results and fail the job if any test fails.


4. Artifact — What is the single deployable artifact?
The single deployable artifact is the Docker image of the `gha-calculator` application. It should be tagged with a unique version or commit SHA and stored in a container registry, such as GitHub Container Registry (GHCR).

5. Environments — Which environments and which needs human approval?
I would use three environments:

- **Development:** For testing new builds and changes.
- **Staging:** For validating the application before production.
- **Production:** For serving real users.

Development and Staging deployments can run automatically after the required checks pass. Production deployment should require human approval before it proceeds.

6. Fail Fast — Which job should run first and why?
The Test job should run early in the pipeline because it detects code errors before expensive operations begin.
A source-code security scan can run in parallel with testing. The Docker image should only be built and published after the required checks pass.
