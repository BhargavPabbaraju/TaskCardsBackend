"""
Domains
"""

from dataclasses import dataclass

from .domain_type import DomainType
from .pokemon_type import PokemonType


@dataclass
class Domain:
    """Domin represents an area of focus within the broader domain_type"""

    key: str
    name: str
    icon: str
    domain_type: DomainType
    pokemon_type: PokemonType

    def to_dict(self):
        """Serialize into JSON serializable dict"""
        return {
            "key": self.key,
            "name": self.name,
            "icon": self.icon,
            "domain_type": self.domain_type.value,
            "pokemon_type": self.pokemon_type.value,
        }


DOMAINS = [
    Domain(
        key="office",
        name="Office",
        icon="Apartment",
        domain_type=DomainType.WORK,
        pokemon_type=PokemonType.FLYING,
    ),
    Domain(
        key="work_tasks",
        name="Work tasks",
        icon="LocalFireDepartment",
        domain_type=DomainType.WORK,
        pokemon_type=PokemonType.FIRE,
    ),
    Domain(
        key="system_design",
        name="System Design",
        icon="Schema",
        domain_type=DomainType.LEARNING,
        pokemon_type=PokemonType.STEEL,
    ),
    Domain(
        key="dsa",
        name="DSA",
        icon="DataObject",
        domain_type=DomainType.LEARNING,
        pokemon_type=PokemonType.PSYCHIC,
    ),
    Domain(
        key="backend",
        name="Backend",
        icon="Memory",
        domain_type=DomainType.LEARNING,
        pokemon_type=PokemonType.ELECTRIC,
    ),
    Domain(
        key="japanese",
        name="Japanese",
        icon="EmojiNature",
        domain_type=DomainType.LEARNING,
        pokemon_type=PokemonType.FAIRY,
    ),
    Domain(
        key="cleaning",
        name="Cleaning",
        icon="CleaningServices",
        domain_type=DomainType.HOME,
        pokemon_type=PokemonType.NORMAL,
    ),
    Domain(
        key="laundry",
        name="Laundry",
        icon="LocalLaundryService",
        domain_type=DomainType.HOME,
        pokemon_type=PokemonType.WATER,
    ),
    Domain(
        key="groceries",
        name="Groceries",
        icon="LocalGroceryStore",
        domain_type=DomainType.HOME,
        pokemon_type=PokemonType.GROUND,
    ),
    Domain(
        key="cooking",
        name="Cooking",
        icon="SoupKitchen",
        domain_type=DomainType.HEALTH,
        pokemon_type=PokemonType.GRASS,
    ),
    Domain(
        key="exercise",
        name="Exercise",
        icon="FitnessCenter",
        domain_type=DomainType.HEALTH,
        pokemon_type=PokemonType.FIGHTING,
    ),
    Domain(
        key="sleep",
        name="Sleep",
        icon="Hotel",
        domain_type=DomainType.HEALTH,
        pokemon_type=PokemonType.DARK,
    ),
    Domain(
        key="hobby_dev",
        name="Hobby Dev",
        icon="GitHub",
        domain_type=DomainType.CREATIVE,
        pokemon_type=PokemonType.DRAGON,
    ),
    Domain(
        key="guitar",
        name="Guitar",
        icon="MusicNote",
        domain_type=DomainType.CREATIVE,
        pokemon_type=PokemonType.BUG,
    ),
    Domain(
        key="anime",
        name="Anime",
        icon="MovieFilter",
        domain_type=DomainType.ENTERTAINMENT,
        pokemon_type=PokemonType.POISON,
    ),
    Domain(
        key="gaming",
        name="Gaming",
        icon="SportsEsports",
        domain_type=DomainType.ENTERTAINMENT,
        pokemon_type=PokemonType.ROCK,
    ),
    Domain(
        key="finance",
        name="Finance",
        icon="Savings",
        domain_type=DomainType.REVIEW,
        pokemon_type=PokemonType.ICE,
    ),
    Domain(
        key="planning",
        name="Planning",
        icon="Savings",
        domain_type=DomainType.REVIEW,
        pokemon_type=PokemonType.GHOST,
    ),
]

DOMAIN_BY_KEY: dict[str, Domain] = {domain.key: domain for domain in DOMAINS}
