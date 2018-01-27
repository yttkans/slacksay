# coding: utf_8
import os
import sys
import click
import requests
import yaml


class SettingsParamType(click.ParamType):
    name = 'settings'

    def convert(self, value, param, ctx):
        with open(value, 'r', encoding='utf_8') as f:
            return yaml.safe_load(f)


URL = 'https://slack.com/api/chat.postMessage'
SETTINGS_TYPE = SettingsParamType()
SETTINGS_DEFAULT = os.path.join(click.get_app_dir('slacksay'), '.slacksay.yaml')


@click.command()
@click.option('--settings', default=SETTINGS_DEFAULT, type=SETTINGS_TYPE)
@click.option('--profile', default='default')
@click.option('--channel', default='')
@click.option('--use_file', is_flag=True)
@click.argument('text')
def main(settings, profile, channel, use_file, text):
    d = settings[profile]
    if channel:
        d['channel'] = channel

    if use_file:
        with open(text, 'r', encoding='utf_8') as f:
            d['text'] = f.read()
    else:
        d['text'] = text

    r = requests.post(URL, data=d)
    r.raise_for_status()
    j = r.json()
    if not j['ok']:
        sys.exit(j['error'])


if __name__ == '__main__':
    main()
