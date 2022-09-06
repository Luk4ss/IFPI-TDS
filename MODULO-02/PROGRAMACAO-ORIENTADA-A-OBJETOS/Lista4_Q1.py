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
        return "CLÍNICA"
       

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


# endregion


#region MÉTODOS
def menu():
    print(''' # MENU DE ATENDIMENTO #
            1 - AGENDAR CONSULTA
            2 - PAGAR CONSULTA
            3-  CANCELAR CONSULTA
            4 - AGENDAR RETORNO
            5 - RELATÓRIO DE CONSULTAS REALIZADAS POR MÊS POR MÉDICO
            6 - RELATÓRIO DE FATURAMENTO DA CLINICA POR MÊS
            7 - PARA O PROGRAMA''')
    return int(input('Digite a sua opção: '))


def agendamento_consulta(cd, clinic):
    nome = input('Digite o seu nome: ')
    cpf =  input('Digite o seu CPF: ')
    sexo = input('Digite o seu sexo: ')
    dt_nascimento = input('Digite a sua data de nascimento: ')
    md_nome = choice(['Dr. Lucas', 'Dra. Karinny', 'Dr. Octopus', 'Dra. Vilma'])
    dia = randint(1, 31)
    mes = randint(1, 12)
    ano = datetime.today().year
    dt_consulta = str(dia) + '/' + str(mes) + '/' + str(ano)
    paciente = Paciente(nome, cpf, sexo, dt_nascimento)
    medico = Medico(md_nome)
    clinic.salvar_registro({cd: [paciente, medico, dt_consulta]}) 
    print(" ### DADOS DO AGENDAMENTO ###")
    print(paciente)
    print(medico)
    print('>>>> Sua consulta foi agendada para: ' + dt_consulta)
    print(f'>>>> Seu código de consulta é: {cd}\n')
    

def pagar_consulta(clinic):
    cd = int(input('Digite o código da consulta que deseja pagar: '))
    re = clinic.registro.get(cd)
    if re is not None:
        print(" ### DADOS DA CONSULTA ###")
        for element in re:
            print(element)
        print('''Você pagou R$ 300 à clinica\n''')
        re[1].saldo = 200
        clinic.saldo = 100
    else:
        print('>>> CONSULTA NÃO ENCONTRADA PARA O CÓDIGIO INFORMADO!\n')

    

def cancelar_consulta(cd, clinic):
    cd = int(input('Digite o código da consulta que deseja cancelar: '))
    re = clinic.registro.pop(cd, -1)
    if re is not None and re != -1:
        print(" ### DADOS DA CONSULTA ###")
        for element in re:
            print(element)
        print('''Consulta cancelada !\n''')
    elif re == -1:
        print('>>> CONSULTA NÃO ENCONTRADA PARA O CÓDIGIO INFORMADO!\n')



def agendamento_retorno(cd, clinic):
    print('>>> AGENDAMENTO DO RETORNO')
    cd_busca = int(input('Digite o código da consulta : '))
    reg = clinic.registro.get(cd_busca)
    _paciente = None
    _medico = None
    if reg is not None:
        _paciente = reg[0]
        _medico = reg[1]
        dia = randint(1, 31)
        mes = randint(1, 12)
        ano = datetime.today().year
        dt_retorno = str(dia) + '/' + str(mes) + '/' + str(ano)
        clinic.salvar_registro({cd: [_paciente, _medico, dt_retorno]})
        print(_paciente)
        print(_medico)
        print(f'RETORNO AGENDADO COM SUCESSO PARA O DIA {dt_retorno}!!\n')
        return True
    else:
        print('>>> CONSULTA NÃO ENCONTRADA PARA O CÓDIGO INFORMADO')
        return False
#endregion


def main():
    clinica = Clinica()
    codigo = 1
    while True:
        try:            
            opcao = menu()
            if opcao == 1:
                if agendamento_consulta(codigo, clinica):
                    codigo += 1
            elif opcao == 2:
                pagar_consulta(clinica)
            elif opcao == 3:
                cancelar_consulta(codigo, clinica)
            elif opcao == 4:
                if agendamento_retorno(codigo, clinica):
                    codigo += 1
        except ValueError:
            print('!!! DADO INVÁLIDO !!! DIGITE UM DADO VÁLIDO')


main()