# Purpose: This script parses a NGINX log file to find and count the most frequent IP addresses.
# Usage: python log_analyzer.py /var/log/nginx/access.log -n 20
# Uses regular expressions to find IP addresses.
# Provides a summary of the top N most common IPs.


import re
from collections import Counter

def analyze_log_file(log_file_path):
    """
    Analyzes a log file to find the most common IP addresses.

    :param log_file_path: Path to the log file.
    :return: A Counter object with IP address frequencies.
    """
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    ip_counts = Counter()

    try:
        with open(log_file_path, 'r') as f:
            for line in f:
                match = ip_pattern.search(line)
                if match:
                    ip_counts[match.group(1)] += 1
    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")
        return None

    return ip_counts

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze a log file for top IP addresses.")
    parser.add_argument("logfile", help="The path to the log file.")
    parser.add_argument("-n", "--top", type=int, default=10, help="The number of top IPs to display.")

    args = parser.parse_args()

    top_ips = analyze_log_file(args.logfile)
    if top_ips:
        print(f"Top {args.top} IP Addresses:")
        for ip, count in top_ips.most_common(args.top):
            print(f"{ip}: {count}")