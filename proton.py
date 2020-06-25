# Proton JS - Proton.py
# by Acropolis Point 

# module imports
import os
import sys
# import modules from bigger modules
from gi.repository import Gtk, Gdk
from gi.repository import WebKit2 as WebKit

# set up file
webview = WebKit.WebView()
path = "start.html"
path = os.path.realpath(path)
webview.load_uri("file://" + path)

# create a window
window = Gtk.Window()
window.set_decorated(False)
window.set_default_size(1, 1)
window.add(webview)
window.show_all()

# quit function
def quit(args):
    Gtk.main_quit()
    os.system("killall flask")

window.connect("destroy", quit)

Gtk.main()
