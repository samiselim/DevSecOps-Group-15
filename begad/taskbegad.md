1- The pipeline will run when a PR is opened against main and when code 
is pushed to main. I will also add workflow to run it manually.

2-I will create test, security scan, build and push, and deploy jobs. Testing and security scanning can run together, while building and deploying must wait for the previous jobs to pass.

3-First, checkout the code, set up Python, install the dependencies, install pytest, and run the tests. If any step fails, the job will stop.

4-The artifact will be a Docker image containing the Python API and its dependencies. I will push it to GHCR and tag it with the commit SHA.

5-I will use Development, Staging, and Production environments. Production deployment will need manual approval before it starts.

6- The test job should run first to catch code errors early and avoid wasting time building a broken application. Security scanning can run at the same time to find vulnerabilities early.

