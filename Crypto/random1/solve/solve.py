from  MTRecover import MT19937Recover

output = []
with open("random.txt", "r" ) as f:
    output = list(map(int, f.readlines()))

random_output = output[:620]
enc_flag = output[620:]

for idx,c in enumerate("REP{"):
    xored_output = ord(c) ^ enc_flag[idx]
    random_output.append(xored_output)

mtb = MT19937Recover()
simulated = mtb.go(random_output)


flag = "REP{"
for i in range(4, len(enc_flag)):
    output = simulated.getrandbits(32)
    flag += chr(enc_flag[i] ^ output)
print(flag)

# REP{mersenne_twister_is_bad_for_encryption}