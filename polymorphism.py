from dataclasses import dataclass

@dataclass
class Person:
	_name: str
	dateOfBirth: str

	@property
	def name(self) -> str:
		return self._name

	@name.setter
	def name(self, newName: str) -> None:
		print("Setting name")
		self._name = newName

@dataclass
class Programer(Person):
	language: str = "Python"

	def program(self) -> None:
		print(f"I'm programing in {self.language}")

@dataclass
class Chef(Person):
	def cook(self) -> None:
		print("I'm cooking")


if __name__ == "__main__":
	person = Person("Ricardo", "06/09/87")

	person.name = "Ricardo Agra"
	person.dateOfBirth = "06/09/1987"

	print(person.name, person.dateOfBirth)

	"""Programer inherits a Person's functionality"""
	programer = Programer("Ricardo", "06/09/1987")
	programer.name = "Ricardo Agra"
	programer.program()

	"""Chef inherits a Person's functionality"""
	chef = Chef("Gordon", "08/10/1966")
	chef.name = "Gordon Ramsy"
	chef.cook()

	try:
		chef.program()
	except Exception:
		print(Exception)
		print("A chef doesn't program")
		