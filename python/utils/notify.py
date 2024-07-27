import logging
import os
import sys
from typing import Optional

from dotenv import load_dotenv
from pypushdeer import PushDeer

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from python.constants import constant


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
            logging.error(f"Load Env exception, {e}")
        push_deer = PushDeer(pushkey=push_key)
        res = push_deer.send_text(msg, desp=description, server=server)
        return res
    except ValueError as _:
        logging.error("[PUSH_DEER] Failed, possibly invalid push_key!", exc_info=True)
    except Exception as _:
        logging.error("[PUSH_DEER] Failed, possibly invalid server or network issues!", exc_info=True)
    return False
