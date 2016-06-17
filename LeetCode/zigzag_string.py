class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        ret_str = ""

        str_arr = list(A)

        #arr = [[0] * int(len(A) / int(B))] * 5
        arr = []
        for i in range(B):
            arr.append([])
            #print(i)

        # Loop through string array
        cur_row = 0
        decreasing = False
        while len(str_arr) > 0:
            if B <= 1: cur_row = 0
            # Take first letter and push onto appropriate row
            cur_letter = str_arr.pop(0)
            for i in range(B): # Increment row counter, until row hits B, then start over
                #print("Cur_row:%d" % cur_row)
                if cur_row == i: arr[cur_row].append(cur_letter)
                else: arr[i].append('.')


            if decreasing: # Decreasing row
                if cur_row <= 0:
                    decreasing = not decreasing
                    cur_row+=1
                else: cur_row-=1
            else: # Increasing row
                if cur_row >= B - 1:
                    decreasing = not decreasing
                    cur_row-=1
                else: cur_row+=1

        #print(arr, str_arr)

        for row in arr:
            for ch in row:
                if ch != '.': ret_str+=ch

        return ret_str

s = Solution()
"""
TESTS
"""
#print(s.convert("PAYPALISHIRING", 3))
#print(s.convert("ABCD", 2))
print(s.convert("kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS", 1))
