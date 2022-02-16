import argparse

parser = argparse.ArgumentParser(description='Set telegram bot token here.')
parser.add_argument('--token', dest='token', help='Set token here')
parser.add_argument('--dbhost', dest='dbhost', default='127.0.0.1')
parser.add_argument('--dbport', dest='dbport', default='5430')
parser.add_argument('--database', dest='database', default='postgres')
parser.add_argument('--dbuser', dest='dbuser', default='postgres')
parser.add_argument('--dbpassword', dest='dbpassword', default='password')


def parse_args():
    return parser.parse_args()
