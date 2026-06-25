class EffectHandler:
    def __init__(self, context, actor):
        self.context = context
        self.actor = actor
        self.effects = context.get("effects", [])
        self.stats = actor.get("stats", {})

    def modify_stat(self, stat, operation, value):
        old_value = self.stats.get(stat, 0)

        if operation == "add":
            new_value = old_value + value
        elif operation == "subtract":
            new_value = old_value - value
        elif operation == "multiply":
            new_value = old_value * value
        else:
            raise ValueError(f"Unknown operation: {operation}")

        self.stats[stat] = new_value
        return old_value, new_value # Should I return here or directly modify the actor's stats? Stat changes are temporary.

    def no_action(self):
        pass # Unsure how to define this one.

    def immune_statuses(self, statuses):
        if statuses is None:
            return None
        
        return statuses

    def berserk_action(self):
        pass # Unsure how to define this one.

    def add_statuses(self, statuses):
        if statuses is None:
            return None
        
        return statuses

    def remove_statuses(self, statuses):
        if statuses is None:
            return None
        
        return statuses


    def handle_effects(self):

        if self.effects is None:
            return None

        for effect in self.effects:
            if effect.get("type") == "modify_stat":
                results = []

                stat = effect.get("stat")
                operation = effect.get("operation")
                value = effect.get("value")

                result = self.modify_stat(stat, operation, value)
                results.append(result)

                return results
            
            elif effect.get("type") == "no_action":
                self.no_action()
            
            elif effect.get("type") == "immune_statuses":
                statuses = effect.get("statuses", [])
                self.immune_statuses(statuses)
            
            elif effect.get("type") == "berserk_action":
                self.berserk_action()
            
            elif effect.get("type") == "add_statuses":
                statuses = effect.get("statuses", [])
                self.add_statuses(statuses)
            
            elif effect.get("type") == "remove_statuses":
                statuses = effect.get("statuses", [])
                self.remove_statuses(statuses)

            else:
                raise ValueError(f"Unknown effect type: {effect.get("type")}")
