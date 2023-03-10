from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root=Tk()
root.title("TRACK NUMBER")
root.geometry("365x584+800+200")
root.resizable(False,False)

def Track():
  enter_number=entry.get()
  number=phonenumbers.parse(enter_number)

  #country
  locate=geocoder.description_for_number(number,'fr')
  country.config(text=locate)

  #operator
  operator=carrier.name_for_number(number,'fr')
  sim.config(text=operator)

  #phone timezone
  time=timezone.time_zones_for_number(number)
  zone.config(text=time)

  #longitude and latitude
  geolocator= Nominatim(user_agent="geoapiExercices")
  location= geolocator.geocode(locate)

  lng=location.longitude
  lat=location.latitude
  longitude.config(text=lng)
  latitude.config(text=lat)

  #time showing in phone
  obj =TimezoneFinder()
  result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

  home=pytz.timezone(result)
  local_time=datetime.now(home)
  current_time=local_time.strftime("%I:%M %p")
  clock.config(text=current_time)

#icon image
icon=PhotoImage(file="logo-image.png")
#logo
logo=PhotoImage(file="logo-image.png")
Label(root,image=logo).place(x=240,y=70)

Eback=PhotoImage(file="search.png")
Label(root,image=Eback).place(x=-5,y=190)

#heading
Heading=Label(root,text="TRACK NUMBER",font=('arial',15,'bold'))
Heading.place(x=90,y=110)

#Entry
entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,justify="center",bd=0,font=("arial",20))
enter_number.place(x=67,y=273)

#search button
Search_image=PhotoImage(file="search-button.png")
search=Button(root,image=Search_image,borderwidth=0,cursor="hand2",bd=0,command=Track)
search.place(x=125,y=350)

#Label(information)
country=Label(root,text="Country:",fg="black",font=("arial",10,'bold'))
country.place(x=50,y=440)

sim=Label(root,text="SIM:",fg="black",font=("arial",10,'bold'))
sim.place(x=200,y=440)

zone=Label(root,text="TimeZone:",fg="black",font=("arial",10,'bold'))
zone.place(x=50,y=480)

clock=Label(root,text="Phone Time:",fg="black",font=("arial",10,'bold'))
clock.place(x=200,y=480)

longitude=Label(root,text="Longitude:",fg="black",font=("arial",10,'bold'))
longitude.place(x=50,y=520)

latitude=Label(root,text="Latitude:",fg="black",font=("arial",10,'bold'))
latitude.place(x=200,y=520)

root.iconphoto(False,icon)
root.mainloop()

