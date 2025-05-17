______          _______                   
| ___ \        (_)  ___|                  
| |_/ / __ ___  _| |_ ___  _ __ __ _  ___ 
|  __/ '__/ _ \| |  _/ _ \| '__/ _` |/ _ \
| |  | | | (_) | | || (_) | | | (_| |  __/
\_|  |_|  \___/| \_| \___/|_|  \__, |\___|
              _/ |              __/ |     
             |__/              |___/ 

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

