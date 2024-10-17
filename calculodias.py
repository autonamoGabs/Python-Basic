from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
def calculo_dias(data_inicio,numero_dias):
    data_cliente = datetime(2022,10,12)
    data_atual = datetime.now()
    dias = data_atual - data_inicio
    print(f'Estamos juntos há {dias.days} dias')
    fut = data_inicio + timedelta(days=numero_dias)
    d = fut.strftime("%A, %d de %B de %Y")
    print(f"Faremos {numero_dias} dias em {d}")
    dias_faltam = abs(data_atual - fut)
    print(f"Faltam {dias_faltam.days} dias para {numero_dias} dias juntos.")


data = datetime(2022,10,12)
dias = int(input("Coloque o número de dias: "))
calculo_dias(data,dias)
