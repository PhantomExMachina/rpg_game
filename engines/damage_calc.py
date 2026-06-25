class DamageCalc():
    def __init__(self, attacker, target, context):
        self.attacker = attacker
        self.target = target
        self.context = context
        

    def calculate(self):
        damage_type = self.context.get("damage_type", "physical")

        if damage_type == "physical":
            return self._calculate_physical_damage()
        
        if damage_type == "magical":
            return self._calculate_magical_damage()
        
        if damage_type == "true":
            return self._calculate_true_damage()
        
        raise ValueError(f"Unknown damage type: {damage_type}")
    
    def _calculate_physical_damage(self):
        power = self.context.get("power", 0)
        multiplier = self.context.get("multiplier", 1.0)

        attack = self.attacker.get_stat("strength")
        defense = self.target.get_stat("defense")

        raw_damage = (attack * multiplier) + power - defense

        return max(1, int(raw_damage))
    
    def _calculate_magical_damage(self):
        power = self.context.get("power", 0)
        multiplier = self.context.get("multiplier", 1.0)

        magic_attack = self.attacker.get_stat("synergy")
        magic_defense = self.target.get_stat("resolve")

        raw_damage = (magic_attack * multiplier) + power - magic_defense

        return max(1, int(raw_damage))
    
    def _calculate_true_damage(self):
        power = self.context.get("power", 1)
        return max(1, int(power))
