from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    my_text = StringProperty("0")
    fsize = 70
    font_size = StringProperty(f"{fsize}dp")
    cnt = 0
    toggle_state = "normal"

    def on_button_click(self):
        self.cnt += 1
        if self.toggle_state == "normal":
            self.fsize += 10
        else:
            self.fsize -= 10

        self.font_size = f"{self.fsize}dp"
        # self.my_text = f"Clicked {self.cnt} time{'' if self.cnt == 1 else 's'}!"
        self.my_text = str(self.cnt)

    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
        else:
            widget.text = "ON"
        # print("toggled ", widget.state)
        self.toggle_state = widget.state


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'lr-tb'
        for i in range(1, 100):
            size = dp(100)
            b = Button(
                text=str(i),
                size_hint=(None, None),
                size=(size, size)
            )
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    """
    def __init__(self, **kwargs):
        # required for internal kivy usage
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    """


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
