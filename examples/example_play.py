from PySide6.QtWidgets import QApplication
from pysoundplayer.widget.sound_player_widget import SoundPlayerWidget
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)
    sound_player = SoundPlayerWidget(file_path="example.wav")
    sound_player.show()
    sys.exit(app.exec())
