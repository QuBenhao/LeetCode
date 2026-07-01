import logging
import os
from typing import Optional

from pypushdeer import PushDeer

import sys; from pathlib import Path; _root = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(_root))
from python.constants import constant


def send_text_message(msg: str, description: Optional[str] = None, server: Optional[str] = None,
                      push_key: Optional[str] = None) -> bool:
    try:
        if not server:
            server = os.getenv(constant.PUSH_SERVER)
        if not push_key:
            push_key = os.getenv(constant.PUSH_KEY)
        push_deer = PushDeer(pushkey=push_key)
        res = push_deer.send_text(msg, desp=description, server=server)
        return res
    except ValueError as _:
        logging.error("[PUSH_DEER] Failed, possibly invalid push_key!", exc_info=True)
    except Exception as _:
        logging.error("[PUSH_DEER] Failed, possibly invalid server or network issues!", exc_info=True)
    return False
