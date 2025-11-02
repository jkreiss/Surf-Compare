import subprocess
import json

def get_bouy_data():
    subprocess.run(
        ["scrapy", "crawl", "lebonsbay", "-O", "ran.json"],
        cwd="buoyscraper"
    )
    with open("buoyscraper/ran.json") as f:
        data = json.load(f)

    return data
