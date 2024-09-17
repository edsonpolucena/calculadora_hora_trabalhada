from datetime import datetime, timedelta

def ajustar_formato_hora(hora):
    hora = hora.strip() 
    
    if len(hora) == 4 and ":" not in hora:
        hora = hora[:2] + ":" + hora[2:]
    elif len(hora) == 3 and ":" not in hora:
        hora = hora[:1] + ":" + hora[1:]
    elif len(hora) == 2 and ":" not in hora:
        hora = "00:" + hora
    return hora

def validar_hora(hora):
    hora = ajustar_formato_hora(hora)
    try:
        return datetime.strptime(hora, '%H:%M')
    except ValueError:
        print("Erro: o formato deve ser HH:mm ou H:mm")
        return None

def calcular_horas_trabalhadas(hora_inicio, hora_fim, intervalo="00:00"):
    inicio = validar_hora(hora_inicio)
    fim = validar_hora(hora_fim)
    intervalo = validar_hora(intervalo)
    
    if not inicio or not fim or not intervalo:
        return None

    horas_trabalhadas = abs(fim - inicio)

    intervalo_timedelta = timedelta(hours=intervalo.hour, minutes=intervalo.minute)
    horas_trabalhadas -= intervalo_timedelta

    return horas_trabalhadas

def main():
    hora_inicio = input("Digite o horário de início (HH:mm ou HHmm): ")
    hora_fim = input("Digite o horário de término (HH:mm ou HHmm): ")
    intervalo = input("Digite a duração do intervalo (HH:mm ou HHmm): ")
    
    horas_trabalhadas = calcular_horas_trabalhadas(hora_inicio, hora_fim, intervalo)
    
    if horas_trabalhadas:
        print(f"Você trabalhou {horas_trabalhadas} horas.")

if __name__ == "__main__":
    main()
