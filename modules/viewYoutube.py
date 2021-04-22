import os
import sys
from selenium import webdriver
import time
from pynput.mouse import Button, Controller
from random import randint, shuffle
import pyperclip


class YoutubeBot:
    def __init__(self, tempo_minimo_video, tempo_maximo_video):
        self.driver = webdriver.Firefox(executable_path=r"d:/Rogerio/projects/viewYoutube/tools/geckodriver.exe")
        self.username = "admin"
        self.password = "4dbf8251"
        self.tempo_minimo_video = tempo_minimo_video
        self.tempo_maximo_video = tempo_maximo_video

    def reset_internet(self):
        driver = self.driver
        print("Restart Internet.")
        try:
            driver.get("http://192.168.15.1/")  # abre configurações do modem
            time.sleep(5)
            mouse = Controller()
            mouse.position = (247, 354)  # posiciona ponteiro no menu comfigurações
            mouse.click(Button.left, 1)  # clica no posicionamento acima
            time.sleep(1)
            mouse.position = (203, 476)  # posiciona ponteiro no submenu reiniciar
            mouse.click(Button.left, 1)  # clica no posicionamento acima
            time.sleep(5)

            pyperclip.copy(self.username)
            mouse.position = (623, 364)  # posiciona ponteiro no campo usuario
            mouse.click(Button.right, 1)  # clica botão direito
            time.sleep(2)
            mouse.position = (699, 477)  # posiciona ponteiro na opção colar
            mouse.click(Button.left, 1)  # clica no posicionamento acima
            time.sleep(2)

            pyperclip.copy(self.password)
            mouse.position = (643, 406)  # posiciona ponteiro na seleção da senha
            mouse.click(Button.right, 1)  # clica botão direito
            time.sleep(2)
            mouse.position = (693, 524)  # posiciona ponteiro na opção colar
            mouse.click(Button.left, 1)  # clica no posicionamento acima
            time.sleep(2)

            mouse.position = (1080, 441)  # posiciona ponteiro no botão entrar
            mouse.click(Button.left, 1)  # clica no posicionamento acima
            time.sleep(3)

            mouse.position = (443, 331)  # posiciona ponteiro no botão reiniciar
            mouse.click(Button.left, 1)  # clica no posicionamento acima
            time.sleep(1)

            mouse.position = (607, 499)  # posiciona ponteiro no botão confirma reiniciar
            mouse.click(Button.left, 1)  # clica no posicionamento acima
            time.sleep(150)
        except:
            driver = self.driver
            driver.close()
            sys.exit()

    @staticmethod
    def carrega_videos():
        arquivo = open("d:/Rogerio/projects/viewYoutube/parameters/videos.txt", 'r')
        videos = []
        for n in arquivo:
            videos.append(n.strip())
        shuffle(videos)
        return videos[:randint(3, 6)]

    def watch_video(self):
        try:
            self.reset_internet()
            driver = self.driver
            for video in self.carrega_videos():
                driver.get(video)  # abre o video do indice atual
                tempo = randint(self.tempo_minimo_video, self.tempo_maximo_video)
                print("Assistindo o video: " + video + " por " + str(tempo) + " segundos.")
                time.sleep(3)
                mouse = Controller()
                mouse.position = (433, 398)  # posiciona ponteiro do mouse no botão de play
                mouse.click(Button.left, 1)  # clica no posicionamento acima para iniciar o video
                time.sleep(tempo)  # Tempo que irá assistir o video
        except:
            driver = self.driver
            driver.close()
            sys.exit()

    def finaliza(self):
        driver = self.driver
        driver.close()
        os.system('shutdown -s')

    @staticmethod
    def captura_ponteiro():
        mouse = Controller()
        time.sleep(2)
        print('The current pointer position is {0}'.format(mouse.position))
