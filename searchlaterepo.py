#!/usr/bin/env python3
"""
search-laterepo: Multi-Platform Repository Search Tool
Optimized for: Performance (Concurrency), Security (URI Encoding), and Robustness.
"""

import sys
import argparse
import requests
import concurrent.futures
from datetime import datetime, timedelta
from typing import List, Optional

# --- Constants ---
RESULTS_LIMIT = 10
LOOKBACK_DAYS = 365
TIMEOUT = 10

def get_date_limit(days: int = LOOKBACK_DAYS) -> str:
    """Returns the ISO date for a specified number of days ago."""
    limit_date = datetime.now() - timedelta(days=days)
    return limit_date.strftime('%Y-%m-%d')

def search_github(keyword: str, date_limit: str) -> List[str]:
    """Searches GitHub for repositories created after date_limit."""
    results = []
    # Using params dict handles URI encoding automatically
    url = "https://api.github.com/search/repositories"
    params = {
        "q": f"{keyword} created:>{date_limit}",
        "sort": "stars",
        "order": "desc"
    }
    
    try:
        resp = requests.get(url, params=params, timeout=TIMEOUT)
        resp.raise_for_status()
        items = resp.json().get('items', [])
        for repo in items[:RESULTS_LIMIT]:
            results.append(repo['html_url'])
    except requests.exceptions.HTTPError as e:
        if resp.status_code == 403:
            results.append("[!] GitHub Error: Rate limited (403).")
        else:
            results.append(f"[!] GitHub HTTP Error: {e}")
    except Exception as e:
        results.append(f"[!] GitHub Error: {e}")
    
    return results

def search_github(keyword: str, date_limit: str) -> List[str]:
    """Searches GitHub for repositories created after date_limit."""
    results = []
    # Using params dict handles URI encoding automatically
    url = "https://api.github.com/search/repositories"
    params = {
        "q": f"{keyword} created:>{date_limit}",
        "sort": "stars",
        "order": "desc"
    }
    
    try:
        resp = requests.get(url, params=params, timeout=TIMEOUT)
        resp.raise_for_status()
        items = resp.json().get('items', [])
        for repo in items[:RESULTS_LIMIT]:
            results.append(repo['html_url'])
    except requests.exceptions.HTTPError as e:
        if resp.status_code == 403:
            results.append("[!] GitHub Error: Rate limited (403).")
        else:
            results.append(f"[!] GitHub HTTP Error: {e}")
    except Exception as e:
        results.append(f"[!] GitHub Error: {e}")
    
    return results

def search_gitlab(keyword: str, date_limit: str) -> List[str]:
    """Searches GitLab for projects created after date_limit."""
    results = []
    url = f"https://gitlab.com/api/v4/projects"
    params = {
        "search": keyword,
        "created_after": f"{date_limit}T00:00:00Z"
    }
    
    try:
        resp = requests.get(url, params=params, timeout=TIMEOUT)
        resp.raise_for_status()
        items = resp.json()
        if isinstance(items, list):
            for repo in items[:RESULTS_LIMIT]:
                results.append(repo.get('web_url', 'N/A'))
    except Exception as e:
        results.append(f"[!] GitLab Error: {e}")
    
    return results

def search_bitbucket(keyword: str, date_limit: str) -> List[str]:
    """Searches Bitbucket for public repositories."""
    results = []
    # Bitbucket search requires specific query syntax and timestamp format
    query = f'name ~ "{keyword}" AND created_on > {date_limit}T00:00:00Z'
    url = "https://api.bitbucket.org/2.0/repositories"
    params = {"q": query}
    
    try:
        resp = requests.get(url, params=params, timeout=TIMEOUT)
        resp.raise_for_status()
        items = resp.json().get('values', [])
        for repo in items[:RESULTS_LIMIT]:
            results.append(f"https://bitbucket.org/{repo['full_name']}")
    except Exception as e:
        results.append(f"[!] Bitbucket Error: {e}")
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Search repositories across GitHub, GitLab, and Bitbucket.")
    parser.add_argument("keyword", help="Search keyword or dork", nargs="?")
    args = parser.parse_args()

    keyword = args.keyword or input("Enter search keyword: ").strip()
    if not keyword:
        print("[!] Error: Keyword is required.")
        sys.exit(1)

    date_limit = get_date_limit()
    print(f"[*] Searching repositories created since: {date_limit}\n")

    # Dispatch tasks concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            executor.submit(search_github, keyword, date_limit): "GitHub",
            executor.submit(search_gitlab, keyword, date_limit): "GitLab",
            executor.submit(search_bitbucket, keyword, date_limit): "Bitbucket"
        }

        for future in concurrent.futures.as_completed(futures):
            platform = futures[future]
            print(f"--- {platform} Results ---")
            try:
                results = future.result()
                if not results:
                    print("No results found.")
                else:
                    for i, link in enumerate(results, 1):
                        print(f"{i}. {link}")
            except Exception as e:
                print(f"[!] Critical Error in {platform} thread: {e}")
            print()

if __name__ == "__main__":
    main()