"""
Discovery script for School Assistant (Mathematics) preparation repository.
Queries educational portals, archives, and repositories for past papers,
syllabus notifications, and open-licensed learning materials.
"""

import sys
import json
import re
import urllib.parse
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9'
}

DISCOVERY_SOURCES = [
    {
        "id": "DISC-01",
        "name": "Sakshi Education - TS TRT 2018 SA Mathematics",
        "url": "https://www.sakshieducation.com/en/competitive-exams/previous-papers/ts-trt-sa-exam-2018mathematics-question-paper-final-key-held-on-4032018-356976",
        "category": "previous_papers",
        "expected_format": "PDF / HTML"
    },
    {
        "id": "DISC-02",
        "name": "Sakshi Education - TG DSC 2024 Final Key & Papers",
        "url": "https://www.sakshieducation.com/en/education-news/telangana-dsc-2024-final-key-released-download-sgt-and-sa-question-papers-key-368688",
        "category": "previous_papers",
        "expected_format": "PDF / HTML"
    },
    {
        "id": "DISC-03",
        "name": "OpenStax - Mathematics College Algebra & Precalculus",
        "url": "https://openstax.org/subjects/math",
        "category": "study_resources",
        "expected_format": "OER Textbooks (CC BY 4.0)"
    },
    {
        "id": "DISC-04",
        "name": "NCERT Textbooks Repository",
        "url": "https://ncert.nic.in/textbook.php",
        "category": "study_resources",
        "expected_format": "Textbooks Class 6-12"
    }
]

def check_source(source):
    print(f"Checking {source['name']} ({source['url']})...")
    try:
        r = requests.get(source['url'], headers=HEADERS, timeout=12)
        print(f" -> Status: {r.status_code}")
        links = []
        if r.status_code == 200:
            found = re.findall(r'href=[\'"]([^\'"]+)[\'"]', r.text)
            for l in found:
                if any(k in l.lower() for k in ['pdf', 'math', 'trt', 'dsc', 'download']):
                    full_link = urllib.parse.urljoin(source['url'], l)
                    if full_link not in links:
                        links.append(full_link)
            print(f" -> Found {len(links)} relevant links.")
        return {"status": r.status_code, "links": links[:10]}
    except Exception as e:
        print(f" -> Error: {e}")
        return {"status": "ERROR", "error": str(e), "links": []}

def main():
    results = {}
    for s in DISCOVERY_SOURCES:
        results[s['id']] = check_source(s)
    
    with open("scripts/discovery_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("Discovery completed. Saved to scripts/discovery_results.json")

if __name__ == "__main__":
    main()
