# crochet_analyzer.py
from db_manager import get_inventory, get_patterns
import json
from crochet_data import Pattern


def find_matching_patterns(inventory, patterns):
    """
    Finds patterns that can be made with the current inventory.
    This demonstrates simple matching logic.
    """
    matches = []


    parsed_patterns = []
    for p in patterns:
        try:

            p['instructions'] = json.loads(p['instructions'].replace("'", '"'))
        except json.JSONDecodeError:

            p['instructions'] = [p['instructions']]


        parsed_patterns.append(Pattern(**p))

    for pattern in parsed_patterns:
        required_weight = pattern.required_weight
        required_hook = pattern.required_hook


        for item in inventory:
            if (item['weight'] == required_weight and
                    item['hook_size_mm'] >= required_hook and
                    item['yardage'] * item['quantity'] > 300):


                analysis = {
                    "pattern_name": pattern.name,
                    "yarn_used": f"{item['quantity']} skeins of {item['name']}",
                    "complexity": pattern.complexity,
                    "estimated_stitches": pattern.get_total_stitches(),
                    "notes": f"Match found using {item['name']}. Total stitches analyzed: {pattern.get_total_stitches()}"
                }
                matches.append(analysis)
                break

    return matches


def main_analysis():
    inventory = get_inventory()
    patterns = get_patterns()

    print("--- Yarn Inventory ---")
    for item in inventory:
        print(f"* {item['quantity']}x {item['name']} ({item['weight']}, {item['yardage']}yds)")

    print("\n--- Running Pattern Matcher ---")
    matches = find_matching_patterns(inventory, patterns)

    if matches:
        print(f"\n✅ Found {len(matches)} potential projects:")
        for match in matches:
            print(f"\n** Pattern: ** {match['pattern_name']}")
            print(f"   -> Required Yarn: {match['yarn_used']}")
            print(f"   -> Complexity: {match['complexity']}")
            print(f"   -> Stitch Estimate: {match['estimated_stitches']} (Simple Count)")
    else:
        print("\n❌ No patterns match your current inventory requirements.")


if __name__ == '__main__':
    main_analysis()