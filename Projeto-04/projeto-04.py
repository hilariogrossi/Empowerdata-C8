# Projeto 04
#### Como usar python para projetos de inteligência artificial
#### Visão Computacional

import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    sucesso, imagem = webcam.read()
    coordenadas, imagem_maos = rastreador.findHands(imagem)

    print(coordenadas)

    cv2.imshow('Projeto 04 - IA', imagem)

    if cv2.waitKey(1) != -1:
        break

webcam.release()

cv2.destroyAllWindows()
