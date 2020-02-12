for f in *.ui; do pyside2-uic "$f" -o $(echo $f | sed s/.ui/_ui.py/); done
pyside2-uic QSoundPlayer.ui -o QSoundPlayer_ui.py --from-imports