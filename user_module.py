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
	age: int = 0

	def say_hello(self) -> str:
		return f"Hello, my name is {self.first_name} {self.last_name}, I am pleased to meet you!"

	def get_age(self) -> int:
		return self.age

	def set_age(self, new_age: int) -> None:
		self.age = new_age
