#4. Write a function that receives as a parameters a list of musical notes (strings),
#  a list of moves (integers) and a start position (integer).
#  The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
# 	Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"] 

def musical_function(m_notes: list[str], m_moves: list[int], m_start_pos: int) -> list[str]:
    musical_result : list[str] = []
    index = m_start_pos
    for move in m_moves:
        musical_result.append(m_notes[index])
        index += move
        index %= len(m_notes)
    musical_result.append(m_notes[index])
    return musical_result


print(musical_function(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))