import onetimepad
import tkinter
import random
import math
import cryptography
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from tkinter import *

import cryptography
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes



def ces():
    chhh=input("Enter encoding or decoding [E/D] : ")
    
    if chhh==1:
        string=str(input("\nEnter your string : "))
        x=''
        w=int(input("Enter char shift : "))
        for i in string:
            n=ord(i)
            s=n+w
            x+=chr(s)
        print("\nThe encrypted code is : ",x)



    
    elif chhh==2:
        string=str(input("\nEnter your string : "))
        y=''
        w=int(input("Enter char shift : "))
        for j in string:
            a=ord(j)
            b=a-w
            y+=chr(b)

        print("\nThe decrypted code is : ",y)



def ass():
    s=input("\nEnter a string : ")
    secret_message = bytes(s,'utf-8')


    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    public_key = private_key.public_key()


    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )


    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )


    print('\n')
    print("Printing the public key : ")
    print('\n')
    print(public_key_pem)


    print('\n')
    print("Printing the private key : ")
    print('\n')
    print(private_key_pem)


    encrypted_data = public_key.encrypt(
        secret_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


    print("\n")
    print("Printing the encrypted key : ")
    print("\n")
    print(encrypted_data.hex())
    print("\n")



    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("\n")
    print("Printing the decrypted key : ")
    print("\n")
    print(decrypted_data.decode('utf-8'))
    print("\n")











def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m





def btostr(a):
    
    str_converted = ""
    for i in a.split(" "):
        str_converted += chr(int(i, 2))
    return str_converted




def tooctal(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(oct(i)[2:]))
  return m




def tohex(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(hex(i)[2:])
  return m


def otostr(a):
    
    str_converted = ""
    for octal_char in a.split(" "):
        str_converted += chr(int(octal_char, 8))
    return str_converted



def htostr(a):
    
    str_converted = ""
    for i in a.split(" "):
        str_converted += chr(int(i, 16))
    return str_converted






def builtin():
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

    root.mainloop()

def bfa():
    root = Tk()
    root.title("CRYPTOGRAPHY")
    root.geometry("800x600")
    global e1
    tkinter.Label(root, text="Enter the string to encode : ").grid(row=0)
    e1=Entry(root)
    e1.grid(row=0, column=1)
    tkinter.Button(root, text="submit",command=c6).grid(row=2)
    

def c8():
    w=[]
    root = Tk()
    root.title("CRYPTOGRAPHY")
    root.geometry("800x600")
    f=e2.get()
    h=[]
    try:
        x=btostr(f)
        h.append(x)
    except:
        print("Not Binary!")
    try:
        y=otostr(f)
        h.append(y)
    except:
         print("Not Octal!")
        
    
    try:
        z=htostr(f)
        h.append(z)
    except:
         print("Not Hexadecimal!")
    tkinter.Label(root,text="Brute forcing code : ").grid(row=0)
    tkinter.Label(root,text=" Possible values are : ").grid(row=2)
    tkinter.Label(root,text=h).grid(row=3)
    #for i in h:
        #if i==e1:
         #   w.append(i)
           # break
            
   # tkinter.Label(root,text="The decoded message is: ").grid(row=5)
   # tkinter.Label(root,text=w).grid(row=5, column=1)
            
    
    

def c7():
    root = Tk()
    root.title("CRYPTOGRAPHY")
    root.geometry("800x600")
    global e2
    tkinter.Label(root,text="Enter the coded message : ").grid(row=0)
    e2=Entry(root)
    e2.grid(row=0,column=1)
    tkinter.Button(root, text= "Submit",command=c8).grid(row=3)
    
    



def c6():
    global c,d
    root = Tk()
    root.title("CRYPTOGRAPHY")
    root.geometry("800x600")
    c=e1.get()
    tkinter.Label(root, text="Encoded text : ").grid(row=0)
    
    b=random.randint(1,3)
    if b==1:
        d=toBinary(c)
    elif b==2:
        d=tooctal(c)
    else:
        d=tohex(c)
    tkinter.Label(root, text=d).grid(row=0,column=1)
    tkinter.Label(root, text="Do you want to try decoding?").grid(row=3)
    tkinter.Button(root, text= "YES",command=c7).grid(row=5)
    
    


print("\n\n******************************************************************\n---------------------------CRYPTOGRAPHY---------------------------\n******************************************************************")
print('''\n1.Symmetric key\n2.Brute force attack\n3.Asymmetric key\n4.Caesar cipher    ''')
ch=int(input('''\n\nEnter your choice of cryptography : '''))
if ch==1:
    builtin()
elif ch==2:
    bfa()
elif ch==3:
    ass()
elif ch==4:
    ces()
    
