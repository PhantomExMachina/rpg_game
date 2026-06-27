from helpers.general_effect_handler import GeneralEffectHandler as GHandler
from helpers.special_effect_handler import SpecialEffectHandler as SHandler

class EffectEngine:
    def __init__(self, context, actor):
        self.context = context
        self.actor = actor
        self.effects = context.get("effects", [])

        self.general_handler = GHandler(context, actor)
        self.special_handler = SHandler(context, actor)

    def handle_effects(self):
        results = []

        if not isinstance(self.effects, list):
            raise TypeError("effects must be a list of dictionaries")

        for effect in self.effects:
            effect_type = effect.get("type")

            if self.general_handler.can_handle(effect_type):
                result = self.general_handler.handle(effect)

            elif self.special_handler.can_handle(effect_type):
                result = self.special_handler.handle(effect)

            else:
                raise ValueError(f"Unknown effect type: {effect_type}")

            results.append(result)

        return results