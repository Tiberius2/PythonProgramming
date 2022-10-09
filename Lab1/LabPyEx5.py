# Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order



def spiralOrder (matrix): 
    ans = []
    

    if (len(matrix) == 0):
        return ans
    
    m = len(matrix)

    marked = [[0 for i in range(m)] for j in range(m)]   # Aici se creeaza o matrice de verificare elemente vizitate de marime m*n

    direction_row = [0, 1, 0, -1]
    direction_column = [1, 0, -1, 0]
    x = 0
    y = 0
    dir = 0

    for i in range(m * m) :
        ans.append(matrix[x][y])
        marked[x][y] = True

        current_row = x + direction_row[dir]
        current_column = y + direction_column[dir]

        if (0 <= current_row  and current_row < m and 0 <=current_column and current_column < m and not(marked[current_row][current_column])) :
            x = current_row
            y = current_column
        else :
            dir = (dir + 1) % 4
            x += direction_row[dir]
            y += direction_column[dir]
    return ans

if __name__ == "__main__":
    matrix = [['f', 'i', 'r','s'], 
              ['n', '_','l', 't'], 
              ['o', 'b','a' ,'_'],
              ['h','t', 'y', 'p']]

    for v in spiralOrder(matrix) :
        print (v, end="")
    print




