
from hashlib import sha256
from ecdsa import curves
import random
from libnum import n2s
# https://strm.sh/studies/bitcoin-nonce-reuse-attack/
sig1 = (78201061741253921857183617514161506815677077307333996106347370059568874593703, 29756929142955066262963236870299661357309727655695073136663808168259552908697)
sig2 = (78201061741253921857183617514161506815677077307333996106347370059568874593703, 38730893756692559761709549156103378697364312950992735304717373181306788835292)
enc = 6597263851042664574872135659293704841752797597054226272058227841138099976687014998226823099285951620
r1, s1 = sig1 
r2, s2 = sig2
n = int(curves.SECP256k1.generator.order())

msg = b"Did you know that Bitcoin uses ECDSA? I wonder if I can break into any Bitcoin wallets..."
half_length = len(msg)//2
msg1, msg2 = msg[:half_length], msg[half_length:]

h1 = int(sha256(msg1).hexdigest(),16)
h2 = int(sha256(msg2).hexdigest(),16)


k = ((h1 - h2) * pow(s1 - s2, -1, n)) % n
rinv = pow(r1,-1, n)
d = ((s1 * k ) - h1)  * rinv % n

random.seed(d)
enc = n2s(enc)
pad = random.randbytes(len(enc))
flag = "".join(map(chr, [b1 ^ b2 for b1,b2 in zip(pad, enc)]))

print(flag)
# REP{nonce_reuse_is_very_very_bad_in_ecdsa}