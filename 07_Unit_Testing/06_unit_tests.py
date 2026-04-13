def total_xp(level, xp_to_add):
    #100 xp per level, convert levels to xp
    current_xp = level * 100
    total_xp = xp_to_add + current_xp
    return total_xp

""" 
    if level == 1 and xp_to_add == 100:
        total_xp = 200
    elif level == 2 and xp_to_add == 250:
        total_xp = 450
    elif level == 170 and xp_to_add == 590:
        total_xp = 17590
"""