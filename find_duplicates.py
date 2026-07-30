"""
find_duplicates.py

Finds duplicate entries in a words.json flashcard file, where a "duplicate"
is defined as two or more entries sharing the same `reading` AND the same
`meaning`.

For each duplicate group it prints:
  - the word (kanji_or_vocab)
  - the reading / meaning they share
  - the line number in the JSON file where each duplicate entry starts
    (the line containing "kanji_or_vocab": "...")
  - the array index (0-based position in the JSON list)

Usage:
    # Just report duplicates (does not touch your file):
    python3 find_duplicates.py words.json

    # Report AND write a cleaned copy with duplicates removed
    # (keeps the FIRST occurrence of each duplicate group, drops the rest):
    python3 find_duplicates.py words.json --remove
    python3 find_duplicates.py words.json --remove -o cleaned_words.json
"""

import json
import sys
import argparse
from collections import defaultdict


def find_line_numbers(filepath, items):
    """
    Walk through the raw file line-by-line and, for each item (in order),
    find the line number where its "kanji_or_vocab" entry begins.
    Assumes items appear in the file in the same order as in the parsed list.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    line_numbers = []
    search_from = 0  # line index to resume searching from

    for item in items:
        target = item["kanji_or_vocab"]
        needle = f'"kanji_or_vocab": "{target}"'
        found_line = None
        for idx in range(search_from, len(lines)):
            if needle in lines[idx]:
                found_line = idx + 1  # 1-indexed line number
                search_from = idx + 1
                break
        line_numbers.append(found_line)

    return line_numbers


def main():
    parser = argparse.ArgumentParser(
        description="Find (and optionally remove) duplicate flashcard entries "
                    "that share the same reading + meaning."
    )
    parser.add_argument("filepath", help="Path to the words.json file")
    parser.add_argument(
        "--remove",
        action="store_true",
        help="Write a cleaned copy of the file with duplicates removed "
             "(keeps the first occurrence of each duplicate group).",
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output path for the cleaned file when using --remove. "
             "Defaults to '<original_name>_deduped.json' next to the input file.",
    )
    args = parser.parse_args()

    filepath = args.filepath

    with open(filepath, "rb") as f:
        items = json.loads(f.read().decode("utf-8"))

    line_numbers = find_line_numbers(filepath, items)

    # Group entries by (reading, meaning)
    groups = defaultdict(list)
    for i, item in enumerate(items):
        key = (item.get("reading", ""), item.get("meaning", ""))
        groups[key].append(i)

    duplicate_groups = {k: v for k, v in groups.items() if len(v) > 1}

    if not duplicate_groups:
        print("No duplicates found (matching on reading + meaning).")
        if args.remove:
            print("Nothing to remove; file is already unique.")
        return

    print(f"Found {len(duplicate_groups)} duplicate group(s):\n")

    # Track which array indices should be dropped (every occurrence
    # after the first one in each duplicate group).
    indices_to_drop = set()

    for (reading, meaning), idxs in duplicate_groups.items():
        word = items[idxs[0]]["kanji_or_vocab"]
        print(f"Word: {word}  |  Reading: {reading}  |  Meaning: {meaning}")
        for pos, i in enumerate(idxs):
            ln = line_numbers[i]
            tag = "KEEP" if pos == 0 else "DROP"
            print(f"    -> array index {i}, line {ln}  [{tag}]")
            if pos != 0:
                indices_to_drop.add(i)
        print()

    if not args.remove:
        print(f"(Dry run only — {len(indices_to_drop)} entries would be removed. "
              f"Re-run with --remove to actually write a cleaned file.)")
        return

    # Build the cleaned list, preserving original order, dropping duplicates
    cleaned = [item for i, item in enumerate(items) if i not in indices_to_drop]

    if args.output:
        out_path = args.output
    else:
        if filepath.lower().endswith(".json"):
            out_path = filepath[:-5] + "_deduped.json"
        else:
            out_path = filepath + "_deduped.json"

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)

    print(f"Removed {len(indices_to_drop)} duplicate entries.")
    print(f"Original entry count: {len(items)}")
    print(f"Cleaned entry count:  {len(cleaned)}")
    print(f"Cleaned file written to: {out_path}")


if __name__ == "__main__":
    main()
