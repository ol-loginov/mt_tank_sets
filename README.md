# Форум "Мир Танков"

([1.35.0.0] "Редактируемые наборы танков в карусели")[http://forum.tanki.su/index.php?/topic/2205714-13500-%d1%80%d0%b5%d0%b4%d0%b0%d0%ba%d1%82%d0%b8%d1%80%d1%83%d0%b5%d0%bc%d1%8b%d0%b5-%d0%bd%d0%b0%d0%b1%d0%be%d1%80%d1%8b-%d1%82%d0%b0%d0%bd%d0%ba%d0%be%d0%b2-%d0%b2-%d0%ba%d0%b0%d1%80%d1%83%d1%81%d0%b5%d0%bb%d0%b8/]

# Настройка мода

## Смена иконок наборов

Вы можете поместить PNG-файл с именем «1.png» в папку `[Папка с игрой]/mods/config/com.github.ol_loginov.editable_tank_sets`, и эта иконка будет использоваться для набора 1. 
То же самое справедливо и для других наборов (просто используйте «2.png», «3.png» и т.д.).

## Совместимость с XVM

Этот мод не может работать одновременно с установленной каруселью танков от XVM. Однако существует способ отключить карусель XVM, чтобы этот мод заработал.
Подробности здесь: https://github.com/ol-loginov/wot_tank_sets/issues/2#issuecomment-1493420544

# Сборка

Благодарности проекту https://github.com/StranikS-Scan/WorldOfTanks-Decompiled

### Порядок действий

1)  Для разработки используется PyCharm PY-145.597.11.
2)  Склонируйте этот git-репозиторий в `[Папка с игрой]/res_mods/[Версия игры]`.
3)  Распакуйте `pycharm-debug.egg` в `[Папка с игрой]/res_mods/[Версия игры]/scripts/common/pydev/pycharm/pydev` и скомпилируйте папку с помощью Python 2.7.
4)  Склонируйте репозиторий «StranikS-Scan/WorldOfTanks-Decompiled» в любую папку (назовем ее `[WOT-Decompiled]`).
5)  Создайте пустой проект в PyCharm. Добавьте в него в качестве Content Root (корня содержимого) следующие папки: `[Папка с игрой]/res_mods/[Версия игры]` и `[WOT-Decompiled]`.

## API для настроек модов (mods settings api)

Оригинальную информацию можно найти здесь:
*   https://wiki.wargaming.net/ru/ModsettingsAPI
*   https://bitbucket.org/IzeBerg/modssettingsapi

## Список модов (mods list)

https://gitlab.com/wot-public-mods/mods-list

## Иконки

Для создания иконок используется следующая команда:

```shell
convert -size 32x17 xc:none -fill white -font "SF-Pro-Bold" -pointsize 12 -gravity center -draw "text 1,0 '1'" 1.png
```
