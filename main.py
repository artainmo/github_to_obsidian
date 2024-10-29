import requests
import sys

USER = "artainmo" 
TOKEN = "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"

def parse_json(url):
    while True:
        response = requests.get(url, headers={"Authorization": f"token {TOKEN}"}, 
                                params={"per_page": 100})
        data = response.json()
        if not data:
            break
        for repo in data:
            yield repo
        if "next" not in response.links:
            break  # Stop if there's no "next" link in the pagination headers
        else:
            url = response.links["next"]["url"] # Update url to the next page link

def files_from_dir(repo, directory=""):
    if stop != STOP:
        return
    for file_or_dir in parse_json(f"https://api.github.com/repos/{USER}/{repo}/contents/{directory}"):
        if file_or_dir["type"] == "dir":
            yield from files_from_dir(repo, file_or_dir["path"]) # Recursively go into all subdirectories.
        else:
            yield file_or_dir

# I will get all the public repos only, I don't need the private ones either way.
def get_all_repos():
    yield from parse_json(f"https://api.github.com/users/{USER}/repos")

repos = get_all_repos()
stop = 1
STOP = 67
for repo in get_all_repos():
    if stop == STOP:
        sys.exit()
    stop += 1
    for file in files_from_dir(repo["name"]):
            print(repo["name"] + "/" + file["path"])
