import sys

if len(sys.argv) != 2:
    raise SystemExit('It failed, just enter the file path you want to decrypt.')
filepath = sys.argv[1]

with open(filepath, 'r', encoding='utf-8') as f:
    strings = f.read()
    step = 5
    output = ''
    for ss in strings:
       new_char = chr(ord(ss) + step)
       output += new_char
       step += 1

print('Result is:', output)
