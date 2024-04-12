"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Patience Njeri, IT@JCU
Started 30/03/2024
"""

from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

BoxLayoutDemo().run()
