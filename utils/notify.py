import os
import traceback
from typing import Optional

from dotenv import load_dotenv
from pypushdeer import PushDeer
from constants import constant


def send_text_message(msg: str, description: Optional[str] = None, server: Optional[str] = None,
                      push_key: Optional[str] = None) -> bool:
    try:
        try:
            load_dotenv()
            if not server:
                server = os.getenv(constant.PUSH_SERVER)
            if not push_key:
                push_key = os.getenv(constant.PUSH_KEY)
        except Exception as e:
            print(f"Load Env exception, {e}")
        push_deer = PushDeer(pushkey=push_key)
        res = push_deer.send_text(msg, desp=description, server=server)
        return res
    except ValueError as _:
        traceback.print_exc()
        print("Possibly invalid push_key!")
    except Exception as _:
        traceback.print_exc()
        print("Possibly invalid server!")
    return False
