import traceback
import requests


def general_request(url: str, func=None, request_method: str = "post", params=None, data=None, json=None, **kwargs):
    try:
        match request_method:
            case "get":
                resp = requests.get(url, params=params, timeout=30, **kwargs)
            case "put":
                resp = requests.put(url, data=data, timeout=30, **kwargs)
            case _:
                resp = requests.post(url, data=data, json=json, timeout=30, **kwargs)
        if resp.status_code != 200:
            print(f"Response code[{resp.status_code}] msg: {resp.text}")
        else:
            return func(resp) if func else resp
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return None
