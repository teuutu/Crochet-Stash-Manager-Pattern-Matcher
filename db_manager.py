# db_manager.py
from crochet_data import Yarn, Pattern
import sqlite_utils

DB_NAME = 'crochet_inventory.db'
db = sqlite_utils.Database(DB_NAME)


def init_db():
    """Initializes tables and adds sample data."""

    # 1. Initialize Yarn Inventory Table
    if not db.table('yarn_inventory').exists():
        db['yarn_inventory'].create({
            "name": str,
            "weight": str,
            "hook_size_mm": float,
            "yardage": int,
            "color": str,
            "quantity": int
        }, pk="name")


    if not db.table('pattern_library').exists():
        db['pattern_library'].create({
            "name": str,
            "required_weight": str,
            "required_hook": float,
            "complexity": str,
            "instructions": str
        }, pk="name")


def add_sample_data():
    """Adds a few sample items and patterns."""

    # Sample Yarn
    db['yarn_inventory'].insert_all([
        Yarn('SoftWool Blue', 'Worsted', 5.0, 400, 'Blue', 2).__dict__,
        Yarn('Cotton Delight', 'Sport', 3.0, 250, 'Red', 3).__dict__,
        Yarn('Bulky Giant', 'Bulky', 8.0, 100, 'Gray', 1).__dict__,
    ], pk="name", replace=True)


    pattern_steps_scarf = [
        "Chain 40.",
        "Row 1: Sc in second ch from hook and in each ch across. (39 sc)",
        "Row 2: Ch 1, turn. Hdc in each sc across. (39 hdc)",
        "Repeat Row 2 until scarf reaches 60 inches."
    ]

    pattern_steps_hat = [
        "Magic Ring. Ch 2 (does not count as st). 10 dc in ring. Join.",
        "Rnd 2: Ch 2. 2 dc in each st around. (20 dc). Join.",
        "Rnd 3: Ch 2. *Dc in next st, 2 dc in next st*. Repeat * around. (30 dc). Join.",
        "Continue increasing until desired size."
    ]

    db['pattern_library'].insert_all([
        Pattern('Simple Scarf', 'Worsted', 5.0, 'Beginner', pattern_steps_scarf).__dict__,
        Pattern('Winter Hat', 'Worsted', 4.0, 'Intermediate', pattern_steps_hat).__dict__,
    ], pk="name", replace=True)

    print("Database initialized and sample data loaded.")


def get_inventory():
    """Fetches all yarn inventory."""
    return list(db['yarn_inventory'].rows)


def get_patterns():
    """Fetches all patterns."""
    return list(db['pattern_library'].rows)


if __name__ == '__main__':
    init_db()
    add_sample_data()