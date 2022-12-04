import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MainWindow import Ui_MainWindow
from UploadWindow import Ui_Form
from RegisWindow import Ui_RegisWindow
from LogWindow import Ui_Login
from RegisSuccess import Ui_RegisSuccess
from ManageWindow import Ui_Console
import pymongo
import time

Sorts = []
DBHeaderLabels = ['name', 'want', 'phone', 'mail']
# DBHeaderLabels = ['name', 'amount', 'want', 'contact']
TableHeaderLabels = ['物品', 'Wants', '手机号', '邮箱']


def insertObj(record):
    objCollection.insert_one(record)


def removeObj(record_id):
    myquery = {"_id": record_id}
    objCollection.delete_one(myquery)


def insertClient(record):
    clientCollection.insert_one(record)


def findUser_name(username):
    myquery = {"username": username}
    users = clientCollection.find(myquery)
    for user in users:
        return user

    return None


def findUser_status(status):
    myquery = {"isChecked": status}
    users = clientCollection.find(myquery)
    userSet = []
    for user in users:
        userSet.append(user)

    if userSet:
        return userSet
    else:
        return None


def updateSorts():
    global Sorts
    Sorts.clear()
    sorts = sortCollection.find({})
    for sort in sorts:
        Sorts.append(sort['name'])


def findSort(name):
    myquery = {"name": name}
    sorts = sortCollection.find(myquery)
    for sort in sorts:
        return sort

    return None


class DropInList(QListWidget):
    def __init__(self):
        super(DropInList, self).__init__()
        # 拖拽设置
        self.setAcceptDrops(True)   # 开启接受拖入事件
        self.setDragEnabled(True)   # 开启拖出功能
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 开启多选模式
        self.setDragDropMode(QAbstractItemView.DragDrop)            # 设置拖放
        self.setDefaultDropAction(Qt.MoveAction)                    # 设置拖放模式为移动


class UploadWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        # 继承父类响应的函数，在此为初始化函数
        super(UploadWindow, self).__init__(parent)
        # 加载UI模型
        self.setupUi(self)
        self.init_combobox()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.resize(600, 300)

    def init_combobox(self):
        updateSorts()
        box = self.comboBox
        box.clear()
        box.addItems(Sorts)


class RegisWindow(QMainWindow, Ui_RegisWindow):
    def __init__(self, parent=None):
        # 继承父类响应的函数，在此为初始化函数
        super(RegisWindow, self).__init__(parent)
        # 加载UI模型
        self.setupUi(self)
        self.hint.setText("")


class RegisSuccess(QMainWindow, Ui_RegisSuccess):
    def __init__(self, parent=None):
        # 继承父类响应的函数，在此为初始化函数
        super(RegisSuccess, self).__init__(parent)
        # 加载UI模型
        self.setupUi(self)


class LoginWindow(QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        # 继承父类响应的函数，在此为初始化函数
        super(LoginWindow, self).__init__(parent)
        # 加载UI模型
        self.setupUi(self)
        self.hint.setText("")


class ManageWindow(QMainWindow, Ui_Console):
    def __init__(self, parent=None):
        # 继承父类响应的函数，在此为初始化函数
        super(ManageWindow, self).__init__(parent)
        # 加载UI模型
        self.passedUsers = None
        self.notPassUsers = None
        self.setupUi(self)
        self.hint.setText("")
        # self.ini_lists()

    def ini_lists(self):
        self.notPassUsers = DropInList()
        self.notPassUsers.setObjectName("notPassUsers")
        self.gridLayout_4.addWidget(self.notPassUsers, 1, 0, 1, 1)
        self.passedUsers = DropInList()
        self.passedUsers.setObjectName("passedUsers")
        self.gridLayout_4.addWidget(self.passedUsers, 1, 1, 1, 1)
        
        passList = self.passedUsers
        notpassList = self.notPassUsers

        passUsers = findUser_status(1)
        notpassUsers = findUser_status(0)

        if passUsers is None:
            passList.clear()
        else:
            for user in passUsers:
                info = user['username'] + ':' + user['address']
                passList.addItem(info)

        if notpassUsers is None:
            notpassList.clear()
        else:
            for user in notpassUsers:
                info = user['username'] + ':' + user['address']
                notpassList.addItem(info)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # 继承父类响应的函数，在此为初始化函数
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 初始化按钮与Slot的通信
        self.init_table()
        self.init_combobox()
        self.hint.setText("左键任意记录可显示详细信息, 右键可删除用户自己上传的记录")

    def init_table(self):
        table = self.tableWidget
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(TableHeaderLabels)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)  # 设置第三列自适应宽度
        table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)

    def init_combobox(self):
        updateSorts()
        box = self.comboBox
        box.clear()
        box.addItems(Sorts)


