from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class DynamicLabels(App):
    status_text = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.name_to_phone:
            labels = Label(text="{names} {phone}".format(names=name, phone=self.name_to_phone[name]))
            self.root.ids.main.add_widget(labels)



DynamicLabels().run()