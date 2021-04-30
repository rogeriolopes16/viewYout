from modules.viewYoutube import *
from random import randint

if __name__ == '__main__':
    # Controles de execução
    tempo_minimo_video = 3
    tempo_maximo_video = 15
    quantidade_execucoes = randint(29, 39)

    openYoutube = YoutubeBot(tempo_minimo_video, tempo_maximo_video)
    i = 0
    print(f"Quantidade de execuções: {quantidade_execucoes}.")
    # Execuções dos videos
    while i < quantidade_execucoes:
        print("Execução: " + str(i + 1))
        openYoutube.watch_video()
        i += 1
        if i < quantidade_execucoes:
            time.sleep(randint(360, 540))  # Tempo que aguardará para proxima execução

    openYoutube.finaliza()