class WindowCtl:
    def __init__(self):
        self.mainWindow = MainWindow()
        self.uploadWindow = UploadWindow()
        self.loginWindow = LoginWindow()
        self.regisWindow = RegisWindow()
        self.regisSuccess = RegisSuccess()
        self.manageWindow = ManageWindow()
        self.init_slots()
        self.CurrentTableRecordsID = []
        self.CurrentClient = None

    def init_window(self):
        self.regisWindow.hide()
        self.mainWindow.hide()
        self.mainWindow.manage.hide()
        self.uploadWindow.hide()
        self.regisSuccess.hide()
        self.manageWindow.hide()
        self.loginWindow.show()
        self.updateTable()

    def init_slots(self):
        self.mainWindow.Upload.clicked.connect(self.upload)
        self.mainWindow.Search.clicked.connect(self.search)
        self.mainWindow.tableWidget.itemClicked.connect(self.showDetail)
        self.mainWindow.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)             # 允许打开上下文菜单
        self.mainWindow.tableWidget.customContextMenuRequested.connect(self.generateTableMenu)  # 绑定右键事件
        self.mainWindow.comboBox.currentIndexChanged.connect(self.comboBoxSelectionChange)
        self.mainWindow.manage.clicked.connect(self.manageInfo)

        self.uploadWindow.Confirm.clicked.connect(self.uploadConfirm)
        self.uploadWindow.Cancel.clicked.connect(self.uploadCancel)
        self.uploadWindow.comboBox.currentIndexChanged.connect(self.updateUploadInfo)

        self.loginWindow.login.clicked.connect(self.login)
        self.loginWindow.regis.clicked.connect(self.register)

        self.regisWindow.regConfirm.clicked.connect(self.regConfirm)
        self.regisWindow.regCancel.clicked.connect(self.regCancel)

        self.manageWindow.addSort.clicked.connect(self.addSort)
        self.manageWindow.delSort.clicked.connect(self.delSort)
        self.manageWindow.sortsBox.currentIndexChanged.connect(self.updateSortDetail)
        self.manageWindow.manageDone.clicked.connect(self.manageDone)

    def addSort(self):
        name = self.manageWindow.sortName.text()
        info = self.manageWindow.sortInfo.text()
        name.replace(" ", "")
        info.replace(" ", "")

        if name == "" or info == "":
            self.manageWindow.hint.setText("请输入完整的类别信息")
            return

        if findSort(name) is None:
            one_sort = {
                "name": name, "info": info
            }

            sortCollection.insert_one(one_sort)
            self.manageWindow.hint.setText("成功添加类别 [%s]" % name)
            updateSorts()
            print(Sorts)
            self.manageWindow.sortsBox.clear()
            self.manageWindow.sortsBox.addItems(Sorts)
        else:
            self.manageWindow.hint.setText("类别 [%s] 似乎已经添加过了捏~(￣▽￣)~*" % name)

    def delSort(self):
        name = self.manageWindow.sortsBox.currentText()
        myquery = {"name": name}
        sortCollection.delete_one(myquery)
        self.manageWindow.hint.setText("成功删除类别 [%s]" % name)

        updateSorts()
        self.manageWindow.sortsBox.clear()
        self.manageWindow.sortsBox.addItems(Sorts)

        self.updateSortDetail()

    def updateSortDetail(self):
        name = self.manageWindow.sortsBox.currentText()
        if name != '':
            sort = findSort(name)

            self.manageWindow.sortName.setText(sort['name'])
            self.manageWindow.sortInfo.setText(sort['info'])

    def manageUsers(self):
        passUsersName = []
        notpassUsersName = []

        for i in range(self.manageWindow.notPassUsers.count()):
            name = self.manageWindow.notPassUsers.item(i).text()
            notpassUsersName.append(name.split(':')[0])

        for i in range(self.manageWindow.passedUsers.count()):
            name = self.manageWindow.passedUsers.item(i).text()
            passUsersName.append(name.split(':')[0])

        for name in passUsersName:
            clientCollection.update_one({"username": name}, {"$set": {"isChecked": 1}})

        for name in notpassUsersName:
            clientCollection.update_one({"username": name}, {"$set": {"isChecked": 0}})

        # print(passUsersName)
        # print(notpassUsersName)

    def manageDone(self):
        # 更新主窗口sortBox的信息
        self.mainWindow.init_combobox()
        # 更新用户审核状态
        self.manageUsers()
        self.manageWindow.hide()

    def manageInfo(self):
        self.manageWindow.show()
        # 更新sortsBox
        self.manageWindow.sortsBox.clear()
        self.manageWindow.sortsBox.addItems(Sorts)
        # 更新lists
        self.manageWindow.ini_lists()

    def login(self):
        username = self.loginWindow.logName.text()
        password = self.loginWindow.logPassword.text()
        username.replace(" ", "")
        password.replace(" ", "")
        if username == "" or password == "":
            self.loginWindow.hint.setText("请先将信息填写完整")
            return

        user = findUser_name(username)

        if user is not None:
            if password == user["password"]:
                if user['isChecked'] == 0:
                    self.loginWindow.hint.setText('用户审核还未通过，请耐心等待')
                elif user['isChecked'] == 1:
                    if user['username'] == 'admin':
                        self.mainWindow.manage.show()
                    self.mainWindow.username.setText(user['username'])
                    self.loginWindow.hide()
                    self.mainWindow.show()
                    self.CurrentClient = user
            else:
                self.loginWindow.hint.setText('用户名或密码错误')
        else:
            self.loginWindow.hint.setText('用户不存在')

    def register(self):
        self.regisWindow.show()

    def clearRegisInformation(self):
        self.regisWindow.name.setText("")
        self.regisWindow.password.setText("")
        self.regisWindow.password_2.setText("")
        self.regisWindow.phone.setText("")
        self.regisWindow.mail.setText("")
        self.regisWindow.address.setText("")
        self.regisWindow.hint.setText("")

    def regConfirm(self):
        username = self.regisWindow.name.text()
        password = self.regisWindow.password.text()
        password_2 = self.regisWindow.password_2.text()
        phone = self.regisWindow.phone.text()
        mail = self.regisWindow.mail.text()
        address = self.regisWindow.address.text()
        username.replace(" ", "")
        password.replace(" ", "")
        password_2.replace(" ", "")
        phone.replace(" ", "")
        mail.replace(" ", "")
        address.replace(" ", "")

        if username == "" or password == "" or password_2 == "" or phone == "" or mail == "" or address == "":
            self.regisWindow.hint.setText("请先将信息填写完整")
            return

        if password_2 != password:
            self.regisWindow.hint.setText("两次输入密码不同")
            return

        user = findUser_name(username)

        if user is not None:
            self.regisWindow.hint.setText("该用户名已被使用")
            return

        one_user = {
            "username": username, "password": password, "phone": phone, "mail": mail, "address": address, "isChecked": 0
        }

        insertClient(one_user)

        self.clearRegisInformation()
        self.regisWindow.hide()
        self.regisSuccess.show()

    def regCancel(self):
        self.clearRegisInformation()
        self.regisWindow.hide()

    def comboBoxSelectionChange(self):
        self.updateTable()

    def clearTable(self):
        table = self.mainWindow.tableWidget

        row = table.rowCount()
        while row != -1:
            table.removeRow(row - 1)
            row -= 1

    def updateTable(self, DB_changed=True, limitation=None):
        # update for upload new records
        if DB_changed:
            self.clearTable()

            sort = self.mainWindow.comboBox.currentText()

            myquery = {"sort": sort}
            records = objCollection.find(myquery)
            self.CurrentTableRecordsID.clear()
            # print(self.CurrentTableRecordsID)

            for record in records:
                self.CurrentTableRecordsID.append(record['_id'])
                row = self.mainWindow.tableWidget.rowCount()
                self.mainWindow.tableWidget.insertRow(row)
                for j in range(4):
                    text = record[DBHeaderLabels[j]]
                    item = QTableWidgetItem(text)
                    self.mainWindow.tableWidget.setItem(row, j, item)

            # print(self.CurrentTableRecordsID)

        # update for search records
        if limitation is not None:
            self.clearTable()

            myquery = {"name": limitation}
            records = objCollection.find(myquery)
            self.CurrentTableRecordsID.clear()
            # print(self.CurrentTableRecordsID)

            for record in records:
                self.CurrentTableRecordsID.append(record['_id'])
                row = self.mainWindow.tableWidget.rowCount()
                self.mainWindow.tableWidget.insertRow(row)
                for j in range(4):
                    text = record[DBHeaderLabels[j]]
                    item = QTableWidgetItem(text)
                    self.mainWindow.tableWidget.setItem(row, j, item)

            # print(type(self.CurrentTableRecordsID[0]))

    def generateTableMenu(self, pos):
        # 获取点击行号
        for i in self.mainWindow.tableWidget.selectionModel().selection().indexes():
            rowNum = i.row()

        menu = QMenu()
        item1 = menu.addAction("删除")

        # 转换坐标系
        screenPos = self.mainWindow.tableWidget.mapToGlobal(pos)

        # 被阻塞
        action = menu.exec(screenPos)
        if action == item1:
            self.delete(rowNum)
        else:
            return

    def showDetail(self, index):
        _id = self.CurrentTableRecordsID[index.row()]
        myquery = {"_id": _id}
        obj = objCollection.find_one(myquery)
        infoSet = obj['info'].split(';')
        currentSort = obj['sort']
        sort = findSort(currentSort)
        sortInfoSet = sort['info'].split(';')
        detailInfo = obj['name'] + ' '

        for i in range(len(sortInfoSet)):
            detailInfo = detailInfo + sortInfoSet[i] + ':' + infoSet[i] + ' '

        self.mainWindow.hint.setText(detailInfo)
        # print(sortInfoSet)
        # print(infoSet)

    def search(self):
        name = self.mainWindow.lineEdit.text()
        if name == '':
            self.updateTable()
        else:
            self.updateTable(False, name)

    def upload(self):
        self.uploadWindow.show()
        self.uploadWindow.hint.setText('请选择你要上传的物品类型')

    def updateUploadInfo(self):
        sortName = self.uploadWindow.comboBox.currentText()
        sort = findSort(sortName)

        self.uploadWindow.hint.setText('详细信息为 [%s] \n信息之间为英文分号(;)\n结尾不用加分号哦(● ◡ ●)' % sort['info'])

    def uploadConfirm(self):
        sort = self.uploadWindow.comboBox.currentText()
        obj = self.uploadWindow.name.text()
        want = self.uploadWindow.want.text()
        info = self.uploadWindow.info.text()

        one_record = {
            "sort": sort, "name": obj, "want": want, "phone": self.CurrentClient['phone'],
            "mail": self.CurrentClient['mail'], "info": info
        }

        print(one_record)

        insertObj(one_record)

        self.updateTable()

        self.uploadWindow.name.setText("")
        self.uploadWindow.want.setText("")
        self.uploadWindow.info.setText("")

        self.uploadWindow.hide()

    def uploadCancel(self):
        self.uploadWindow.hide()

    def delete(self, index):
        _id = self.CurrentTableRecordsID[index]
        myquery = {"_id": _id}
        obj = objCollection.find_one(myquery)

        if obj['phone'] == self.CurrentClient['phone']:
            removeObj(_id)

            # print('delete')
            # print(self.DeleteRecordID)

            self.updateTable()

            self.mainWindow.hint.setText("成功删除记录")
        else:
            self.mainWindow.hint.setText("您没有权限删除其他用户上传的记录")


if __name__ == "__main__":
    myClient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myClient['Test']
    objCollection = mydb['Objs']
    clientCollection = mydb['Clients']
    sortCollection = mydb['Sorts']

    # res = clientCollection.delete_many({})  # clear all records
    # res = objCollection.delete_many({})

    app = QApplication(sys.argv)
    ctl = WindowCtl()
    ctl.init_window()
    sys.exit(app.exec_())
