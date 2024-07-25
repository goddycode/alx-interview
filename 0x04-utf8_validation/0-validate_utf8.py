#!/usr/bin/python3
""" UTF-8 validation """


def validUTF8(data):
    """ validates UTF-8 encoding """

    """
    # Step 1: turn data into binary
    bin_data = []
    for number in data:
        # step 1: convert number to binary string
        bin_str = bin(number)[2:]  # Remove '0b' prefix

        # step 2: ensure it's 8 bits long
        while len(bin_str) < 8:
            bin_str = '0' + bin_str

        bin_data.append(bin_str)

    # Step 2: Check UTF-8 encoding rules
    i = 0
    while i < len(bin_data):
        if bin_data[i].startswith('0'):
            # Single-byte character
            i += 1
        elif bin_data[i].startswith('110'):
            # Two-byte character
            if i + 1 >= len(bin_data) or not bin_data[i + 1].startswith('10'):
                return False
            i += 2
        elif bin_data[i].startswith('1110'):
            # Three-byte character
            if (i + 2 >= len(bin_data) or
                    not bin_data[i + 1].startswith('10') or
                    not bin_data[i + 2].startswith('10')):
                return False
            i += 3
        elif bin_data[i].startswith('11110'):
            # Four-byte character
            if (i + 3 >= len(bin_data) or
                    not bin_data[i + 1].startswith('10') or
                    not bin_data[i + 2].startswith('10') or
                    not bin_data[i + 3].startswith('10')):
                return False
            i += 4
        else:
            # Invalid start of UTF-8 character
            return False

    return True
    """
    # Initialize the number of expected continuation bytes
    n_bytes = 0

    for num in data:
        if n_bytes == 0:
            # Determine the number of bytes in the character
            if num >> 5 == 0b110:
                n_bytes = 1
            elif num >> 4 == 0b1110:
                n_bytes = 2
            elif num >> 3 == 0b11110:
                n_bytes = 3
            elif num >> 7:
                # If the first bit is 1, but it doesn't match any valid pattern
                return False
        else:
            # Check continuation byte
            if num >> 6 != 0b10:
                return False
            n_bytes -= 1

    # If n_bytes is not 0, it means we were expecting more continuation bytes
    return n_bytes == 0
