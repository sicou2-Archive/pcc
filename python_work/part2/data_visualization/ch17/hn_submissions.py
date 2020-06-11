from operator import itemgetter

from plotly.graph_objects import Bar
from plotly import offline
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
ind = 0
for submission_id in submission_ids[:5]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"Number: {ind} id: {submission_id}\tstatus: {r.status_code}")
    ind += 1
    response_dict = r.json()

# This is just a hack to get the code to work. I am sure there is a more robust
 # way to do this properly.
    try:
        response_dict['descendants']
    except KeyError:
        response_dict['descendants'] = 0

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],

    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

xlabels, comments = [], []
for submission_dict in submission_dicts:
    # print(f"\nTitle: {submission_dict['title']}")
    # print(f"Discussion link: {submission_dict['hn_link']}")
    # print(f"Comments: {submission_dict['comments']}")
    title = submission_dict['title']
    link = submission_dict['hn_link']
    xlabels.append(f"<a href='{link}'>{title}</a>")
    comments.append(int(submission_dict['comments']))

data = [{
    'type': 'bar',
    'x': xlabels,
    'y': comments,
    'hovertext': comments,
}]

layout = {
    'title': "Most commented current HN threads",
    'xaxis': {'title': "Title of Thread"},
    'yaxis': {'title': "Number of Comments"},
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, 'data/HN_comments.html')
