from viewYoutube import *
from random import randint

if __name__ == '__main__':
    # Controles de execução
    tempo_minimo_video = randint(555, 666)
    tempo_maximo_video = randint(888, 999)
    quantidade_execucoes = randint(3, 5)


    openYoutube = YoutubeBot(tempo_minimo_video, tempo_maximo_video)
    i = 0
    print(f"Quantidade de vezes a executar: {quantidade_execucoes}.")
    # Execuções dos videos
    while i < quantidade_execucoes:
        print("Execução: " + str(i + 1))
        openYoutube.watch_video()
        i += 1
        if i < quantidade_execucoes:
            time.sleep(randint(700, 1000))  # Tempo que aguardará para proxima execução

    openYoutube.finaliza()
