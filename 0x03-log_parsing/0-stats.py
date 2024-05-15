#!/usr/bin/python3
"""
parsing HTTP request logs.
"""

import sys


def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(status, count))


def parse_line(line, total_size, status_counts):
    parts = line.split()
    if len(parts) >= 9:
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        except ValueError:
            pass
    return total_size, status_counts


def main():
    total_size = 0
    status_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0
    try:
        for line in sys.stdin:
            total_size, status_counts = parse_line(
                line,
                total_size,
                status_counts
            )
            line_count += 1
            if line_count == 10:
                print_stats(total_size, status_counts)
                line_count = 0
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
