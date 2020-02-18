#-------------------------------------------------
#
# Project created by QtCreator 2020-01-24T11:12:19
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = pysoundplayer
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += \
        main.cpp \
        mainwindow.cpp

HEADERS += \
        mainwindow.h

FORMS += \
        mainwindow.ui \
    gui/QSoundPlayer.ui \
    src/pysoundplayer/gui/QSoundPlayer.ui \
    examples/spectrogram_vizualizer.ui \
    src/pysoundplayer/examples/spectrogram_vizualizer2.ui \
    src/pysoundplayer/examples/spectrogram_vizualizer.ui \
    src/pysoundplayer/gui/ui/QImageOptions.ui \
    src/pysoundplayer/gui/ui/QSoundPlayer.ui \
    src/pysoundplayer/gui/ui/QSpectrogramOptions.ui \
    src/pysoundplayer/gui/ui/QSpectrogramViewer.ui \
    src/pysoundplayer/examples/QSpectrogramVizualizer.ui \
    src/pysoundplayer/gui/ui/QSpectrogramVizualizer.ui

RESOURCES += \
    gui/qsoundplayer.qrc \
    src/pysoundplayer/gui/qsoundplayer.qrc \
    src/pysoundplayer/gui/ui/qsoundplayer.qrc
