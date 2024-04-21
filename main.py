import sys
from typing import List

from kavenegar import KavenegarAPI
from pyaction import io


def main(args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    api_key = io.read("api_key")
    receptor = io.read("receptor")
    message = io.read("message")

    api = KavenegarAPI(api_key)
    params = {
        "receptor": receptor,
        "message": message,
    }
    api.sms_send(params)


if __name__ == "__main__":
    main(sys.argv[1:])
