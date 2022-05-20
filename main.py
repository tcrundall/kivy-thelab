"""
https://youtu.be/l8Imtec4ReQ?t=6224
"""
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
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
    count_enabled = BooleanProperty(False)

    default_slider_val = NumericProperty(50)
    # slider_value_txt = StringProperty(str(default_slider_val.defaultvalue))

    textbox_contents = StringProperty("")

    def on_button_click(self):
        print(self.count_enabled)
        if self.count_enabled:
            self.cnt += 1
            self.fsize += 10

            self.font_size = f"{self.fsize}dp"
            self.my_text = str(self.cnt)

    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True
        print(self.count_enabled)

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

#     def on_slider_value(self, widget):
#         print("Slider: ", str(int(widget.value)))
#         # self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.textbox_contents = widget.text


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
