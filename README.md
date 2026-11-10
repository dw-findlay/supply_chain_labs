# Secure Supply Chain Module: Starter Repository

This repository contains the starter files for the Secure Software Supply Chain module.

## Pre-Module: Your First Task

Your first goal is to create a deterministic, reproducible environment. This is the foundation for the secure software supply chain activities that follow.

> **Important:** This exercise requires **Python 3.12**. Some package versions in this repository are intentionally not the latest versions because they will be used in later software supply chain security activities. **Do not update the specified package versions unless instructed to do so.**

### 1. Verify Python 3.12

#### Windows

Open **Command Prompt** and run:

```cmd
py -3.12 --version
```

You should see:

```text
Python 3.12.x
```

If Python 3.12 is not available on your personal computer, install the 64-bit version of Python 3.12 before continuing.


#### macOS/Linux

Run:

```bash
python3.12 --version
```

You should see:

```text
Python 3.12.x
```

If Python 3.12 is not available on your personal computer, install the 64-bit version of Python 3.12 before continuing.

---

### 2. Clone This Repository

```cmd
git clone https://github.com/dw-findlay/supply_chain_labs.git
cd supply_chain_labs
```

### 3. Create a Local Virtual Environment

#### Windows Command Prompt

```cmd
py -3.12 -m venv .venv
.\.venv\Scripts\activate
```

#### macOS/Linux

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

After activation, verify that the virtual environment is using Python 3.12:

```cmd
python --version
```

You should see:

```text
Python 3.12.x
```

> The `.gitignore` file is already configured to ignore the `.venv` directory.

### 4. Install the Supply Chain Tools

Install `pip-tools`, `cyclonedx-bom`, and `pip-audit`:

```cmd
pip install pip-tools cyclonedx-bom pip-audit
```

### 5. Compile Your Dependencies

Use `pip-compile` to generate a hash-pinned `requirements.txt` file from `pyproject.toml`:

```cmd
pip-compile --generate-hashes pyproject.toml -o requirements.txt
```

### 6. Synchronize Your Environment

Use `pip-sync` to install the exact versions specified in your newly generated lock file:

```cmd
pip-sync requirements.txt
```

### 7. Verify Your Environment

Run:

```cmd
pip check
```

If this command produces no output, your environment is consistent and the installed packages have no dependency conflicts detected by `pip check`.

### 8. Submit Your Readiness Check

Take a screenshot showing:

1. The successful `pip check` command.
2. The contents of your `requirements.txt` file, including the generated hashes.

You are now ready for the next meeting, where we will discuss software supply chain risks and generate our first Software Bill of Materials (SBOM).
