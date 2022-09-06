from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class miles_to_kilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        Window.size = (800, 400)
        return self.root

    def handle_increment(self, convert):
        value = self.get_miles() + convert
        self.root.ids.input_miles.text = str(value)
        self.calculate_user_input()

    def get_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0

    def calculate_user_input(self):
        miles_to_km = 1.60934
        value = self.get_miles()
        result = value * miles_to_km
        self.root.ids.output_label.text = str(result)

miles_to_kilometers().run()