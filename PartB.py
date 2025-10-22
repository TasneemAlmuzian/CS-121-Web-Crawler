#!/usr/bin/env python3
"""
Part B: Intersection of Two Files
Author: Tasneem Almuzian
Student ID: 72925030

CLI: python3 PartB.py <file1> <file2>
Output: ONLY the integer count of common tokens (last line and only line).

Tokenizer rule: same as Part A — ASCII alphanumeric sequences, case-insensitive.

Complexities:
- token_stream: O(n) time, O(1) extra space (yields lazily).
- count_common_tokens: O(n + m) time; O(u1 + c) space,
  where u1 = #unique tokens in file1, c = #unique tokens in the intersection.
"""

import sys

CHUNK = 4096


def token_stream(file_path):
    """Yield tokens lazily so we don't keep the whole file in RAM."""
    current = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            while True:
                chunk = f.read(CHUNK)
                if not chunk:
                    break
                for ch in chunk:
                    if ch.isascii() and ch.isalnum():
                        current.append(ch.lower())
                    else:
                        if current:
                            yield "".join(current)
                            current = []
            if current:
                yield "".join(current)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)


def count_common_tokens(file1, file2):
    """Count distinct common tokens between two files."""
    seen1 = set(token_stream(file1))
    common_seen = set()
    for tok in token_stream(file2):
        if tok in seen1:
            common_seen.add(tok)
    return len(common_seen)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 PartB.py <file1> <file2>")
        sys.exit(1)

    f1, f2 = sys.argv[1], sys.argv[2]
    print(count_common_tokens(f1, f2))  # Must print ONLY the number