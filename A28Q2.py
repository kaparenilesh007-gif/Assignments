


import sys

word_counter = 0
def main():
    FileName = sys.argv[1]

    global word_counter

    with open(FileName,"r") as file:
        word_counter = len(file.read().split())

    print(f"Total words: {word_counter}")

if __name__=="__main__":
    main()
