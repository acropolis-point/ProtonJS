import os
import sys

from gi.repository import Gtk, Gdk
from gi.repository import WebKit2 as WebKit

webview = WebKit.WebView()
path = "start.html"
path = os.path.realpath(path)
webview.load_uri("file://" + path)

window = Gtk.Window()
window.set_decorated(False)
window.set_default_size(1, 1)
window.add(webview)
window.show_all()

def quit(args):
    Gtk.main_quit()
    os.system("killall flask")

window.connect("destroy", quit)

Gtk.main()
