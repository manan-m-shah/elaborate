import requests
import base64
from app.utils.storage import get_new_temp_dir
from app.utils.command_executor import clone
from app.core.parser import parseFile
from app.secrets import GITHUB_ACCESS_TOKEN


# Service to fetch repository contents from GitHub
def fetch_repo(repo_owner, repo_name):
    # Creating a temporary folder to clone the repository
    temp_folder = get_new_temp_dir()

    # Cloning the repository
    url = f"https://{GITHUB_ACCESS_TOKEN}@github.com/{repo_owner}/{repo_name}.git"
    clone(url, temp_folder)

    # Parsing the repository files
    contents = parseFile(repo_owner, repo_name, temp_folder)

    return contents


# Service to fetch repository files from GitHub
def fetch_repository_files(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/trees/main?recursive=1"
    headers = {
        "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tree_data = response.json()
        files = [item["path"] for item in tree_data.get("tree", []) if item["type"] == "blob"]
        return files
    return []


# Service to fetch repository file content from GitHub
def fetch_file_content(repo_owner, repo_name, file_path):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    headers = {
        "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        content_data = response.json()
        if "content" in content_data:
            content = base64.b64decode(content_data["content"]).decode("utf-8")
            return content
    return None


