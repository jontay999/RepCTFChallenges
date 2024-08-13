
from random import getrandbits

flag = "REP{FAKE_FLAG}"
output = []
# Here's some random output
for _ in range(620):
    output.append(getrandbits(32))

# Here's the flag, try to break the encryption :)
for i in range(len(flag)):
    random_byte = getrandbits(32)
    output.append(ord(flag[i]) ^ random_byte)

with open("random.txt", "w") as f:
    output = "\n".join(map(str, output))
    f.write(output)