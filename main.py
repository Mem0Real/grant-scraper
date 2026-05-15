from scrapers.crawler import crawl
from scrapers.parser import extract_content
from scrapers.relevance import calculate_relevance
from scrapers.summarizer import summarize

import json

SEED_URLS = [
    "https://vc4a.com",
    "https://solve.mit.edu",
    "https://www.gsma.com/mobilefordevelopment/"
]

results = []

for site in SEED_URLS:

    links = crawl(site)

    for link in links[:20]:

        print(f"\nChecking: {link}")

        content = extract_content(link)

        if not content:
            continue

        score = calculate_relevance(content)

        if score >= 3:

            summary = summarize(content)

            entry = {
                "url": link,
                "relevance_score": score,
                "summary": summary
            }

            results.append(entry)

            print("[+] Relevant Grant Found")

with open("data/grants.json", "w", encoding="utf-8") as f:

    json.dump(results, f, indent=4)

print("\nDone.")