from .prompts import prompt_assertion_reason, prompt_mcq, prompt_mcq_list, prompt_mcq_solution, prompt_subjective, prompt_match, prompt_comprehension, prompt_answer, prompt_solution

import click
import pyperclip
from .choice_option import ChoiceOption


@click.command(
    help="Copy the prompt to the clipboard."
)
@click.option(
    "-p",
    "--prompt",
    cls=ChoiceOption,
    type=click.Choice(
        [
            "assertion_reason",
            "mcq",
            "mcq_solution",
            "subjective",
            "match",
            "comprehension",
            "answer",
            "solution",
            "prompt",
        ],
        case_sensitive=False),
    prompt=True,
    default=2,
    show_default=True,
    help="Prompt to use for the completion",
)
def copyprompt(prompt):
    """
    Copy the prompt to the clipboard.
    """
    if prompt == "assertion_reason":
        pyperclip.copy(prompt_assertion_reason)
    elif prompt == "mcq":
        pyperclip.copy(prompt_mcq)
    elif prompt == "mcq_list":
        pyperclip.copy(prompt_mcq_list)
    elif prompt == "mcq_solution":
        pyperclip.copy(prompt_mcq_solution)
    elif prompt == "subjective":
        pyperclip.copy(prompt_subjective)
    elif prompt == "match":
        pyperclip.copy(prompt_match)
    elif prompt == "comprehension":
        pyperclip.copy(prompt_comprehension)
    elif prompt == "answer":
        pyperclip.copy(prompt_answer)
    elif prompt == "solution":
        pyperclip.copy(prompt_solution)
    else:
        pyperclip.copy(prompt)
    print(f"Prompt copied to clipboard: {prompt}")
