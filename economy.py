import tkinter as tk
form=tk.Tk()
form.title("Economy Simulator")
etiket=tk.Label(text="Economy",fg="black")
etiket.pack()
etiket2=tk.Label(form,text="Simulator",fg="black")
etiket2.pack()
print("Ekonomi Simülatörüne Hoş Geldiniz")
print("Borç Seviyesi 300, Enflasyon 250, Dolar 50, İşsizlik 100'ü bulursa oyun biter")
faiz=8
dolar=23
enflasyon=175
borç=200
işsizlik=40
def artar():
    global faiz
    faiz=faiz+1
    print("Faiz Artar")
    print(faiz)
    global dolar
    dolar=dolar-2
    print("Dolar Azalır")
    print(dolar)
    global enflasyon
    enflasyon=enflasyon-10
    print("Enflasyon Azalır")
    print(enflasyon)
    global işsizlik
    işsizlik=işsizlik+10
    print("İşsizlik Artar")
    print(işsizlik)
    global borç
    borç=borç+10
    print("Borç Artar")
    print(borç)


form.state("normal")

def azalır():
    global faiz
    faiz=faiz-1
    print("Faiz Artar")
    print(faiz)
    global dolar
    dolar=dolar+2
    print("Dolar Azalır")
    print(dolar)
    global enflasyon
    enflasyon=enflasyon+10
    print("Enflasyon Azalır")
    print(enflasyon)
    global işsizlik
    işsizlik=işsizlik-10
    print("İşsizlik Artar")
    print(işsizlik)
    global borç
    borç=borç-10
    print("Borç Artar")
    print(borç)


buton=tk.Button(form,text="Faizi Arttır",fg="black",bg="green",command=artar)
buton.pack()
buton2=tk.Button(form,text="Faizi Düşür",fg="black",bg="green",command=azalır)
buton2.pack()

form.mainloop()
