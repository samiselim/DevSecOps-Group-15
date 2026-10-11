1- PRs, pushing to main, Releasing a version (tags), and hotfixs

2- jobs by default work in parallel unless you add a `needs:` then the job waits for "what it needs"
    - jobs like:
        - build
        - testing
        - publishing (docker images or packages)
        - deploy staging
        - pre-deploy testing
        - deploy production

3- steps:
    - checkout code
    - setting up runtime
    - restoring cache
    - installing dependencies
    - starting services 
    - running tests

4- artifact: Dockerfile

5- first environment that should pass thro is dev then staging which needs no human approval and final one production and this one does need a human approval yes 

6- linting then unit tests and bulding images