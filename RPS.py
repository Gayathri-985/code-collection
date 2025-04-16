import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # First few moves
    if len(opponent_history) < 5:
        return "R"

    # Build a string from the last 5 opponent moves
    sequence = "".join(opponent_history[-5:])

    # Optional: Recognize common patterns and respond
    responses = {
        "RRRRR": "P",
        "PPPPP": "S",
        "SSSSS": "R",
        "RPSRP": "S",
        "PSRPS": "R",
    }

    for pattern, move in responses.items():
        if pattern in sequence:
            return move

    # Frequency analysis to guess opponent’s most likely next move
    counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        if move in counts:
            counts[move] += 1

    # Predict the opponent's next move is their most frequent move so far
    prediction = max(counts, key=counts.get)

    # Counter their likely move
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[prediction]
