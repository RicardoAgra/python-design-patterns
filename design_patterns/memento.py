from collections import deque 
from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar

from ..concepts.polymorphism import Chef, Person, Programer

T = TypeVar("T")

class ActionType(Enum):
	UNDO = 0
	ADD = 1

@dataclass
class Memento(Generic[T]):
	stack: deque([T]) = deque([])
	_actions: deque((ActionType, T)) = deque([])
	
	@property
	def actions(self)->deque:
		return self._actions
	
	@actions.setter
	def name(self, new_actions: deque([T])) -> None:
		self._actions = new_actions

	def addAction(self, action: T) -> None:
		self._actions.append((ActionType.ADD, T))
		self.stack.append(action)
	
	def undo(self) -> None:
		if len(self._actions) == 0:
			print("Error [Memento.undo]: no actions")
			return
		
		previous_action = self.stack.pop()
		self._actions.append((ActionType.UNDO, previous_action))

	def redo(self) -> None:
		if len(self._actions) == 0:
			print("Error [Memento.redo]: no actions")
			return

		previous_action = self._actions[-1]

		if previous_action[0] == ActionType.ADD:
			print("Error [Memento.redo]: previous action is not an UNDO")

		else:
			self.actions.append((ActionType.ADD, previous_action[1]))
			self.stack.append(previous_action[1])

	def print_stack(self) -> T:
		return '\"' + ''.join(str(self.stack)) + '\"'


if __name__ == '__main__':
	person_memento = Memento[Person]()

	person_memento.redo()
	print("Stack after redo: " + person_memento.print_stack() + "\n")

	person_memento.undo()
	print("Stack after undo: " + person_memento.print_stack() + "\n")

	person_memento.addAction(Programer("1", "", "Python"))
	print("Stack after addAction: " + person_memento.print_stack() + "\n")

	person_memento.addAction(Chef("2", ""))
	print("Stack after addAction: " + person_memento.print_stack() + "\n")

	person_memento.undo()
	print("Stack after undo: " + person_memento.print_stack() + "\n")

	person_memento.redo()
	print("Stack after redo: " + person_memento.print_stack() + "\n")

	person_memento.redo()
	print("Stack after redo: " + person_memento.print_stack() + "\n")

	person_memento.addAction(Programer("3", "", "JavaScript"))
	print("Stack after addAction: " + person_memento.print_stack() + "\n")

	person_memento.addAction(Programer("4", "", "TypeScript"))
	print("Stack after addAction: " + person_memento.print_stack() + "\n")

	person_memento.addAction(Chef("5", ""))
	print("Stack after addAction: " + person_memento.print_stack() + "\n")

	person_memento.addAction(Chef("6", ""))
	print("Stack after addAction: " + person_memento.print_stack() + "\n")

	person_memento.undo()
	print("Stack after undo: " + person_memento.print_stack() + "\n")

	person_memento.undo()
	print("Stack after undo: " + person_memento.print_stack() + "\n")

	person_memento.redo()
	print("Stack after redo: " + person_memento.print_stack() + "\n")

	person_memento.undo()
	print("Stack after undo: " + person_memento.print_stack() + "\n")





