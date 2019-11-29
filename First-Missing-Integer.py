class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        l = [None] * (len(A) + 1)
        for i in range(len(A)):
            if A[i] > 0 and A[i] <= len(A):
                l[A[i]] = 1


        for i in range(1, len(l)):
            if l[i] != 1:
                return i

        return (len(A) + 1)