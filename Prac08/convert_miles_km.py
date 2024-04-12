"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Patience Njeri, IT@JCU
Started 30/03/2024
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesToKmConverter(App):
    km_output = StringProperty("0.0")

    def build(self):
        return Builder.load_file("convert_miles_km.kv")

    def handle_increment(self, value):
        try:
            miles = float(self.root.ids.miles_input.text)
        except ValueError:
            miles = 0.0
        miles += value
        self.root.ids.miles_input.text = str(miles)
        self.calculate_km()

    def calculate_km(self):
        try:
            miles = float(self.root.ids.miles_input.text)
        except ValueError:
            miles = 0.0
        km = miles * MILES_TO_KM
        self.km_output = str(km)

    def handle_text_input(self, text):
        self.calculate_km()

MilesToKmConverter().run()
