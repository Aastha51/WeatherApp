from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=text_field.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
        data=requests.get(api).json()
        con=data['weather'][0]['main']
        des=data['weather'][0]['description']
        temp=int(data['main']['temp']-273.15)
        pressure=data['main']['pressure']
        humidity=data['main']['humidity']
        wind=data['wind']['speed']
        T.config(text=(temp,"°"))
        c.config(text=(con,"|","feels","like",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=des)
        p.config(text=pressure)
    
    except Exception as e:
        messagebox.showerror("weather app","invalid entry!!")

search_im=PhotoImage(file="C:/Users/Asus/Downloads/search.png")
myimage=Label(image=search_im)
myimage.place(x=20,y=20)

text_field=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040")
text_field.place(x=50,y=40)
text_field.focus()

search_icon=PhotoImage(file="C:/Users/Asus/Downloads/search_icon.png")
my_imageicon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
my_imageicon.place(x=400,y=34)

logo_im=PhotoImage(file="C:/Users/Asus/Downloads/logo.png")
logo=Label(image=logo_im)
logo.place(x=150,y=100)

frame_im=PhotoImage(file="C:/Users/Asus/Downloads/box.png")
frame=Label(image=frame_im)
frame.pack(padx=5,pady=5,side=BOTTOM)

name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)

clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)


label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)


label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)


label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)


label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)


T=Label(font=("arial",70,"bold"),fg="#ee666d")
T.place(x=400,y=150)
c=Label(font=("arial",15,"bold"),fg="#ee666d")
c.place(x=400,y=250)
w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)
root.mainloop()

