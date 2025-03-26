#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""
import sys

total_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}
line_count = 0

try:
    for line in sys.stdin:
        line_parts = line.split()
        if len(line_parts) >= 9:
            try:
                status_code = line_parts[-2]
                file_size = int(line_parts[-1])

                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size
            except (ValueError, IndexError):
                pass
        else
            try:
                if len(line_parts) >= 2:
                    status_code = line_parts[-2]
                    file_size = int(line_parts[-1])
                    if status_code in status_codes:
                        status_codes[status_code] += 1
                    total_size += file_size
                elif len(line_parts) == 1:
                total_size += int(line_parts[-1])
            except (ValueError, IndexError):
                pass

        line_count += 1
        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    pass

print(f"File size: {total_size}")
for code in sorted(status_codes.keys()):
    if status_codes[code] > 0:
        print(f"{code}: {status_codes[code]}")
