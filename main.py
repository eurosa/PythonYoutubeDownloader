import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# from pytube import YouTube
from pytube import YouTube
import mainwindow

list_urls = ['https://youtu.be/HhMgOcAiAlE',
             'https://www.youtube.com/watch?v=D5NK5qMM14g']


# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)  # gets defined in the UI file
        # self.setStyleSheet("background-color: yellow;")
        self.ui.getAllStrem.clicked.connect(self.youTubeVideo)

    def youTubeVideo(self):
        for url in list_urls:

            try:
                yt_obj = YouTube(url)
                yt_obj.streams.get_highest_resolution().download()
            except Exception as e:
                print(e)
                raise Exception('Some exception occurred.')
            print('All YouTube videos downloaded successfully.')


def main():
    # a new app instance
    app = QApplication(sys.argv)
    app.setStyle("QtCurve")  # dataModel.get_power_on_image_path()
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
