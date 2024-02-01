import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"  # 1
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}  # 2
r = requests.get(url, headers=headers)  # 3
print(f" status code: {r.status_code}")  # 4

# Convert the response object to a dict.
response_dict = r.json()  # 5

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore info about the repos.
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository")
for repo_dict in repo_dicts:
    print("\nSelected information about first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
