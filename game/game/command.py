# Class to apply command to control the game


class Command:

	@staticmethod
	def command(command):
		try:
			args = command.split(" ")
			getattr(Command, args[0])(args)
		except Exception as e:
			print("\n[COMMAND] Error on command " + command + "()")
			print(e)

	@staticmethod
	# 1 = functionName
	def help(args="none"):
		commandsHelp = {
			"help": "Usage: help {functionName}\n  Shows how to use a function\n  No argument: displays the list of available functions"
		}
		if not args == "none":
			if args[1] in commandsHelp:
				print("\n:::: Help for command " + args[1] + "() ::::")
				print(commandsHelp[args[1]] + "\n")
			else:
				print("[COMMAND] Error : No command called \"" + args[1] + "()\"")
		else:
			print("\n:::: Commands list ::::")
			for key, value in commandsHelp.items():
				print(key + "\n" + commandsHelp[key] + "\n")