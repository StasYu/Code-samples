players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}


updated_players = tuple([i_keys + i_val for i_keys, i_val in players.items()])
print(updated_players)