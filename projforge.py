#!/usr/bin/env python3

import os
import sys
import shutil
import subprocess
import argparse
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

ascii_banner = r"""
______          _______                   
| ___ \        (_)  ___|                  
| |_/ / __ ___  _| |_ ___  _ __ __ _  ___ 
|  __/ '__/ _ \| |  _/ _ \| '__/ _` |/ _ \
| |  | | | (_) | | || (_) | | | (_| |  __/
\_|  |_|  \___/| \_| \___/|_|  \__, |\___|
              _/ |              __/ |     
             |__/              |___/ 

             Python Project Builder
"""

script_version = "1.0.0"

GPT_PROMPTS = [
    "Generate a complete `config.py` with constants, default settings, and comments.",
    "Review all files for consistent style and unused imports. Suggest cleanups.",
    "Check `modules/` for missing `__init__.py`, circular imports, or unused modules.",
    "Simulate a CLI user session and validate argument parsing in `cli.py`.",
    "Help me structure `main.py` to support both daemon mode and CLI mode.",
    "Create a test file for `utils.py` using `pytest`, with coverage for all functions.",
    "Generate a `logger.py` module that supports file+console output with rotating logs.",
    "Review `.project_manifest.json` and generate a system diagram from its data.",
    "Create a Markdown changelog from recent commits or `project_notes.txt`.",
    "Summarize this entire codebase for onboarding a new developer."
]

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def create_project_structure(base_path, name, today, author, license_text, description, python_version, license_choice):
    def make_executable(filepath):
        os.chmod(filepath, os.stat(filepath).st_mode | 0o111)

    os.makedirs(os.path.join(base_path, "modules"), exist_ok=True)

    main_path = os.path.join(base_path, "main.py")
    write_file(main_path, f"""#!/usr/bin/env python3
# main.py - Entry point
# Created {today}

if __name__ == '__main__':
    print('Hello from {name}')
""")
    make_executable(main_path)

    write_file(os.path.join(base_path, "config.py"), f"# config.py - Configuration settings\n# Created {today}\n\nCONFIG = {{}}\n")

    cli_path = os.path.join(base_path, "cli.py")
    write_file(cli_path, f"""#!/usr/bin/env python3
# cli.py - Command-line interface logic
# Created {today}

def parse_args():
    pass
""")
    make_executable(cli_path)

    utils_path = os.path.join(base_path, "utils.py")
    write_file(utils_path, f"""#!/usr/bin/env python3
# utils.py - Helper functions
# Created {today}

def helper():
    pass
""")
    make_executable(utils_path)

    write_file(os.path.join(base_path, "modules/__init__.py"), "")
    write_file(os.path.join(base_path, "modules/example_module.py"), f"# example_module.py - Sample module\n# Created {today}\n\ndef example():\n    pass\n")
    write_file(os.path.join(base_path, "requirements.txt"), "")
    write_file(os.path.join(base_path, "project_notes.txt"), f"# project_notes.txt - Notes, ideas, todos\n# Created {today}\n")
    write_file(os.path.join(base_path, "gpt_prompts.txt"), "\n".join(GPT_PROMPTS))

    write_file(os.path.join(base_path, "README.md"), f"""# {name}

![Python](https://img.shields.io/badge/python-{python_version or '3.8'}-blue)
![License](https://img.shields.io/badge/license-{license_choice or 'Unspecified'}-lightgrey)

{ascii_banner}

## {name}

Project initialized on {today}.

## ✅ Setup Checklist

- [ ] Create and activate virtual environment
- [ ] Install requirements
- [ ] Initialize Git repository
- [ ] Run `main.py` to test

Run `main.py` to get started.
""")

    if license_text:
        write_file(os.path.join(base_path, "LICENSE"), license_text)

    setup_py = f'''from setuptools import setup, find_packages

setup(
    name="{name}",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={{"console_scripts": ["{name} = main:main"]}},
    author="{author or 'Your Name'}",
    description=f"{description or 'Replace this with a short project description.'}"
)
'''
    write_file(os.path.join(base_path, "setup.py"), setup_py)

    write_file(os.path.join(base_path, "pyproject.toml"), f'''[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "{name}"
version = "0.1"
description = "{description or 'Replace this with a short project description.'}"
authors = [{{ name = "{author or 'Your Name'}" }}]
requires-python = ">={python_version or '3.8'}"
''')

    manifest = f'''{{
  "name": "{name}",
  "created": "{today}",
  "modules": ["main.py", "config.py", "cli.py", "utils.py", "modules/"]
}}'''
    write_file(os.path.join(base_path, ".project_manifest.json"), manifest)

    stub = f'''#!/usr/bin/env python3
"""
Main module for {name}
Created on {today}
"""

def main():
    print("Hello from {name}!")

if __name__ == "__main__":
    main()
'''
    entry_path = os.path.join(base_path, f"{name}.py")
    write_file(entry_path, stub)
    make_executable(entry_path)

