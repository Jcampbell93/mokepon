class ElementalType:
    STRENGTH_MAPPING = {
        "fire": {
            "strengths": ['grass'],
            "weaknesses": ['rock', 'water']
        },
        "water": {
            "strengths": ['fire'],
            "weaknesses": ['grass']
        },
        "rock": {
            "strengths": ['fire'],
            "weaknesses": ['water', 'grass']
        },
        "grass": {
            "strengths": ['water', 'rock'],
            "weaknesses": ['fire']
        },
        "normal": {
            "strengths": [],
            "weaknesses": ['rock']
        },
        "electric": {
            "strengths": ['water'],
            "weaknesses": ['rock']
        },
    }

    def __init__(self, name: str):
        self.name = name
        self.strengths = self.STRENGTH_MAPPING[name]["strengths"]
        self.weaknesses = self.STRENGTH_MAPPING[name]["weaknesses"]


class Mokepon:
    def __init__(self, name: str, health: int, damage: int, elemental_type: type(ElementalType)):
        self.name = name
        self.health = health
        self.damage = damage
        self.is_alive = True
        self.elemental_type = elemental_type

    def take_damage(self, damage: int, damage_type):
        damage_multiplier = 1

        if damage_type in self.elemental_type.strengths:
            damage_multiplier = 0.5

        elif damage_type in self.elemental_type.weaknesses:
            damage_multiplier = 2

        self.health = self.health - damage * damage_multiplier
        if self.health <= 0:
            self.is_alive = False
