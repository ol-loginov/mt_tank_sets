Огромная благодарность проекту https://github.com/StranikS-Scan/WorldOfTanks-Decompiled

## Порядок действий

1)  Для разработки используется PyCharm PY-145.597.11.
2)  Склонируйте этот git-репозиторий в `[Папка с игрой]/res_mods/[Версия игры]`.
3)  Распакуйте `pycharm-debug.egg` в `[Папка с игрой]/res_mods/[Версия игры]/scripts/common/pydev/pycharm/pydev` и скомпилируйте папку с помощью Python 2.7.
4)  Склонируйте репозиторий «StranikS-Scan/WorldOfTanks-Decompiled» в любую папку (назовем ее `[WOT-Decompiled]`).
5)  Создайте пустой проект в PyCharm. Добавьте в него в качестве Content Root (корня содержимого) следующие папки: `[Папка с игрой]/res_mods/[Версия игры]` и `[WOT-Decompiled]`.

## API для настроек модов (mods settings api)

Оригинальную информацию можно найти здесь:
*   https://wiki.wargaming.net/ru/ModsettingsAPI
*   https://github.com/IzeBerg/modssettingsapi/

## Список модов (mods list)

https://gitlab.com/wot-public-mods/mods-list

## Иконки

Для создания иконок используется следующая команда:

```shell
convert -size 32x17 xc:none -fill white -font "SF-Pro-Bold" -pointsize 12 -gravity center -draw "text 1,0 '1'" 1.png
```