def main():
    parser = argparse.ArgumentParser(description="🛠️  Python Project Generator", add_help=False)
    parser.add_argument('--name', type=str, help='Name of your project')
    parser.add_argument('--venv', action='store_true', help='Automatically create a virtual environment')
    parser.add_argument('--test', action='store_true', help='Run in test mode and prompt to delete afterward')
    parser.add_argument('--author', type=str, help='Author name to include in setup.py')
    parser.add_argument('--license', type=str, help='License type (e.g., MIT, Apache-2.0, GPL-3.0)')
    parser.add_argument('--help', action='store_true', help='Show this help message and exit')
    parser.add_argument('--version', action='store_true', help='Show script version and exit')

    args = parser.parse_args()

    if args.help:
        print(f"""
{ascii_banner}

{Fore.CYAN}Usage:{Style.RESET_ALL}
  ./projforge.py [options]

{Fore.CYAN}Options:{Style.RESET_ALL}
  --name <project_name>      Set project name (optional, will prompt if not provided)
  --venv                     Create a Python virtual environment
  --author <your_name>       Add author to setup.py
  --license <type>           Add license (MIT, Apache-2.0, GPL-3.0)
  --test                     Enable test mode (project will prompt for deletion after)
  --version                  Show script version
  --help                     Show this help message and exit

Example:
  ./projforge.py --name myapp --venv --author "Jane Doe" --license MIT
""")
        return

    if args.version:
        print(f"projforge.py version {script_version}")
        return

    print(ascii_banner)
    today = datetime.now().strftime("%Y-%m-%d")

    name = args.name or input("\U0001F4C1 Enter your project name: ").strip()
    if not name:
        print("\u274C Project name required.")
        return

    author = args.author or input("\U0001F464 Enter author name [optional]: ").strip()
    description = input("\U0001F4DD Enter a short project description [optional]: ").strip()
    python_version = input("\U0001F40D Target Python version (e.g. 3.10) [default: current]: ").strip()
    license_choice = args.license or input("\U0001F4DC Enter license type (MIT, Apache-2.0, GPL-3.0) [optional]: ").strip()

    base_path = os.path.abspath(name)
    if os.path.exists(base_path):
        response = input(f"\u26A0\uFE0F Directory '{name}' already exists. Delete and recreate? [y/N]: ").strip().lower()
        if response == 'y':
            shutil.rmtree(base_path)
            print("\U0001F5D1\uFE0F Deleted existing directory.")
        else:
            print("\u274C Aborting setup.")
            return
    os.makedirs(base_path, exist_ok=True)

    license_templates = {
        "MIT": f"""MIT License\n\nCopyright (c) {today[:4]} {author or 'Your Name'}\n\nPermission is hereby granted... [MIT License Text Truncated]""",
        "Apache-2.0": f"""Apache License 2.0\n\nCopyright (c) {today[:4]} {author or 'Your Name'}\n\nLicensed under the Apache License... [Apache License Text Truncated]""",
        "GPL-3.0": f"""GNU GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007\n\nCopyright (C) {today[:4]} {author or 'Your Name'}\n... [GPL Text Truncated]"""
    }

    license_text = license_templates.get(license_choice, "")
    create_project_structure(base_path, name, today, author, license_text, description, python_version, license_choice)

    if args.venv or input("\U0001F40D Create a virtual environment in this project? [y/N]: ").strip().lower() == 'y':
        venv_path = os.path.join(base_path, ".venv")
        subprocess.run(["python3", "-m", "venv", venv_path], check=True)
        write_file(os.path.join(base_path, "venv.txt"), f"""# Virtual Environment for {name}
Created: {today}

To activate:
  source .venv/bin/activate  # macOS/Linux
  .venv\\Scripts\\activate    # Windows

To install requirements:
  pip install -r requirements.txt

To deactivate:
  deactivate
""")
        print("\u2705 Virtual environment created with helper file 'venv.txt'.")

    print("\n\U0001F389 " + Fore.GREEN + "Project setup complete!" + Style.RESET_ALL)

    if args.venv or os.path.exists(os.path.join(base_path, ".venv")):
        print(f"""{Fore.CYAN}\U0001F527 To get started:{Style.RESET_ALL}
  1. Activate your virtual environment:
     source .venv/bin/activate  # macOS/Linux
     .venv\\Scripts\\activate  # Windows

  2. Install requirements:
     pip install -r requirements.txt
""")
    else:
        print(f"""{Fore.CYAN}\U0001F527 To get started:{Style.RESET_ALL}
  1. (Optional) Create and activate a virtual environment
     python3 -m venv .venv
     source .venv/bin/activate  # macOS/Linux
     .venv\\Scripts\\activate  # Windows

  2. Install requirements:
     pip install -r requirements.txt
""")

    print(f"""{Fore.MAGENTA}\U0001F4D8 Next Steps:{Style.RESET_ALL}
  - Run your app:     python3 main.py
  - Explore README:   ./README.md
  - Review prompts:   ./gpt_prompts.txt
  - Track ideas:      ./project_notes.txt
  - Add Git:          git init && git add . && git commit -m 'Initial commit'

\U0001F4A1 Tip: You can use --name, --venv, --author, and --license to customize your setup.

{Fore.YELLOW}\U0001F4C1 Project created at:{Style.RESET_ALL} {base_path}
""")

    if args.test:
        confirm = input("\U0001F9EA Delete this test project directory now? [y/N]: ").strip().lower()
        if confirm == "y":
            shutil.rmtree(base_path)
            print("\U0001F9F9 Deleted test directory.")
        else:
            print("\U0001F4E6 Test directory kept.")

if __name__ == "__main__":
    main()

