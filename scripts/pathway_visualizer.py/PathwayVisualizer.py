from debugvis import Context
from sims4.math import Vector3
import services
from sims4.commands import Command, CommandType

overlay_active = False #Global toggle flag

@Command('pathway.toggle_overlay', command_type=CommandType.Live)
def toggle_overlay(_connection=None):
	global overlay_active
	output = services.get_command_output(_connection)
	object_manager = services.object_manager()

	if overlay_active:
		overlay_active = False
		output("Overlay turned OFF.")
		return
		
	overlay_active = True
	output("Overlay turned ON.")

	origion = Vector3(0, 0, 0) #may change later
	grid_size = 10
	spacing = 1.0

	with Context('PathwayGrid', _connection) as context:
		for x in range(grid_size):
			for z in range(grid_size):
				point = origin + Vector3(x * spacing, 0, z * spacing)

				blocked = False
				for obj in object_manager.get_all_objects():
						if hasattr(obj, 'footprint_component') and obj.footprint_component is not None:
							if obj.footprint_component.get_is_routing_obstacle(): 
								if(point - obj.position).magnitude() < 1.0:
									blocked  = True
									break

				if blocked: 
					Context.draw_line(point, point + Vector3(0, 1, 0), color=(255, 0, 0)) #red
				else:
					context.draw_line(point, point + Vector3(0, 1, 0), color=(0, 255, 0)) #green
		output("Grid overlay drawn.")