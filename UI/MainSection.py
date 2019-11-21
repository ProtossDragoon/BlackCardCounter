import sys
from PIL import Image, ImageQt
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.layout = self.setLayout(grid)

        DealerCardSection=QLabel()
        DealerCardSection.setText("Dealer Card Section")
        grid.addWidget(DealerCardSection,0,0)

        Often_Probability=QLabel()
        Often_Probability.setText("Probability")
        grid.addWidget(Often_Probability,0,1)

        My_Card_Section=QLabel()
        My_Card_Section.setText("My Card State")
        grid.addWidget(My_Card_Section,1,1)

        Player2_Card_Section=QLabel()
        Player2_Card_Section.setText(("Plyaer2 Card Section"))
        grid.addWidget(Player2_Card_Section,1,2)


        Player3_Card_Section=QLabel()
        Player3_Card_Section.setText
        grid.addWidget(QLabel('Often Probability'), 0, 1)
        grid.addWidget(QLabel('My Card Section:'), 1, 1)
        grid.addWidget(QLabel('Player2 Card Section:'), 1, 2)
        grid.addWidget(QLabel('Player3 Card Section:'), 1, 3)
        grid.addWidget(QLabel('Player4 Card Section:'), 1, 3)


        grid.addWidget(QLabel('Player4 Card Section:'), 1, 3)
        grid.addWidget(QLabel('Player4 Card Section:'), 1, 3)


        self.setWindowTitle('Black Jack Card Counter')
        self.setGeometry(300, 300, 1000, 700)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())