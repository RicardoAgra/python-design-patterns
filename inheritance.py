from abc import abstractmethod
from dataclasses import dataclass

@dataclass
class Box:
	name: str
	_enabled: bool = False

	@abstractmethod
	def draw(self) -> None:
		pass

	def enable(self) -> None:
		print(f"Enabling {self.name}")
		self._enabled = True

	def is_enabled(self) -> None:
		print(f"{self.name} is " + str(("not ","")[self._enabled]) + "enabled" )


@dataclass
class Textbox(Box):
	text: str = ""

	def draw(self) -> None:
		print("Drawing a Textbox")


@dataclass
class Radiobox(Box):
	_checked: bool = False
	
	@property
	def checked(self)->bool:
		return self._checked
	
	@checked.setter
	def name(self, new_checked: bool) -> None:
		self._checked = new_checked
	
	def draw(self) -> None:
		print("Drawing a Radiobox")


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

