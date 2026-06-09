# Mao Robotica com IA e Visao Computacional - IFAI

Projeto didatico do IFAI - Laboratorio de Experimentos em Inteligencia Artificial.

Esta e uma nova implementacao, limpa e simples, inspirada conceitualmente no projeto original de WellingtonDev25. A estrutura foi pensada para aulas do Curso Tecnico em Informatica: poucos arquivos, responsabilidades claras e comentarios que ajudam a entender o caminho da informacao.

Fluxo do sistema:

```text
Webcam
  |
  v
MediaPipe Hands
  |
  v
Deteccao dos dedos
  |
  v
Python
  |
  v
Arduino
  |
  v
Servomotores
```

## 1. Apresentacao do IFAI

O IFAI - Laboratorio de Experimentos em Inteligencia Artificial e um espaco para criar, testar e apresentar prototipos interativos com IA.

Neste experimento, os estudantes veem uma aplicacao completa ligando visao computacional e automacao fisica.

## 2. Objetivo do laboratorio

"Proporcionar aos estudantes do Curso Tecnico em Informatica Integrado ao Ensino Medio uma experiencia pratica e investigativa com tecnologias de Inteligencia Artificial.

O projeto propoe a criacao de experimentos interativos envolvendo processamento de linguagem natural, visao computacional, geracao de imagens, chatbots e automacao inteligente.

Os estudantes atuarao desde a fase de pesquisa e planejamento ate o desenvolvimento e apresentacao dos prototipos em eventos institucionais, como o #VemProIF."

## 3. Objetivo do experimento

Controlar uma mao robotica com 5 dedos usando a deteccao da mao humana pela webcam.

A webcam captura a imagem. O MediaPipe Hands encontra os landmarks da mao. O Python interpreta quais dedos estao abertos ou fechados. O Arduino recebe os comandos e move um servo para cada dedo.

## 4. Arquitetura do sistema

- `app/main.py`: organiza o fluxo principal da aplicacao.
- `app/hand_tracker.py`: usa MediaPipe para encontrar a mao na imagem.
- `app/finger_detector.py`: transforma landmarks em estados dos dedos.
- `app/arduino_controller.py`: envia angulos para os servos via pyFirmata.
- `app/config.py`: centraliza porta COM, pinos, angulos e parametros.

O fluxo foi mantido simples para que o estudante consiga acompanhar a execucao lendo primeiro o arquivo `app/main.py`.

## 5. Tecnologias utilizadas

- Python 3.10.x
- OpenCV
- MediaPipe Hands
- pyFirmata
- pyserial
- Arduino
- Servomotores
- VS Code

## 6. Estrutura do projeto

```text
mao-robotica-ifai/
+-- .vscode/
|   +-- settings.json
|   +-- extensions.json
+-- app/
|   +-- main.py
|   +-- hand_tracker.py
|   +-- finger_detector.py
|   +-- arduino_controller.py
|   +-- config.py
+-- arduino/
|   +-- mao_robotica_5_dedos.ino
+-- scripts/
|   +-- configurar_ambiente.bat
|   +-- atualizar_projeto.bat
|   +-- abrir_vscode.bat
|   +-- executar.bat
|   +-- verificar_ambiente.bat
+-- requirements.txt
+-- README.md
+-- .gitignore
+-- LICENSE
```

## 7. Como criar o ambiente virtual

No Windows, abra o terminal na pasta do projeto e execute:

```bat
scripts\configurar_ambiente.bat
```

Esse script cria a pasta `.venv`, ativa o ambiente virtual e instala as dependencias do `requirements.txt`.

## 8. Como instalar dependencias

Se preferir fazer manualmente:

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

O projeto recomenda Python 3.10.x.

## 9. Como abrir no VS Code

Execute:

```bat
scripts\abrir_vscode.bat
```

O VS Code esta configurado para usar:

```text
.venv\Scripts\python.exe
```

Se o comando `code` nao estiver no PATH, abra o VS Code manualmente e escolha a pasta do projeto.

## 10. Como executar

