#!/usr/bin/env python
import argparse
import json
import logging
import os
import subprocess
import sys

PY3 = sys.version_info[0] == 3

if PY3:
    from urllib.request import Request, urlopen
else:
    from urllib2 import urlopen, Request

__version__ = '1.0.0'
__log__ = logging.getLogger('slackme')


def slack_notify(url, channel, name, text, icon_emoji):
    req = Request(
        url=url, headers={'Content-Type': 'application/json'},
        data=json.dumps({
            'channel': channel,
            'username': name,
            'text': text,
            'icon_emoji': ':%s:' % icon_emoji,
        }).encode())
    try:
        urlopen(req).close()
    except Exception as e:
        __log__.error(e)


def git_user():
    try:
        name = subprocess.check_output('git config user.name'.split())
        if PY3:
            name = name.decode()
    except Exception as e:
        __log__.error(e)
        name = '?'
    return name.strip()


class HelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            return super(HelpFormatter, self)._format_action_invocation(
                action=action)
        if PY3:
            default = self._get_default_metavar_for_optional(action)
        else:
            default = action.dest.upper()
        args_string = self._format_args(action, default)
        return '%s %s' % (', '.join(action.option_strings), args_string)


parser = argparse.ArgumentParser(
    formatter_class=HelpFormatter,
    description='A tiny utility to send Slack messages using '
                'Incoming WebHook.')
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s ' + __version__)
parser.add_argument('-n', '--name', default='slackme',
                    help='username for the message, default: `slackme`')
parser.add_argument('-i', '--icon-emoji', default='rocket', metavar='EMOJI',
                    help='emoji for the massage, default: `rocket`')
parser.add_argument('-u', '--url', default=os.environ.get('SLACK_URL'),
                    help='hook url which can also be provided via '
                         'environment variable SLACK_URL')
parser.add_argument('-c', '--channels', nargs='+', metavar='CHANNEL')
parser.add_argument('text', metavar='TEXT', nargs='+',
                    help='parts of message to be merged into one')


def main():
    args = parser.parse_args()

    if not args.url:
        print('Please provide your webhook url.')
        exit(1)

    text = ' '.join(args.text)

    if '{git_user}' in text:
        text = text.replace('{git_user}', git_user())

    for channel in args.channels:
        slack_notify(url=args.url, channel=channel, name=args.name, text=text,
                     icon_emoji=args.icon_emoji)


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()
