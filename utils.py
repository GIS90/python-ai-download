import hashlib
from datetime import datetime


def hashlib_md5(content: str, length: int =8):
    _c = content + datetime.now().strftime("%Y%m%d%H%M%S") 
    return hashlib.md5(_c.encode()).hexdigest()[:length]