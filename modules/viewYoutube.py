import os
import sys
from selenium import webdriver
import time
from random import randint, shuffle
import pyautogui
from parameters.parameters import *

class YoutubeBot:
    def __init__(self, tempo_minimo_video, tempo_maximo_video):
        self.driver = webdriver.Firefox(executable_path=r"d:/Rogerio/projects/viewYoutube/tools/geckodriver.exe")
        self.username = user_internet
        self.password = pass_internet
        self.tempo_minimo_video = tempo_minimo_video
        self.tempo_maximo_video = tempo_maximo_video

    def reset_internet(self):
        driver = self.driver
        print("Restart Internet.")
        try:
            driver.get(ip_internet)  # abre configurações do modem
            time.sleep(5)

            pyautogui.click(247, 354)  # posiciona ponteiro no menu comfigurações
            time.sleep(1)
            pyautogui.click(203, 476)  # posiciona ponteiro no submenu reiniciar
            time.sleep(5)

            pyautogui.click(623, 364)  # posiciona ponteiro no campo usuario
            pyautogui.write(self.username)
            time.sleep(1)

            pyautogui.click(643, 406)  # posiciona ponteiro na seleção da senha
            pyautogui.write(self.password)
            time.sleep(1)

            pyautogui.press('enter')  # enter no botão entrar
            time.sleep(3)

            pyautogui.click(443, 331)  # posiciona ponteiro no botão reiniciar
            time.sleep(1)

            pyautogui.click(607, 499)  # posiciona ponteiro no botão confirma reiniciar
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
        qtd_videos = randint(int(len(videos)/2), len(videos))
        return videos[:qtd_videos]

    def watch_video(self):
        try:
            self.reset_internet()
            driver = self.driver
            for video in self.carrega_videos():
                driver.get(video)  # abre o video do indice atual
                tempo = randint(self.tempo_minimo_video, self.tempo_maximo_video)
                print("Assistindo o video: " + video + " por " + str(tempo) + " segundos.")
                time.sleep(8)
                pyautogui.click(433, 398)  # posiciona ponteiro do mouse no botão de play
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
        time.sleep(3)
        print('The current pointer position is {0}'.format(pyautogui.position()))
