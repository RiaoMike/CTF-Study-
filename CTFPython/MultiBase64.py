
import base64
import sys

if len(sys.argv) != 2:
    raise SystemExit('It failed...Please enter only one argv as file destination')

file_destination = sys.argv[1]
with open(file_destination, 'r', encoding='utf-8') as f:
    strings = f.read()
    while True:
        try:
            strings = base64.b64decode(strings)
        except base64.binascii.Error:
            print('Result is: ', str(strings, 'utf-8'))
            break
