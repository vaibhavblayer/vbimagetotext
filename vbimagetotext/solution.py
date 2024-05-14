import click
from .functions import process_text
import os
from .prompts import prompt_solution
from rich.console import Console
import sys
from .choice_option import ChoiceOption


@click.command(
    help="Process text using OpenAI's GPT-4 model to solve problem."
)
@click.option(
    "-t",
    "--text",
    type=click.Path(exists=True),
    required=True,
    help="Text to process",
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
@click.option(
    "--max-tokens",
    type=int,
    default=2000,
    show_default=True,
    help="The maximum number of tokens to generate.",
)
@click.option(
    "-p",
    "--prompt",
    type=str,
    default=prompt_solution,
    show_default=True,
    help="Prompt to use for the completion",
)
def solution(text, model, max_tokens, prompt):
    """
    Process text using OpenAI's GPT-4 model to solve problem.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        console = Console()
        console.print(
            "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.", style="bold red")
        sys.exit(1)

    process_text(text, prompt, model, api_key, max_tokens)
