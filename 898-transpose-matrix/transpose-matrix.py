class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        

        rows=len(matrix)

        columns=len(matrix[0])

        new_matrix=[]


        for c in range(columns):

            row=[]

            for r in range(rows):

                row.append(matrix[r][c])

            new_matrix.append(row)

        return new_matrix