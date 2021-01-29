import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QScrollArea, QApplication


class Widget(QWidget):

    def __init__(self, parent=None):
        super(Widget, self).__init__()

        # Add a button and connect it to its slot
        btn_new = QPushButton("Add a new line of text")
        btn_new.clicked.connect(self.add_new_line_text)

        # the main widget
        self.widget = QWidget()
        # Add a vertical layout
        layout = QVBoxLayout(self)
        # Add a text line and disable it
        for _ in range(1):
            line_text = QLineEdit("foo")
            line_text.setEnabled(True)
            # Add the text to the vertical widget
            layout.addWidget(line_text)
            # Stretch it a little
            layout.addStretch()
        # Add the layout to the widget    
        self.widget.setLayout(layout)

        # Declare a QSrollArea and add the widget to it.
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # Make it resizable
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.widget)

        # The main window vertical layout 
        vLayout = QVBoxLayout(self)
        # Add a button to it
        vLayout.addWidget(btn_new)
        # Add scroll to it
        vLayout.addWidget(scroll)
        # Set this as the main widget layout
        self.setLayout(vLayout)

    def add_new_line_text(self):
        line_text = QLineEdit("bar")
        self.widget.layout().insertWidget(self.widget.layout().count() - 1, line_text)
        print(str(self.widget.layout().count() - 1)+" "+str(line_text))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Widget()
    dialog.show()
    app.exec_()
