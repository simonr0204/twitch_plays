import twitch
from keyholder import holdForSeconds as Press
from secrets import username, key
from collections import Counter


def collect_messages(t):
    new_messages = t.twitch_recieve_messages()

    if not new_messages:
        return
    else:
        msgs = [message['message'].lower() for message in new_messages]
        inputs = [char for message in msgs for char in message]
        return inputs


def most_frequent(commands):
    occurrences = Counter(commands)
    return occurrences.most_common(1)[0][0]


def main():

    t = twitch.Twitch()
    t.twitch_connect(username, key)

    while True:
        inputs = collect_messages(t)

        if inputs is None:
            continue

        command = most_frequent(inputs)

        print('Executing : {}'.format(command))
        Press(command, 0.1)


if __name__ == '__main__':
    main()
