import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

result=0
result_list=[]

class my_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(850,200,380,550)
        self.setFixedSize(self.size())# kullanıcı pencereyi büyültüp küçültemesin...
        self.UI()

    def UI(self):
    #   işlem kutucuğu :
        self.gir=QLineEdit(self)
        self.gir.resize(335,30)
        self.gir.move(20,25)
        self.gir.setText("O")
        self.gir.setAlignment(Qt.AlignRight)# girilen değerleri sağdan sola doğru olmasını sağlar
        self.gir.setStyleSheet("font:14pt Arial Bold;border:3px solid gray;border-radius:5px;background-color:#e6e6fa;")# süsleme
        
    #   sayı kutucukları :
        sayılar=list()
        for i in range(1,10):
            i=QPushButton(str(i),self)# str(i) yapmalıyız çünkü butonlar içine sadece string değerleri alır
            i.setFont(QFont("Arial",15))
            i.resize(70,40)
            i.setStyleSheet("background-color:white")
            i.clicked.connect(self.sayi)
            sayılar.append(i)
        temp=0
        for i in range(0,3):
            for j in range(0,3):
                sayılar[temp].move(25+j*90,70+i*70)
                temp+=1

    #   işlem kutucukları :
        islemler=["+","-","*","/"]
        nev=[]
        for r in islemler:
            r=QPushButton(str(r),self)
            r.setFont(QFont("Arial",15))
            r.resize(70,40)
            r.setStyleSheet("background-color:white")
            r.clicked.connect(self.operator)
            nev.append(r)
            
        for i in range(0,4):
            nev[i].move(300,70+i*70)
    #   status bar : --> pencerenin sol alt kısmında bilgi verme amacıyla konulur
        self.sb=QStatusBar()
        self.setStatusBar(self.sb)  
        self.sb.setFont(QFont("Verdana",14))      
    
    #   diğer kutucuklar  :
        self.sıfır_butonu=QPushButton("0",self)
        self.sıfır_butonu.setStyleSheet("background-color:white")
        self.sıfır_butonu.resize(250,40)
        self.sıfır_butonu.setFont(QFont("Arial",15))
        self.sıfır_butonu.move(25,280)
        self.sıfır_butonu.clicked.connect(self.sayi)
        
        self.c_butonu=QPushButton("C",self)
        self.c_butonu.setStyleSheet("background-color:white")
        self.c_butonu.resize(70,40)
        self.c_butonu.setFont(QFont("Arial",15))
        self.c_butonu.move(25,340)
        self.c_butonu.clicked.connect(self.clear)
        
        self.buton=QPushButton(".",self)
        self.buton.setStyleSheet("background-color:white")
        self.buton.resize(70,40)
        self.buton.setFont(QFont("Arial",15))
        self.buton.move(110,340)
        self.buton.clicked.connect(self.operator)
        
        self.es=QPushButton("=",self)
        self.es.setStyleSheet("background-color:white")
        self.es.resize(70,40)
        self.es.setFont(QFont("Arial",15))
        self.es.move(200,340)
        self.es.clicked.connect(self.esit)

        self.geri=QPushButton(self)
        self.geri.setIcon(QIcon("python.png"))# PNG RESMİ YÜKLEME
        self.geri.setStyleSheet("background-color:white")
        self.geri.resize(70,40)
        self.geri.setFont(QFont("Arial",15))
        self.geri.move(300,340)
        self.geri.clicked.connect(self.dlt)

    #   fonksiyonlar :
    def sayi(self):
        mesaj=self.sender().text()# self.sender().text() ---> kullanıcı butona tıklarsa o butonun içindeki değeri bize döndürür...
        
        if self.gir.text() == "O":# kutunun içerisine daha önce bir değer girilmemişse :
            self.gir.setText(mesaj)# hangi butona tıklandıysa kutunun içine onu yaz
        else:# ama kutunun içerisine daha önce bir değer girilmişse :
            self.gir.setText(self.gir.text()+mesaj)# daha önceki değerin yanına yeni tıklana butonun değerini yazdır (str işlemi)

    def operator(self):
        text=self.sender().text()
        
        if self.gir.text() !="O":
            self.gir.setText(self.gir.text()+text)
        
    def clear(self):
        self.gir.setText("O")
    
    def dlt(self):
        msg=self.gir.text()
        n_msg=msg[:-1]
        self.gir.setText(n_msg)
        if len(n_msg)==0:
            self.gir.setText("O")
            
#           Bu alttakini yapacağına üstteki gibi yap daha kullanışlı...
#       if self.gir.text() != "O":
#           self.gir.setText(n_msg)
#       else:
#           self.gir.setText("O")

    def esit(self):
        cont=self.gir.text()
        result=eval(cont)# eval(x) ---> x ile ilgili bütün matematiksel işlemleri yapar, özel br fonksiyondur
        self.gir.setText(str(result))
        result_list.append(cont)
        result_list.reverse()
        self.sb.showMessage("Geçmiş: "+"__".join(result_list[:3]))







def window():
    
    app = QApplication(sys.argv)
    win = my_window()# win değişkenini yarattığımız class'tan bir nesne gibi yaptık

    win.show()
    sys.exit(app.exec_())


window()
