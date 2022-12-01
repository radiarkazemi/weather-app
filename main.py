from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

ui, _ = loadUiType("weather-app.ui")


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.weather_pushButton.clicked.connect(self.weather)

    def weather(self):
        city = self.city_lineEdit.text()

        geolocation = Nominatim(user_agent="geoapiExercises")
        location = geolocation.geocode(city)
        obj = TimezoneFinder()

        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        self.timezone_label.setText(result)
        self.long_lat_label.setText(f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")

        home = pytz.timezone(result)
        location_time = datetime.now(home)
        current_time = location_time.strftime("%I:%M %p")
        self.clock_label.setText(current_time)

        api = f"https://api.openweathermap.org/data/2.5/forecast?lat={location.latitude}" \
              f"&lon={location.longitude}&appid=API-Key"

        api2 = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}" \
               f"&lon={location.longitude}&appid=API-Key"

        json_data = requests.get(api2).json()
        json_data2 = requests.get(api).json()
        print(json_data)

        temp = json_data["main"]["temp"]
        humidity = json_data["main"]["humidity"]
        pressure = json_data["main"]["pressure"]
        wind = json_data["wind"]["speed"]
        description = json_data["weather"][0]["description"]

        self.temperature_label.setText(f"{temp - 273.15:.2f} °C")
        self.humidity_label.setText(f"{humidity}%")
        self.pressure_label.setText(f"{pressure}hPa")
        self.wind_label.setText(f"{wind}m/s")
        self.description_label.setText(description)

        # first cell
        first_day_image = json_data['weather'][0]["icon"]
        photo1 = QPixmap(f"icon/{first_day_image}@2x.png").scaled(200, 200)
        self.label_9.setPixmap(photo1)
        first = datetime.now()
        self.firstday_label.setText(first.strftime("%A"))

        temp_day1_min = ((json_data["main"]["temp_min"]) - 273.15)
        temp_day1_max = ((json_data["main"]["temp_max"]) - 273.15)
        self.temp_label.setText(f"Min: {temp_day1_min:.2f}\nMax: {temp_day1_max:.2f}")

        # second cell
        second_day_image = json_data2['list'][1]["weather"][0]["icon"]
        photo2 = QPixmap(f"icon/{second_day_image}@2x.png").scaled(100, 100)
        self.icon2_label.setPixmap(photo2)
        second = first + timedelta(days=1)
        self.day2_label.setText(second.strftime("%A"))

        temp_day2_min = ((json_data2["list"][1]["main"]["temp_min"]) - 273.15)
        temp_day2_max = ((json_data2["list"][1]["main"]["temp_max"]) - 273.15)
        self.temp2_label.setText(f"Min: {temp_day2_min:.2f}\nMax: {temp_day2_max:.2f}")

        # third cell
        third_day_image = json_data2['list'][2]["weather"][0]["icon"]
        photo3 = QPixmap(f"icon/{third_day_image}@2x.png").scaled(100, 100)
        self.icon3_label.setPixmap(photo3)
        third = first + timedelta(days=2)
        self.day3_label.setText(third.strftime("%A"))

        temp_day3_min = ((json_data2["list"][2]["main"]["temp_min"]) - 273.15)
        temp_day3_max = ((json_data2["list"][2]["main"]["temp_max"]) - 273.15)
        self.temp3_label.setText(f"Min: {temp_day3_min:.2f}\nMax: {temp_day3_max:.2f}")

        # fourth cell
        fourth_day_image = json_data2['list'][3]["weather"][0]["icon"]
        photo4 = QPixmap(f"icon/{fourth_day_image}@2x.png").scaled(100, 100)
        self.icon4_label.setPixmap(photo4)
        fourth = first + timedelta(days=3)
        self.day4_label.setText(fourth.strftime("%A"))

        temp_day4_min = ((json_data2["list"][3]["main"]["temp_min"]) - 273.15)
        temp_day4_max = ((json_data2["list"][3]["main"]["temp_max"]) - 273.15)
        self.temp4_label.setText(f"Min: {temp_day4_min:.2f}\nMax: {temp_day4_max:.2f}")

        # fifth cell
        fifth_day_image = json_data2['list'][4]["weather"][0]["icon"]
        photo5 = QPixmap(f"icon/{fifth_day_image}@2x.png").scaled(100, 100)
        self.icon5_label.setPixmap(photo5)
        fifth = first + timedelta(days=4)
        self.day5_label.setText(fifth.strftime("%A"))

        temp_day5_min = ((json_data2["list"][4]["main"]["temp_min"]) - 273.15)
        temp_day5_max = ((json_data2["list"][4]["main"]["temp_max"]) - 273.15)
        self.temp5_label.setText(f"Min: {temp_day5_min:.2f}\nMax: {temp_day5_max:.2f}")

        # sixth cell
        sixth_day_image = json_data2['list'][5]["weather"][0]["icon"]
        photo6 = QPixmap(f"icon/{sixth_day_image}@2x.png").scaled(100, 100)
        self.icon6_label.setPixmap(photo6)
        sixth = first + timedelta(days=5)
        self.day6_label.setText(sixth.strftime("%A"))

        temp_day6_min = ((json_data2["list"][5]["main"]["temp_min"]) - 273.15)
        temp_day6_max = ((json_data2["list"][5]["main"]["temp_max"]) - 273.15)
        self.temp6_label.setText(f"Min: {temp_day6_min:.2f}\nMax: {temp_day6_max:.2f}")

        # seventh cell
        seventh_day_image = json_data2['list'][6]["weather"][0]["icon"]
        photo7 = QPixmap(f"icon/{seventh_day_image}@2x.png").scaled(100, 100)
        self.icon7_label.setPixmap(photo7)
        seventh = first + timedelta(days=6)
        self.day7_label.setText(seventh.strftime("%A"))

        temp_day7_min = ((json_data2["list"][6]["main"]["temp_min"]) - 273.15)
        temp_day7_max = ((json_data2["list"][6]["main"]["temp_max"]) - 273.15)
        self.temp7_label.setText(f"Min: {temp_day7_min:.2f}\nMax: {temp_day7_max:.2f}")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
