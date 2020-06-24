import os
import sys

from gi.repository import Gtk, Gdk
from gi.repository import WebKit2 as WebKit

webview = WebKit.WebView()
path = sys.argv[5]
path = os.path.realpath(path)
webview.load_uri("file://" + path)

scrolledWindow = Gtk.ScrolledWindow()
scrolledWindow.add(webview)

window = Gtk.Window()

if (sys.argv[3] == "false"):
    window.set_decorated(False)

window.set_default_size(int(sys.argv[1]), int(sys.argv[2]))
window.set_title(sys.argv[4])
window.set_icon_from_file(sys.argv[6])
window.add(scrolledWindow)
window.show_all()

def quit(args):
    Gtk.main_quit()
    os.system("killall flask")
window.connect("destroy", quit)

Gtk.main()