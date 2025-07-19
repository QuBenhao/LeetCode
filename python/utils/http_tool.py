import logging
import time
from typing import Optional, List
import base64

import requests


def general_request(url: str, func=None, request_method: str = "post",
                    params=None, data=None, json=None, depth=3, **kwargs):
    try:
        match request_method:
            case "get":
                resp = requests.get(url, params=params, timeout=30, **kwargs)
            case "put":
                resp = requests.put(url, data=data, timeout=30, **kwargs)
            case _:
                resp = requests.post(url, data=data, json=json, timeout=30, **kwargs)
        if resp.status_code == 200:
            return func(resp) if func else resp
        if resp.status_code == 429 and depth > 0:
            logging.warning(f"{url} Too many requests, please try again later!")
            time.sleep((4 - depth) * 3)
            return general_request(url, func, request_method, params, data, json, depth - 1, **kwargs)
        if resp.status_code == 403:
            logging.warning(f"{url} Access denied! msg: {resp.text}")
            time.sleep(1)
            return None
        logging.debug(f"Response code[{resp.status_code}] msg: {resp.text}")
    except requests.ConnectTimeout:
        if depth > 0:
            time.sleep((4 - depth) * 2)
            logging.warning(f"{url} Connection timeout!")
            return general_request(url, func, request_method, params, data, json, depth - 1, **kwargs)
        else:
            logging.error(f"{url} Connection timeout!", exc_info=True)
    except Exception as _:
        logging.error(f"Request error: {url}, params: {params}, data: {data}, json: {json}", exc_info=True)
    return None


def github_iterate_repo(owner: str, repo: str, branch: str = "master", folder_path: str = "") -> List[str]:
    response = None
    try:
        # GitHub API URL for the repository tree
        api_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"

        # Get the repository tree
        response = requests.get(api_url)
        response.raise_for_status()
        tree = response.json().get('tree', [])

        # Iterate through the tree and print folder and file names
        files = []
        for item in tree:
            path = item['path']
            if not path.startswith(folder_path):
                continue
            if item['type'] == 'tree':
                logging.debug(f"Folder: {path}")
            elif item['type'] == 'blob':
                files.append(path)
        return files
    except requests.exceptions.RequestException as _:
        if response and response.status_code == 403 and "API rate limit exceeded" in response.text:
            logging.warning("API rate limit exceeded. Maximum 60 requests per hour. You can change ip or wait 1 hour.")
        else:
            logging.debug(f"Error accessing the GitHub API", exc_info=True)
    except Exception as _:
        logging.error(f"An error occurred while iterating the GitHub repository", exc_info=True)
    return []


def github_get_file_content(owner: str, repo: str, file_path: str, branch: str = "master") -> Optional[str]:
    response = None
    try:
        # GitHub API URL for the file content
        api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}?ref={branch}"

        # Get the file content
        response = requests.get(api_url)
        response.raise_for_status()
        file_content = response.json().get('content', '')

        # Decode the base64 content
        decoded_content = base64.b64decode(file_content).decode('utf-8')
        return decoded_content

    except requests.exceptions.RequestException as e:
        if response and response.status_code == 403 and "API rate limit exceeded" in response.text:
            logging.warning("API rate limit exceeded. Maximum 60 requests per hour. You can change ip or wait 1 hour.")
        else:
            logging.debug(f"Error accessing the GitHub API", exc_info=True)
    except Exception as e:
        logging.error(f"An error occurred while getting the file content: {e}", exc_info=True)
    return None
