# -*- coding: utf-8 -*-
import cv2, datetime, os, time
from diference_opencv import different


def universalCap(width = 1280 ,heigth = 720, device = 0,interval = 1,difference_target = 95, fps = 1, inside_folder = str(os.getcwd()) + "_images"):
    
#este bloco faz a configuração da camera e captura o primeiro quadro.
    
    print("__________IMAGE 1__________")
    try: #selecionando parametros para a captura.
        camera = cv2.VideoCapture(device) #parametro para selecionar dispositivo (0 é o padrão).
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, width )
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, heigth)
        camera.set(cv2.CAP_PROP_FPS, fps)
    except:
        raise Exception ("_____ERROR WITH CAMERA SET/PROPERTIES_____")
    try: #iniciar a camera
        camera.isOpened()== True 
    except:
        raise Exception ("_____ERROR WHILE OPENING CAMERA_____")

    #lendo o horario da captura, lendo retorno da camera.
    current_time = datetime.datetime.now()
    ret,frame = camera.read()
    
    if (ret==False): #checando o retorno da camera
        raise Exception ("_____ERROR WHILE READING CAMERA DATA(check properties)_____")
    try: #criar diretorio para armazenar imagem 1
        if not os.path.exists(str(os.getcwd()) + "_images"):
            os.makedirs(str(os.getcwd()) + "_images")
    except:
        raise Exception ("_____ERROR WHILE CREATING FOLDER FOR UNIVERSAL_____")

    try: #cria o nome do arquivo e grava a imagem 1 em disco.
        file_name = "%s-%s-%s-%s-%s-%s.png"%(current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second)
        full_file_path = os.path.join(inside_folder, file_name)
        cv2.imwrite(full_file_path, frame)
        print("FRAME1 WRITE AT", full_file_path)
    except:
        raise Exception ("_____ERROR WHILE SAVING IMAGE AT STORAGE_____")
    
    time.sleep(interval) #adiciondo intervalo entre as capturas 1 e 2.

#o bloco a baixo captura o segundo quadro e utiliza o modulo difference_opencv para comparar as imagens e decidir se mantem a nova ou a apaga.
    
    print("__________IMAGE 2__________")
    current_time2 = datetime.datetime.now()#momento da captura para criar o nome do arquivo.
    ret2,frame2 = camera.read() #leitura da imagem 2 utilizando o mesmo objeto "camera" para utilizar os mesmos parametros da imagem 1.
    #cria o nome do arquivo para imagem 2
    file_name2 = "%s-%s-%s-%s-%s-%s.png"%(current_time2.day, current_time2.month, current_time2.year, current_time2.hour, current_time2.minute, current_time2.second)
    full_file_path2 = os.path.join(inside_folder, file_name2)

    if (ret2==False):#novamente verificação de retorno mas para a imagem 2
        raise Exception ("_____ERROR WHILE READING CAMERA DATA FOR IMAGE 2(check properties)_____")

#utilizando a função para diferenciar quadros.
    if different(frame, frame2, difference_target) == True: 
        try: #grava a imagem 2 em disco.
            cv2.imwrite(full_file_path2, frame2)
            print("*DIFFERENT, WRITE AT ", full_file_path2)
        except:
            raise Exception ("_____ERROR WHILE SAVING IMAGE 2 AT STORAGE_____")

    else:#não armazena em disco a imagem 1, isso permite que ao terminar o grande loop não seja mantida sempre a imagem 1
        print("*IMAGE SIMILAR, REMOVING IMAGE %s"%(full_file_path))
        os.remove(full_file_path)
    time.sleep(interval) # intervalo entre a captura 2 e 1.


    """o proximo passo é remover a imagem mais atual em caso de repetida pois a diferença se acumula ao longo do tempo """
