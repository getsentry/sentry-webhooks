sentry-webhooks
===============

An extension for Sentry that adds support for creating various web hooks.

Install
-------

Install the package via ``pip``::

    pip install sentry-webhooks

You can now configure webhooks via the plugin configuration panel within your project.

Callback Receivers
------------------

Your callback will receive a POST request whenever there is a new event, with the following data
as JSON:

::

    {
      "id": "27379932",
      "project": "project-slug",
      "project_name": "Project Name",
      "culprit": "raven.scripts.runner in main",
      "level": "error",
      "url": "https://app.getsentry.com/getsentry/project-slug/group/27379932/",
      "checksum": "c4a4d06bc314205bb3b6bdb612dde7f1",
      "logger": "root",
      "message": "This is an example Python exception",
      "event": {
        "extra": {},
        "sentry.interfaces.Stacktrace": {
          "frames": [
            {
              // stacktrace information
            }
          ]
        },
        "tags": [
          ["foo", "bar"],
        ],
        "sentry.interfaces.User": {
          // user information
        },
        "sentry.interfaces.Http": {
          // HTTP request information
        }
      }
    }
