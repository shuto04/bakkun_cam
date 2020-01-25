
from kivy.properties import ObjectProperty

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

Builder.load_file('start_screen.kv')
Builder.load_file('ask_take_photo.kv')
Builder.load_file('display_camera_image.kv')
Builder.load_file('ask_tweet_picture.kv')
Builder.load_file('end_screen.kv')
client = mqtt.Client()


class MainRoot(BoxLayout):
    start_screen = None
    ask_take_photo = None
    display_camera_image = None
    ask_tweet_picture = None
    end_screen = None
    image_texture = ObjectProperty(None)
    image_capture = ObjectProperty(None)

    def __init__(self, **kwargs):
        # 起動時に各画面を作成して使い回す
        self.start_screen = Factory.Start_screen()
        self.ask_take_photo = Factory.Ask_take_photo()
        self.display_camera_image = Factory.Display_camera_image()
        self.ask_tweet_picture = Factory.Ask_tweet_picture()
        self.end_screen = Factory.End_screen()
        super(MainRoot, self).__init__(**kwargs)

    # mqttでYes, No送る
    def send_selected_key(self, data):
        ch = data
        print(f"publish: {ch}")
        client.publish("key", ch)

    # 画面遷移のための処理たち
    # Todo:引数で遷移先を渡すかたちにする
    def go_to_start_screen(self):
        self.clear_widgets()
        self.add_widget(self.start_screen)

    def go_to_ask_take_photo(self):
        self.clear_widgets()
        self.add_widget(self.ask_take_photo)

    def go_to_display_camera_image(self):
        self.clear_widgets()
        self.add_widget(self.display_camera_image)

    def go_to_ask_tweet_picture(self):
        self.clear_widgets()
        self.add_widget(self.ask_tweet_picture)

    def go_to_end_screen(self):
        self.clear_widgets()
        self.add_widget(self.end_screen)


class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = 'UI test '

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
