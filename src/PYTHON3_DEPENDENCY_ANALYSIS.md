# HomeCampus: Python 3 Dependency Analysis

This document outlines the key dependencies in the HomeCampus application and their migration path to Python 3.

## Core Framework Dependencies

| Dependency | Current Use | Python 3 Compatibility | Migration Path |
|------------|-------------|------------------------|----------------|
| **Tipfy** | Web framework for GAE | ❌ Not compatible | Replace with Flask, including new routing and handler definitions |
| **TipfyExt** | Tipfy extensions (Jinja2, forms) | ❌ Not compatible | Use Flask extensions (Flask-WTF, native Jinja2) |
| **Werkzeug** | WSGI utilities | ✅ Compatible with upgrades | Upgrade to latest version (2.3.x+) |
| **Jinja2** | Template engine | ✅ Compatible with upgrades | Upgrade to latest version (3.x+) |

## Google App Engine Dependencies

| Dependency | Current Use | Python 3 Compatibility | Migration Path |
|------------|-------------|------------------------|----------------|
| **google.appengine.ext.db** | Database models | ❌ Not compatible | Migrate to Cloud NDB or Firestore |
| **google.appengine.api.mail** | Email services | ❌ Not compatible | Use SendGrid API or similar email service |
| **google.appengine.api.users** | User authentication | ❌ Not compatible | Implement Firebase Auth or another auth system |
| **cloudstorage** | File storage | ❌ Not compatible | Use google-cloud-storage library |

## Standard Library Changes

| Python 2 Module | Python 3 Change | Files Affected | Migration Notes |
|-----------------|-----------------|----------------|----------------|
| **urllib/urllib2** | Reorganized into urllib.request, urllib.parse, etc. | Subscribe.py, Paypal.py | Update import paths and API calls |
| **StringIO** | Moved to io module | cloudstorage_api.py | Replace with io.StringIO or io.BytesIO |
| **print without ()** | Print is a function in Python 3 | 25+ files | Add parentheses to all print statements |
| **except Exception, e** | Changed syntax | 200+ files | Update to `except Exception as e` |
| **dict.iteritems()** | Removed in Python 3 | 150+ files | Replace with dict.items() |

## Third-Party Libraries

| Library | Current Version | Python 3 Compatible Version | Migration Notes |
|---------|----------------|----------------------------|-----------------|
| **simplejson** | Unknown | simplejson 3.17+ | Could switch to built-in json module |
| **wtforms** | Unknown | wtforms 3.0+ | Update to latest version |
| **babel** | Unknown | babel 2.9+ | Update to latest version |
| **pytz** | Unknown | pytz 2021.1+ | Consider using datetime.timezone instead |
| **blinker** | Unknown | blinker 1.4+ | Update to latest version |

## Recommended Replacements for Tipfy Components

| Tipfy Component | Flask/Python 3 Equivalent |
|----------------|---------------------------|
| RequestHandler | Flask views or class-based views |
| Rule | Flask app.route decorators |
| SessionMiddleware | Flask-Session |
| Tipfy.app | Flask application instance |
| cached_property | Built-in @property or functools.cached_property |
| Auth | Flask-Login |
| i18n | Flask-Babel |

## Strategy for Dependencies Migration

1. **Create requirements.txt** with Python 3 compatible versions:
   ```
   Flask==2.3.2
   Flask-WTF==1.1.1
   Jinja2==3.1.2
   Werkzeug==2.3.6
   google-cloud-ndb==2.1.1
   google-cloud-storage==2.9.0
   wtforms==3.0.1
   ```

2. **Framework Migration Sequence**:
   - First implement Flask base structure
   - Migrate URL routing
   - Create equivalent authentication mechanism
   - Implement session handling
   - Migrate form handling

3. **Database Models Migration**:
   - Create model equivalents in Cloud NDB
   - Develop migration utilities for data
   - Update all database queries

4. **Testing Approach**:
   - Start with unit tests for core components
   - Implement integration tests for critical paths
   - Test authentication flows before deployment