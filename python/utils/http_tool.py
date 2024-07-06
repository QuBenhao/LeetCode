import time
import traceback
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
            print("Too many requests, please try again later!")
            time.sleep((4 - depth) * 3)
            return general_request(url, func, request_method, params, data, json, depth - 1, **kwargs)
        print(f"Response code[{resp.status_code}] msg: {resp.text}")
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return None
