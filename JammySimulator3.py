#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simple yes/no function demo."""

def yesno(question):
    """Simple Yes/No Function."""
    prompt = f'{question} ? (y/n): '
    ans = input(prompt).strip().lower()
    if ans not in ['y', 'n']:
        print(f'{ans} is invalid, please try again...')
        return yesno(question)
    if ans == 'y':
        return "Go take some lax."
    return "Congratulations. You won."


def main():
    ans = yesno("Are you alive?")
    print(f'{ans}')



if __name__ == '__main__':
    main()