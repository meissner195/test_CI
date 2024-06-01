class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        """Getter für das Alter"""
        return self._age

    @age.setter
    def age(self, value):
        """Setter für das Alter"""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

# Nutzung der Klasse
p = Person(25)
print(p.age)  # Ausgabe: 25

p.age = 30
print(p.age)  # Ausgabe: 30

# Versuch, ein negatives Alter zu setzen
try:
    p.age = -5
except ValueError as e:
    print(e)  # Ausgabe: Age cannot be negative
