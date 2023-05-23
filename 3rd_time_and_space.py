# 7 kyu
# Parts of a list

# DESCRIPTION:
# Write a function partlist that gives all the ways to divide a list (an array) of at least two elements into two non-empty parts.

# Each two non empty parts will be in a pair (or an array for languages without tuples or a structin C - C: see Examples test Cases - )
# Each part will be in a string
# Elements of a pair must be in the same order as in the original array.
# Examples of returns in different languages:
# a = ["az", "toto", "picaro", "zone", "kiwi"] -->
# [["az", "toto picaro zone kiwi"], ["az toto", "picaro zone kiwi"], ["az toto picaro", "zone kiwi"], ["az toto picaro zone", "kiwi"]] 
# or
#  a = {"az", "toto", "picaro", "zone", "kiwi"} -->
# {{"az", "toto picaro zone kiwi"}, {"az toto", "picaro zone kiwi"}, {"az toto picaro", "zone kiwi"}, {"az toto picaro zone", "kiwi"}}
# or
# a = ["az", "toto", "picaro", "zone", "kiwi"] -->
# [("az", "toto picaro zone kiwi"), ("az toto", "picaro zone kiwi"), ("az toto picaro", "zone kiwi"), ("az toto picaro zone", "kiwi")]
# or 
# a = [|"az", "toto", "picaro", "zone", "kiwi"|] -->
# [("az", "toto picaro zone kiwi"), ("az toto", "picaro zone kiwi"), ("az toto picaro", "zone kiwi"), ("az toto picaro zone", "kiwi")]
# or
# a = ["az", "toto", "picaro", "zone", "kiwi"] -->
# "(az, toto picaro zone kiwi)(az toto, picaro zone kiwi)(az toto picaro, zone kiwi)(az toto picaro zone, kiwi)"
# Note
# You can see other examples for each language in "Your test cases"

def partlist(arr):
    if len(arr) < 2:
        return ("Invalid input")
    else:         
        answer_list = []
        for i in range (1,len(arr)):
            first_part = " ".join(arr[:i])
            second_part = " ".join(arr[i:])
            answer_list.append((first_part, second_part))
        return answer_list
    
# 
# So the for loop iterates n-1 times, because n is the length of thr input list "arr". 
# In each iteration the code creates two parts by joining of arr using the join function. 
# the time complexity of the join is O(m) where m is the length of the resulting string.  
# Because the length of each part at most is n the time complexity of the join op is O(n).
# the code that appends the resulting tuple to the answer_list, each append op takes constant time.
# so the complexity of the for loop is O(n) * 0(n) = 0(n^2) so time is 0(n^2) and space is 0(n)
#  time quadratic ans space is linear
