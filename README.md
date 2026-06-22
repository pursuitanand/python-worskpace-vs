# Python Workspace VS

A Python development workspace configured for learning, experimentation, and building Python applications using Visual Studio Code.

## Overview

This repository serves as a centralized Python workspace for:

* Python development and testing
* Learning and practicing Python concepts
* Building small utilities and automation scripts
* Experimenting with libraries and frameworks
* Managing projects in a structured environment

## Prerequisites

* Python 3.10+
* Git
* Visual Studio Code

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/pursuitanand/python-worskpace-vs.git
cd python-worskpace-vs
```

### Create a Virtual Environment

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Install Dependencies

If a requirements file exists:

```bash
pip install -r requirements.txt
```

## Project Structure

```text
python-worskpace-vs/
├── src/                # Application source code
├── tests/              # Unit and integration tests
├── docs/               # Documentation
├── requirements.txt    # Project dependencies
├── .gitignore
└── README.md
```

## Running the Project

```bash
python main.py
```

or

```bash
python src/main.py
```

## Development

Install development tools:

```bash
pip install black flake8 pytest
```

Format code:

```bash
black .
```

Lint code:

```bash
flake8 .
```

Run tests:

```bash
pytest
```

## Git Workflow

Push changes to GitHub:

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

Set remote repository:

```bash
git remote add origin https://github.com/pursuitanand/python-worskpace-vs.git
git branch -M main
git push -u origin main
```

## Recommended VS Code Extensions

* Python
* Pylance
* Black Formatter
* GitLens
* Jupyter

## Future Enhancements

* Add CI/CD workflows
* Docker support
* Automated testing pipeline
* Project templates
* Development containers

## License

This project is licensed under the MIT License.

## Author

Anand Pursuit

GitHub: https://github.com/pursuitanand
