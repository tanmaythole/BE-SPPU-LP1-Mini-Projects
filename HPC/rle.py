import math

def rle_encode(str1):
    ans = ""
    val = 0
    i = 1
    while(i < len(str1)):
        while(i<len(str1) and str1[i] == str1[i-1]):
            i+=1
        ans += str1[val] + str(i-val)
        val = i
        i+=1
    return ans

def rle_decode(str2):
    i=0
    ans = ""
    while(i<len(str2)):
        word = str2[i]
        i+=1
        num = ""
        while(i<len(str2) and str2[i].isdigit()):
            num += str(str2[i])
            i+=1
        ans+= word*int(num)
    return ans

str1 = input("Enter the string: ")
print("String to be encoded: ", str1)
a = rle_encode(str1)
print("Run Length Encoding: ", a)
print("Decoded string: ", rle_decode(a))