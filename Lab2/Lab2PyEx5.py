# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
import numpy as np

def change_matrix(matrix):
    for i in range(rows):
        for j in range(columns):
            if i > j :
                print("yes")
                matrix[i][j] = 0
            





if __name__ == "__main__":
    rows = int(input("Enter the number of rows:"))
    columns = int(input("Enter the number of columns:"))
    matrix = [[int(input()) for x in range (columns)] for y in range(rows)]

    change_matrix(matrix)

    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end= " ")
        print ()


