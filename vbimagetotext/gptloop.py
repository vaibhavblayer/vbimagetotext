import click
import os
import subprocess

from .gptvision import gptvision
from .choice_option import ChoiceOption


@click.command(
    help="Process images using OpenAI's GPT-4 Vision model and extract the response."
)
@click.option(
    "-i",
    "--image",
    type=click.Path(exists=True),
    required=True,
    help="Path to the image file",
)
@click.option(
    '-r',
    '--ranges',
    nargs=2,
    default=([1, 1]),
    type=click.Tuple([int, int]),
    show_default=True,
    help="Range of pages to extract text from",
)
@click.option(
    "-p",
    "--prompt",
    cls=ChoiceOption,
    type=click.Choice(
        [
            "assertion_reason",
            "mcq",
            "mcq_list",
            "mcq_solution",
            "subjective",
            "subjective_list",
            "match",
            "comprehension",
            "answer",
            "subjective_irodov",
            "solution_irodov",
            "prompt",
        ],
        case_sensitive=False),
    prompt=True,
    default=2,
    show_default=True,
    help="Prompt to use for the completion",
)
@click.option(
    "-m",
    "--model",
    cls=ChoiceOption,
    type=click.Choice(
        [
            "gpt-4o",
            "gpt-4-turbo",
            "gpt-4-turbo-preview",
            "gpt-4-vision-preview",
        ],
        case_sensitive=False),
    prompt=True,
    default=1,
    show_default=True,
    help="Prompt to use for the completion",
)
@click.pass_context
def gptloop(ctx, image, ranges, prompt, model):
    """
    Process images using OpenAI's GPT-4 Vision model and extract the response.
    """
    for i in range(ranges[0], ranges[1] + 1):
        dirname = os.path.dirname(image)
        filename = os.path.basename(image)
        extension = os.path.splitext(filename)[1]
        basename = filename.split('_')[0]
        image_path = os.path.join(dirname, f"{basename}_{i}{extension}")
        ctx.invoke(gptvision, image=[image_path],
                   prompt=prompt, model=model, max_tokens=1000)
        subprocess.run(f"pbpaste > ./src/src_tex/problem_{i}.tex", shell=True)
