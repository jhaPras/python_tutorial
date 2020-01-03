import textwrap

def wrap(string, max_width):
    value=textwrap.wrap(string,max_width)
    for v in value:
        print(v)


wrap('abcdefghijklmnopqrstuvwxyz',max_width=4)
