import sublime
from sublime_plugin import EventListener

known_windows = []

class HideMenu(EventListener):
	def on_new(self, view):
		window = view.window()
		if not window.id() in known_windows:
			known_windows.append(window.id())
			window.run_command("toggle_menu")

def plugin_loaded():
	for window in sublime.windows():
		known_windows.append(window.id())
