def calculate_damage(base_damage, ap, ap_ratio, resist, flat_pen, percent_pen):
    """Calculates damage dealt after mitigation."""
    effective_resist = (resist - flat_pen) * (1 - percent_pen / 100)
    damage = base_damage + (ap * ap_ratio)
    mitigated_damage = damage * (100 / (100 + effective_resist))
    return mitigated_damage

def compare_item_choices(level, current_flat_pen, mage_stats):
    """Compares the damage increase from AP vs. penetration upgrades."""

    ap_upgrade = 32.5
    flat_pen_upgrade = 7
    percent_pen_upgrade = 10

    if not 8 <= level <= 18:
        print("Invalid level. Please choose a level between 8 and 18.")
        return

    base_damage, ap_ratio = mage_stats[level - 8]
    current_ap = (3 + level)**2  # Corrected AP scaling

    # resist Calculations
    low_resist_base = 30 + 1.3 * (level - 1) * (0.7025 + 0.0175 * (level - 1))
    high_resist_base = 32 + 2.05 * (level - 1) * (0.7025 + 0.0175 * (level - 1))

    resist_values = [low_resist_base, high_resist_base, low_resist_base + 40, high_resist_base + 40, low_resist_base + 80, high_resist_base + 80, low_resist_base + 120, high_resist_base + 120]

    print(f"\nLevel: {level}")
    print("Base Damage:", base_damage)
    print("AP Ratio:", ap_ratio)
    print("Current AP:", current_ap)
    print("Current Flat Pen:", current_flat_pen)
    print("\nresist\t\t+32.5 AP Increase\t+7 Flat + 10% Pen Increase")
    print("-" * 60)

    for resist in resist_values:
        current_damage = calculate_damage(base_damage, current_ap, ap_ratio, resist, current_flat_pen, 0)
        ap_upgraded_damage = calculate_damage(base_damage, current_ap + ap_upgrade, ap_ratio, resist, current_flat_pen, 0)
        ap_increase = (ap_upgraded_damage - current_damage) / current_damage * 100

        pen_upgraded_damage = calculate_damage(base_damage, current_ap, ap_ratio, resist, current_flat_pen + flat_pen_upgrade, percent_pen_upgrade)
        pen_increase = (pen_upgraded_damage - current_damage) / current_damage * 100

        print(f"{resist:.2f}\t\t{ap_increase:.2f}%\t\t\t{pen_increase:.2f}%")

# Mage Stats Array:
mage_stats = [
    [798, 4.19],  # Level 8
    [825.71, 4.38], # Level 9
    [869.29, 4.52], # Level 10
    [889.29, 4.62], # Level 11
    [908.57, 4.7],  # Level 12
    [936.43, 4.84], # Level 13
    [957.77, 4.84], # Level 14
    [979.11, 4.84], # Level 15
    [1000.45,4.84], # Level 16
    [1021.79,4.84], # Level 17
    [1043.13,4.84]  # Level 18
]

# Example usage with the array and scaled AP:
current_flat_pen = 12

for level in range(8, 19):
    compare_item_choices(level, current_flat_pen, mage_stats)