import globals

class Event_Handler():
    def __init__(self, level):
        self.current_level = level
        self.all_events = []

    #loops through all current events and take care of them. Remove that event from the list.
    #TODO: find a way to make level specific events handled by the level object
    def update(self):
        handled_events = []
        for index, event in enumerate(self.all_events):
            if event == "charecter killed":
                if self.current_level.number == 2:
                    if self.current_level.player.hp > 0 and self.current_level.player.hp < self.current_level.player.max_hp:
                        self.current_level.add_text("The cookie will make you feel better", globals.SCREEN_WIDTH/2, globals.SCREEN_TOP + 400)
                        self.current_level.current_text += 1
                        handled_events.append(index)
                    elif self.current_level.player.hp < 0:
                        self.current_level.add_text("Better luck next time", globals.SCREEN_WIDTH/2, globals.SCREEN_TOP + 400)
                        self.current_level.current_text += 1
                        handled_events.append(index)
                    else:
                        self.current_level.add_text("Nice", globals.SCREEN_WIDTH/2, globals.SCREEN_TOP + 400)
                        self.current_level.current_text += 1
                        handled_events.append(index)
        
        for event_to_remove in handled_events:
            self.all_events.pop(event_to_remove)
    
    # a method that other objects can call on the event handler to add an event to the queue
    def throw_event(self, event):
        self.all_events.append(event)
        
    
    