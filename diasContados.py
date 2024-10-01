import time
tempo = time.time()
data = '12/10/2022'
formato = '%d/%m/%Y'
structTempo = time.strptime(data,formato)
x = tempo - time.mktime(structTempo)
z = x // (3600 * 24)
print(int(z))
