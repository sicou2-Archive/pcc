import requests

from plotly.graph_objs import Bar
from plotly import offline


def get_requests():
    """Make an API call and store the response."""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")
    return r


def process_response(response):
    """Process response and results from get_reqests."""
    response_dict = response.json()

    # Explore imformation about the repositories.
    repo_dicts = response_dict['items']
    repo_links, stars, labels = [], [], []

    # Examine the first repository.
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    return repo_links, stars, labels


def data_visualization(repo_links, stars, labels):
    ''' Make visualization.'''
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


if __name__ == '__main__':
    r = get_requests()
    repo_links, stars, labels = process_response(r)
    data_visualization(repo_links, stars, labels)
