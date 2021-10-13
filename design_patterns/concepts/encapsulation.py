from abc import abstractmethod
from dataclasses import dataclass

class InformalUserInterface:
	@abstractmethod
	def say_hello(self) -> str:
		pass

	@abstractmethod
	def get_age(self) -> int:
		pass

	@abstractmethod
	def set_age(self, new_age: int) -> None:
		pass


@dataclass
class User(InformalUserInterface):
	"""Class for registering an user"""
	first_name: str
	last_name: str
	_age: int = float('inf')

	"""This methods internal procedures can be changed without affecting it's dependencies"""
	def say_hello(self) -> str:
		return f"Hello, my name is {self.first_name} {self.last_name}, I am pleased to meet you!"
	
	@property
	def age(self)->int:
		return self._age
	
	@age.setter
	def name(self, new_age: int) -> None:
		if new_age < 0:
			return
		self._age = new_age


if __name__ == "__main__":
	new_user = User("Ricardo", "Agra")

	print(new_user.say_hello(), '\n')

	print("User's age is:", new_user.get_age(), '\n')