def start_solo_match(username, region):
    return {
        "player": username,
        "region": region,
        "status": "match_found",
        "players": 1
    }
