from kivymd.app import MDApp
from kivy.lang import Builder


kv = """
Screen:
	MDBoxLayout:
		orientation:"vertical"
		MDLabel:
			text:"Hello world!"
			color:"red"
			halign:"center"
		MDBoxLayout:
			background_color:1,1,0,1
			MDLabel:
				text:"this is my first App."
				font_size:dp(20)
				color:0,0,0,1
				halign:"center"
"""

class MYApp(MDApp):
	def build(self):
		return Builder.load_string(kv) 
		
if __name__ == "__main__":
	MYApp().run()