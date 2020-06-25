import os
import sys
import json

from gi.repository import GLib
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
window.connect("destroy", quit)

def checkClose():
    theFile = open("output.json", "r")
    theFileParsed = json.load(theFile)
    if (theFileParsed['close'] == sys.argv[4]):
        Gtk.main_quit()
GLib.timeout_add(100, checkClose)

Gtk.main()
