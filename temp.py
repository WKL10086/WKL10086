import json

# Create a dictionary with uppercase letter keys and empty string values
game_state = {chr(i): "" for i in range(ord("A"), ord("Z") + 1)}

# Write the dictionary to a JSON file
with open("game_state.json", "w") as f:
    json.dump(game_state, f)
