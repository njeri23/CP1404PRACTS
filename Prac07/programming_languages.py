class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic=False):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage for printing."""
        return f"{self.name} ({self.year})"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def has_pointer_arithmetic(self):
        """Check if language has pointer arithmetic."""
        return self.pointer_arithmetic


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, True)  # Added pointer_arithmetic

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    print("Languages with pointer arithmetic:")
    for language in languages:
        if language.has_pointer_arithmetic():
            print(language.name)

if __name__ == "__main__":
    run_tests()
