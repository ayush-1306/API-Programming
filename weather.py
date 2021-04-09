# importing the libraries 
from tkinter import *
from tkinter import messagebox
import requests 
import json 
import datetime 
from PIL import ImageTk, Image 

# necessary details 
root = Tk() 
root.title("Weather Application - Made By Ayush") 
root.geometry("500x600+250+10") 
root['background'] = "black"
root.resizable(False,False)

# Image 
new = ImageTk.PhotoImage(Image.open(r"D:\Presentation\download (1).jpg")) 
panel = Label(root, image=new) 
panel.place(x= 125, y=0) 
dt = datetime.datetime.now()

def clock_sharing():
	time_string = dt.strftime("%H:%M:%S")
	date_string = dt.strftime("%d/%m/%y")
	date = Label(root, text="DATE\n"+date_string, bg='black',fg = "springgreen", font=('georgia', 15)) 
	date.place(x=0, y=0)
	hour = Label(root, text="TIME \n"+time_string,bg='black',fg = 'springgreen',font =('georgia',15)) 
	hour.place(x=415, y=0)
clock_sharing()


# Theme for the respective time the application is used 
if int((dt.strftime('%I'))) >= 8 & int((dt.strftime('%I'))) <= 5: 
	img = ImageTk.PhotoImage(Image.open(r"D:\Presentation\images.jpg")) 
	panel = Label(root, image=img) 
	panel.place(x=125, y=0) 
else: 
	img = ImageTk.PhotoImage(Image.open(r"D:\Presentation\images (2).jpg")) 
	panel = Label(root, image=img) 
	panel.place(x=125, y=0) 


# City Search 
city_name = StringVar() 
city_entry = Entry(root, textvariable=city_name, width=30,font = ('Helvitica',12)) 
city_entry.place(x = 0,y = 250)
api_key = ""#enter your api key

def city_name(): 

	# API Call 
	api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q="
							+ city_entry.get() + "&appid="+api_key) 

	api = json.loads(api_request.content) 
	try :
		y = api['main']
		current_temprature = y['temp']
		current_temprature = round(current_temprature - 273.15,2)
		humidity = y['humidity']
		tempmin = round(y['temp_min'] - 273.15,2)
		tempmax = round(y['temp_max'] - 273.15,2)
		wind = api['wind']
		wind_spd = wind['speed']
		#Coordinates
		x = api['coord']
		longitude = x['lon']
		latitude = x['lat']
		#Country
		z = api['sys']
		country = z['country']
		citi = api['name']
		# Adding the received info into the screen 
		lable_temp.configure(text=current_temprature) 
		lable_humidity.configure(text=humidity) 
		max_temp.configure(text=tempmax) 
		min_temp.configure(text=tempmin) 
		lable_lon.configure(text=longitude) 
		lable_lat.configure(text=latitude)
		lable_country.configure(text=country) 
		lable_citi.configure(text=citi)
		wind_sd.configure(text = wind_spd)
	except:
		messagebox.showerror("Error","City not found")
		city_entry.delete(0 , END)

# Search Bar and Button 
city_nameButton = Button(root, text="Search",font = ('Helvitica',12), command=city_name) 
city_nameButton.place(x = 280,y = 250)

# Country Names and Coordinates 
lable_citi = Label(root, text="...",bg='black',fg = 'springgreen', font=("bold", 15)) 
lable_citi.place(x=10, y=340) 

lable_country = Label(root, text="...",bg='black',fg = 'springgreen', font=("bold", 15)) 
lable_country.place(x=100, y=340) 

lable_lon = Label(root, text="longitude",bg='black',fg = 'springgreen', font=("Helvetica", 15)) 
lable_lon.place(x=10, y=370) 
lable_lat = Label(root, text="latitude",bg='black',fg = 'springgreen', font=("Helvetica", 15)) 
lable_lat.place(x=90, y=370) 

# Current Temperature 
lable_temp = Label(root, text="...",bg='black',fg = 'springgreen',font=("Helvetica", 80)) 
lable_temp.place(x= 180, y=300) 


# Other temperature details 
humi = Label(root, text="Humidity",bg='black',fg = 'red', font=( 15)) 
humi.place(x=3, y=410) 
lable_humidity = Label(root, text="...",bg='black',fg = 'springgreen',font=( 15)) 
lable_humidity.place(x=90, y=410) 

#maximum temperature
maxi = Label(root, text="Maximum Temperature",  bg='black',fg = 'red',font=( 15)) 
maxi.place(x=3, y=440) 
max_temp = Label(root, text="...",bg = 'black', fg = 'springgreen', font=( 15)) 
max_temp.place(x=210, y=440) 
#minimum temperature
mini = Label(root, text="Minimum Temperature",bg = 'black',fg = 'red', font=( 15)) 
mini.place(x=3, y=470) 
min_temp = Label(root, text="...",bg = 'black',fg = 'springgreen', font=( 15)) 
min_temp.place(x=210, y=470) 
#wind
wind_speed= Label(root, text="Wind Speed", bg = 'black',width=10, font=( 15),fg = 'red') 
wind_speed.place(x=3, y=500) 
wind_sd = Label(root, text="...", width=0,bg='black', font=( 15),fg = 'springgreen') 
wind_sd.place(x=120, y=500) 

# Note 
note = Label(root, text="All temperatures are in degree celsius.", bg='black',fg = 'springgreen',font=("italic", 20)) 
note.place(x=20, y=540) 

root.mainloop()
