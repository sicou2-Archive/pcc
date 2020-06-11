import requests

from plotly.graph_objs import Bar
from plotly import offline


# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:c%2B%2B&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results
response_dict = r.json()
# print(f"Total repositories: {response_dict['total_count']}")
# # Explore imformation about the repositories.
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
# print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
# repo_dict = repo_dicts[0]


# print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])
    # print(f"Name: {repo_dict['name']}")
    # print(f"Owner: {repo_dict['owner']['login']}")
    # print(f"Stars: {repo_dict['stargazers_count']}")
    # print(f"Repository: {repo_dict['html_url']}")
    # print(f"Created: {repo_dict['created_at']}")
    # print(f"Updated: {repo_dict['updated_at']}")
    # print(f"Description: {repo_dict['description']}")

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)


# # Process results.
# print(response_dict.keys())

# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },


}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='data/python_repos.html')
