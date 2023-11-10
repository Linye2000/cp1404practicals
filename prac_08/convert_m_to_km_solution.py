"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder

__author__ = 'Lindsay Ward'

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

    def handle_increment(self, increment):
        self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + int(increment))

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) * MILES_TO_KM
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


MilesConverterApp().run()