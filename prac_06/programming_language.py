class ProgrammingLanguage:
    def __init__(self, field, typing, reflection, year):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.lower() == "dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}."
