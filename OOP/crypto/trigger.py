from crypto import Crypto

cryp = Crypto(" ")
cryp.update(43)

in_m = "Eia raese.esoiaeesé ha sa  ct,fb ntnradctjm"
out_m = cryp.decrypt(in_m, 17)

print(out_m)
