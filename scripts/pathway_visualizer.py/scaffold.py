from sims4.commands import Command, CommandType, CheatOutput
import services

@Command('pathway.visualize_objects', command_type=CommandType.Live)
def visualize_objects(_connection=None):
	output = CheatOutput(_connection)
	object_manager = services.object_manager()

	output("Listing all objects on the lot: ")
	for obj in object_manager.get_all_objects():
		try:
			position = obj.position
			footprint = obj.get_footprint_polygon()
			output(f"Object: {obj.definition.name}, Position: {position}, Footprint: {footprint}")
		except Exception as e:
			output(f"Could not get data for object: {obj}, Error: {e}")

			