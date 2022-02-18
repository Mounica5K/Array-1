 #TC : O(mxn); m = rows and n = columns
 #SC: O(1)
  
  def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        idx = 0
        res = [0]*m*n
        row, col = 0, 0
        dirc = 1
        
        while idx<m*n:
            res[idx]=mat[row][col]
            idx += 1
            #MoveRight
            if(dirc == 1):
                if(col == n-1):
                    row += 1
                    dirc = 0
                elif(row == 0):
                    col += 1
                    dirc = 0
                else:
                    row -= 1
                    col += 1
            # MoveDown   
            elif(dirc == 0):
                if(row == m-1):
                    col += 1
                    dirc = 1
                elif(col == 0):
                    row += 1
                    dirc = 1
                else:
                    row += 1
                    col -= 1
        return res
