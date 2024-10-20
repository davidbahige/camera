from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from plyer import camera
from kivy.core.window import Window


class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Bouton pour prendre une photo
        self.capture_button = Button(text="Prendre une photo", size_hint=(1, 0.2))
        self.capture_button.bind(on_press=self.take_picture)

        layout.add_widget(self.capture_button)
        return layout

    def take_picture(self, *args):
        # Appel de la fonction de caméra pour prendre une photo
        camera.take_picture(filename='photo.jpg', on_complete=self.camera_callback)

    def camera_callback(self, filepath):
        # Cette fonction est appelée une fois que la photo est prise
        if filepath:
            print(f"Photo enregistrée à l'emplacement : {filepath}")
        else:
            print("Échec de la prise de photo")


if __name__ == '__main__':
    CameraApp().run()
