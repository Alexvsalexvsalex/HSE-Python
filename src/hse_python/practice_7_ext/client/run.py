import argparse

from core import Client, ClientError


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Client for hour income calculator''')
    parser.add_argument('server_url', type=str, help='Server url')
    args = parser.parse_args()

    server_url = args.server_url

    client = Client(server_url)
    while True:
        print("Type your request: <year> <month> <salary>")
        try:
            year, month, salary = map(int, input().split())
            try:
                print("Result is", client.get_hour_income(year, month, salary))
            except ClientError as e:
                print("Client error:", e)
        except ValueError as e:
            print("Invalid input:", e)
        print()