"""Serve static assets for development.

This blueprint mirrors the static file handling defined in ``app.yaml`` when
running the legacy Tipfy application on Google App Engine.  The assets live in
subdirectories such as ``js/`` and ``stylesheets/`` under ``src``.  These
directories are ignored by git but are expected to exist locally during
development.
"""

import os
from flask import Blueprint, current_app, send_from_directory


static_bp = Blueprint("static", __name__)


def _asset_path(folder: str) -> str:
    """Return absolute path to ``folder`` relative to the application root."""

    return os.path.join(current_app.root_path, folder)


@static_bp.route("/js/<path:filename>")
def js(filename: str):
    return send_from_directory(_asset_path("js"), filename)


@static_bp.route("/stylesheets/<path:filename>")
def stylesheets(filename: str):
    return send_from_directory(_asset_path("stylesheets"), filename)


@static_bp.route("/images/<path:filename>")
def images(filename: str):
    return send_from_directory(_asset_path("images"), filename)


@static_bp.route("/Worksheets/<path:filename>")
def worksheets(filename: str):
    return send_from_directory(_asset_path("Worksheets"), filename)

