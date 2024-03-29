# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1930, 1077)
        self.home_widget = QtWidgets.QWidget(MainWindow)
        self.home_widget.setObjectName("home_widget")
        self.label_header_home = QtWidgets.QLabel(self.home_widget)
        self.label_header_home.setGeometry(QtCore.QRect(0, 0, 1941, 211))
        self.label_header_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_header_home.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(2,0,36,1), stop:1 rgba(9,121,35,1), stop:2 rgba(0,212,255,1));\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_header_home.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_header_home.setObjectName("label_header_home")
        self.lineEdit_mes_header = QtWidgets.QLineEdit(self.home_widget)
        self.lineEdit_mes_header.setGeometry(QtCore.QRect(840, 50, 301, 61))
        self.lineEdit_mes_header.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_mes_header.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"font: 87 28pt \"Arial Black\";\n"
"border:none;\n"
"")
        self.lineEdit_mes_header.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_mes_header.setObjectName("lineEdit_mes_header")
        self.image_cifrao_header = QtWidgets.QTextBrowser(self.home_widget)
        self.image_cifrao_header.setGeometry(QtCore.QRect(1030, 20, 24, 24))
        self.image_cifrao_header.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image_cifrao_header.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/images_home/cifrao.png);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"")
        self.image_cifrao_header.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.image_cifrao_header.setObjectName("image_cifrao_header")
        self.label_entradas = QtWidgets.QLabel(self.home_widget)
        self.label_entradas.setGeometry(QtCore.QRect(340, 130, 211, 141))
        self.label_entradas.setStyleSheet("font: 14pt \"Sans Serif Collection\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(51, 51, 51);\n"
"border-radius:10px;")
        self.label_entradas.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_entradas.setIndent(16)
        self.label_entradas.setObjectName("label_entradas")
        self.lineEdit_entradas_valor = QtWidgets.QLineEdit(self.home_widget)
        self.lineEdit_entradas_valor.setGeometry(QtCore.QRect(360, 200, 181, 41))
        self.lineEdit_entradas_valor.setStyleSheet("background-color: transparent;\n"
"color: rgb(51, 51, 51);\n"
"\n"
"\n"
"\n"
"font: 18pt \"Arial Rounded MT Bold\";\n"
"border:none;")
        self.lineEdit_entradas_valor.setObjectName("lineEdit_entradas_valor")
        self.label_saidas = QtWidgets.QLabel(self.home_widget)
        self.label_saidas.setGeometry(QtCore.QRect(880, 130, 211, 141))
        self.label_saidas.setStyleSheet("font: 14pt \"Sans Serif Collection\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(51, 51, 51);\n"
"border-radius:10px;")
        self.label_saidas.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_saidas.setIndent(16)
        self.label_saidas.setObjectName("label_saidas")
        self.lineEdit_saidas_valor = QtWidgets.QLineEdit(self.home_widget)
        self.lineEdit_saidas_valor.setGeometry(QtCore.QRect(890, 200, 191, 41))
        self.lineEdit_saidas_valor.setStyleSheet("background-color: transparent;\n"
"color: rgb(51, 51, 51);\n"
"\n"
"\n"
"\n"
"font: 18pt \"Arial Rounded MT Bold\";\n"
"border:none;")
        self.lineEdit_saidas_valor.setObjectName("lineEdit_saidas_valor")
        self.label_total = QtWidgets.QLabel(self.home_widget)
        self.label_total.setGeometry(QtCore.QRect(1360, 130, 211, 141))
        self.label_total.setStyleSheet("font: 14pt \"Sans Serif Collection\";\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(246, 68, 68);")
        self.label_total.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_total.setIndent(16)
        self.label_total.setObjectName("label_total")
        self.lineEdit_total_valor = QtWidgets.QLineEdit(self.home_widget)
        self.lineEdit_total_valor.setGeometry(QtCore.QRect(1390, 200, 161, 41))
        self.lineEdit_total_valor.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"\n"
