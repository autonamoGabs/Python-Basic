import time
tempo = time.localtime()
st = time.time()
ano = tempo.tm_year
string_tempo = f"01/01/{ano+1}"
formato = "%m/%d/%Y"
tempo_em_struct = time.strptime(string_tempo, formato)
seg_anoquevem = time.mktime(tempo_em_struct)
x = seg_anoquevem - st
dias = x // (24*60*60)
horas = int((x / (24*60*60) - dias) * 24)
minutos = int(((x / (24*60*60) - dias) * 24 - horas)*60)
segundos = (((x / (24*60*60) - dias) * 24 - horas)*60 - minutos)*60

print(dias,horas,minutos,segundos)

dias = x // (24 * 60 * 60)
resto_dias = x % (24 * 60 * 60)
horas = resto_dias // (60 * 60)
resto_horas = resto_dias % (60 * 60)
minutos = resto_horas // 60
segundos = int(resto_horas % 60)

print(int(dias), int(horas), int(minutos), segundos)
