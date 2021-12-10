# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:12:20 2020

@author: Haji Davud

CRYPTO MACHINE 

"""
from PyQt5 import QtWidgets,uic

def desifre(file,keyword):
    sifre = file.split()
    key=keyword
    keylen=len(key)
    c=0                                                                 
    son1=""

    for i in range(len(sifre)):                   #]DQLW GFa_G=salam davud keyword=haci
        if i!=0:
            son1+=" "
            
        for b in range(len(sifre[i])):
            if keylen-1>c:
                if ord(sifre[i][b])-ord(key[c])<0:# 0 ra bareber olmaqina diqqet ele!
                    son1+=chr(ord(sifre[i][b])+126-ord(key[c]))
                    c+=1
                
                
                else:
                    son1+=ord(sifre[i][b])-key[c]
            else:
                if ord(sifre[i][b])-ord(key[c])<0:# 0 ra bareber olmaqina diqqet ele!
                    son1+=chr(ord(sifre[i][b])+126-ord(key[c]))
                    c=0
                
                
                else:
                    son1+=ord(sifre[i][b])-key[c]
                    c=0
            
    
    return son1
    
def cevirici(crypto,key):
    crypto=crypto.split()
    acar = key #line edit 3 u gonder
    son=0
    son1=""
    c=0
    for i in range(len(crypto)):
        if i!=0:
            son1+=" "#bunuda sifrelemk isdiyirikse son1+= ord(" ") etmey olar ama gerek sifrelenmis sozude nezere alasan
            
        for b in range(len(crypto[i])):
            if len(acar)-1>c:
                #print(c,"if")
                son=ord(crypto[i][b])+ord(acar[c])
                if son>126:
                    son1+=chr(son%126)
                else:
                    son1+=chr(son)
                c+=1
            else:
                #print(c,"else")
                son=ord(crypto[i][b])+ord(acar[c])
                if son>126:
                    son1+=chr(son%126)
                else:
                    son1+=chr(son)
                c=0
        son=""  # eger istiyirsense  acar sozde hardan qalib ordan basdamasin 
        #bu for'da c ni 0 beraber et  || yoruma bax
        #c=0 
    return son1

def sifreliyen():
    a=cevirici(dlg.lineEdit.text(),dlg.lineEdit_3.text())
    dlg.lineEdit_2.setText(a)
    
def desifreliyen():
    a=desifre(dlg.lineEdit.text(),dlg.lineEdit_3.text())
    dlg.lineEdit_2.setText(a)   
   


    
app = QtWidgets.QApplication([])
dlg= uic.loadUi("crypto.ui")

dlg.pushButton.clicked.connect(sifreliyen)
dlg.pushButton_2.clicked.connect(desifreliyen)


dlg.show()
app.exec()    

