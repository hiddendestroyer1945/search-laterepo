import requests
from datetime import datetime, timedelta

def get_date_one_year_ago():
    """Returns the ISO date for exactly one year ago."""
    one_year_ago = datetime.now() - timedelta(days=365)
    return one_year_ago.strftime('%Y-%m-%d')

def search_github(keyword, date_limit):
    print(f"\n--- Searching GitHub for '{keyword}' ---")
    # GitHub uses 'created:>YYYY-MM-DD' in the query
    url = f"https://api.github.com/search/repositories?q={keyword}+created:>{date_limit}&sort=stars&order=desc"
    try:
        response = requests.get(url)
        items = response.json().get('items', [])
        for i, repo in enumerate(items[:10], 1): # Top 10 results
            print(f"{i}. {repo['html_url']}")
    except Exception as e:
        print(f"GitHub Error: {e}")

def search_gitlab(keyword, date_limit):
    print(f"\n--- Searching GitLab for '{keyword}' ---")
    # GitLab uses 'created_after' parameter
    url = f"https://gitlab.com/api/v4/projects?search={keyword}&created_after={date_limit}T00:00:00Z"
    try:
        response = requests.get(url)
        items = response.json()
        for i, repo in enumerate(items[:10], 1):
            print(f"{i}. {repo['web_url']}")
    except Exception as e:
        print(f"GitLab Error: {e}")

def search_bitbucket(keyword, date_limit):
    print(f"\n--- Searching Bitbucket for '{keyword}' ---")
    # Bitbucket uses a 'q' filter for public repos
    # Note: Bitbucket's public search is more restrictive without an API key
    url = f"https://api.bitbucket.org/2.0/repositories?q=name~\"{keyword}\"+AND+created_on+>+\"{date_limit}\""
    try:
        response = requests.get(url)
        items = response.json().get('values', [])
        for i, repo in enumerate(items[:10], 1):
            print(f"{i}. https://bitbucket.org/{repo['full_name']}")
    except Exception as e:
        print(f"Bitbucket Error: {e}")

def main():
    keyword = input("Enter your keyword: ")
    date_limit = get_date_one_year_ago()
    
    print(f"Searching repositories created since: {date_limit}")
    
    search_github(keyword, date_limit)
    search_gitlab(keyword, date_limit)
    search_bitbucket(keyword, date_limit)

if __name__ == "__main__":
    main()