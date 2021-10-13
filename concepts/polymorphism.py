from abc import abstractmethod
from dataclasses import dataclass
from multipledispatch import dispatch

@dataclass
class Box:
	name: str

	@abstractmethod
	def draw(self) -> None:
		print(f"[Box] Drawing a {self.name}")

	"""Method Overloading is Polymorphic (Compile-time Polymorphism)"""
	@dispatch()
	def capitalize_name(self) -> None:
		self.name = self.name.capitalize()

	@dispatch(int)
	def capitalize_name(self, charNumber: int) -> None:
		self.name = self.name[:charNumber].upper() + self.name[charNumber:]

"""Inheritance allows Polymorphic assignments (Run-time Polymorphism)"""
@dataclass
class Textbox(Box):
	def draw(self) -> None:
		print(f"[Textbox] Drawing a {self.name}")

@dataclass
class Radiobox(Box):	
	def draw(self) -> None:
		print(f"[Radiobox] Drawing a {self.name}")

@dataclass
class NotABox:
	def erase(self) -> None:
		print("Erasing drawings")


if __name__ == "__main__":
	box: Box = Box('box in lowercase letters')
	box.draw()

	box.capitalize_name()
	box.draw()

	box.capitalize_name(25)
	box.draw()

	box = Radiobox('Radiobox')
	box.draw()

	box = Textbox('Textbox')
	box.draw()
