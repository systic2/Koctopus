import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        btn1 = QPushButton('경기 검색', self)
        btn1.setText('경기 검색')

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString('yyyy M d'))

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(cal)
        leftLayout.addWidget(btn1)
        leftLayout.addWidget(self.lbl)

        tableWidget = QTableWidget(7, 3)
        tableWidget.setHorizontalHeaderLabels(['홈팀', 'vs', '어웨이팀'])
        # tableWidget.resizeColumnsToContents()
        # tableWidget.resizeRowsToContents()
        centerLayout = QVBoxLayout()
        centerLayout.addWidget(tableWidget)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(centerLayout)

        self.setLayout(layout)

        self.setWindowTitle("Koctopus")
        self.setWindowIcon(QIcon('octopus.png'))
        self.resize(1000, 800)
        self.center()
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString('yyyy M d'))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())