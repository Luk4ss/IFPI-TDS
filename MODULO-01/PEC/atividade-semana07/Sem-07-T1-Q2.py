dia = int(input().strip())
mes = int(input().strip())
ano = int(input().strip())

dia_ = int(input().strip())
mes_ = int(input().strip())
ano_ = int(input().strip())

if ano_ > ano:
    print(f'{dia_}/{mes_}/{ano_}')
elif ano_ == ano:
    if mes_ > mes:
        print(f'{dia_}/{mes_}/{ano_}')
    elif mes_ == mes:
        if dia_ > dia:
            print(f'{dia_}/{mes_}/{ano_}')
        else:
            print(f'{dia}/{mes}/{ano}')
    else:
        print(f'{dia}/{mes}/{ano}')
else:
    print(f'{dia}/{mes}/{ano}')
