from PyQt5.QtCore import Qt
import PyQt5.QtWidgets as qtw
from smarket_task import Ui_MainWindow
#import smarket_task

class xy(qtw.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.expression=""
        self.expression_label.setText(self.expression)
        #self.total_label.setText=("")
        
        self.pushButton1.clicked.connect(lambda:self.addchar("5"))
        self.pushButton2.clicked.connect(lambda:self.addchar("7"))
        self.pushButton3.clicked.connect(lambda:self.addchar("3"))
        self.pushButton4.clicked.connect(lambda:self.addchar("2.5"))
        self.pushButton5.clicked.connect(lambda:self.addchar("4"))
        self.plus_button.clicked.connect(lambda:self.addchar("+"))
        
        self.equal_button.clicked.connect(self.get_result)
        self.clear_button.clicked.connect(self.clear)


    def addchar(self,Char):
        self.expression+=Char
        self.expression_label.setText(self.expression)

    def get_result(self):
        result=str(eval(self.expression))
        #self.total_label.setText(result)
        self.expression_label.setText(result)

    def clear(self):
        self.expression=""
        #self.expression_label.setText(self.expression)
        #self.total_label.setText("")
        self.expression_label.setText("")

app=qtw.QApplication([])
x=xy()
x.show()
app.exec()