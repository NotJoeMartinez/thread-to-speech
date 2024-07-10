import os
import sys

import click


from dotenv import load_dotenv
from rich.console import Console

THREAD_TO_SPEECH_VERSION = "1.0.0"
console = Console()


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(THREAD_TO_SPEECH_VERSION, message='thread to speech version: %(version)s')
def cli():
    pass


@cli.command(
    help="test"
)
def test():
    print(THREAD_TO_SPEECH_VERSION)