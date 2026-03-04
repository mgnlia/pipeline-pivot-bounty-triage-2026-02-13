#!/usr/bin/env python3
"""
Selects and prints the fallback bounty target when a GO/KILL decision is KILL for tscircuit #770.
Usage: python3 scripts/select_fallback.py
"""
import os
import sys

ARTIFACT = os.path.join(os.path.dirname(__file__), '..', 'artifacts', 'ed8e95-770-checklist-gokill-v2.md')


def main():
    try:
        with open(ARTIFACT, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Decision file not found at {ARTIFACT}")
        sys.exit(1)

    if 'Decision: KILL' in content:
        print('Fallback target detected:')
        print('  Archestra #1301 — https://github.com/archestra-ai/archestra/issues/1301')
    else:
        print('No KILL decision found for tscircuit #770. No fallback needed.')


if __name__ == '__main__':
    main()