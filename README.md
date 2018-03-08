# GPIO-ATV-Script-2
Ein weiteres Script was irgend ein Relay beim ATV Steuern soll...


## Bekannte Angaben:

Es gibt mehrere Signale, die als GPIO Input vom Raspberry Pi gelesen werden. Hier gibt es einen Pin der eine Ausgabe fordern soll, ein pin der die Eingaben zurücksetzen soll und mehrere Pins die DTMF Töne Binär eingeben sollen. Und natürlich die pins zur Ausgabe der DTMF Töne ;-).

```
  Input Pins:

  6 Eingäng:
  0  0  0 0 0 0
  |  |  DTMF Töne
  |  |
  |  |
  |  |
  | Reset
  Ausführen was eingegeben wurde

  8 Ausgänge:

  0 0 0 0 0 0 0 0

  DTMF 1 == Pin 1
  DTMF 2 == Pin 2
  ...

```


# Setup:
*Wie wird das Programm installiert* ***(bei Internet in einem Terminal auf dem Raspberry Pi)***

```bash
# Pakete aktualisieren:
sudo apt update
sudo apt upgrade -y
sudo apt install -y git vim tmux python3 
echo -e "set expandtab\nset tabstop=4\
  \nset shiftwidth=4\nset fileencoding=utf-8\ 
  \nset encoding=utf-8\ncolorscheme elflord\
  \nsyntax on" > ~/.vimrc

# Projekt herunterladen:
git clone https://github.com/DO1JLR/GPIO-ATV-Script-2.git

# Hilfetext:
~/GPIO-ATV-Script-2/main.py --help

# Programm Ausführen:
~/GPIO-ATV-Script-2/main.py 
```

## Updaten

```bash
# Aktualisieren des Programms:
cd ~/GPIO-ATV-Script-2/
git pull
cd ~
```

# Update ohne Netzwerkanbindung:

Herunterladen des letzten Releases: [Download](https://github.com/DO1JLR/GPIO-ATV-Script-2/releases/latest)

# Weitere Informationen
Als erstes erkennt das Programm, welche Pins ein Input Signal haben. Basierend darauf wird dann ein oder kein Signal gegeben.
**[Pinbelegung](https://de.pinout.xyz/)**
*Tipp: Es wird die Kategorie: "Physical Pin" verwendet.*

```
Es gibt 2 Eingänge zur Steuerung
Es gibt 4 Eingänge für die DTMF Töne
Es gibt 8 Ausgänge, also für jeden DTMF Ton einen 
```
### Steuerungspins:
| **GPIO-Input** | **Funktion**         |
|:--------------:|:--------------------:|
|  37            | Ausführen            |
|  35            | Eingabe zurücksetzen |
|                |                      |

### DTMF Eingänge:
| **GPIO-Input** | **Funktion**          |
|:--------------:|:---------------------:|
|  33            | DTMF - erster Input   |
|  31            | DTMF - zweiter Input  |
|  29            | DTMF - dritter Input  |
|  27            | DTMF - vierter Input  |

### einzelne Ausgänge:

| **GPIO-Output** | **DTMF Ton**    |
|:---------------:|:---------------:|
|  11             | DTMF Signal #1  |
|  13             | DTMF Signal #2  |
|  15             | DTMF Signal #3  |
|  16             | DTMF Signal #4  |
|  18             | DTMF Signal #5  |
|  19             | DTMF Signal #6  |
|  21             | DTMF Signal #7  |
|  23             | DTMF Signal #8  |




