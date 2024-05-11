from PIL import Image
from math import ceil
from typing import List


def resize(width, height):
    if width > 1024 or height > 1024:
        if width > height:
            height = int(height * 1024 / width)
            width = 1024
        else:
            width = int(width * 1024 / height)
            height = 1024
    return width, height


def count_image_tokens(image_path: str):
    """
    Calculates the number of tokens used by an image.

    Args:
        image_path (str): The path to the image file.

    Returns:
        int: The number of tokens used by the image.
    """
    # Open the image and get its size
    with Image.open(image_path) as img:
        width, height = img.size

    # Resize the image if necessary
    width, height = resize(width, height)

    # Calculate the number of tokens
    h = ceil(height / 512)
    w = ceil(width / 512)
    total = 85 + 170 * h * w

    return total


def count_total_image_tokens(image_paths: List[str]) -> int:
    """
    Calculates the total number of tokens used by a list of images.

    Args:
        image_paths (List[str]): The paths to the image files.

    Returns:
        int: The total number of tokens used by the images.
    """
    total_tokens = 0
    for image_path in image_paths:
        total_tokens += count_image_tokens(image_path)
    return total_tokens


def calculate_image_cost(image_path: List[str], cost_per_million_tokens: float = 10.0, exchange_rate: float = 84, tax_rate: float = 0.18) -> None:
    """
    Calculates and prints the cost of the API call in rupees, including tax.

    Args:
        image_path (str): The path to the image file.
        cost_per_million_tokens (float, optional): The cost per million tokens. Defaults to 60.0.
        exchange_rate (float, optional): The exchange rate from dollars to rupees. Defaults to 74.5.
        tax_rate (float, optional): The tax rate. Defaults to 0.18.
    """
    tokens = count_total_image_tokens(image_path)
    print(f"Number of tokens used by the image: {tokens}")
    cost_in_dollars = (tokens / 1000000) * cost_per_million_tokens
    cost_in_rupees = cost_in_dollars * exchange_rate
    cost_with_tax = cost_in_rupees * (1 + tax_rate)
    print(f"Cost of API call: Images including tax: ₹{cost_with_tax:.2f}")

    return cost_with_tax


def calculate_input_cost(input_text: str, cost_per_million_tokens: float = 10.0, exchange_rate: float = 84, tax_rate: float = 0.18) -> None:
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
    print(f"Cost of API call: Input including tax: ₹{cost_with_tax:.2f}")

    return cost_with_tax


def calculate_output_cost(input_text: str, cost_per_million_tokens: float = 30.0, exchange_rate: float = 84, tax_rate: float = 0.18) -> None:
    """
    Calculates and prints the cost of the API call in rupees, including tax.

    Args:
        input_text (str): The input text.
        cost_per_million_tokens (float, optional): The cost per million tokens. Defaults to 60.0.
        exchange_rate (float, optional): The exchange rate from dollars to rupees. Defaults to 74.5.
        tax_rate (float, optional): The tax rate. Defaults to 0.18.
    """
    output_tokens = len(input_text.split())
    print(f"Number of output tokens: {output_tokens}")
    cost_in_dollars = (output_tokens / 1000000) * cost_per_million_tokens
    cost_in_rupees = cost_in_dollars * exchange_rate
    cost_with_tax = cost_in_rupees * (1 + tax_rate)
    print(f"Cost of API call: Output including tax: ₹{cost_with_tax:.2f}")

    return cost_with_tax
