# Check if string is palindrome?
# Very long string constrains; O(n)


lng_str_not_palindrome = "IamverylongstringtocheckIamnotpalindromeIamverylongstringtocheckIamnotpalindromeIamverylongstringtocheckIamnotpalindromeIamverylongstringtocheckIamnotpalindrome"
lng_str_palindrome = "mnogoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooogonm"

def is_palindrome(string: str) -> bool:
    return string == string[::-1]

print(is_palindrome(lng_str_palindrome))

def two_pointers_technique(string: str) -> bool:
    start = 0
    end = len(string) - 1
    
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

print(two_pointers_technique(lng_str_not_palindrome))



