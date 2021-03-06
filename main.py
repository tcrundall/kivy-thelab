"""
https://youtu.be/l8Imtec4ReQ?t=8491
"""
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.properties import Clock
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


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class CanvasExample3(Widget):
    pass


class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 200, 200), width=30)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(500, 300, 100, 150), width=2)
            self.rect = Rectangle(pos=(200, 400), size=(150, 100))

    def on_button_click(self):
        print(self.get_right())
        print(self.width)
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)


        diff = self.width - (x + w)
        if diff < inc:
            inc = diff

        x += inc
        # x = min(x, self.width - w)
        self.rect.pos = (x, y)


class CanvasExample5(Widget):
    accel = dp(-0.1)
    vx = dp(10)
    vy = dp(-4)
    positioned = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        with self.canvas:
            self.ball = Ellipse(
                pos=(self.center_x, self.center_y),
                size=(self.ball_size, self.ball_size),
            )
            Color(rgba=(1,0,0,0.5))
            self.marker = Ellipse(
                pos=(self.center_x, self.center_y),
                size=(self.ball_size, self.ball_size),
            )
        Clock.schedule_interval(self.update, 1/60.)

    def on_size(self, *args):
        if not self.positioned:
            x, y = self.center
            w, h = self.ball.size
            self.ball.pos = (x - w/2, y - h/2)
            self.marker.pos = (x - w/2, y - h/2)
        self.positioned = True
    
    def update(self, dt):
        print("updating!")
        # self.ball.pos = (x+dp(10), y)
        x, y = self.ball.pos
        w, h = self.ball.size
        
        x += self.vx
        y += self.vy
        if x < 0:
            self.vx *= -1
            x *= -1
        if y < 0:
            self.vy *= -1
            y *= -1

        diff_x = self.width - (x+w)
        if diff_x < 0:
            self.vx *= -1
            x += 2 * diff_x

        diff_y = self.height - (y+h)
        if diff_y < 0:
            self.vy *= -1
            y += 2 * diff_y
        self.vx += self.accel
        self.vy += self.accel

        self.ball.pos = (x, y)


class CanvasExample6(Widget):
    pass


class CanvasExample7(BoxLayout):
    pass


TheLabApp().run()
