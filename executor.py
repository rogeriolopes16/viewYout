from viewYoutube import *
from random import randint

if __name__ == '__main__':
    # Controles de execução
    tempo_minimo_video = randint(39, 60)
    tempo_maximo_video = randint(70, 122)
    quantidade_execucoes = randint(5, 8)

    openYoutube = YoutubeBot(tempo_minimo_video, tempo_maximo_video)
    i = 0

    # Execuções dos videos
    while i < quantidade_execucoes:
        print("Execução: " + str(i + 1))
        openYoutube.watch_video()
        i += 1
        if i < quantidade_execucoes:
            time.sleep(randint(555, 1111))  # Tempo que aguardará para proxima execução

    openYoutube.finaliza()
