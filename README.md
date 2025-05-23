# HomeCampus

HomeCampus is an educational platform. (Further details about its specific functionality will be added as more information is gathered).

## Project Status

This project is currently undergoing a migration from Python 2 (using the Tipfy framework and older Google App Engine APIs) to Python 3 (using Flask and newer Google Cloud services like Cloud NDB and Cloud Storage).

## Key Technologies

- Python 3
- Flask (web framework, replacing Tipfy)
- Jinja2 (template engine)
- Werkzeug (WSGI utilities)
- Google Cloud NDB (database models, replacing `google.appengine.ext.db`)
- Google Cloud Storage (file storage, replacing `cloudstorage`)
- WTForms (forms handling)

## Setup and Installation

(Specific setup instructions will be added here as the migration progresses.)

### Dependencies

Key Python dependencies are listed in `src/PYTHON3_DEPENDENCY_ANALYSIS.md`.
(Instructions for installing dependencies, e.g., using `pip install -r requirements.txt`, will be added once `requirements.txt` is finalized.)

## Running the Project

(Specific instructions for running the project, including local development server commands, will be added here as the migration progresses.)

## Contributing

We welcome contributions to HomeCampus! If you'd like to contribute, please follow these general guidelines:

1. **Fork the repository:** Start by forking the main HomeCampus repository to your own GitHub account.
2. **Create a new branch:** For each new feature or bug fix, create a new branch in your forked repository. This helps keep your changes organized. Use a descriptive branch name (e.g., `feature/new-login-system` or `fix/issue-123`).
3. **Make your changes:** Implement your feature or fix the bug in your branch.
4. **Write clear commit messages:** Commit your changes with clear and concise messages that explain the purpose of the commit.
5. **Add tests (recommended):** If you're adding a new feature or fixing a bug, consider adding unit tests or integration tests to ensure your changes work as expected and to prevent regressions.
6. **Submit a pull request:** Once your changes are complete and tested, submit a pull request from your branch to the main HomeCampus repository. Provide a clear description of your changes in the pull request.

## License

Please specify the project license here. For example, MIT License, Apache License 2.0, etc.
