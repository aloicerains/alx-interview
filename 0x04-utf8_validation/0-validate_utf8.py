#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Function validates the data"""
    no_bytes = 0
    for num in data:
        binary = format(num, '#010b')[-8:]
        if no_bytes == 0:
            for bit in binary:
                if bit == '0':
                    break
                no_bytes += 1
            if no_bytes == 0:
                continue  # one byte character
            if no_bytes > 4:
                return False
        else:
            # process integes to adhere to pattern '10xxxx'
            if not (binary[0] == '1' and binary[1] == '0'):
                return False
            no_bytes -= 1
            return no_bytes == 0
    return True
