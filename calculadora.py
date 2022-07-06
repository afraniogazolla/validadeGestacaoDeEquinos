import datetime
#Programado por Afranio Gazolla - Professor e Zootecnista
print("**************************************************")
print("* Verificador de Validade de Gestacao de Equinos *")
print("**************************************************")

print("Informacoes de Cobertura:")
print("")
anoCobertura  = int(input('Digite o Ano de Cobertura: '))
mesCobertura  = int(input('DIgite o Mes de Cobertura: '))
diaCobertura  = int(input('Digite o Dia de Cobertura: '))
dataCobertura = datetime.date(anoCobertura, mesCobertura, diaCobertura)

print("Informacoes de Nascimento:")
print("")
anoNascimento  = int(input('Digite o Ano de Nascimento: '))
mesNascimento  = int(input('Digite o Mes de Nascimento: '))
diaNascimento  = int(input('Digite o Dia de Nascimento: '))
dataNascimento = datetime.date(anoNascimento, mesNascimento, diaNascimento)

intervaloDias =  (dataNascimento-dataCobertura).days

if(intervaloDias >= 365):
    mensagem = "O equino nasceu com  " + str(intervaloDias) + " dias, portanto pode ser registrad."
    
if(intervaloDias<=310):
    mensagem = "O potro nasceu com apenas " + str(intervaloDias) + " dias, portanto nao pode ser registrado."
    
if(intervaloDias>310 and intervaloDias<365):
    mensagem = "O potro pode ser registrado, pois nasceu com " + str(intervaloDias) + " dias ( entre 310 e 365 dias)."
print(mensagem)



