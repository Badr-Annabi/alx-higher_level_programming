#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end='')
            i += 1
            print('\n\n', end='')
        else:
            print(text[i], end='')
        i += 1
