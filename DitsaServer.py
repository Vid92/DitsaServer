# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DitsaServer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess
import time

from combobox import ComboBoxDelegate

class Ui_DitsaServer(object):
	def __init__(self,MainWindowSer, parent=None):
		object.__init__(parent)
	#def setupUi(self, MainWindow):
		MainWindowSer.setObjectName("MainWindowSer")
		MainWindowSer.setFixedSize(371, 421)
		MainWindowSer.setToolTip("")
		MainWindowSer.setToolTipDuration(2)
		self.centralWidget = QtWidgets.QWidget(MainWindowSer)
		self.centralWidget.setObjectName("centralWidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
		self.gridLayout.setContentsMargins(11, 11, 11, 11)
		self.gridLayout.setSpacing(6)
		self.gridLayout.setObjectName("gridLayout")
		self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
		self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
		self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget.setShowGrid(True)
		self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
		self.tableWidget.setWordWrap(True)
		self.tableWidget.setCornerButtonEnabled(False)
		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.horizontalHeader().setVisible(True)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(172)
		self.tableWidget.verticalHeader().setVisible(False)
		
	#	form = Ui_Form(self)
	#	self.gridLayout.addWidget(form, 0, 0, 1, 1)
		self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
		
		self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
		#self.progressBar.setProperty("value", 24)
		self.progressBar.setObjectName("progressBar")
		self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)

		MainWindowSer.setCentralWidget(self.centralWidget)
		self.mainToolBar = QtWidgets.QToolBar(MainWindowSer)
		self.mainToolBar.setObjectName("mainToolBar")
		MainWindowSer.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
		self.statusBar = QtWidgets.QStatusBar(MainWindowSer)
		self.statusBar.setObjectName("statusBar")
		MainWindowSer.setStatusBar(self.statusBar)

		self.actionSave = QtWidgets.QAction(QtGui.QIcon('/home/ditsa/Prueba/DitsaServer/image/guardar.png'),'Save',MainWindowSer)
		self.actionUpdateHost = QtWidgets.QAction(QtGui.QIcon('/home/ditsa/Prueba/DitsaServer/image/ethernet.png'),'UpdateHost',MainWindowSer)

		self.mainToolBar.addAction(self.actionUpdateHost)
		self.mainToolBar.addAction(self.actionSave)

		self.retranslateUi(MainWindowSer)
		QtCore.QMetaObject.connectSlotsByName(MainWindowSer)

		self.tableWidget.setHorizontalHeaderLabels(('Hostname','Assigned Address'))

		MainWindowSer.showEvent = self.showEvent
		MainWindowSer.closeEvent = self.closeEvent

		self.hostname = ['ditsaServer1','ditsaServer2','ditsaServer3','ditsaServer4','ditsaServer5','ditsaServer6','ditsaServer7','distaServer8','ditsaServer9','ditsaServer10','ditsaServer11','ditsaServer12','ditsaServer13','ditsaServer14','ditsaServer15','ditsaServer16','ditsaServer17','ditsaServer18','ditsaServer19','ditsaServer20','ditsaServer21','ditsaServer22','ditsaServer23','ditsaServer24','ditsaServer25','ditsaServer26','ditsaServer27','ditsaServer28','ditsaServer29','ditsaServer30'] #raspberrypi
		self.listHostname = list()
		self.tmprow = list()

		self.flagEmpty = False
		self.flagSave = False
		self.flagBtn = False
		self.actionSave.triggered.connect(self.on_actionsave)
		self.actionUpdateHost.triggered.connect(self.pingHostname)

		self.MainWindowSer = MainWindowSer

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Ditsa Server"))
	#	self.tableWidget.setSortingEnabled(False)

	def showEvent(self,event):
		print("showEvent")

	def closeEvent(self,event):
		print("closeEvent")
		if self.flagSave != True and self.flagBtn!= False:
			msg = QtWidgets.QMessageBox()
			returnExit = msg.warning(self.MainWindowSer,'Warning',"Do you want to save changes in this file?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Cancel)

			if returnExit == msg.Yes:
				self.on_actionsave()
				if self.flagEmpty != False:
					event.ignore()
				time.sleep(1)
			elif returnExit == msg.No:
				MainWindowSer.close()
			elif returnExit == msg.Cancel:
				event.ignore()

	def pingHostname(self):
		self.flagBtn = True
		self.count = 0
		self.listHostname.clear()
		self.tableWidget.clearContents()
		self.progressBar.setFormat("Finding ...")

		n = len(self.hostname)
		self.percentage = 100.0 / float(n)

		self.progressBar.setValue(self.count)
		time.sleep(1)

		j = 0
		for i in range(n):
			QtGui.QGuiApplication.processEvents()	
			response = os.system("ping -c 1 " + self.hostname[i]+".local") #comando para consola
			#self.response = subprocess.Popen("ping -c 1 "+self.hostname[i]+".local",shell = True,stdout = subprocess.PIPE).stdout.read()
			#self.response = subprocess.call(["ping", "-c 1 ",self.hostname[i]+".local"])
			#self.response = subprocess.Popen(["ping", "-c 1 ",self.hostname[i]+".local"])
		#	salida = response.stdout.read()
		#	response.stdout.close()
		#	salida = salida.decode(sys.getdefaultencoding())
			# and then check the response...
		#	print("response:",self.response)

			self.count += self.percentage
			self.progressBar.setValue(self.count)
		
			if response == 0:
				j+=1
				self.listHostname.append(self.hostname[i])	
				self.tableWidget.setRowCount(j)
				self.itemAddr()

				for k in range(len(self.listHostname)):
					self.tabItem(self.listHostname[k],j-1,0)

		self.progressBar.setValue(100)
		self.progressBar.setFormat("Ready!")

		for x in range(len(self.listHostname)):
			itm = QtWidgets.QTableWidgetItem()			
			itm.setBackground(QtGui.QColor("white"))
			self.tableWidget.setItem(x,1,itm)
		
	def tabItem(self,name,rw,col):
		lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
		item = QtWidgets.QTableWidgetItem(name)
		item.setTextAlignment(QtCore.Qt.AlignCenter)
		item.setFont(lblt)
		#item.setBackground(QtGui.QColor('lightblue'))
		item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
		self.tableWidget.setItem(rw,col,item)

		itm = QtWidgets.QTableWidgetItem("---")
		itm.setTextAlignment(QtCore.Qt.AlignCenter)
		itm.setBackground(QtGui.QColor("lightgray"))
		itm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
		self.tableWidget.setItem(rw,1,itm)

	def itemAddr(self):
		self.cbid = ComboBoxDelegate(self)
		self.tableWidget.setItemDelegateForColumn(1,self.cbid)

	def on_actionsave(self):
		print("Save")
		if self.flagBtn != False: 
			self.flagEmpty = False
			self.tmprow.clear()
			row = self.tableWidget.rowCount()
			msg = QtWidgets.QMessageBox()

			for i in range(row):
				for j in range(2):
					data = self.tableWidget.item(i,j)
					if data != None:
						x = data.text()
						self.tmprow.append(x)
					
					if j == 1 and data == None:
						self.tmprow.clear()
						self.flagEmpty = True
						print("renglon vacio!!")
						msg.critical(self.MainWindowSer,'Error',"Cannot save program empty or incomplete")
			
			if self.flagEmpty != True:
				print("tmprow:",self.tmprow)
				self.flagSave = True
				settings = QtCore.QSettings('/home/ditsa/DitsaNet/Settings/ServerConfig.ini', QtCore.QSettings.NativeFormat)
				settings.setValue("servers",self.tmprow)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindowSer = QtWidgets.QMainWindow()
	ui = Ui_DitsaServer(MainWindowSer)
	#ui.setupUi(MainWindow)
	MainWindowSer.show()
	sys.exit(app.exec_())
