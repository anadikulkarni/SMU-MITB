def caesar(text, shift):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = upper.lower()
    new = ''
    for e in text:
        if e.isalpha():
            if e.isupper():
                loc = upper.find(e)
                new += upper[(loc+shift)%26]
            if e.islower():
                loc = lower.find(e)
                new += lower[(loc+shift)%26]
        else:
            new += e
    return(new)

def is_palindrome(s):
    forward = ''
    for e in s:
        if e.isalnum():
            forward += e
    forward = forward.upper()
    backward = forward[::-1]
    return forward == backward

if __name__ == "__main__":
    assert caesar("ABC XYZ", 1) == "BCD YZA"
    assert caesar("Hello, World!", 3) == "Khoor, Zruog!"
    assert caesar("xyz XYZ 123!", 2) == "zab ZAB 123!"

    assert is_palindrome("racecar")
    assert is_palindrome("A man, a plan, a canal: Panama!")
    assert not is_palindrome("Hello, World!")