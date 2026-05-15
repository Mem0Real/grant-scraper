def summarize(text, max_sentences=5):

    if not text:
        return ""

    sentences = text.split(".")

    summary = ".".join(sentences[:max_sentences])

    return summary.strip()