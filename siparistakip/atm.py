from tkinter import *
import requests
from tkinter import messagebox

ekran=Tk()
ekran.title("ATM")
ekran.geometry("1200x700+1000+200")
ekran.resizable(False,False)  #ekran boyutu degistirilememesi icin resizable da false yaz🎀
yaziFont="Arial 12"

hesap={"Bakiye":30000}

def paracekEkranAc():
    paracekFrame.place(x=350,y=210)

def paracekEkrankapat():
    paracekFrame.place_forget()

def paracek():
    cekicelecektutar=int(paracekEntry.get())
    if cekicelecektutar>hesap["Bakiye"]:
        messagebox.showerror("Hata","Bakiye Yetersiz")
        paracekEntry.delete(0,END)
    else:
        hesap["Bakiye"]=hesap["Bakiye"] - cekicelecektutar
        bakiyeLabel.config(text=f"Bakiye: {hesap['Bakiye']} TL") 
        paracekEntry.delete(0,END)
    
def parayatirEkranAc():
    parayatirFrame.place(x=350,y=210)
    
def parayatirEkranKapat():
    parayatirFrame.place_forget()

def parayatir():
    yatirilacaktutar=int(parayatirEntry.get())
    hesap["Bakiye"]=hesap["Bakiye"] + yatirilacaktutar
    bakiyeLabel.config(text=f"Bakiye: {hesap['Bakiye']} TL")

def dovizalEkranAc():
    dovizalFrame.place(x=350,y=210)
    
def dovizalEkranKapat():
    dovizalFrame.place_forget()
    
def dovizcevir():
    url="https://api.genelpara.com/embed/doviz.json"
    bilgi=requests.get(url)
    if bilgi.status_code==200:
        data=bilgi.json()
        print(data)
        usdSatis=float(data["USD"]["satis"])
        euroSatis=float(data["EUR"]["satis"])
        
        tutar=float(doviztutarEntry.get())  #ondalikli sayi türüne float tipi denir
        tur=(dovizturuEntry.get()).upper()  #usd ve eur'u buyuk harfle girmekle ugrasmamak icin upper🎀
        
        if tutar>hesap["Bakiye"]:
            messagebox.showerror("HATA","Bakiye Yetersiz")
            doviztutarEntry.delete(0,END)
            dovizturuEntry.delete(0,END)
        else:
            if tur=="USD":
               miktar=round((tutar/usdSatis),2)
               hesap["Bakiye"]=hesap["Bakiye"]-tutar
               bakiyeLabel.config(text=f"Bakiye: {hesap['Bakiye']} TL  USD:{miktar}$")
        
            elif tur=="EUR":
                 miktar=round((tutar/euroSatis),2)
                 hesap["Bakiye"]=hesap["Bakiye"]-tutar
                 bakiyeLabel.config(text=f"Bakiye: {hesap['Bakiye']} TL  EUR:{miktar}€")
            
        doviztutarEntry.delete(0,END)
        dovizturuEntry.delete(0,END)
    else:
        messagebox.showerror("HATA","API'den veri gelmedi")
        


atmresim=PhotoImage(file="Ileriseviye\images\ekran.png")
resimLabel=Label(ekran,image=atmresim)
resimLabel.pack()

bakiyeFrame=Frame(ekran,width=500,height=40,bg="gray")
bakiyeFrame.place(x=350,y=160)

bakiyeLabel=Label(bakiyeFrame,text=f"Bakiye: {hesap['Bakiye']} TL",font=yaziFont,bg="gray")  
bakiyeLabel.place(x=10,y=10)

bakiyecekButon=Button(ekran,text="Bakiye Cek",border=0,bg="#ddd",width=10,command=paracekEkranAc)
bakiyecekButon.place(x=143,y=343)

parayatirButon=Button(ekran,text="Para Yatir",border=0,bg="#ddd",width=10,command=parayatirEkranAc)
parayatirButon.place(x=145,y=403)

parayatirFrame=Frame(ekran,width=500,height=100)

parayatirLabel=Label(parayatirFrame,text="Yatirilicak Tutar:",font=yaziFont)
parayatirLabel.place(x=10,y=10)

parayatirEntry=Entry(parayatirFrame,font=yaziFont,width=25,border=3)
parayatirEntry.place(x=200,y=10)

parayatirtamam=Button(parayatirFrame,text="Tamam",font=yaziFont,width=20,border=1,command=parayatir)
parayatirtamam.place(x=80,y=50)

parayatiriptal=Button(parayatirFrame,text="Iptal",font=yaziFont,width=20,border=1,command=parayatirEkranKapat)
parayatiriptal.place(x=270,y=50)

paracekFrame=Frame(ekran,width=500,height=100)

paracekLabel=Label(paracekFrame,text="Cekilecek Tutar:",font=yaziFont)
paracekLabel.place(x=10,y=10)

paracekEntry=Entry(paracekFrame,font=yaziFont,width=25,border=3)
paracekEntry.place(x=200,y=10)

paracektamam=Button(paracekFrame,text="Tamam",font=yaziFont,width=20,border=1,command=paracek)
paracektamam.place(x=80,y=50)

paracekiptal=Button(paracekFrame,text="Iptal",font=yaziFont,width=20,border=1,command=paracekEkrankapat)
paracekiptal.place(x=270,y=50)

dovizalButon=Button(ekran,text="Döviz Al",border=0,bg="#ddd",width=10,command=dovizalEkranAc)
dovizalButon.place(x=980,y=343)

dovizalFrame=Frame(ekran,width=500,height=140)

doviztutarLabel=Label(dovizalFrame,text="Cevrilecek Tutar:",font=yaziFont)
doviztutarLabel.place(x=10,y=10)

doviztutarEntry=Entry(dovizalFrame,font=yaziFont,width=25,border=3)
doviztutarEntry.place(x=200,y=10)

dovizturuLabel=Label(dovizalFrame,text="Döviz Türü(EUR/USD):",font=yaziFont)
dovizturuLabel.place(x=10,y=50)

dovizturuEntry=Entry(dovizalFrame,font=yaziFont,width=25,border=3)
dovizturuEntry.place(x=200,y=50)

dovizaltamam=Button(dovizalFrame,text="Tamam",font=yaziFont,width=20,border=1,command=dovizcevir)
dovizaltamam.place(x=80,y=100)

dovizaliptal=Button(dovizalFrame,text="Iptal",font=yaziFont,width=20,border=1,command=dovizalEkranKapat)
dovizaliptal.place(x=270,y=100)

ekran.mainloop()

