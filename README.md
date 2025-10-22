# Secure Supply Chain Module: Starter Repository

This repository contains the starter files for the module.

## Pre-module: Your First Task 

Your first goal is to create a deterministic, reproducible environment. This is the foundation for all secure development.

1.  **Clone this repository:**
    ```bash
    git clone [repository-url]
    cd [repository-folder]
    ```

2.  **Create a local virtual environment:** 
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # (or .\.venv\Scripts\activate on Windows)
    ```
    *Note: The `.gitignore` file is already configured to ignore this `.venv` directory.* 

3.  **Install `pip-tools`:**
    ```bash
    pip install pip-tools
    ```

4.  **Compile your dependencies:** Use `pip-compile` to generate a hash-pinned `requirements.txt` file from the `pyproject.toml`.
    ```bash
    pip-compile --generate-hashes pyproject.toml -o requirements.txt
    ```

5.  **Sync your environment:** Use `pip-sync` to install the *exact* versions from your new lock file.
    ```bash
    pip-sync requirements.txt
    ```

6.  **Verify your environment:** Run `pip check` to ensure all dependencies are compatible.
    ```bash
    pip check
    ```
    If this command produces no output, your environment is consistent and correct.

7.  **Submit your readiness check:** Take a screenshot showing the successful `pip check` command and the presence of your `requirements.txt` file (showing the hashes).

You are now ready for Meeting 1, where we will discuss supply-chain risks and generate our first Software Bill of Materials (SBOM).
