# function to check if small string is there in big string

# We can iteratively check for every word, but Python provides us an inbuilt function find() which checks if a substring is present in the string, which is done in one line.

def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
            
# driver code
string = "riya bhatia"
sub_str ="riya"
check(string, sub_str)
