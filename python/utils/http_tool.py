import traceback
import requests


def general_request(url: str, func=None, request_method: str = "post", params=None, data=None, json=None, **kwargs):
    try:
        match request_method:
            case "get":
                resp = requests.get(url, params=params, **kwargs)
            case "put":
                resp = requests.put(url, data=data, **kwargs)
            case _:
                resp = requests.post(url, data=data, json=json, **kwargs)
        if resp.status_code != 200:
            print(f"{resp.status_code}: {resp.text}")
        return func(resp) if func else resp
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return None
