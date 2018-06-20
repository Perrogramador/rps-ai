from guizero import App, Text, Slider, PushButton

class GUI:
    def __init__(self, title):
        app = App(title)
        
        h_label = Text(app, "h minimum")
        self.h_Slider = Slider(app, end=255, command=self.set_h)
        s_label = Text(app, "s minimum")
        self.s_Slider = Slider(app, end=255, command=self.set_s)
        v_label = Text(app, "v minimum")
        self.v_Slider = Slider(app, end=255, command=self.set_v)
        H_label = Text(app, "h maximum")
        self.H_Slider = Slider(app, end=255, command=self.set_H)
        S_label = Text(app, "s maximum")
        self.S_Slider = Slider(app, end=255, command=self.set_S)
        V_label = Text(app, "v maximum")
        self.V_Slider = Slider(app, end=255, command=self.set_V)

        app.display()

    def set_h(self, n):
        self.h = n
    def set_s(self, n):
        self.s = n
    def set_v(self, n):
        self.v = n
    def set_H(self, n):
        self.H = n
    def set_S(self, n):
        self.S = n
    def set_V(self, n):
        self.V = n




asd = GUI("Hello there")



