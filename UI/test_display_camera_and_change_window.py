
import cv2
import time
from kivy.graphics.texture import Texture
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivy.app import App
from kivy.factory import Factory

from kivy.uix.boxlayout import BoxLayout

# 日本語フォント表示対応
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
import paho.mqtt.client as mqtt

resource_add_path("./UI/fonts/IPAexfont00301")
LabelBase.register(DEFAULT_FONT, 'ipaexg.ttf')

# kvファイルを画面ごとに分離してバラで読み込む
from kivy.lang import Builder

Builder.load_file('window1.kv')
Builder.load_file('window2.kv')
Builder.load_file('window3.kv')
client = mqtt.Client()


class MainRoot(BoxLayout):
    window1 = None
    window2 = None
    window3 = None
    image_texture = ObjectProperty(None)
    image_capture = ObjectProperty(None)

    def __init__(self, **kwargs):
        # 起動時に各画面を作成して使い回す
        self.window1 = Factory.Window1()
        self.window2 = Factory.Window2()
        self.window3 = Factory.Window3()
        super(MainRoot, self).__init__(**kwargs)

    # mqttでYes, No送る
    def send_selected_key(self, data):
        ch = data
        print(f"publish: {ch}")
        client.publish("key", ch)

    # 画面遷移のための処理
    def change_disp(self):
        self.clear_widgets()
        self.add_widget(self.window1)

    def change_disp2(self):
        self.clear_widgets()
        self.add_widget(self.window2)

    def change_disp3(self):
        self.clear_widgets()
        self.add_widget(self.window3)

    def play(self):
        global flg
        flg = not flg
        if flg == True:
            self.image_capture = cv2.VideoCapture(0)
            Clock.schedule_interval(self.update, 1.0 / 30)
        else:
            Clock.unschedule(self.update)
            self.image_capture.release()

    def update(self, dt):
            ret, frame = self.image_capture.read()
            if ret:
                buf = cv2.flip(frame, 0)
                image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
                image_texture.blit_buffer(buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
                camera = self.ids['camera']
                camera.texture = image_texture


    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

class MainApp(App): 
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = 'UI test '
    pass

    # keyをmqttで送るための処理
    def on_connect(client, userdata, flag, rc):
        print("Connected with result code " + str(rc))

    def on_disconnect(client, userdata, flag, rc):
        if rc != 0:
            print("Unexpected disconnection.")

    def on_publish(client, userdata, mid):
        print(f"publish #{mid}")

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish
    client.connect("localhost", 1883, 60)
    client.loop_start()

if __name__ == "__main__":
    flg = False
    MainApp().run()

