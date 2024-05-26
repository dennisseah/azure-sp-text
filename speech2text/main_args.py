import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Execute an experiment.")
    parser.add_argument(
        "-f",
        "--file-path",
        type=str,
        help="Specify the MP4 file path",
        required=True,
    )
    parser.add_argument(
        "-l",
        "--lang",
        type=str,
        help="Optional: Specify the language code for the speech recognition.",
        default="en-US",
    )
    parser.add_argument(
        "-p",
        "--max-pause",
        type=int,
        help="Optional: Specify maximum pause in seconds between speeches.",
        default=30,
    )
    return parser.parse_args()
