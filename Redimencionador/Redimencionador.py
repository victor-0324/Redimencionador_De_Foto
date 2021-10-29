import os
from PIL import Image
import os.path
from tkinter import filedialog
import time 


def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('.jpg'):
        return True
    return False 

def reduzir_tamanho(input_dir, output_dir, ext='.jpg'):
    lista_de_arquivo = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    for nome in lista_de_arquivo:
        imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB') 

        #pergute_rdm = input('Qual o tamanho que deseja redimencionar:?\nex:Nunca almente a resolução da foto se ele for pequena só diminua se for grande\n')                 

        redimencionada = imagem.resize((3,4))
        nome_sem_ext = os.path.splitext(nome)[0]
        redimencionada.save(os.path.join(output_dir, nome_sem_ext + ext))                  
                  


def verificador_file():
    origem = filedialog.askdirectory()
    print('Agora escolha a pasta onde queira salva as novas fotos 3x4.\n')
    print('><><><><><><><><><><><><><><><><><><><\n')
    time.sleep(3)
    destino = filedialog.askdirectory()
    return  reduzir_tamanho(origem, destino)

while True:
    print('\n><><><><>< REDIMENCIONADOR ><><><><><\n')
    print('><><><><><><><><><><><><><><><><><><><\n')

    print('Primeiro deve escolher a pasta onde esta as fotos para redimencionar\ndepois escolha onde quer salva as novas fotos 3x4\n')
    start = input('digite 1 para começa a redimencionar ou 2 para cancela.\n:')
    print('><><><><><><><><><><><><><><><><><><><\n')

    if start == '1':
        print('Escolha uma pasta para redimencionar as fotos ...\n')
        print('><><><><><><><><><><><><><><><><><><><\n')
        time.sleep(2)  
        verificador_file()

        print(f'Pasta salva no arquivo desejado.\n')
        print('><><><><><><><><><><><><><><><><><><><\n')

        time.sleep(3) 
        continua = input('Deseja continua Novos redimencionamento?, 1 para sim, 2 para não\n:')

        if continua == '1':
            continue
        elif continua == '2':
            print('Ok encerrando.\n.\n.\n.\n')
            print('Esse script foi desenvolvido por\nVitor F. Lima\nEstudante de programação nas horas vagas\n.\n.\n.\n')
            time.sleep(8)
            break
        else:
            print('><><><><><><><><><><><><><><><><><><><')
            print('          Erro!! Digite 1 ou 2'        )
            print('><><><><><><><><><><><><><><><><><><><\n')
            time.sleep(3)
            continue
    elif start == '2':
        print("OK programa finalizado.\n")
        print('Esse script foi desenvolvido por\nVitor F. Lima\nEstudante de programação nas horas vagas\n.\n.\n.\n')
        time.sleep(8)
        print('><><><><><><><><><><><><><><><><><><><\n')
        break

    else:
        print('><><><><><><><><><><><><><><><><><><><')
        print('          Erro!!  Digite 1 ou 2        ')
        print('><><><><><><><><><><><><><><><><><><><\n')
        time.sleep(3)
        continue




