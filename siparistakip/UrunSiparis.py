from tkinter import * 
import sqlite3
from tkinter import messagebox

screen=Tk()
screen.title("Online Fashion Boutique")
screen.geometry("900x500+800+200")
screen.config(bg="#dddddd")

appResim=PhotoImage(file="Ileriseviye\siparistakip\images\\fashion4.png")
appResim=appResim.subsample(3,3)
appLabel=Label(screen,image=appResim)
appLabel.pack()

listelekutusu=""
listelePenceresi=""

yaziFontu="Arial 15"

siparisveritabani=sqlite3.connect("Ileriseviye\siparistakip\sipariskaydi.db")
curr=siparisveritabani.cursor()

curr.execute('''CREATE TABLE IF NOT EXISTS SiparisKaydi (
  musteriId INT PRIMARY KEY,
  musteriAdi VARCHAR (50),
  musteriSoyadi VARCHAR(50),
  urunNo INT,
  tarih VARCHAR(15)
  ) ''')
siparisveritabani.commit()
siparisveritabani.close()

def kaydet():
    musteriNo=musteriId.get()
    musteri=musteriAdi.get()
    musteris=musteriSoyad.get()
    tarih=siparistarihi.get()
    urunkod=urunno.get()
    
    siparisveritabani=sqlite3.connect("Ileriseviye\siparistakip\sipariskaydi.db")
    curr=siparisveritabani.cursor()
    curr.execute(''' INSERT INTO SiparisKaydi (musteriId,musteriAdi,musteriSoyadi,tarih,urunno) VALUES 
    (?,?,?,?,?)''',(musteriNo,musteri,musteris,tarih,urunkod))
    siparisveritabani.commit()
    siparisveritabani.close()
    
def duzenle():
  secilen=listelekutusu.curselection()
  secilmis=secilen[0]
  bilgi=listelekutusu.get(secilmis)
  print(bilgi[0])
  
  guncellepenceresi=Toplevel(listelePenceresi)
  guncellepenceresi.geometry("250x250")
  guncellepenceresi.title("Güncelle")
  
  Label(guncellepenceresi,text="Müsteri Ad:").place(x=20,y=10)
  musteriAdi=Entry(guncellepenceresi)
  musteriAdi.place(x=100,y=10)

  Label(guncellepenceresi,text="Müsteri Soyad:").place(x=20,y=40)
  musteriSoyad=Entry(guncellepenceresi)
  musteriSoyad.place(x=100,y=40)

  Label(guncellepenceresi,text="Siparis Tarihi:").place(x=20,y=70)
  siparistarihi=Entry(guncellepenceresi)
  siparistarihi.place(x=100,y=70) 
  
  Label(guncellepenceresi,text="Ürün No.:").place(x=20,y=100)
  urunno=Entry(guncellepenceresi)
  urunno.place(x=100,y=100)(x=100,y=70) 
  
  def guncelleme():
     yenimusteri=musteriAdi.get()
     yenimusteris=musteriSoyad.get()
     yenitarih=siparistarihi.get()
     yeniurunkod=urunno.get()
     
     siparisveritabani=sqlite3.connect("Ileriseviye\siparistakip\sipariskaydi.db")
     curr=siparisveritabani.cursor()
     curr.execute(''' UPDATE SiparisKaydi SET musteriAdi=? ,musteriSoyadi=? ,tarih=?, urunno=?
                  WHERE musteriId=? ''',(yenimusteri,yenimusteris,yenitarih,yeniurunkod,bilgi[0]))
     siparisveritabani.commit()
     siparisveritabani.close()
     
     listele()
    
  guncellebuton=Button(guncellepenceresi,text="Güncelle",command=guncelleme)
  guncellebuton.place(x=120,y=120)
  
def sil():
  cevap=messagebox.askokcancel("Onay Kutusu","Silmek istediginize emin misiniz?")
  
  if cevap:
    secilen=listelekutusu.curselection()
    secilmis=secilen[0]
    bilgi=listelekutusu.get(secilen)
    print(bilgi[0])
    siparisveritabani=sqlite3.connect("Ileriseviye\siparistakip\sipariskaydi.db")
    curr=siparisveritabani.cursor()
    curr.execute(''' DELETE FROM SiparisKaydi WHERE musteriId=?''',(bilgi[0],))
    siparisveritabani.commit()
    siparisveritabani.close()
     
    listele()
  
  

def listele():
  global listelekutusu
  global listelePenceresi
  listelePenceresi=Toplevel(screen)
  listelePenceresi.geometry("350x500+500+300")
  listelePenceresi.title("Listeleme Ekrani")
  
  duzenlebuton=Button(listelePenceresi,text="Düzenle",command=duzenle)
  duzenlebuton.place(x=20,y=400)
  
  silButon=Button(listelePenceresi,text="Kayit Sil",command=sil)
  silButon.place(x=100,y=400)
  
  siparisveritabani=sqlite3.connect("Ileriseviye\siparistakip\sipariskaydi.db")
  curr=siparisveritabani.cursor()
  curr.execute('''SELECT * FROM sipariskaydi''')
  bilgiler=curr.fetchall()
  
  siparisveritabani.close()
  print(bilgiler)
  
  listelekutusu=Listbox(listelePenceresi,height=20,width=40)
  listelekutusu.place(x=20,y=10)
  
  for bilgi in bilgiler:
    listelekutusu.insert(END,bilgi)

    
    
Label(screen,text="Müsteri ID:",font=yaziFontu).place(x=250,y=20)
musteriId=Entry(screen)
musteriId.place(x=400,y=20)

Label(screen,text="Müsteri Ad:",font=yaziFontu).place(x=250,y=55)
musteriAdi=Entry(screen)
musteriAdi.place(x=400,y=55)

Label(text="Müsteri Soyad:",font=yaziFontu).place(x=250,y=90)
musteriSoyad=Entry(screen)
musteriSoyad.place(x=400,y=90)

Label(screen,text="Siparis Tarihi:",font=yaziFontu).place(x=250,y=125)
siparistarihi=Entry(screen)
siparistarihi.place(x=400,y=125)   

Label(screen,text="Ürün No.:",font=yaziFontu).place(x=250,y=160)
urunno=Entry(screen)
urunno.place(x=400,y=160) 

kaydetbuton=Button(screen,text="Kaydet",command=kaydet)
kaydetbuton.pack()

listeleButon=Button(screen,text="Listele",command=listele)
listeleButon.pack()









screen.mainloop()