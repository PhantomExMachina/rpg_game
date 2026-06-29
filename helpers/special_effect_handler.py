class SpecialEffectHandler():
    def __init__(self, context, actor):
        self.context = context
        self.actor = actor

        self.effects = context.get("effects", [])
        self.stats = actor.get("stats", {})

    # Game mechanics and complex effect-handling functions here



        def berserk_action(self):
            pass # Unsure how to define this one.

        def poison(self):
            max_health = self.stats.get("max_health", 0)
            damage = max_health * 0.95
            
            current_health = current_health - damage

            

