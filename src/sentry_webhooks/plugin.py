"""
sentry_webhooks.plugin
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django import forms
from django.utils import simplejson
from sentry.utils.safe import safe_execute
from django.utils.translation import ugettext_lazy as _
from sentry.plugins import Plugin

import sentry_webhooks
import urllib2


class WebHooksOptionsForm(forms.Form):
    urls = forms.CharField(label=_('Repository Name'),
        widget=forms.Textarea(attrs={'class': 'span6', 'placeholder': 'https://getsentry.com/callback/url'}),
        help_text=_('Enter callback URLs to POST new events to (one per line).'))


class WebHooksPlugin(Plugin):
    author = 'Sentry Team'
    author_url = 'https://github.com/getsentry/sentry'
    version = sentry_webhooks.VERSION
    description = "Integrates web hooks."
    resource_links = [
        ('Bug Tracker', 'https://github.com/getsentry/sentry-webhooks/issues'),
        ('Source', 'https://github.com/getsentry/sentry-webhooks'),
    ]

    slug = 'webhooks'
    title = _('WebHooks')
    conf_title = title
    conf_key = 'webhooks'
    project_conf_form = WebHooksOptionsForm

    def is_configured(self, project, **kwargs):
        return bool(self.get_option('urls', project))

    def get_group_data(self, group, event):
        data = {
            'id': str(group.id),
            'checksum': group.checksum,
            'project': group.project.slug,
            'project_name': group.project.name,
            'logger': group.logger,
            'level': group.get_level_display(),
            'culprit': group.culprit,
            'message': event.message,
        }
        data['event'] = event.data or {}
        return data

    def get_webhook_urls(self, project):
        return filter(bool, self.get_option('urls', project).strip().splitlines())

    def send_webhook(self, url, data):
        req = urllib2.Request(url, data)
        req.add_header('User-Agent', 'sentry-webhooks/%s' % self.version)
        req.add_header('Content-Type', 'application/json')
        resp = urllib2.urlopen(req)
        return resp

    def post_process(self, group, event, is_new, is_sample, **kwargs):
        if not is_new:
            return

        if not self.is_configured(group.project):
            return

        data = simplejson.dumps(self.get_group_data(group, event))
        for url in self.get_webhook_urls(group.project):
            safe_execute(self.send_webhook, url, data)
