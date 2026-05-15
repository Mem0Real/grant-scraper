import trafilatura

def extract_content(url):

    downloaded = trafilatura.fetch_url(url)

    if downloaded is None:
        return None

    text = trafilatura.extract(downloaded)

    return text