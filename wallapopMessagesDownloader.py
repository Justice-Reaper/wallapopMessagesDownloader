#!/usr/bin/python

import requests
from datetime import datetime
import argparse

def timestamp_to_readable(ts):
    return datetime.fromtimestamp(ts / 1000).strftime('%Y-%m-%d %H:%M:%S')

def main():
    parser = argparse.ArgumentParser(description='Download Wallapop messages')
    parser.add_argument('-t', '--token', required=True, help='Bearer authentication token')
    args = parser.parse_args()

    base_url = "https://api.wallapop.com/bff/messaging/inbox"
    params = {
        "page_size": 1000000000,
        "max_messages": 1000000000
    }
    headers = {
        "Authorization": f"Bearer {args.token}"
    }

    with open('wallapop_messages.txt', 'w', encoding='utf-8') as f:
        next_from = None
        while True:
            current_params = params.copy()
            if next_from:
                current_params['from'] = next_from

            try:
                response = requests.get(base_url, params=current_params, headers=headers)
                response.raise_for_status()

                data = response.json()

                for conv in data.get('conversations', []):
                    item_title = conv['item']['title']
                    with_user_name = conv['with_user']['name']
                    f.write(f"Conversation about: {item_title} (with {with_user_name})\n")
                    f.write("-" * 50 + "\n")

                    messages = conv['messages']['messages']
                    if not messages:
                        f.write("No messages in this conversation.\n")
                    else:
                        sorted_messages = sorted(messages, key=lambda msg: msg['timestamp'])
                        for msg in sorted_messages:
                            if msg['type'] == 'text':
                                sender = "You" if msg['from_self'] else with_user_name
                                time = timestamp_to_readable(msg['timestamp'])
                                text = msg['text']
                                f.write(f"[{time}] {sender}: {text}\n")
                    f.write("\n" + "=" * 50 + "\n\n")

                next_from = data.get('next_from')
                if not next_from:
                    break

            except requests.exceptions.HTTPError as e:
                print(f"HTTP Error: {e}")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")
                break

    print("Messages saved to 'wallapop_messages.txt'")

if __name__ == "__main__":
    main()
