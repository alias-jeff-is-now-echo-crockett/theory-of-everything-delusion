import requests
from bs4 import BeautifulSoup as bs

def embed_message(target_message, larger_message):
    """
    Embeds a smaller target message within a larger message by capitalizing 
    matching letters in order. For example:
    
    target: "dog"
    larger: "today is a good day"
    result: "toDay is a gOod day"  (capitalized D, O, G)

    Args:
        target_message (str): The message to be hidden.
        larger_message (str): The base text where letters will be capitalized.

    Returns:
        str: The larger message with hidden message embedded via capitalization.

    Raises:
        ValueError: If the target message cannot be fully embedded in the larger message.
    """
    target_message = target_message.replace(" ", "").lower()
    larger_chars = list(larger_message)
    target_index = 0
    indices = []

    for i, ch in enumerate(larger_chars):
        if target_index >= len(target_message):
            break
        if ch.lower() == target_message[target_index]:
            larger_chars[i] = ch.upper()
            indices.append(i)
            target_index += 1

    if target_index < len(target_message):
        raise ValueError("Target message cannot be fully embedded in the larger message.")

    return ''.join(larger_chars), sum(indices)

def extract_hidden_message(larger_message):
    """
    Extracts the hidden (capitalized) message from the larger message.

    Args:
        larger_message (str): The text containing the hidden message.

    Returns:
        str: The hidden message spelled out by capitalized letters.
    """
    return ''.join(ch for ch in larger_message if ch.isupper())

# Example usage
if __name__ == "__main__":
    url = "https://www.gematrix.org/?word=666"
    target_message = "this is a function that embeds a message within a larger message"
    
    # Get the web page text
    text = requests.get(url).text.lower()
    
    # Optional: extract visible content only (strip HTML tags)
    soup = bs(text, 'html.parser')
    larger_message = soup.get_text()

    # Embed the hidden message
    try:
        embedded, number = embed_message(target_message, larger_message)
        # print("Embedded message preview:", embedded[:500])  # preview first 500 chars

        # Extract it back
        recovered = extract_hidden_message(embedded)
        print("Recovered hidden message:", recovered)
        print("Number: ", number)
    except ValueError as e:
        print("Error:", e)


