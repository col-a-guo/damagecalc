def calculate_damage(base_damage, ap, ap_ratio, mr, flat_pen, percent_pen):
    """Calculates damage dealt after mitigation."""
    effective_mr = (mr - flat_pen) + (1 - percent_pen / 100)
    damage = base_damage * (1 + ap * ap_ratio / 100)
    mitigated_damage = damage * (100 / (100 + effective_mr))
    return mitigated_damage

def compare_item_choices(base_damage, ap_ratio, current_ap, current_flat_pen, mr_values):
    """Compares the damage increase from AP vs. penetration upgrades."""

    ap_upgrade = 32.5
    flat_pen_upgrade = 7
    percent_pen_upgrade = 10

    print("Base Damage:", base_damage)
    print("AP Ratio:", ap_ratio)
    print("Current AP:", current_ap)
    print("Current Flat Pen:", current_flat_pen)
    print("\nMR\t\t+32.5 AP Increase\t+7 Flat + 10% Pen Increase")
    print("-" * 60)

    for mr in mr_values:
        current_damage = calculate_damage(base_damage, current_ap, ap_ratio, mr, current_flat_pen, 0)
        ap_upgraded_damage = calculate_damage(base_damage, current_ap + ap_upgrade, ap_ratio, mr, current_flat_pen, 0)

        ap_increase = (ap_upgraded_damage - current_damage) / current_damage * 100

        pen_upgraded_damage = calculate_damage(base_damage, current_ap, ap_ratio, mr, current_flat_pen + flat_pen_upgrade, percent_pen_upgrade)
        pen_increase = (pen_upgraded_damage - current_damage) / current_damage * 100

        print(f"{mr:.2f}\t\t{ap_increase:.2f}%\t\t\t{pen_increase:.2f}%")

# Example usage (using the values from our discussion):
base_damage = 500
ap_ratio = 2.5907
current_ap = 150
current_flat_pen = 12
mr_values = [33.5, 40.75, 53.5, 60.75]

compare_item_choices(base_damage, ap_ratio, current_ap, current_flat_pen, mr_values)

#Example with different base damage and ap ratios
base_damage = 300
ap_ratio = 1.8
current_ap = 100
current_flat_pen = 6
mr_values = [30, 45, 60, 75]
compare_item_choices(base_damage, ap_ratio, current_ap, current_flat_pen, mr_values)