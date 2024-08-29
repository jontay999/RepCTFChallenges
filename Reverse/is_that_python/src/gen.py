import dis


flag = "REP{i_thought_python_is_an_interpreted_language}"
enc = ""
for c in flag:
  a = ord(c) * 2
  b = a - 8
  c = b // 2
  enc += chr(c)
print(enc)
# NALwe[pdkqcdp[lupdkj[eo[]j[ejpanlnapa`[h]jcq]cay


def decrypt():
    encrypted = "NALwe[pdkqcdp[lupdkj[eo[]j[ejpanlnapa`[h]jcq]cay"
    out = ""
    for c in encrypted:
        a = ord(c) * 2
        b = a + 8
        c = b // 2
        out += chr(c)

# decrypt()
with open("what_is_this.txt", "w") as f:
   f.write(dis.dis(decrypt))
    

