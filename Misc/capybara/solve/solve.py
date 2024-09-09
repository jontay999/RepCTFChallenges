from scipy.io import wavfile
import numpy as np
import binascii


def duckspeak(input):
    mapping={'0':'Nak','1':'Nanak','2':'Nananak','3':'Nanananak','4':'Nak?','5':'nak?','6':'Naknak','7':'Naknaknak','8':'Nak.','9':'Naknak.','a':'Naknaknaknak','b':'nanak','c':'naknak','d':'nak!','e':'nak.','f':'naknaknak'}
    hex_representation = binascii.hexlify(input.encode()).decode()
    print(hex_representation)
    output = []
    for i in hex_representation:
        output.append(mapping[i])
    duckspeak_str = ' '.join(output).strip()
    bits = bin(int.from_bytes(duckspeak_str.encode('utf-8', 'surrogatepass'), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def duckspeak_dec(input):
    mapping = {'Nak':'0','Nanak':'1','Nananak':'2','Nanananak':'3','Nak?':'4','nak?':'5','Naknak':'6','Naknaknak':'7','Nak.':'8','Naknak.':'9','Naknaknaknak':'a','nanak':'b','naknak':'c','nak!':'d','nak.':'e','naknaknak':'f'}
    n = int('0b'+input, 2)
    duckspeak_str = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', 'surrogatepass')
    hex_representation = []
    for i in duckspeak_str.split(' '):
        hex_representation.append(mapping[i])
    flag = binascii.unhexlify(''.join(hex_representation)).decode()
    return flag

def encode(flag):
    flag_d = duckspeak(flag)
    flag_bin = [int(i) for i in flag_d]

    fs, data = wavfile.read("capybara_original.wav")
    print(data.shape)
    ch2 = data.copy()
    for id in range(len(flag_bin)):
        ch2[id*100,1] = (ch2[id*100,1] & ~1) | flag_bin[id] #lsb substitution
    print(ch2.shape) #verify
    wavfile.write("capybara.wav", fs, ch2[:len(flag_bin)*100,:].astype(np.int16))

def decode():
    fs, data = wavfile.read("capybara.wav")
    print(data.shape)
    ch2 = []
    for id in range(0,data.shape[0],100):
        ch2.append(str(data[id,1]%2))
    print(len(ch2)) #verify
    bits = ''.join(ch2)
    flag = duckspeak_dec(bits)
    return flag

if __name__ == '__main__':
    flag = "REP{Lsb_5uBsT1tUt!0N_15_dUcK1n9_!NS3cuR3!}"

    #Encode
    encode(flag)

    #Decode
    flag = decode()
    print(flag)