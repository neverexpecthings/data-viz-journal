import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"  # 1
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}  # 2
r = requests.get(url, headers=headers)  # 3
print(f" status code: {r.status_code}")  # 4

# Process overall results.
response_dict = r.json()  #
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repo info.
repo_dicts = response_dict["items"]
repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

    # Build hover texts.
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make viz.
title = "Most-Starred Python Projects on Github"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(
    x=repo_names,
    y=stars,
    title=title,
    labels=labels,
    hover_name=hover_texts,
)

fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
)

fig.show()
