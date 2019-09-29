# Static class to manage every input from key and mouse

from game.inputs.keyboardmanager import KeyBoardManager as kbm
from game.inputs.mousemanager import MouseManager as mm


class InputManager:
	ESCAPE = 0

	inputs = None
	type = None

	@staticmethod
	def init(inpt):
		# Reservs some inputs for player inputs
		actions = ["ECHAP"]

		InputManager.inputs = []
		InputManager.type = []
		for i in range(0, len(actions)):
			InputManager.inputs.append(inpt[actions[i]][0][1])
			InputManager.type.append(inpt[actions[i]][0][0])

	@staticmethod
	def input(inpt):
		if InputManager.type[inpt] == 0:
			return kbm.getKey(InputManager.inputs[inpt])
		else:
			return mm.getButton(InputManager.inputs[inpt])

	@staticmethod
	def inputReleased(inpt):
		if InputManager.type[inpt] == 0:
			return kbm.keyReleased(InputManager.inputs[inpt])
		else:
			return mm.buttonReleased(InputManager.inputs[inpt])

	@staticmethod
	def inputPressed(inpt):
		if InputManager.type[inpt] == 0:
			return kbm.keyPressed(InputManager.inputs[inpt])
		else:
			return mm.buttonPressed(InputManager.inputs[inpt])

	# Get state of each inputs in a table
	@staticmethod
	def getState():
		import math
		values = []
		for i in range(1, len(InputManager.inputs)):
			key = 0
			if InputManager.type[i] == 0:
				if kbm.state[InputManager.inputs[i]]:
					key += 3
				if kbm.oldState[InputManager.inputs[i]]:
					key -= 1
					key = math.fabs(key)
			else:
				if mm.state[InputManager.inputs[i]]:
					key += 3
				if mm.oldState[InputManager.inputs[i]]:
					key -= 1
					key = math.fabs(key)

			values.append(key)
		return values

	@staticmethod
	def dispose():
		kbm.dispose()
		mm.dispose()
