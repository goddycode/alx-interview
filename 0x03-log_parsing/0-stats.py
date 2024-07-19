#!/usr/bin/python3
"""
Log parsing
"""
import sys

# Define valid status codes
VALID_CODES = {"200", "301", "400", "401", "403", "404", "405", "500"}

# Initialize variables
total_size = 0
line_count = 0
status_counts = {code: 0 for code in VALID_CODES}


def print_stats():
    """Prints statistics on total file size and status code counts."""
    print(f"Total file size: {total_size}")
    print("Number of lines by status code:")
    for code, count in sorted(status_counts.items()):
        if count:
            print(f"{code}: {count}")
    print()  # Add an empty line for better readability


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line_count += 1
            # Split the line based on spaces
            data = line.strip().split()

            # Check if the line format is valid
            if len(data) != 6:
                continue

            # Extract IP, status code, and file size
            ip_address = data[0]
            status_code = data[4]
            try:
                file_size = int(data[5])
            except ValueError:
                continue

            # Update total size and status code counts
            total_size += file_size
            if status_code in VALID_CODES:
                status_counts[status_code] += 1

            # Print statistics every 10 lines or on interrupt
            if line_count % 10 == 0 or line_count == 1:
                print_stats()

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received. Printing final statistics:")
        print_stats()

