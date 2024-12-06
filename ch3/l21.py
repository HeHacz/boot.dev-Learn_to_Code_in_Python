def get_punched(health = 0, armor = 0):
    damage = 50 - armor
    return health - damage

def get_slashed(health = 0, armor = 0):
    damage = 100 - armor
    return health - damage 