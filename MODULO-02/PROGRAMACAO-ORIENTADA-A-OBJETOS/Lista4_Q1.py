from datetime import *
from random import *

# region CLASSES


class Clinica:

    def __init__(self):
      self.nome = 'CLINICA DO TRABALHADOR'
      self.registro = {}
      self.saldo = 0
    
    def salvar_registro(self, regs):
        self.registro.update(regs)

    def __str__(self):
        return self.nome

    def mostrar_registro(self):
        for codigo in self.registro.keys():
            consulta = self.registro[codigo]
            print(F'CÓDIGO: {codigo}, DADOS: {consulta.paciente.nome}, {consulta.medico.nome}, {consulta.dt_consulta}, PAGO:{consulta.pago}')

    def faturamento_por_mes(self):
        meses = { 
            1: 'JANEIRO',
            2: 'FEVEREIRO',
            3: 'MARÇO',
            4: 'ABRIL',
            5: 'MAIO',
            6: 'JUNHO',
            7:'JULHO',
            8:'AGOSTO',
            9:'SETEMBRO',
            10:'OUTUBRO',
            11:'NOVEMBRO',
            12:'DEZEMBRO'
            }

        for mes in range(1, 13):
            print(f'# {meses[mes]} #')
            saldo_mes = 0
            for consulta in self.registro.values():
                mes_consulta = int(consulta.dt_consulta[3:5])
                if mes == mes_consulta and consulta.pago and not consulta.cancelada:
                    saldo_mes += 300
            print(f'Saldo da clínica nesse mês: R$ {saldo_mes}\n')
    
    def faturamento_por_mes_por_medico(self):
        meses = { 
            1: 'JANEIRO',
            2: 'FEVEREIRO',
            3: 'MARÇO',
            4: 'ABRIL',
            5: 'MAIO',
            6: 'JUNHO',
            7:'JULHO',
            8:'AGOSTO',
            9:'SETEMBRO',
            10:'OUTUBRO',
            11:'NOVEMBRO',
            12:'DEZEMBRO'
            }

        for mes in range(1, 13):
            saldo_m1 = 0
            saldo_m2 = 0
            print(f'# {meses[mes]} #')
            for consulta in self.registro.values():
                mes_consulta = int(consulta.dt_consulta[3:5])
                if mes == mes_consulta and consulta.pago and consulta.medico.nome == 'Dr. Octopus' and not consulta.cancelada:
                    saldo_m1 += 200
                if mes == mes_consulta and consulta.pago and consulta.medico.nome == 'Dra. Vilma' and not consulta.cancelada:
                    saldo_m2 += 200
            print(f'>> Faturamento do Dr. Octopus: R$ {saldo_m1}')
            print(f'>> Faturamento da Dra. Vilma: R$ {saldo_m2}')



class Paciente:

    def __init__(self, nome, cpf, sexo, dt_nascimento):
        self.nome = nome
        self.cpf = cpf,
        self.sexo = sexo
        self.dt_nascimento = dt_nascimento

    def __str__(self):
        return "Paciente: " + self.nome

        
class Medico:

    def __init__(self,nome):
        self.nome = nome
        self.saldo = 0

    def receber_pagamento(self, valor):
        self.saldo += valor

    def __str__(self):
        return "Médico: " + self.nome


class Consulta:

    def __init__(self, paciente, medico, agendamento=""):
        self.paciente = paciente
        self.medico = medico
        self.dt_consulta = agendamento
        self.dt_retorno = ""
        self.pago = False
        self.cancelada=False


# endregion


#region MÉTODOS
def menu():
    print('''### MENU DE ATENDIMENTO ###
            1 - AGENDAR CONSULTA
            2 - PAGAR CONSULTA
            3-  CANCELAR CONSULTA
            4 - AGENDAR RETORNO
            5 - RELATÓRIO DE CONSULTAS REALIZADAS POR MÊS POR MÉDICO
            6 - RELATÓRIO DE FATURAMENTO DA CLINICA POR MÊS
            7 - LISTAR REGISTRO DA CLÍNICA
            8 - PARAR O PROGRAMA
            ''')
    return int(input('Digite a sua opção: '))


def agendamento_consulta(cd, clinic):
    print(' >>>> PREENCHA OS DADOS ABAIXO PARA O AGENDAMENTO DA CONSULTA <<<< ')
    nome = input('Digite o seu nome: ')
    cpf =  input('Digite o seu CPF: ')
    sexo = input('Digite o seu sexo: ')
    dt_nascimento = input('Digite a sua data de nascimento: ')
    md_nome = choice(['Dr. Octopus', 'Dra. Vilma'])
    while True:
        dia_int = randint(1, 28)
        mes_int = randint(1, 12)
        if dia_int < 10:    
            dia = '0' + str(dia_int)
        if dia_int > 9:
            dia = str(dia_int)
        if mes_int < 10:
            mes = '0' + str(mes_int)
        if mes_int > 9: 
            mes = str(mes_int)
        ano = str(datetime.today().year)
        dt_consulta = dia + '/' + mes + '/' + str(ano)
        if   datetime.strptime(dt_consulta, "%d/%m/%Y") > datetime.today():
            break
    paciente = Paciente(nome, cpf, sexo, dt_nascimento)
    medico = Medico(md_nome)
    consulta = Consulta(paciente, medico, dt_consulta)
    clinic.salvar_registro({cd: consulta}) 
    print(" ### DADOS DO AGENDAMENTO ###")
    print(paciente)
    print(medico)
    print('>>>> Sua consulta foi agendada para: ' + dt_consulta)
    print(f'>>>> Seu código de consulta é: {cd}\n')
    return True
    

