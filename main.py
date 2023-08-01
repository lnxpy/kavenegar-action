import os
import sys

from kavenegar import KavenegarAPI


def main(args: list[str]) -> None:
    """main function

    Args:
        args (list[str]): STDIN arguments
    """

    # now you can access the inputs like
    #    f"Hello {os.environ["INPUT_NAME"]}"
    #

    api_key = os.environ["INPUT_API_KEY"]
    receptor = os.environ["INPUT_RECEPTOR"]
    message = os.environ["INPUT_MESSAGE"]

    api = KavenegarAPI(api_key)
    params = {
        "receptor": receptor,
        "message": message,
    }
    api.sms_send(params)


if __name__ == "__main__":
    main(sys.argv)
