import re
import sys

targets = sys.stdin.readline().rstrip()
explosion = sys.stdin.readline().rstrip()
while True:
    result = re.sub(explosion, '', targets)
    if len(result) == len(targets):
        break
    targets = result
if targets:
    print(targets)
else:
    print('FRULA')