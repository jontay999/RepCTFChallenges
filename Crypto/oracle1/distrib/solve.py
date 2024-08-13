from pwn import *

p = remote("127.0.0.1", 8000)

p.recvuntil(b"crack it if you can: ")
cipher = p.recvline().strip().decode('utf-8')
blocks = [cipher[i:i+32] for i in range(0,len(cipher),32)]
padding_good = "That was nice!"
padding_bad = "That wasn't so nice..."

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzREP{}_"
def is_padding_wrong(payload):
    p.sendlineafter(b">", b"1")
    p.sendlineafter(b"hex):", payload.encode('utf-8'))
    p.recvuntil(b":")
    msg = p.recvline().strip().decode('utf-8')
    print("payload:", payload)
    return msg == padding_bad

def find_char(first_block, second_block, padding):
    # first_block is known, trying to find out contents of second_block
    # first_block is xored with output of second_block
    first_block = [int(first_block[i:i+2], 16) for i in range(0,len(first_block), 2)]
    
    modified_block = first_block[:]
    # our second_block has `padding` amount of padding bytes
    # we want to cause it to have `padding+1` amount of padding bytes
    # first_block[-padding-1:]  ^ second_block[-padding-1:]
    for i in range(padding):
        modified_block[-i-1] ^= ((padding+1) ^ (padding))

    flag_block = ""
    while padding < 16:
        for i in alphabet:
            testing_block = modified_block[:]
            testing_block[-padding-1] ^= ((ord(i)) ^ (padding+1))
            payload_block = [bytes([j]) for j in testing_block]
            payload_block = (b"".join(payload_block)).hex()

            if not is_padding_wrong(payload_block+second_block):
                flag_block = i + flag_block
                padding += 1

                modified_block = testing_block
                for i in range(padding):
                    modified_block[-i-1] ^= ((padding+1) ^ (padding))
                if padding > 16: return flag_block
                break

    print(flag_block)
    return flag_block

initial_padding = 4
final_flag = ""
for i in range(len(blocks)-2):
    final_flag += find_char(blocks[i], blocks[i+1], 0)

final_flag += find_char(blocks[-2], blocks[-1], 4)
print(final_flag)

p.close()