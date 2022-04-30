# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'netAssitui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NetAssist(object):
    def setupUi(self, NetAssist):
        NetAssist.setObjectName("NetAssist")
        NetAssist.resize(821, 702)
        self.centralwidget = QtWidgets.QWidget(NetAssist)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.RecvSettings = QtWidgets.QGroupBox(self.centralwidget)
        self.RecvSettings.setMaximumSize(QtCore.QSize(221, 16777215))
        self.RecvSettings.setObjectName("RecvSettings")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.RecvSettings)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.recv2file = QtWidgets.QCheckBox(self.RecvSettings)
        self.recv2file.setObjectName("recv2file")
        self.gridLayout_4.addWidget(self.recv2file, 0, 0, 1, 2)
        self.newline = QtWidgets.QCheckBox(self.RecvSettings)
        self.newline.setObjectName("newline")
        self.gridLayout_4.addWidget(self.newline, 1, 0, 1, 2)
        self.timestamp = QtWidgets.QCheckBox(self.RecvSettings)
        self.timestamp.setObjectName("timestamp")
        self.gridLayout_4.addWidget(self.timestamp, 2, 0, 1, 2)
        self.stopdsp = QtWidgets.QCheckBox(self.RecvSettings)
        self.stopdsp.setObjectName("stopdsp")
        self.gridLayout_4.addWidget(self.stopdsp, 4, 0, 1, 1)
        self.save_btn = QtWidgets.QPushButton(self.RecvSettings)
        self.save_btn.setObjectName("save_btn")
        self.gridLayout_4.addWidget(self.save_btn, 5, 0, 1, 1)
        self.hex_recv = QtWidgets.QCheckBox(self.RecvSettings)
        self.hex_recv.setObjectName("hex_recv")
        self.gridLayout_4.addWidget(self.hex_recv, 3, 0, 1, 2)
        self.clr_btn = QtWidgets.QPushButton(self.RecvSettings)
        self.clr_btn.setObjectName("clr_btn")
        self.gridLayout_4.addWidget(self.clr_btn, 5, 1, 1, 1)
        self.gridLayout_9.addWidget(self.RecvSettings, 1, 0, 1, 1)
        self.NetSettings = QtWidgets.QGroupBox(self.centralwidget)
        self.NetSettings.setMaximumSize(QtCore.QSize(221, 16777215))
        self.NetSettings.setObjectName("NetSettings")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.NetSettings)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.prot_lb = QtWidgets.QLabel(self.NetSettings)
        self.prot_lb.setObjectName("prot_lb")
        self.gridLayout_5.addWidget(self.prot_lb, 0, 0, 1, 1)
        self.prot_box = QtWidgets.QComboBox(self.NetSettings)
        self.prot_box.setEditable(False)
        self.prot_box.setObjectName("prot_box")
        self.prot_box.addItem("")
        self.prot_box.addItem("")
        self.prot_box.addItem("")
        self.gridLayout_5.addWidget(self.prot_box, 1, 0, 1, 2)
        self.localip_lb = QtWidgets.QLabel(self.NetSettings)
        self.localip_lb.setObjectName("localip_lb")
        self.gridLayout_5.addWidget(self.localip_lb, 2, 0, 1, 1)
        self.Localip_lineedit = QtWidgets.QLineEdit(self.NetSettings)
        self.Localip_lineedit.setObjectName("Localip_lineedit")
        self.gridLayout_5.addWidget(self.Localip_lineedit, 3, 0, 1, 2)
        self.localport_lb = QtWidgets.QLabel(self.NetSettings)
        self.localport_lb.setOpenExternalLinks(False)
        self.localport_lb.setObjectName("localport_lb")
        self.gridLayout_5.addWidget(self.localport_lb, 4, 0, 1, 1)
        self.Localport_lineedit = QtWidgets.QLineEdit(self.NetSettings)
        self.Localport_lineedit.setObjectName("Localport_lineedit")
        self.gridLayout_5.addWidget(self.Localport_lineedit, 5, 0, 1, 2)
        self.open_btn = QtWidgets.QPushButton(self.NetSettings)
        self.open_btn.setObjectName("open_btn")
        self.gridLayout_5.addWidget(self.open_btn, 6, 0, 1, 1)
        self.close_btn = QtWidgets.QPushButton(self.NetSettings)
        self.close_btn.setObjectName("close_btn")
        self.gridLayout_5.addWidget(self.close_btn, 6, 1, 1, 1)
        self.gridLayout_9.addWidget(self.NetSettings, 0, 0, 1, 1)
        self.SendSettings = QtWidgets.QGroupBox(self.centralwidget)
        self.SendSettings.setMaximumSize(QtCore.QSize(221, 16777215))
        self.SendSettings.setObjectName("SendSettings")
        self.gridLayout = QtWidgets.QGridLayout(self.SendSettings)
        self.gridLayout.setObjectName("gridLayout")
        self.file_send_btn = QtWidgets.QPushButton(self.SendSettings)
        self.file_send_btn.setObjectName("file_send_btn")
        self.gridLayout.addWidget(self.file_send_btn, 6, 0, 1, 2)
        self.chk_send_after_receive = QtWidgets.QCheckBox(self.SendSettings)
        self.chk_send_after_receive.setObjectName("chk_send_after_receive")
        self.gridLayout.addWidget(self.chk_send_after_receive, 4, 0, 1, 1)
        self.ms_lbl = QtWidgets.QLabel(self.SendSettings)
        self.ms_lbl.setObjectName("ms_lbl")
        self.gridLayout.addWidget(self.ms_lbl, 5, 3, 1, 1)
        self.Sendloop = QtWidgets.QCheckBox(self.SendSettings)
        self.Sendloop.setObjectName("Sendloop")
        self.gridLayout.addWidget(self.Sendloop, 5, 0, 1, 1)
        self.Sendclear = QtWidgets.QCheckBox(self.SendSettings)
        self.Sendclear.setObjectName("Sendclear")
        self.gridLayout.addWidget(self.Sendclear, 2, 0, 1, 3)
        self.Sendcheck = QtWidgets.QCheckBox(self.SendSettings)
        self.Sendcheck.setObjectName("Sendcheck")
        self.gridLayout.addWidget(self.Sendcheck, 1, 0, 1, 3)
        self.file_load = QtWidgets.QCheckBox(self.SendSettings)
        self.file_load.setObjectName("file_load")
        self.gridLayout.addWidget(self.file_load, 0, 0, 1, 2)
        self.loopinterval = QtWidgets.QLineEdit(self.SendSettings)
        self.loopinterval.setObjectName("loopinterval")
        self.gridLayout.addWidget(self.loopinterval, 5, 2, 1, 1)
        self.clr_btn2 = QtWidgets.QPushButton(self.SendSettings)
        self.clr_btn2.setObjectName("clr_btn2")
        self.gridLayout.addWidget(self.clr_btn2, 6, 2, 1, 2)
        self.hex_send = QtWidgets.QCheckBox(self.SendSettings)
        self.hex_send.setObjectName("hex_send")
        self.gridLayout.addWidget(self.hex_send, 3, 0, 1, 3)
        self.gridLayout_9.addWidget(self.SendSettings, 2, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_9)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.Datarecv = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Datarecv.sizePolicy().hasHeightForWidth())
        self.Datarecv.setSizePolicy(sizePolicy)
        self.Datarecv.setMinimumSize(QtCore.QSize(0, 450))
        self.Datarecv.setObjectName("Datarecv")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Datarecv)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.DataRecvtext = QtWidgets.QTextBrowser(self.Datarecv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.DataRecvtext.sizePolicy().hasHeightForWidth())
        self.DataRecvtext.setSizePolicy(sizePolicy)
        self.DataRecvtext.setReadOnly(True)
        self.DataRecvtext.setObjectName("DataRecvtext")
        self.gridLayout_3.addWidget(self.DataRecvtext, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clients_lbl = QtWidgets.QLabel(self.Datarecv)
        self.clients_lbl.setObjectName("clients_lbl")
        self.horizontalLayout.addWidget(self.clients_lbl)
        self.clients_list = QtWidgets.QComboBox(self.Datarecv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clients_list.sizePolicy().hasHeightForWidth())
        self.clients_list.setSizePolicy(sizePolicy)
        self.clients_list.setEditable(False)
        self.clients_list.setObjectName("clients_list")
        self.horizontalLayout.addWidget(self.clients_list)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.remoteip_lbl = QtWidgets.QLabel(self.Datarecv)
        self.remoteip_lbl.setObjectName("remoteip_lbl")
        self.horizontalLayout_2.addWidget(self.remoteip_lbl)
        self.remoteip_text = QtWidgets.QLineEdit(self.Datarecv)
        self.remoteip_text.setObjectName("remoteip_text")
        self.horizontalLayout_2.addWidget(self.remoteip_text)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.remoteport_lbl = QtWidgets.QLabel(self.Datarecv)
        self.remoteport_lbl.setObjectName("remoteport_lbl")
        self.horizontalLayout_3.addWidget(self.remoteport_lbl)
        self.remoteport_text = QtWidgets.QLineEdit(self.Datarecv)
        self.remoteport_text.setObjectName("remoteport_text")
        self.horizontalLayout_3.addWidget(self.remoteport_text)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.gridLayout_10.addWidget(self.Datarecv, 0, 0, 1, 1)
        self.Datasend = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Datasend.sizePolicy().hasHeightForWidth())
        self.Datasend.setSizePolicy(sizePolicy)
        self.Datasend.setMinimumSize(QtCore.QSize(550, 0))
        self.Datasend.setObjectName("Datasend")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Datasend)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.DataSendtext = QtWidgets.QTextBrowser(self.Datasend)
        self.DataSendtext.setReadOnly(False)
        self.DataSendtext.setObjectName("DataSendtext")
        self.horizontalLayout_4.addWidget(self.DataSendtext)
        self.send_Btn = QtWidgets.QPushButton(self.Datasend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_Btn.sizePolicy().hasHeightForWidth())
        self.send_Btn.setSizePolicy(sizePolicy)
        self.send_Btn.setObjectName("send_Btn")
        self.horizontalLayout_4.addWidget(self.send_Btn)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.Datasend, 1, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_10)
        NetAssist.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NetAssist)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 23))
        self.menubar.setObjectName("menubar")
        NetAssist.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NetAssist)
        self.statusbar.setObjectName("statusbar")
        NetAssist.setStatusBar(self.statusbar)

        self.retranslateUi(NetAssist)
        self.prot_box.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NetAssist)

    def retranslateUi(self, NetAssist):
        _translate = QtCore.QCoreApplication.translate
        NetAssist.setWindowTitle(_translate("NetAssist", "NetAssist"))
        self.RecvSettings.setTitle(_translate("NetAssist", "接收区设置"))
        self.recv2file.setText(_translate("NetAssist", "保存数据到文件"))
        self.newline.setText(_translate("NetAssist", "自动换行显示"))
        self.timestamp.setText(_translate("NetAssist", "显示接收时间"))
        self.stopdsp.setText(_translate("NetAssist", "暂停显示"))
        self.save_btn.setText(_translate("NetAssist", "保存数据"))
        self.hex_recv.setText(_translate("NetAssist", "16进制显示"))
        self.clr_btn.setText(_translate("NetAssist", "清空显示"))
        self.NetSettings.setTitle(_translate("NetAssist", "网络设置"))
        self.prot_lb.setText(_translate("NetAssist", "1.协议类型"))
        self.prot_box.setItemText(0, _translate("NetAssist", "TCP Server"))
        self.prot_box.setItemText(1, _translate("NetAssist", "TCP Client"))
        self.prot_box.setItemText(2, _translate("NetAssist", "UDP"))
        self.localip_lb.setText(_translate("NetAssist", "2.本地IP地址"))
        self.Localip_lineedit.setText(_translate("NetAssist", "127.0.0.1"))
        self.localport_lb.setText(_translate("NetAssist", "3.本地端口号"))
        self.Localport_lineedit.setText(_translate("NetAssist", "8888"))
        self.open_btn.setText(_translate("NetAssist", "开始监听"))
        self.close_btn.setText(_translate("NetAssist", "断开"))
        self.SendSettings.setTitle(_translate("NetAssist", "发送设置"))
        self.file_send_btn.setText(_translate("NetAssist", "发送文件"))
        self.chk_send_after_receive.setText(_translate("NetAssist", "收到数据后发送"))
        self.ms_lbl.setText(_translate("NetAssist", "ms"))
        self.Sendloop.setText(_translate("NetAssist", "周期发送"))
        self.Sendclear.setText(_translate("NetAssist", "发送完自动清空"))
        self.Sendcheck.setText(_translate("NetAssist", "自动发送附加位"))
        self.file_load.setText(_translate("NetAssist", "载入文件"))
        self.clr_btn2.setText(_translate("NetAssist", "清空显示"))
        self.hex_send.setText(_translate("NetAssist", "16进制发送"))
        self.Datarecv.setTitle(_translate("NetAssist", "网络数据接收"))
        self.clients_lbl.setText(_translate("NetAssist", "客户端:"))
        self.remoteip_lbl.setText(_translate("NetAssist", "远程IP"))
        self.remoteport_lbl.setText(_translate("NetAssist", "端口号"))
        self.Datasend.setTitle(_translate("NetAssist", "数据发送"))
        self.send_Btn.setText(_translate("NetAssist", "发送"))
