from dataclasses import dataclass

@dataclass
class Person:
	_name: str
	dateOfBirth: str

	@property
	def name(self) -> str:
		print(f"[Getting {self._name}'s name...]")
		return self._name

	@name.setter
	def name(self, newName: str) -> None:
		print(f"[Setting {self._name}'s name to {newName}...]")
		self._name = newName

@dataclass
class Programmer(Person):
	language: str = "Python"

	def program(self) -> None:
		print(f"I'm programming in {self.language}\n")

@dataclass
class Chef(Person):
	def cook(self) -> None:
		print("I'm cooking\n")


if __name__ == "__main__":
	ricardo = Person("Ricardo", "06/09/1987")

	print(ricardo.name, "\n")

	ricardo.name = "Ricardo Agra"

	print(ricardo.name, "\n")	

	"""Programmer inherits a Person's attributes and methods"""
	Programmer = Programmer("Programmer", "06/09/1987")
	Programmer.name = "Senior Programmer"
	Programmer.program()

	"""Chef inherits a Person's attributes and methods"""
	chef = Chef("Gordon", "08/10/1966")
	chef.name = "Gordon Ramsy"
	chef.cook()

	try:
		chef.program()
	except AttributeError:
		print(AttributeError)
		print("[Error: A chef doesn't program]")
		