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

Your callback will recive a POST request whenever there is a new event, with the following data
as JSON:

::

    {
        'id': '134343',
        'project': 'project-slug',
        'message': 'This is an example',
        'culprit': 'foo.bar.baz',
        'logger': 'root',
        'level': 'error'
    }