KEYWORDS = [
    "grant",
    "funding",
    "innovation",
    "startup",
    "accelerator",
    "Africa",
    "women entrepreneurs",
    "manufacturing",
    "food technology",
    "AI",
    "robotics"
]

def calculate_relevance(text):

    if not text:
        return 0

    score = 0

    text = text.lower()

    for keyword in KEYWORDS:

        if keyword.lower() in text:
            score += 1

    return score