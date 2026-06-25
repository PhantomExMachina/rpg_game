
class StatCalculator:
    def __init__(self, actor):
        self.actor = actor
        self.stats = actor.get("stats", {})
    
    def calculate_physical_accuracy(self):
        """
        Physical accuracy impacts the chance of successfully landing a physical attack. Evasion is also factored in to lower the chance of a successful hit.
        """

        agility = self.stats.get("agility", 0)
        luck = self.stats.get("luck", 0)

        physical_accuracy = 75 + (agility * 0.5) + (luck * 0.2)
        return physical_accuracy
    
    def calculate_magical_accuracy(self):
        """
        Magical accuracy impacts the chance of successfully landing a spell / ability. Evasion is also factored in to lower the chance of a successful hit.
        """

        synergy = self.stats.get("synergy", 0)
        luck = self.stats.get("luck", 0)

        magical_accuracy = 75 + (synergy * 0.5) + (luck * 0.2)
        return magical_accuracy
    
    def calculate_evasion(self):
        """
        Evasion represents the odds of avoiding an attack or spell.
        """

        agility = self.stats.get("agility", 0)
        luck = self.stats.get("luck", 0)

        evasion = (agility * 0.25) + (luck * 0.1)
        return evasion
    
    def calculate_crit_chance(self):
        """
        Crit_chance represents the chance of inflicting a critical hit, which ordinarily deals 1.5x damage.
        Both regular attacks and spells / abilities can be critical hits.
        """

        luck = self.stats.get("luck", 0)

        crit_chance = 5 + luck * 0.5
        return crit_chance
    
    def calculate_resistance(self):
        """
        Resistance is the how likely the enemy status effect will fail to apply. Only applies to primary effect, not secondary/incidental status effects.
        
        - Example 1:    Entity casts Eruption, resulting in heavy fire-based damage to the entire team. Has a chance of proccing "burning", based on caster spell_proc_chance (flat percentage chance).
                        The odds of burning being applied is NOT be impacted by resistance (due to it being a secondary / incidental effect).

        - Example 2:    Entity casts Engulf, resulting in no immediate damage, but having a base 75% chance of causing "burning" for each enemy on the field.
                        The odds of burning being applied IS impacted by caster spell_proc_chance (additive percentage bonus) AND enemy resistance.
        """
        
        resolve = self.stats.get("resolve", 0)
        vitality = self.stats.get("vitality", 0)
        
        resistance = 5 + (resolve * 0.10) + (vitality * 0.10)
        return resistance
    
    def calculate_weapon_proc_chance(self):
        """
        Weapon proc chance only effects the proc chance of weapons that feature a proccable status.

        - Example: Flametongue is capable of inflicting the burning status, which is solely based on the user weapon_proc_chance stat.
        """

        strength = self.stats.get("strength", 0)
        luck = self.stats.get("luck", 0)

        weapon_proc_chance = 1 + (strength * 0.01) + (luck * 0.1)
        return weapon_proc_chance
    
    def calculate_spell_proc_chance(self):
        """
        Spell proc chance effects the proc chance of spells that feature a proccable status whether it be a primary or secondary effect

        - Example 1:    Tornado is capable of inflicting the confused status, which is solely based on the user spell_proc_chance stat, as a flat percentage.

        - Example 2:    Inhibit is only capable of inflicting the confused status, which has a base chance of succeeding after calculating spell accuracy.
                        Spell_proc_chance is factored in as an additive percent bonus to the base chance of proccing. Enemy resistance is applied thereafter.
        """

        synergy = self.stats.get("synergy", 0)
        luck = self.stats.get("luck", 0)

        spell_proc_chance = 1 + (synergy * 0.01) + (luck * 0.1)
        return spell_proc_chance
    
    def calculate_all(self):
        return {
            "physical_accuracy": self.calculate_physical_accuracy(),
            "magical_accuracy": self.calculate_magical_accuracy(),
            "evasion": self.calculate_evasion(),
            "crit_chance": self.calculate_crit_chance(),
            "resistance": self.calculate_resistance(),
            "weapon_proc_chance": self.calculate_weapon_proc_chance(),
            "spell_proc_chance": self.calculate_spell_proc_chance()
        }