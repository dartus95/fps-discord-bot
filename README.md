[![Python Syntax Test](https://github.com/dartus95/fps-discord-bot/actions/workflows/python-app.yml/badge.svg)](https://github.com/dartus95/fps-discord-bot/actions/workflows/python-app.yml) 
![GitHub release (latest by date)](https://img.shields.io/github/v/release/dartus95/fps-discord-bot)
![GitHub License](https://img.shields.io/github/license/dartus95/fps-discord-bot)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/dartus95/fps-discord-bot/latest)

<!-- ![Static Badge](https://img.shields.io/badge/Release%20Version-Version%201.1.0-brightgreen) -->

# FPS Discord Bot
Tento bot byl vytvořen pro účely klanu Fatal Puppies Squad, a jedná se o bota, který ukládá soubor Arma 3 mise vytvořený Zeusem bez nutnosti přihlašovat se na vzdálený server Windows nebo používat programy jako AnyDesk, Teamviewer a další.

Jeho cílem je přijmout soubor zaslaný na konkrétní kanál Discord jako přílohu a uložit jej do určeného adresáře na serveru, kde je bot spuštěn. V podstatě jej tedy lze použít i v dalších případech, kdy by bylo nahrávání souborů na server za normálních okolností příliš obtížné nebo nechcete někomu zbytečně poskytovat přístup.

## Vlastnosti
Seznam funkcí, které tento bot umí:
* Nahrát soubor s misí z konkrétního kanálu Discordu do zadané složky na serveru Windows.
* Potvrdit, že soubor byl úspěšně nahrán.
* Kontrola typu souboru - kontrola, zda má soubor správnou příponu (.pbo).
* Kontrola velikosti souboru - kontrola, zda má soubor správnou velikost (výchozí: 5 MB).
* Příkaz pro kontrolu, zda je bot spuštěn (Ve výchozím nastavení: !check)

## Jak na přidání bota na vlastní Discord server
Pro správnou funkci je třeba změnit tři věci v souboru fps_bot.py:
* Nejprve je třeba vytvořit bota na stránce Discord Developer - https://discord.com/developers/applications.
    - Musíte vzít vygenerovaný token a vložit ho do souboru fps_bot.py.
    - Poté musíte bota pozvat na svůj server
* Do souboru .py vložte Discord Channel ID (existuje spousta návodů, jak Channel ID získat).
* Ujistěte se, že bot má práva k zobrazení zadaného kanálu na vašem serveru
* Zadejte cestu, kam bude soubor uložen (nezapomeňte zachovat dvojitá lomítka jinak tento krok nebude fungovat)
