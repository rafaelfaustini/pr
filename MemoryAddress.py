from enum import Enum
class MemoryAddress(Enum):
    INFLATION = int("4203B498", 16)
    INTEREST = int("4203B7E0", 16)
    GROWTH = int("4204B87C", 16)
    UNEMPLOYMENT = int("42060388", 16)
    POVERTY = int("42051044", 16)