def pagar_consulta(clinic):
    cd = int(input('Digite o código da consulta que deseja pagar: '))
    reg = clinic.registro.get(cd)
    if reg is not None and not reg.cancelada:
        print(" ### DADOS DA CONSULTA ###")
        print(f'Nome do paciente: {reg.paciente.nome}')
        print(f'Nome do médico: {reg.medico.nome}')
        print(f'Data da consulta: {reg.dt_consulta}')
        print('''Você pagou R$ 300 à clinica\n''')        
        clinic.saldo = 100
        reg.medico.saldo = 200
        reg.pago = True
    elif reg is None:
        print('>>> CONSULTA NÃO ENCONTRADA PARA O CÓDIGIO INFORMADO!\n')
    else:
        print('>>> NÃO É POSSÍVEL PAGAR UMA CONSULTA QUE FOI CANCELADA!\n')

    

def cancelar_consulta(cd, clinic):
    cd = int(input('Digite o código da consulta que deseja cancelar: '))
    reg = clinic.registro.get(cd)
    if reg is not None and reg.pago and len(reg.dt_retorno) < 2:
        print(" ### DADOS DO CANCELAMENTO ###")
        print(f'Nome do paciente: {reg.paciente.nome}')
        print(f'Nome do médico: {reg.medico.nome}')
        print(f'Data da consulta: {reg.dt_consulta}')
        print('''Consulta CANCELADA !\n''')
        clinic.saldo -= 100
        reg.medico.saldo -= 200
        reg.cancelada = True
        reg.pago = False
    elif reg is None:
        print('>>> CONSULTA NÃO ENCONTRADA PARA O CÓDIGO INFORMADO')
    elif len(reg.dt_retorno) > 1:
        print('>>> VOCÊ NÃO PODE CANCELAR UMA CONSULTA QUE JÁ FOI REALIZADA')
    else:
        print('ESTÁ CONSULTA AINDA NÃO ESTÁ PAGA. POR FAVOR, PRIMEIRO PAGUE A CONSULTA PARA OBTER O DIREITO DE RETORNO.')
        return False



def agendamento_retorno(cd, clinic):

    print('>>> AGENDAMENTO DO RETORNO <<<')
    cd_busca = int(input('Digite o código da consulta : '))
    reg = clinic.registro.get(cd_busca)
    if reg is not None and reg.pago and not reg.cancelada:
        while True:
            dia = randint(1, 28)
            mes = randint(1, 12)
            ano = datetime.today().year
            dt_retorno = str(dia) + '/' + str(mes) + '/' + str(ano)
            if datetime.strptime(reg.dt_consulta, "%d/%m/%Y") < datetime.strptime(dt_retorno, "%d/%m/%Y"):
                break
        reg.dt_retorno = dt_retorno
        print('### DADOS DO AGENDAMENTO ###')
        print(f'Paciente: {reg.paciente.nome}')
        print(f'Médico: {reg.medico.nome}')
        print(f'RETORNO AGENDADO COM SUCESSO PARA O DIA {dt_retorno}!!\n')
        return True
    elif reg is None:
        print('>>> CONSULTA NÃO ENCONTRADA PARA O CÓDIGO INFORMADO')
    elif reg.cancelada:
        print('ESTÁ CONSULTA ESTÁ CANCELADA. NÃO É POSSÍVEL AGENDAR UM RETORNO PARA ELA.')
        return False
    else:
        print('ESTÁ CONSULTA AINDA NÃO ESTÁ PAGA. POR FAVOR, PRIMEIRO PAGUE A CONSULTA PARA OBTER O DIREITO DE RETORNO.')
        return False
    
#endregion


def main():
    clinica = Clinica()
    codigo = 1
    while True:               
        opcao = menu()
        if opcao == 1:
            print('-----------------------------------------------------------------')
            if agendamento_consulta(codigo, clinica):
                codigo += 1
            print('-----------------------------------------------------------------')
        elif opcao == 2:
            print('-----------------------------------------------------------------')
            pagar_consulta(clinica)
            print('-----------------------------------------------------------------')
        elif opcao == 3:
            print('-----------------------------------------------------------------')
            cancelar_consulta(codigo, clinica)
            print('-----------------------------------------------------------------')
        elif opcao == 4:
            print('-----------------------------------------------------------------')
            agendamento_retorno(codigo, clinica)
            print('-----------------------------------------------------------------')
        elif opcao == 5:
            print('-----------------------------------------------------------------')
            clinica.faturamento_por_mes_por_medico()
            print('-----------------------------------------------------------------')
        elif opcao == 6:
            print('-----------------------------------------------------------------')
            clinica.faturamento_por_mes()
            print('-----------------------------------------------------------------')
        elif opcao == 7:
            print('-----------------------------------------------------------------')
            clinica.mostrar_registro()
            print('-----------------------------------------------------------------')
        else:
            break



main()