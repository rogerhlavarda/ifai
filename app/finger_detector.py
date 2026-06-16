"""Regras simples para saber se cada dedo esta aberto ou fechado.

Este modulo recebe os landmarks encontrados pelo MediaPipe e transforma
esses pontos em informacao simples para o restante do projeto:
True significa dedo aberto, False significa dedo fechado.
"""

from config import FINGER_NAMES

# O MediaPipe Hands fornece 21 landmarks da mao, numerados de 0 a 20.
# Para os dedos longos, comparamos a ponta com uma articulacao intermediaria.
FINGER_POINTS = {
    "indicador": {"tip": 8, "pip": 6},
    "medio": {"tip": 12, "pip": 10},
    "anelar": {"tip": 16, "pip": 14},
    "minimo": {"tip": 20, "pip": 18},
}

DEFAULT_HAND_STATE = {
    "polegar": True,
    "indicador": True,
    "medio": True,
    "anelar": True,
    "minimo": True,
}


def detect_fingers(hand_landmarks, handedness=None):
    """Retorna True para dedo aberto e False para dedo fechado."""
    if hand_landmarks is None:
        return DEFAULT_HAND_STATE.copy()

    landmarks = getattr(hand_landmarks, "landmark", None)

    if landmarks is None or len(landmarks) <= 20:
        return DEFAULT_HAND_STATE.copy()

    states = {
        "polegar": is_thumb_open(landmarks, handedness),
    }

    for finger_name, points in FINGER_POINTS.items():
        states[finger_name] = is_finger_open(
            landmarks,
            points["tip"],
            points["pip"],
        )

    return states


def is_finger_open(landmarks, tip_id, pip_id):
    """Dedos longos abertos ficam com a ponta acima da articulacao PIP."""
    finger_tip = landmarks[tip_id]
    finger_pip = landmarks[pip_id]

    # Na imagem, y menor significa mais alto na tela.
    # Se a ponta esta acima da junta PIP, consideramos o dedo aberto.
    return finger_tip.y < finger_pip.y


def is_thumb_open(landmarks, handedness=None):
    """O polegar abre para o lado, por isso usa uma regra horizontal."""
    thumb_tip = landmarks[4]
    thumb_ip = landmarks[3]

    if handedness == "Left":
        return thumb_tip.x > thumb_ip.x

    if handedness == "Right":
        return thumb_tip.x < thumb_ip.x

    # Se o MediaPipe nao informar o lado, usamos uma regra simples:
    # quanto maior a distancia horizontal, maior a chance de estar aberto.
    return abs(thumb_tip.x - thumb_ip.x) > 0.04
