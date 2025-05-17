<!-- # QuickRepo -->

<p align="center">
  <img src="assets/projforge.png" alt="quickrepo banner" width="40%">
</p> 

# ProjForge 🛠️

A Python-powered project generator for fast, flexible bootstrapping of CLI-based Python modules. Built with developer experience in mind — featuring smart prompts, file scaffolding, virtual environment setup, and even GPT-friendly prompt files.

![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Status](https://img.shields.io/badge/status-stable-green)

---

## ✨ Features

- Interactive and flag-based setup
- Creates `main.py`, `cli.py`, `utils.py`, and a modular `modules/` folder
- Includes `README.md`, `setup.py`, `pyproject.toml`, and `requirements.txt`
- GPT prompt list for AI code reviews or onboarding
- Auto-creates virtual environment (optional)
- Test mode with cleanup option
- ANSI-colored CLI output (via `colorama`)
- Git-friendly scaffolding and `.project_manifest.json` file

---

## 🚀 Usage

Run it directly:

```bash
./projforge.py
```

Or use flags:

```bash
./projforge.py --name myapp --venv --author "Jane Doe" --license MIT
```

Available flags:

```bash
--name <project_name>      Set project name (optional, will prompt if not provided)
--venv                     Create a Python virtual environment
--author <your_name>       Add author to setup.py
--license <type>           Add license (MIT, Apache-2.0, GPL-3.0)
--test                     Enable test mode (project will prompt for deletion after)
--version                  Show script version
--help                     Show this help message and exit
```

## ✅ Project Checklist

Create and activate virtual environment

Install requirements

Run main.py to test

    Initialize Git repository

## 🧠 GPT Prompt File

The gpt_prompts.txt file contains useful suggestions for AI-based analysis and assistance, including test generation, code summarization, and more.

## 📦 Setup Example

```bash
./projforge.py --name mycliapp --venv --author "Your Name" --license MIT
cd mycliapp
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python3 main.py
```

## 🪪 License

MIT License. See LICENSE file for full terms.
