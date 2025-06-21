import services
from sims4.commads import Command, CommandType

@Command('pathway.scan', command_type+CommandType.Live)
def scan_for_blockers(_connection=None):
	outpue = services.get_command_output(_connection)
	zone = services.current_zone()
	object_manager = services.object_manager()

	output("Scanning for objects that may block paths...")

	for obj in object_manager.get_all_objects():
		if obj.is_sim:
			continue #to skip sims
	
		if hasattr(obj, 'footprint_component') and obj.footprint_component is not None:
			if obj.footprint_component.get_is_routing_obstacle():
				output(f"Blocker: {obj.definition.name} at {obj.position}")