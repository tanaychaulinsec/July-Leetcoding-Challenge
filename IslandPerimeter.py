class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                cb=4 #cb=contribution, maximum of which is 4 
                if(grid[i][j]==1):
                    if(i-1>=0 and grid[i-1][j]!=0):
                        cb-=1
                    if(j-1>=0 and grid[i][j-1]!=0):
                        cb-=1
                    if(i+1<len(grid) and grid[i+1][j]!=0):
                        cb-=1
                    if(j+1<len(grid[0]) and grid[i][j+1]!=0):
                        cb-=1
                    peri+=cb #remember to add this contribution to the actual perimeter.
        
        return peri