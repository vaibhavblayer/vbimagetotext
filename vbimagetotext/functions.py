import re
import requests
from rich.console import Console
import pyperclip
from typing import List
import base64
import subprocess


def encode_image(image_path):
    """
    Encodes the image located at the given image_path into base64 format.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The base64 encoded string representation of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def create_image_dicts(image_names: List[str]) -> List[dict]:
    """
    Encodes images to base64 and creates a list of dictionaries with image data.

    Args:
        image_names (List[str]): List of image file names.

    Returns:
        List[dict]: List of dictionaries containing base64 encoded image data.
    """
    image_dicts = []
    for image_name in image_names:
        base64_image = encode_image(image_name)
        image_dict = {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}"
            }
        }
        image_dicts.append(image_dict)
    return image_dicts


def process_images(image_names: List[str], prompt: str, api_key: str, max_tokens: int) -> str:
    """
    Processes images using OpenAI's GPT-4 Vision, extracts LaTeX code from the response,
    copies the first match to the clipboard, and prints the message in deep pink color.

    Args:
        image_names (List[str]): List of image file names.
        prompt (str): Prompt for the GPT-4 Vision model.
        api_key (str): OpenAI API key.

    Returns:
        str: First match of the LaTeX code in the response.
    """
    image_dicts = create_image_dicts(image_names)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    *image_dicts
                ]
            }
        ],
        "max_tokens": max_tokens
    }

    message = ""

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        response_json = response.json()

        if 'choices' in response_json and 'message' in response_json["choices"][0]:
            message = response_json["choices"][0]["message"]["content"]
        else:
            console = Console()
            console.print(
                "Error: 'choices' or 'message' not found in the API response.", style="bold red")
            return "Error: 'choices' or 'message' not found in the API response."
    else:
        console = Console()
        console.print(
            f"Error: API request failed with status code {response.status_code}.", style="bold red")
        return f"Error: API request failed with status code {response.status_code}."

    pattern = r"```latex(.*?)```"
    matches = re.findall(pattern, message, re.DOTALL)

    if matches:
        pyperclip.copy(matches[0])
        subprocess.Popen("pbpaste | bat -l latex", shell=True)
        return matches[0]
    else:
        pyperclip.copy(message)
        subprocess.Popen("pbpaste | bat -l latex", shell=True)
        return message


def process_text(input_file: str, prompt: str, api_key: str, max_tokens: int) -> str:
    """
    Processes text using OpenAI's GPT-4, extracts LaTeX code from the response,
    copies the first match to the clipboard, and prints the message in deep pink color.

    Args:
        input_file (str): Path to the input file to be processed.
        prompt (str): Prompt for the GPT-4 model.
        api_key (str): OpenAI API key.
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: First match of the LaTeX code in the response.
    """
    with open(input_file, 'r') as file:
        input_text = file.read()

    calculate_cost(input_text)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "text",
                        "text": input_text
                    }
                ]
            }
        ],
        "max_tokens": max_tokens
    }

    message = ""

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        response_json = response.json()

        if 'choices' in response_json and 'message' in response_json["choices"][0]:
            message = response_json["choices"][0]["message"]["content"]

            calculate_cost(message, 30.0)

    pyperclip.copy(message)
    subprocess.Popen("pbpaste | bat -l latex", shell=True)

    return message


def calculate_cost(input_text: str, cost_per_million_tokens: float = 10.0, exchange_rate: float = 84, tax_rate: float = 0.18) -> None:
    """
    Calculates and prints the cost of the API call in rupees, including tax.

    Args:
        input_text (str): The input text.
        cost_per_million_tokens (float, optional): The cost per million tokens. Defaults to 60.0.
        exchange_rate (float, optional): The exchange rate from dollars to rupees. Defaults to 74.5.
        tax_rate (float, optional): The tax rate. Defaults to 0.18.
    """
    input_tokens = len(input_text.split())
    print(f"Number of input tokens: {input_tokens}")
    cost_in_dollars = (input_tokens / 1000000) * cost_per_million_tokens
    cost_in_rupees = cost_in_dollars * exchange_rate
    cost_with_tax = cost_in_rupees * (1 + tax_rate)
    print(f"Cost of API call including tax: ₹{cost_with_tax:.2f}")
