import os
import base64
import hashlib

import pyperclip
from gooey import Gooey, GooeyParser


class NotSetSaltError(Exception):
    """没有设置salt值, 请在环境变量设置 HASHPASS_SALT"""


def generate_password(domain, salt, length=16):
    raw_password = domain + salt
    raw_password = raw_password.encode('utf8')
    s = hashlib.sha256(raw_password).digest()
    full_password = base64.b64encode(s)
    return full_password.decode('utf8')[:length]


@Gooey(
    program_name="哈希密码生成程序",
    language='Chinese',
)
def main():
    parser = GooeyParser()
    parser.add_argument('domain', metavar='域名')
    parser.add_argument('length', default=16, type=int, metavar='密码长度')
    salt = os.environ.get('HASHPASS_SALT')
    if not salt:
        raise NotSetSaltError("请在环境变量设置HASHPASS_SALT")
    args = parser.parse_args()
    hash_password = generate_password(args.domain, salt, args.length)
    pyperclip.copy(hash_password)


if __name__ == "__main__":
    main()