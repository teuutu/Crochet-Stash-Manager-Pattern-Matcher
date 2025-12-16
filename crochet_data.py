# crochet_data.py

class Yarn:
    """Represents a single type or skein of yarn in the inventory."""

    def __init__(self, name, weight, hook_size_mm, yardage, color, quantity=1):
        self.name = name
        self.weight = weight  
        self.hook_size_mm = hook_size_mm
        self.yardage = yardage
        self.color = color
        self.quantity = quantity

    def __repr__(self):
        return (f"Yarn('{self.name}', Weight: {self.weight}, Hook: {self.hook_size_mm}mm, "
                f"Qty: {self.quantity}, Total Length: {self.yardage}yds)")


class Pattern:
    """Represents a pattern with its requirements and instructions."""

    def __init__(self, name, required_weight, required_hook, complexity, instructions):
        self.name = name
        self.required_weight = required_weight
        self.required_hook = required_hook
        self.complexity = complexity
        self.instructions = instructions

    def get_total_stitches(self):
        """Simple analysis function: counts common stitch abbreviations."""
        total_stitches = 0


        stitch_abbreviations = ['sc', 'dc', 'tr', 'hdc']


        for step in self.instructions:
            for abbrev in stitch_abbreviations:
                total_stitches += step.lower().count(abbrev)

        return total_stitches