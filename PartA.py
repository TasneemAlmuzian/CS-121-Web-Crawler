#!/usr/bin/env python3
"""
Part A: Word Frequencies
Author: Tasneem Almuzian
Student ID: 72925030

This program reads a text file, tokenizes it into alphanumeric words (case-insensitive),
computes word frequencies, and prints them in descending order of frequency.
Output format: <token> -> <freq>
"""

import sys
from collections import defaultdict

# Function: tokenize(TextFilePath)
# Runtime Complexity: O(n), where n = number of characters in the file.
# Explanation: Each character is read once and processed in constant time.
def tokenize(file_path):
    tokens = []
    current_token = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                for ch in chunk:
                    # Handle alphanumeric characters only
                    if ch.isalnum():
                        current_token.append(ch.lower())
                    else:
                        if current_token:
                            tokens.append("".join(current_token))
                            current_token = []
            # Append last token if any
            if current_token:
                tokens.append("".join(current_token))
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)

    return tokens

# Function: computeWordFrequencies(List<Token>)
# Runtime Complexity: O(m), where m = number of tokens.
# Explanation: Each token is processed exactly once in a single pass.
def computeWordFrequencies(tokens):
    freq_map = defaultdict(int)
    for token in tokens:
        try:
            freq_map[token] += 1
        except Exception:
            # Skip bad tokens
            continue
    return freq_map

# Function: print(Frequencies<Token, Count>)
# Runtime Complexity: O(k log k), where k = number of unique tokens.
# Explanation: Sorting dominates the runtime.
def print_frequencies(freq_map):
    sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    for token, count in sorted_items:
        print(f"{token} -> {count}")

# Main entry point
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 PartA.py <textfile>")
        sys.exit(1)

    file_path = sys.argv[1]
    tokens = tokenize(file_path)
    frequencies = computeWordFrequencies(tokens)
    print_frequencies(frequencies)