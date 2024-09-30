"""
The Student class is a dataclass that represents a student
with a name, grades, and a graduation status.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Student:
    """
    A class representing a student with a name, grades, and a graduation status.
    """

    name: str
    grades: List[int] = field(default_factory=list)
    graduated: bool = False
