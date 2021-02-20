import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QSpinBox, QGridLayout
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

        self.ui.getAllStrem.clicked.connect(self.addtextbox)

    def youTubeVideo(self):
        for url in list_urls:

            try:
                yt_obj = YouTube(url)
                yt_obj.streams.get_highest_resolution().download()
            except Exception as e:
                print(e)
                raise Exception('Some exception occurred.')
            print('All YouTube videos downloaded successfully.')

    def home(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.label = QLabel(self)
        self.label.setText("NO")
        self.grid.addWidget(self.label, 0, 1)

        #        self.input1 = QLineEdit(self)
        self.input1 = QSpinBox(self)  # +++
        self.input1.setMinimum(1)
        self.input1.setMaximum(12)
        self.input1.setValue(3)

        self.grid.addWidget(self.input1, 0, 5)

        self.pushButton_ok = QPushButton("Press me", self)
        self.pushButton_ok.clicked.connect(self.addtextbox)  # (self.addCheckbox)
        self.grid.addWidget(self.pushButton_ok, 0, 10)

    def addtextbox(self):
        countLayout = self.layout().count()
        if countLayout > 3:
            for it in range(countLayout - 3):
                w = self.layout().itemAt(3).widget()
                self.layout().removeWidget(w)
                w.hide()
        self.lineEdits = []  # +++

        for n in range(self.ui.input1.value()):
            self.bursttime = QLabel(self)
            self.bursttime.setText("b_{}".format(n))

            self.timeinput = QLineEdit(self)
            self.timeinput.textChanged.connect(lambda text, i=n: self.editChanged(text, i))  # +++

            self.ui.grid.addWidget(self.bursttime, 2 * n + 1, 0)
            self.ui.grid.addWidget(self.timeinput, 2 * n + 1, 1)

            self.lineEdits.append('')  # +++

        self.go = QPushButton("GO")  # , self)
        self.ui.grid.addWidget(self.go, 2 * n + 2, 0)
        self.go.clicked.connect(self.printvalues)

    def printvalues(self):
        # fetch data in some way
        for i, v in enumerate(self.lineEdits):  # +++
            print("bursttime: b_{}, timeinput: {}".format(i, v))  # +++
            try:
                yt_obj = YouTube(v)
                yt_obj.streams.get_highest_resolution().download()
            except Exception as e:
                print(e)
                raise Exception('Some exception occurred.')
            print('All YouTube videos downloaded successfully.')

    def editChanged(self, text, i):  # +++
        self.lineEdits[i] = text  # +++

    def addCheckbox(self):
        print("def addCheckbox(self):")


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
