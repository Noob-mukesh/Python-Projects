def pastebin(content):
    """
    Function to post content to a pastebin service and return the URL of the paste.
    
    Args:
    content (str): The content to be pasted
    
    Returns:
    str: The URL of the paste
    """
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"}

    data = {"snippet":content}
    
    response = requests.post(f'https://bin.kv2.dev/', json=data, headers=headers)
    yield response.url

print(next(pastebin("hi")))