import sys

# Define valid status codes
VALID_CODES = {"200", "301", "400", "401", "403", "404", "405", "500"}

# Initialize variables
total_size = 0
line_count = 0
status_counts = {code: 0 for code in VALID_CODES}
invalid_lines = 0  # Track the number of lines with invalid format

def print_stats():
    """Prints statistics on total file size and status code counts."""
    print(f"Total file size: {total_size}")
    print("Number of lines by status code:")
    for code, count in sorted(status_counts.items()):
        if count:
            print(f"{code}: {count}")
    print()  # Add an empty line for better readability

def parse_log_line(line):
    """Parses a log line and updates metrics."""
    data = line.strip().split()

    # Check if the line format is valid (6 elements)
    if len(data) != 6:
        invalid_lines += 1
        return

    # Extract elements (handle potential exceptions)
    try:
        ip_address = data[0]
        # Date is optional, not used for metrics
        # status_code = int(data[4])  # Potential error if not integer
        status_code = data[4]  # Extract status code as string for validation
        if status_code not in VALID_CODES:
            return  # Skip lines with invalid status code
        status_code = int(status_code)  # Convert to integer after validation

        file_size = int(data[5])

        # Update total size and status code counts
        total_size += file_size
        status_counts[status_code] += 1

    except ValueError:
        # Handle potential conversion errors (invalid format)
        invalid_lines += 1
        pass


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line_count += 1
            parse_log_line(line)

            # Print statistics every 10 lines or on interrupt
            if line_count % 10 == 0 or line_count == 1:
                print_stats()

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received. Printing final statistics:")
        print_stats()

    # Print information about invalid lines (optional)
    if invalid_lines:
        print(f"Number of lines with invalid format: {invalid_lines}")
