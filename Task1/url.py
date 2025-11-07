import urls_tools

def manageUrls(urls, action):
    """
    Manage URLs based on the specified action.

    Args:
        urls (list): List of URLs to manage.
        action (str): Action to perform on the URLs. Options are 'checkValid', 'shorten', 'format'.

    Returns:
        list: Updated list of URLs after performing the specified action.
    """
    
    
    updated_urls = []
    
    for url in urls:
        if action == 'checkValid':
            is_valid = urls_tools.is_valid_url(url)
            updated_urls.append((url, is_valid))
        elif action == 'shorten':
            shortened_url = urls_tools.shorten_url(url)
            updated_urls.append(shortened_url)
        elif action == 'format':
            formatted_url = urls_tools.format_url(url)
            updated_urls.append(formatted_url)
        else:
            raise ValueError("Invalid action specified. Choose from 'checkValid', 'shorten', 'format'.")
    
    return updated_urls     