"""

It's an implicit (and smart) count of occurrence.
BANANA (for kevin):
For i=1 we are sure that there is an occurrence for all this substrings that start with a vowel (s[i] = 'A'):

- A
- AN
- ANA
- ANAN
- ANANA
So we add len(s)-i = 6-1 = 5 to kevin score.
For i=3:

- A
- AN
- ANA
(+3)
For i=5:

- A
(+1)

"""

def minion_game(s):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s) - i)

    if kevsc > stusc:
        print(f"Kevin {kevsc}")
    elif kevsc < stusc:
        print(f"Stuart {stusc}")
    else:
        print("Draw")


if __name__ == '__main__':
    # s = input()
    s = "BANANA"
    minion_game(s)