"font: 18pt \"Arial Rounded MT Bold\";\n"
"border:none;")
        self.lineEdit_total_valor.setObjectName("lineEdit_total_valor")
        self.image_cifrao_header_2 = QtWidgets.QTextBrowser(self.home_widget)
        self.image_cifrao_header_2.setGeometry(QtCore.QRect(1530, 160, 24, 24))
        self.image_cifrao_header_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image_cifrao_header_2.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/images_home/total.png);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"")
        self.image_cifrao_header_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.image_cifrao_header_2.setObjectName("image_cifrao_header_2")
        self.image_cifrao_header_3 = QtWidgets.QTextBrowser(self.home_widget)
        self.image_cifrao_header_3.setGeometry(QtCore.QRect(1050, 150, 24, 24))
        self.image_cifrao_header_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image_cifrao_header_3.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/images_home/down.png);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"")
        self.image_cifrao_header_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.image_cifrao_header_3.setObjectName("image_cifrao_header_3")
        self.image_cifrao_header_4 = QtWidgets.QTextBrowser(self.home_widget)
        self.image_cifrao_header_4.setGeometry(QtCore.QRect(510, 160, 24, 24))
        self.image_cifrao_header_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image_cifrao_header_4.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/images_home/up.png);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"")
        self.image_cifrao_header_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.image_cifrao_header_4.setObjectName("image_cifrao_header_4")
        self.textEdit_Doc = QtWidgets.QTextEdit(self.home_widget)
        self.textEdit_Doc.setGeometry(QtCore.QRect(580, 350, 821, 71))
        self.textEdit_Doc.setObjectName("textEdit_Doc")
        self.lineEdit_mes_header_2 = QtWidgets.QLineEdit(self.home_widget)
        self.lineEdit_mes_header_2.setGeometry(QtCore.QRect(580, 290, 301, 61))
        self.lineEdit_mes_header_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_mes_header_2.setStyleSheet("background-color: transparent;\n"
"font: 22pt \"Sans Serif Collection\";\n"
"color: rgb(51, 51, 51);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"")
        self.lineEdit_mes_header_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_mes_header_2.setObjectName("lineEdit_mes_header_2")
        self.lineEdit_mes_header_3 = QtWidgets.QLineEdit(self.home_widget)
        self.lineEdit_mes_header_3.setGeometry(QtCore.QRect(580, 440, 301, 61))
        self.lineEdit_mes_header_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_mes_header_3.setStyleSheet("background-color: transparent;\n"
"font: 22pt \"Sans Serif Collection\";\n"
"color: rgb(51, 51, 51);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"")
        self.lineEdit_mes_header_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_mes_header_3.setObjectName("lineEdit_mes_header_3")
        self.textEdit_Cliente = QtWidgets.QTextEdit(self.home_widget)
        self.textEdit_Cliente.setGeometry(QtCore.QRect(580, 500, 821, 71))
        self.textEdit_Cliente.setObjectName("textEdit_Cliente")
        self.textEdit_formaPagamento = QtWidgets.QTextEdit(self.home_widget)
        self.textEdit_formaPagamento.setGeometry(QtCore.QRect(570, 650, 821, 71))
        self.textEdit_formaPagamento.setObjectName("textEdit_formaPagamento")
        self.lineEdit_mes_header_4 = QtWidgets.QLineEdit(self.home_widget)
        self.lineEdit_mes_header_4.setGeometry(QtCore.QRect(570, 590, 301, 61))
        self.lineEdit_mes_header_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_mes_header_4.setStyleSheet("background-color: transparent;\n"
"font: 22pt \"Sans Serif Collection\";\n"
"color: rgb(51, 51, 51);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"")
        self.lineEdit_mes_header_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_mes_header_4.setObjectName("lineEdit_mes_header_4")
        self.dateEdit = QtWidgets.QDateEdit(self.home_widget)
        self.dateEdit.setGeometry(QtCore.QRect(570, 800, 821, 71))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(18)
        self.dateEdit.setFont(font)
        self.dateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_mes_header_5 = QtWidgets.QLineEdit(self.home_widget)
        self.lineEdit_mes_header_5.setGeometry(QtCore.QRect(570, 740, 301, 61))
        self.lineEdit_mes_header_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_mes_header_5.setStyleSheet("background-color: transparent;\n"
"font: 22pt \"Sans Serif Collection\";\n"
"color: rgb(51, 51, 51);\n"
"\n"
"\n"
"\n"
"border:none;\n"
"")
        self.lineEdit_mes_header_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_mes_header_5.setObjectName("lineEdit_mes_header_5")
        self.pushButton = QtWidgets.QPushButton(self.home_widget)
        self.pushButton.setGeometry(QtCore.QRect(570, 920, 821, 91))
        self.pushButton.setStyleSheet("background-color: rgb(0, 210, 135);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Sans Serif Collection\";\n"
"border-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_voltar = QtWidgets.QPushButton(self.home_widget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(50, 70, 64, 64))
        self.pushButton_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_voltar.setStyleSheet("border-image: url(:/images_home/voltar.png);")
        self.pushButton_voltar.setText("")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.radioButton_entrada = QtWidgets.QRadioButton(self.home_widget)
        self.radioButton_entrada.setGeometry(QtCore.QRect(790, 290, 131, 21))
        self.radioButton_entrada.setStyleSheet("font: 16pt \"Sans Serif Collection\";\n"
"color: rgb(0, 210, 135);")
        self.radioButton_entrada.setObjectName("radioButton_entrada")
        self.radioButton_saida = QtWidgets.QRadioButton(self.home_widget)
        self.radioButton_saida.setGeometry(QtCore.QRect(1070, 290, 111, 21))
        self.radioButton_saida.setStyleSheet("font: 16pt \"Sans Serif Collection\";\n"
"color: rgb(246, 68, 68);")
        self.radioButton_saida.setObjectName("radioButton_saida")
        MainWindow.setCentralWidget(self.home_widget)
        self.menu_opcoes = QtWidgets.QMenuBar(MainWindow)
        self.menu_opcoes.setGeometry(QtCore.QRect(0, 0, 1930, 21))
        self.menu_opcoes.setObjectName("menu_opcoes")
        self.menu_opcoes_item0 = QtWidgets.QMenu(self.menu_opcoes)
        self.menu_opcoes_item0.setObjectName("menu_opcoes_item0")
        MainWindow.setMenuBar(self.menu_opcoes)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionProcurar = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images_home/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProcurar.setIcon(icon)
        self.actionProcurar.setObjectName("actionProcurar")
        self.actionCadastrar = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images_home/create.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCadastrar.setIcon(icon1)
        self.actionCadastrar.setObjectName("actionCadastrar")
        self.actionApagar = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images_home/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionApagar.setIcon(icon2)
        self.actionApagar.setObjectName("actionApagar")
        self.actionAtualizar = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images_home/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAtualizar.setIcon(icon3)
        self.actionAtualizar.setObjectName("actionAtualizar")
        self.actionVer_Meses = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images_home/olhinho.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVer_Meses.setIcon(icon4)
        self.actionVer_Meses.setObjectName("actionVer_Meses")
        self.actionNovo_mes = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images_home/novo_mes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNovo_mes.setIcon(icon5)
        self.actionNovo_mes.setObjectName("actionNovo_mes")
        self.actionFechar_mes = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images_home/fechar_mes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFechar_mes.setIcon(icon6)
        self.actionFechar_mes.setObjectName("actionFechar_mes")
        self.actionDetalhes_do_Saldo = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images_home/saldo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDetalhes_do_Saldo.setIcon(icon7)
        self.actionDetalhes_do_Saldo.setObjectName("actionDetalhes_do_Saldo")
        self.actionFechamento_do_Dia = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images_home/fechamento_dia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFechamento_do_Dia.setIcon(icon8)
        self.actionFechamento_do_Dia.setObjectName("actionFechamento_do_Dia")
        self.menu_opcoes_item0.addAction(self.actionProcurar)
        self.menu_opcoes_item0.addAction(self.actionCadastrar)
        self.menu_opcoes_item0.addAction(self.actionApagar)
        self.menu_opcoes_item0.addAction(self.actionAtualizar)
        self.menu_opcoes_item0.addAction(self.actionVer_Meses)
        self.menu_opcoes_item0.addAction(self.actionNovo_mes)
        self.menu_opcoes_item0.addAction(self.actionFechar_mes)
        self.menu_opcoes_item0.addAction(self.actionDetalhes_do_Saldo)
        self.menu_opcoes_item0.addAction(self.actionFechamento_do_Dia)
        self.menu_opcoes.addAction(self.menu_opcoes_item0.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_header_home.setText(_translate("MainWindow", "HERMANN.FINANCE  "))
        self.lineEdit_mes_header.setText(_translate("MainWindow", "FEVEREIRO"))
        self.label_entradas.setText(_translate("MainWindow", "Entradas"))
        self.lineEdit_entradas_valor.setText(_translate("MainWindow", "+ R$ 2.273,31"))
        self.label_saidas.setText(_translate("MainWindow", "Saidas"))
        self.lineEdit_saidas_valor.setText(_translate("MainWindow", "- R$ 10.127,82"))
        self.label_total.setText(_translate("MainWindow", "Total"))
        self.lineEdit_total_valor.setText(_translate("MainWindow", "- R$ 7.854,51"))
        self.lineEdit_mes_header_2.setText(_translate("MainWindow", "DOC N°"))
        self.lineEdit_mes_header_3.setText(_translate("MainWindow", "CLIENTE"))
        self.lineEdit_mes_header_4.setText(_translate("MainWindow", "FORMA PAGAMENTO"))
        self.lineEdit_mes_header_5.setText(_translate("MainWindow", "DATA"))
        self.pushButton.setText(_translate("MainWindow", "Confirmar"))
        self.radioButton_entrada.setText(_translate("MainWindow", "ENTRADA"))
        self.radioButton_saida.setText(_translate("MainWindow", "SAIDA"))
        self.menu_opcoes_item0.setTitle(_translate("MainWindow", "Opções"))
        self.actionProcurar.setText(_translate("MainWindow", "Procurar"))
        self.actionCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.actionApagar.setText(_translate("MainWindow", "Apagar"))
        self.actionAtualizar.setText(_translate("MainWindow", "Atualizar"))
        self.actionVer_Meses.setText(_translate("MainWindow", "Ver Meses"))
        self.actionNovo_mes.setText(_translate("MainWindow", "Novo Mês"))
        self.actionFechar_mes.setText(_translate("MainWindow", "Fechar Mês"))
        self.actionDetalhes_do_Saldo.setText(_translate("MainWindow", "Detalhes do Saldo"))
        self.actionFechamento_do_Dia.setText(_translate("MainWindow", "Fechamento do Dia"))
        
import images_home.resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
