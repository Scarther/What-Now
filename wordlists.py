#!/usr/bin/env python3
"""
Combines multiple wordlist files into a single, deduplicated wordlist.
Optimized for Linux systems and large files by writing to disk incrementally.
"""

import argparse
import sys
from pathlib import Path

def combine_and_dedupe(input_files, output_file):
    """
    Combines wordlists, deduplicates, and writes to output file efficiently.
    """
    seen_words = set()
    words_written = 0
    
    # Open the output file for writing right away
    try:
        output_path = Path(output_file)
        out_f = output_path.open('w', encoding='utf-8')
    except Exception as e:
        print(f"Error: Could not open output file '{output_file}': {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Processing {len(input_files)} file(s) and writing to '{output_file}'...")

    for file_path in input_files:
        path_obj = Path(file_path)
        if not path_obj.is_file():
            print(f"Warning: Input file not found, skipping: {file_path}", file=sys.stderr)
            continue
            
        print(f"  - Reading: {file_path}")
        try:
            with path_obj.open('r', encoding='utf-8', errors='ignore') as in_f:
                for line in in_f:
                    word = line.strip()
                    # Check if the word is new and not empty
                    if word and word not in seen_words:
                        seen_words.add(word)
                        out_f.write(word + '\n')
                        words_written += 1
        except Exception as e:
            print(f"Error reading file {file_path}: {e}", file=sys.stderr)
            continue
            
    # Close the output file
    out_f.close()
    
    print(f"\nDone. Found {len(seen_words)} unique words and wrote {words_written} to '{output_file}'.")

def main():
    parser = argparse.ArgumentParser(
        description="Combine multiple wordlists into a single, deduplicated wordlist.",
        epilog="Example: ./combine_wordlists.py list1.txt list2.txt -o combined.txt"
    )
    parser.add_argument(
        'input_files',
        nargs='+',
        help="One or more input wordlist files to combine."
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help="The output file for the deduplicated wordlist."
    )
    
    args = parser.parse_args()
    
    combine_and_dedupe(args.input_files, args.output)

if __name__ == "__main__":
    main()
