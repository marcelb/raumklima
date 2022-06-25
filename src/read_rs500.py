#!/usr/bin/env python3

from rs500reader.reader import Rs500Reader


def get_and_print():
    reader = Rs500Reader()
    data = reader.get_data()
    print('{')
    print('"channels" : [')
    for i in range(1, 9, 1):
        chan_data = data.get_channel_data(i)
        if chan_data is not None:
            if i != 1:
                print(", ")
            print('{')
            print('"id" : {:7d}, "temp" : {:8.1f}, "hum" : {:6d}'.format(i, chan_data.temperature, chan_data.humidity))
            print('}')
    print(']')
    print('}')


if __name__ == '__main__':
    get_and_print()