Depois de configurar o ambiente e conectar o Arduino:

```bat
scripts\executar.bat
```

Durante a execucao:

- Pressione `Q` para sair.
- Pressione `ESC` para sair.

Se o Arduino nao conectar, a webcam ainda abre para permitir testar a deteccao dos dedos.

## 11. Como calibrar os servos

Abra `app/config.py` e ajuste os angulos:

```python
SERVO_ANGLES = {
    "polegar": {"aberto": 20, "fechado": 150},
    "indicador": {"aberto": 20, "fechado": 150},
    "medio": {"aberto": 20, "fechado": 150},
    "anelar": {"aberto": 20, "fechado": 150},
    "minimo": {"aberto": 20, "fechado": 150},
}
```

Os angulos precisam ser calibrados porque cada mao robotica pode ter montagem, linha, elasticos e limites mecanicos diferentes. Um valor errado pode forcar o servo ou travar uma peca.

## 12. Como alterar a porta COM

Abra `app/config.py` e altere:

```python
ARDUINO_PORT = "COM3"
```

No Windows, a porta costuma ser `COM3`, `COM4` ou parecida. No Linux, normalmente aparece como `/dev/ttyACM0` ou `/dev/ttyUSB0`.

## 13. Como carregar o StandardFirmata

Este projeto usa pyFirmata. Por isso, antes de executar o Python, carregue o StandardFirmata no Arduino:

1. Abra a IDE Arduino.
2. Conecte o Arduino ao computador.
3. Selecione a placa correta.
4. Selecione a porta correta.
5. Abra `Arquivo > Exemplos > Firmata > StandardFirmata`.
6. Clique em carregar.

O arquivo `arduino/mao_robotica_5_dedos.ino` e um exemplo alternativo para estudo futuro com comunicacao serial simples. Ele nao substitui o StandardFirmata nesta versao.

## 14. Solucao de problemas

**A webcam nao abre**

Verifique se outra aplicacao esta usando a camera. Se houver mais de uma webcam, altere `CAMERA_INDEX` em `app/config.py`.

**O Arduino nao conecta**

Confira a porta COM em `app/config.py`, feche o Monitor Serial da IDE Arduino e confirme se o StandardFirmata foi carregado.

**Os servos mexem ao contrario**

Troque os valores `aberto` e `fechado` do dedo correspondente em `app/config.py`.

**Um servo parece forcar a estrutura**

Reduza o angulo fechado ou aberto daquele dedo. Calibre sempre com movimentos pequenos.

**As bibliotecas nao importam**

Execute:

```bat
scripts\verificar_ambiente.bat
```

Se houver erro, execute novamente:

```bat
scripts\configurar_ambiente.bat
```

## 15. Creditos ao projeto original

Esta implementacao foi criada do zero para uso didatico no IFAI, inspirada conceitualmente no repositorio:

https://github.com/WellingtonDev25/mao-robotica-mediapipe

Creditos ao autor original, WellingtonDev25, pela ideia inicial de controlar servos com deteccao de mao usando MediaPipe.

## Como a deteccao dos dedos funciona

O MediaPipe Hands fornece 21 landmarks da mao. Landmark e um ponto de referencia anatomico, como a ponta de um dedo ou uma articulacao.

Para indicador, medio, anelar e minimo, o codigo compara a ponta do dedo com uma articulacao intermediaria:

| Dedo | Ponta | Articulacao |
| --- | --- | --- |
| Indicador | 8 | 6 |
| Medio | 12 | 10 |
| Anelar | 16 | 14 |
| Minimo | 20 | 18 |

Quando a ponta esta acima da articulacao intermediaria, consideramos o dedo aberto. Na imagem da webcam, um valor `y` menor significa que o ponto esta mais alto.

O polegar usa uma regra horizontal porque ele abre para o lado.

## Pinos dos servos

| Dedo | Pino Arduino |
| --- | --- |
| Polegar | 3 |
| Indicador | 5 |
| Medio | 9 |
| Anelar | 10 |
| Minimo | 11 |

