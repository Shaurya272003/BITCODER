import onetimepad       

from tkinter import *          

root = Tk() 

root.title("CRYPTOGRAPHY") 

root.geometry("800x600") 

  

def encryptMessage():                       

    pt = e1.get() 
     

    ct = onetimepad.encrypt(pt, 'random') 

    e2.insert(0, ct) 

  

def decryptMessage():                      

    ct1 = e3.get() 
 

    pt1 = onetimepad.decrypt(ct1, 'random') 

    e4.insert(0, pt1) 

      
 


label1 = Label(root, text ='plain text')                

label1.grid(row = 10, column = 1) 

label2 = Label(root, text ='encrypted text') 

label2.grid(row = 11, column = 1) 

l3 = Label(root, text ="cipher text") 

l3.grid(row = 10, column = 10) 

l4 = Label(root, text ="decrypted text") 

l4.grid(row = 11, column = 10) 

  


e1 = Entry(root) 

e1.grid(row = 10, column = 2) 

e2 = Entry(root) 

e2.grid(row = 11, column = 2) 

e3 = Entry(root) 

e3.grid(row = 10, column = 11) 

e4 = Entry(root) 

e4.grid(row = 11, column = 11)
 
 

ent = Button(root, text = "encrypt", bg ="light blue", fg ="black", command = encryptMessage) 

ent.grid(row = 13, column = 2) 

  


b2 = Button(root, text = "decrypt", bg ="light blue", fg ="black", command = decryptMessage) 

b2.grid(row = 13, column = 11)
