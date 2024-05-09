import click
from .gptvision import gptvision
from .geminivision import geminivision
from .copyprompt import copyprompt
from .solution import solution

CONTEXT_SETTINGS = dict(
    help_option_names=[
        '-h',
        '--help'
    ],
    auto_envvar_prefix='VBIMAGETOTEXT',
)


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass


main.add_command(gptvision)
main.add_command(geminivision)
main.add_command(copyprompt)
main.add_command(solution)
