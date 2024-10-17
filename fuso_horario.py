from datetime import datetime
from zoneinfo import ZoneInfo

agora = datetime.now(ZoneInfo('UTC'))  # Definindo um fuso horário inicial

fuso_sp = ZoneInfo('America/Sao_Paulo') 
fuso_tk = ZoneInfo("Asia/Tokyo")
fuso_nyc = ZoneInfo("America/New_York")

h_sp = agora.astimezone(fuso_sp)
h_tk = agora.astimezone(fuso_tk)
h_nyc = agora.astimezone(fuso_nyc)

l = {"São Paulo": h_sp, "Tóquio": h_tk, "Nova Iorque": h_nyc}

for k, v in l.items():
    if v.hour > 17 or v.hour < 9:
        con = "Fechada"
    else:
        con = "Aberta"
    print(f"{k}: {v.date()} {v.time()} - {con}")
