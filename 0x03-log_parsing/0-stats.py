#!/usr/bin/python3
""" log parsing """
import sys


def print_logs(status_counts, total_size):
    """ prints current logs """
    print("File size: {}".format(total_size))
    for key, val in sorted(status_counts.items()):
        if val != 0:
            print("{}: {}".format(key, val))


# Initialize variables
total_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_counter = 0

try:
    # Read input lines from standard input
    for line in sys.stdin:
        # Split the line into parts and reverse the order
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        # Check if line has enough parts
        if len(parsed_line) > 2:
            line_counter += 1

            # Process up to 10 lines
            if line_counter <= 10:
                total_size += int(parsed_line[0])  # Accumulate file size
                status_code = parsed_line[1]  # Get status code

                # Check if status code is valid and update count
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

            # Every 10 lines, print logs
            if line_counter == 10:
                print_logs(status_code_counts, total_size)
                line_counter = 0  # Reset line counter

finally:
    # Print final logs
    print_logs(status_code_counts, total_size)
