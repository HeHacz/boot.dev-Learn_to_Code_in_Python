level = "25"
name = "Lopen"
character_class = "Windrunner"
account_active = True
pvp_rank = "Squire"
max_health = 79
max_mana = 274
armor = 12.0
magic_resistance = 15.4

print("Character Report")
print(f"{name} is a level {level} {character_class}, ranked as a {pvp_rank}.")
print(f"They have {max_health} max health and {max_mana} max mana.")
print(f"They have {armor} armor and {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

# Don't edit below this line

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"level: {type(level).__name__}, name: {type(name).__name__}, character_class: {type(character_class).__name__}"
)
print(
    f"account_active: {type(account_active).__name__}, pvp_rank: {type(pvp_rank).__name__}, max_health: {type(max_health).__name__}"
)
print(
    f"max_mana: {type(max_mana).__name__}, armor: {type(armor).__name__}, magic_resistance: {type(magic_resistance).__name__}"
)
