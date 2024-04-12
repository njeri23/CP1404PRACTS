"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Patience Njeri, IT@JCU
Started 30/03/2024
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class DynamicLabelsApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # List of names
        names = ['John', 'Alice', 'Bob', 'Eve']

        # Dynamically create Labels for each name
        for name in names:
            label = Label(text=name)
            root.add_widget(label)

        return root


if __name__ == "__main__":
    DynamicLabelsApp().run()
