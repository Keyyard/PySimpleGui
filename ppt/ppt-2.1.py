
import numpy as np
import matplotlib.pyplot as plt
import math


#Binh phuong toi thieu
def bptt():
    #Nhap du lieu tu nguoi dung
    x_data = np.array([float(x) for x in input("Nhap it nhat 2 gia tri x: ").split()])
    y_data = np.array([float(x) for x in input("Nhap it nhat 2 gia tri y: ").split()])
    
    #hinh thanh ma tran A
   
    A = np.vstack([x_data**2, x_data, np.ones(len(x_data))]).T

    a, b, c = np.linalg.lstsq(A, y_data, rcond=None)[0]

    print("a = ", round(a,4))
    print("b = ", round(b,4))
    print("c= ", round(c,4))
    print("y = ", round(c,4), " + ", round(b,4), "x", "+", round(a,4), "x**2")

 
def f(x):
    return x**3 + x - 5
#phuong phap day cung
def ppdc():
    #Nhap du lieu tu nguoi dung
    print("Nhap khoang nghiem a, b")
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))
    if f(a) * f(b) > 0:
        print("Khong co nghiem trong khoang nay")
        return
    epsi = float(input("Bam enter de tiep tuc voi epsilon = 0.00001 hoac nhap sai so epsilon: ") or 0.00001)
    #Tinh x
    x = a - (b - a) * f(a) / (f(b) - f(a))
    if f(x) * f(a) < 0:
        while abs(x - b) > epsi:
            b = x
            x = a - (b - a) * f(a) / (f(b) - f(a))
            #print(a, b, x, f(x))
    else:
        while abs(x - a) > epsi:
            a = x
            x = a - (b - a) * f(a) / (f(b) - f(a))
            #print(a, b, x, f(x))
    print("x = ", x)

def stop():
    input("")
def pick():
    #chon 1 hoac 2 de chon phuong phap va co the chon lai neu nhap sai va sau khi chon xong va su dung phuong phap thi cho chon lai
    print("=====================================")
    print("Chon phuong phap: ")
    print("1. Binh phuong toi thieu")
    print("2. Phuong phap day cung")
    while True:
        choice = int(input("Nhap lua chon: "))
        if choice == 1:
            bptt()
        elif choice == 2:
            ppdc()
        else:
            print("Nhap sai, nhap lai: ")
            continue
        stop()
        print("=====================================")
        print("Chon lai phuong phap: ")
        print("1. Binh phuong toi thieu")
        print("2. Phuong phap day cung")

if __name__ == "__main__":
    pick()