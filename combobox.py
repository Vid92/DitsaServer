# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ComboBoxDelegate(QtWidgets.QStyledItemDelegate):
	def __init__(self,parent=None):
		super(ComboBoxDelegate, self).__init__()
		self.parent = parent

		self.part = list()
		self.general = ["1-16","17-32","33-48","49-64","65-80","81-96","97-112","113-128","129-144","145-160","161-176","177-192","193-208","209-224","225-240","241-256","257-272","273-288","289-304","305-320","321-336","337-352","353-368","369-384","385-400","401-416","417-432","433-448","449-464","465-480"]
	
	def createEditor(self, parent, option, index):
		cb = QtWidgets.QComboBox(parent)
		
		if len(self.part) < len(self.parent.listHostname):
			for i in range(len(self.parent.listHostname)):
				self.part.append(self.general[i])

		cb.addItems(self.part)
		return cb

	def setEditorData(self, editor, index):
		cbIndex = index.model().data(index,QtCore.Qt.EditRole)
		if cbIndex!=None:
			editor.setCurrentText(cbIndex)
			#print("cbIndex:",cbIndex)

	def setModelData(self,editor,model,index):
		model.setData(index,editor.currentText(),QtCore.Qt.EditRole)


