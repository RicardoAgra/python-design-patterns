from dataclasses import dataclass, field
from inheritance import Box, Radiobox, Textbox
from typing import List


@dataclass
class Canvas:
	_box: Box
	
	@property
	def box(self)->Box:
		return self._box
	
	@box.setter
	def box(self, new_box: Box) -> None:
		self._box = new_box
	
	def draw(self):
		self.box.draw()

if __name__ == '__main__':
	"""Canvas provides a draw method that relies on an internal variable."""
	"""By using polymorphism, we can provide different behaviours while  """
	"""avoiding nested logical jumps."""

	canvas = Canvas(Textbox('Textbox'))

	canvas.draw()

	canvas.box = Radiobox('Radiobox')

	canvas.draw()
