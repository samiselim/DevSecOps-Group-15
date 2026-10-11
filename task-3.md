# Lab Task: Python Calculator with GitHub Actions

**Lab:** GitHub Actions – Introduction to CI/CD  
**Duration:** 45–60 Minutes  
**Objective:** Build a simple Python calculator, automate its execution using GitHub Actions, and practice Git branching and Pull Requests.

## Task 1: Create the Calculator Application

In your existing GitHub repository, create a single Python file named `calculator.py`.

Your application must contain the following functions:

- `add(a, b)` – Returns the sum of two numbers.
- `subtract(a, b)` – Returns the difference between two numbers.
- `multiply(a, b)` – Returns the product of two numbers.
- `divide(a, b)` – Returns the result of dividing two numbers and handles division by zero.

At the end of the file, call each function with sample values and print the results.

**Expected example output:**

```text
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```

Run the application locally using:

```bash
python3 calculator.py
```

## Task 2: Configure GitHub Actions

Create the following workflow file in your existing repository:

`.github/workflows/ci.yml`

Configure the workflow to:

1. Run automatically when code is pushed to the `main` branch.
2. Run when a Pull Request targets the `main` branch.
3. Support manual execution using `workflow_dispatch`.
4. Use an Ubuntu GitHub-hosted runner.
5. Check out the repository code.
6. Set up Python 3.13.
7. Execute `calculator.py`.

**Note:** Do not add pytest, flake8, or automated testing steps. The workflow should only execute the calculator application.

## Task 3: Push Your Changes

1. Stage your changes.
2. Commit using the message `feat: add calculator and GitHub Actions workflow`.
3. Push your changes to the `main` branch.
4. Open your GitHub repository and navigate to the **Actions** tab.
5. Verify that the workflow completed successfully.
6. Inspect the logs and confirm the calculator output.

## Task 4: Git Branching and Pull Requests

1. Create a new branch named `feature/update-calculator`.
2. Add a new function called `power(a, b)` that calculates exponentiation.
3. Call the new function and print its result.
4. Commit using the message `feat: add power operation`.
5. Push the feature branch to GitHub.
6. Create a Pull Request targeting `main`.
7. Verify that GitHub Actions executes automatically.
8. Review the workflow logs.
9. Merge the Pull Request after the workflow succeeds.

## Task 5: Submission

Submit the following:

- GitHub repository URL.
- Pull Request URL.
- Screenshot of the successful GitHub Actions workflow.
- Screenshot of the calculator output in the workflow logs.

## Completion Checklist

- [ ] Calculator implemented in one Python file.
- [ ] Calculator runs locally.
- [ ] GitHub Actions workflow configured.
- [ ] Workflow runs successfully on `main`.
- [ ] Feature branch created.
- [ ] Power function added.
- [ ] Pull Request created.
- [ ] GitHub Actions runs for the Pull Request.
- [ ] Pull Request merged.
- [ ] Required evidence submitted.

**Expected Outcome:** Understand how GitHub Actions automates application execution and how Git branches and Pull Requests fit into a basic CI/CD workflow.