import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MainWindow import Ui_MainWindow
from UploadWindow import Ui_Form
from DeleteWindow import Ui_AreYouSure
import pymongo
import time

UploadFlag = 0  # 0表示用户正在上传，1表示上传成功，-1表示上传失败
DeleteFlag = 0  # 0表示用户正在删除，1表示删除成功，-1表示删除失败
DBHeaderLabels = ['name', 'amount', 'want', 'contact']
Sorts = ['水果', '日用品', '零食']


def insertRecord(record):
    myCollection.insert_one(record)


def removeRecord(record_id):
    myquery = {"_id": record_id}
    myCollection.delete_one(myquery)


def uploadReady():
    global UploadFlag

    while UploadFlag == 0:
        time.sleep(0.5)

    if UploadFlag == 1:
        UploadFlag = 0
        return 1
    elif UploadFlag == -1:
        UploadFlag = 0
        return -1


def deleteReady():
    global DeleteFlag

    while DeleteFlag == 0:
        time.sleep(0.5)

    if DeleteFlag == 1:
        DeleteFlag = 0
        return 1
    elif DeleteFlag == -1:
        DeleteFlag = 0
        return -1


class DeleteWindow(QMainWindow, Ui_AreYouSure):
    def __init__(self, parent=None):
        # 继承父类响应的函数，在此为初始化函数
        super(DeleteWindow, self).__init__(parent)
        # 加载UI模型
        self.DeleteRecordID = 0
        self.ui_delete = Ui_AreYouSure()
        self.ui_delete.setupUi(self)
        self.delete_init_slots()

    def updateDeleteRecordID(self, DeleteRecordID):
        self.DeleteRecordID = DeleteRecordID

    def delete_init_slots(self):
        self.ui_delete.Yes.clicked.connect(self.confirm)
        self.ui_delete.No.clicked.connect(self.cancel)

    def confirm(self):
        global DeleteFlag
        myquery = {"_id": self.DeleteRecordID}
        myCollection.delete_one(myquery)

        DeleteFlag = 1
        # print(self.DeleteRecordID)

    def cancel(self):
        global DeleteFlag
        DeleteFlag = -1


class UploadWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        # 继承父类响应的函数，在此为初始化函数
        super(UploadWindow, self).__init__(parent)
        # 加载UI模型
        self.ui_start = Ui_Form()
        self.ui_start.setupUi(self)
        self.init_slots()
        self.init_combobox()
        self.resize(600, 300)

    def init_slots(self):
        self.ui_start.Confirm.clicked.connect(self.confirm)
        self.ui_start.Cancel.clicked.connect(self.cancel)

    def init_combobox(self):
        box = self.ui_start.comboBox
        box.addItems(Sorts)

    def confirm(self):
        global UploadFlag

        sort = self.ui_start.comboBox.currentText()
        obj = self.ui_start.text1.text()
        amu = self.ui_start.text2.text()
        want = self.ui_start.text3.text()
        contact = self.ui_start.text4.text()

        one_record = {
            "sort": sort, "name": obj, "amount": amu, "want": want, "contact": contact
        }

        print(one_record)
        insertRecord(one_record)

        UploadFlag = 1

        self.ui_start.text1.setText("")
        self.ui_start.text2.setText("")
        self.ui_start.text3.setText("")
        self.ui_start.text4.setText("")

    def cancel(self):
        global UploadFlag

        UploadFlag = -1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # 继承父类响应的函数，在此为初始化函数
        super(MainWindow, self).__init__(parent)
        self.deleteWindow = DeleteWindow()
        self.uploadWindow = UploadWindow()
        # 加载UI模型
        self.ui_start = Ui_MainWindow()
        self.ui_start.setupUi(self)
        # 初始化按钮与Slot的通信
        self.init_slots()
        self.init_table()
        self.init_combobox()
        self.CurrentTableRecordsID = []
        self.DeleteRecordID = 0
        self.updateTable()

    def init_slots(self):
        self.ui_start.Upload.clicked.connect(self.upload)
        self.ui_start.Search.clicked.connect(self.search)

    def init_table(self):
        table = self.ui_start.tableWidget
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(['物品', '数量', 'Wants', '联系方式'])
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.itemDoubleClicked.connect(self.delete)

    def init_combobox(self):
        box = self.ui_start.comboBox
        box.addItems(Sorts)

        box.currentIndexChanged.connect(self.comboBoxSelectionChange)

    def comboBoxSelectionChange(self):
        box = self.ui_start.comboBox
        self.updateTable()

    def clearTable(self):
        table = self.ui_start.tableWidget

        row = table.rowCount()
        while row != -1:
            table.removeRow(row - 1)
            row -= 1

    def updateTable(self, DB_changed=True, limitation=None):
        # update for upload new records
        if DB_changed:
            self.clearTable()

            sort = self.ui_start.comboBox.currentText()

            myquery = {"sort": sort}
            records = myCollection.find(myquery)
            self.CurrentTableRecordsID.clear()
            # print(self.CurrentTableRecordsID)

            for record in records:
                self.CurrentTableRecordsID.append(record['_id'])
                row = self.ui_start.tableWidget.rowCount()
                self.ui_start.tableWidget.insertRow(row)
                for j in range(4):
                    text = record[DBHeaderLabels[j]]
                    item = QTableWidgetItem(text)
                    self.ui_start.tableWidget.setItem(row, j, item)

            # print(type(self.CurrentTableRecordsID[0]))

        # update for search records
        if limitation is not None:
            self.clearTable()

            myquery = {"name": limitation}
            records = myCollection.find(myquery)
            self.CurrentTableRecordsID.clear()
            # print(self.CurrentTableRecordsID)

            for record in records:
                self.CurrentTableRecordsID.append(record['_id'])
                row = self.ui_start.tableWidget.rowCount()
                self.ui_start.tableWidget.insertRow(row)
                for j in range(4):
                    text = record[DBHeaderLabels[j]]
                    item = QTableWidgetItem(text)
                    self.ui_start.tableWidget.setItem(row, j, item)

            # print(type(self.CurrentTableRecordsID[0]))

    def search(self):
        name = self.ui_start.lineEdit.text()
        if name == '':
            self.updateTable()
        else:
            self.updateTable(False, name)

    def checkUpload(self, UploadState):
        self.uploadWindow.hide()
        if UploadState == 1:
            self.updateTable(True)
        elif UploadState == -1:
            self.updateTable(False)

    def checkDelete(self, DeleteState):
        self.deleteWindow.hide()
        if DeleteState == 1:
            self.updateTable(True)
        elif DeleteState == -1:
            self.updateTable(False)

    def upload(self):
        self.uploadWindow.show()

        self.ui_start.timeThread = waitUploadThread()
        self.ui_start.timeThread.sinout.connect(self.checkUpload)  # 设置线程结束函数
        self.ui_start.timeThread.start()  # 开启线程

    def delete(self, index):
        self.deleteWindow.show()
        self.DeleteRecordID = self.CurrentTableRecordsID[index.row()]
        self.deleteWindow.updateDeleteRecordID(self.DeleteRecordID)

        self.ui_start.timeThread = waitDeleteThread()
        self.ui_start.timeThread.sinout.connect(self.checkDelete)
        self.ui_start.timeThread.start()


class waitUploadThread(QThread):
    sinout = pyqtSignal(int)

    def __init__(self):
        super(waitUploadThread, self).__init__()

    def run(self):
        result = uploadReady()
        self.sinout.emit(result)


class waitDeleteThread(QThread):
    sinout = pyqtSignal(int)

    def __init__(self):
        super(waitDeleteThread, self).__init__()

    def run(self):
        result = deleteReady()
        self.sinout.emit(result)


if __name__ == "__main__":
    # myClient = pymongo.MongoClient('mongodb://localhost:27017/')
    # myClient = pymongo.MongoClient(host='192.168.31.194', port=27017)
    myClient = pymongo.MongoClient(host='120.241.144.224', port=26214)
    mydb = myClient['Test']
    myCollection = mydb['Objs']

    # res = myCollection.delete_many({})  # clear all records

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
