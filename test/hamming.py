class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        # binx = bin(x)[2:]
        # biny = bin(y)[2:]

        # l = max(x, y)
        # binx_new = binx.zfill(l)
        # biny_new = biny.zfill(l)

        # count = 0
        # for i in range(l):
        #     if binx_new[i] != biny_new[i]:
        #         count += 1


        # return count

        xor = x ^ y

        hamming_disctance = bin(xor).count('1')

        return hamming_disctance
    

        


#Example 1
x = 1
y = 4
print(Solution().hammingDistance(x, y))