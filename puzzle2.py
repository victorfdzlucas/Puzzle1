from puzzle1 import *
import threading
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class Window(Gtk.Window):
    def __init__(self):
        # crea la finestra
        Gtk.Window.__init__(self, title="RC522")
        self.set_default_size(400, 100)
        self.set_border_width(5)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.rf = Rfid()

        # crea el cuadre on aniràn el botó y l'ID de la targeta
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.box.set_homogeneous(False)
        self.add(self.box)

        # crea un cuadre d'event que canvia de color on apareix l'ID de la targeta
        self.eventbox = Gtk.EventBox()
        self.eventbox.override_background_color(0, Gdk.RGBA(0, 0, 8, 1))

        self.label = Gtk.Label('<span foreground="white">Please, login with your university card </span>')
        self.label.set_use_markup(True)
        self.eventbox.add(self.label)

        # Crea un botó
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.clicked)
        self.box.pack_start(self.eventbox, True, True, 0)
        self.box.pack_start(self.button, True, True, 0)

    # Funció trucada quan premem el botó
    def clicked(self, widget):
        # Torna a l'anterior label
        self.label.set_label('<span foreground="white">Please, login with your university card </span>')
        self.eventbox.override_background_color(0, Gdk.RGBA(0, 0, 8, 1))

        if threading.active_count() == 1:
            thread = threading.Thread(target=self.scan, daemon=True)
            thread.start()

    # Funció que escaneja la targeta
    def scan(self):
        self.uid = self.rf.read_uid()

        self.eventbox.override_background_color(0, Gdk.RGBA(8, 0, 0, 1))
        self.label.set_label('<span foreground="white">UID: ' + self.uid + '</span>')

def reader_main():
    finestra = Window()
    finestra.connect("destroy", Gtk.main_quit)
    finestra.show_all()

    thread = threading.Thread(target=finestra.scan, daemon=True)
    thread.start()

if __name__ == "__main__":
    reader_main()
    Gtk.main()
