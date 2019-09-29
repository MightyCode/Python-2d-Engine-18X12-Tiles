# Static class to load entity from args

class LoadEntity:

	entities = {
	}

	@staticmethod
	def instance(args):
		# If the instance complete without problem
		try:
			if args[0] in LoadEntity.entities:
				return ["True", LoadEntity.entities[args[0]](args)]
			else:
				return ["False", "This type of entity doesn't exist"]
		except Exception as e:
			return ["False", e]
