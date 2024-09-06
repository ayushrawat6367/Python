class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = ['']*numRows
        cycleLen = 2 * numRows - 2
        
        for i, char in enumerate(s):
            row = i % cycleLen
            if row >= numRows:
                row = cycleLen - row 
            
            rows[row] += char
        
        return ''.join(rows)
    
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))
print(sol.convert("PAYPALISHIRING", 4))
print(sol.convert("A", 1))