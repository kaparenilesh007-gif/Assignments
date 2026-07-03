def CheckVowel(char):
    VowelChar = {"A","E","I","O","U","a","e","i","o","u"}
    if char in VowelChar:
        print("Entered character is Vowel")
    else:
        print("Entered character is Constant")


def main():
    Char = input("Enter Character: ")
    CheckVowel(Char)

if __name__=="__main__":
    main()