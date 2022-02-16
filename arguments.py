import argparse

parser = argparse.ArgumentParser(description='Set telegram bot token here.')
parser.add_argument('--token', dest='token', help='Set token here')


def parse_args():
    return parser.parse_args()
