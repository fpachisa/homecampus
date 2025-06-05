# HomeCampus

HomeCampus is an online school of mathematics that allows students to learn, practice and track their progress. The code in this repository powers the web portal where parents and teachers can manage accounts, generate worksheets and monitor results.

## Table of Contents
- [Project Status](#project-status)
- [Features](#features)
- [Directory Overview](#directory-overview)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Project Status

The platform was originally built for Python 2 on Google App Engine using the Tipfy framework. Work is underway to migrate the application to Python 3 with Flask and newer Google Cloud services (Cloud NDB, Cloud Storage, etc.). Many modules still contain legacy Python 2 code and may not run under a pure Python 3 environment.

## Features

- **Structured syllabus** with notes and video tutorials across multiple grade levels.
- **Practice exercises** that are automatically graded.
- **Worksheet generation** for offline practice and homework.
- **Progress reports** for parents and teachers to monitor strengths and weaknesses.
- **Account management** for both parents and teachers to manage child profiles.

## Directory Overview

```
src/
├── app.yaml               # Google App Engine configuration (currently python27)
├── Database/              # Datastore models and utilities
├── templates/             # Jinja2 HTML templates
├── Grade7/                # Grade specific handlers and content
├── ...                    # Additional handlers for learning, practice and reports
```

See `src/PYTHON3_DEPENDENCY_ANALYSIS.md` for details on libraries and the migration plan.

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/homecampus.git
   cd homecampus
   ```

2. **Create a Python 3 virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   A final `requirements.txt` file has not yet been published. You can install the core libraries listed in `src/PYTHON3_DEPENDENCY_ANALYSIS.md`:

   ```bash
   pip install Flask Flask-WTF Jinja2 Werkzeug google-cloud-ndb google-cloud-storage wtforms
   ```

## Running the Application

Until all modules are ported to Python 3, the legacy Python 2 code can be run using the Google App Engine SDK:

```bash
dev_appserver.py src/app.yaml
```

As the migration progresses a Flask development server will replace the App Engine runtime for local testing.

## Contributing

1. **Fork the repository** and create a new branch for each change.
2. **Make your edits** and commit with clear messages.
3. **Open a pull request** describing your contribution. Adding tests is encouraged.

## License

Specify the project license here (e.g. MIT, Apache 2.0).
