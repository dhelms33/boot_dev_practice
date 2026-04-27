def take_magic_damage(health, resist, amp, spell_power):
    """ 
    First, calculate the total maximum damage to be inflicted by multiplying the spell_power by the amp. Then, subtract the resist from the total damage to get the actual damage dealt. Apply that damage to the player's health and return the new health.
    """
    max_damage = spell_power * amp
    total_damage = max_damage - resist
    new_health = health - total_damage

    if new_health >= 0:
        return new_health
    else:
        return("You are dead, you health is ", new_health)
    return new_health