from dataclasses import dataclass

@dataclass
class Box:
	name: str
	_enabled: bool = False

	def enable(self) -> None:
		print(f"Enabling {self.name}")
		self._enabled = True

	def is_enabled(self) -> None:
		print(f"{self.name} is " + str(("not ","")[self._enabled]) + "enabled" )

@dataclass
class Textbox(Box):
	text: str = ""

@dataclass
class Radiobox(Box):
	_checked: bool = False

if __name__ == "__main__":
	print('Inheritance')

	textbox = Textbox("Textbox", text="Inheritance prevents code duplication")

	print(textbox.text)

	textbox.is_enabled()
	textbox.enable()
	textbox.is_enabled()
	
	radiobox = Radiobox("Radiobox")
	radiobox.is_enabled()
	radiobox.enable()
	radiobox.is_enabled()

