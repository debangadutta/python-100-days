import random
import string

def random_letters():
    return random.choices(string.ascii_lowercase, k=3)

sentence = input("Enter the input sentence: ")
words = sentence.split(" ")

print("Select:\n1 for Encode\n2 for Decode")
num = int(input(""))
end_str = []

if num==1:
    print("\nEncode Mode Activated!\n")
    for word in words:
        if len(word)>=3:
            word = word [1:] + word[0]
            randoms_begin = random_letters()
            for i in range(3): word = randoms_begin[i] + word
            randoms_end = random_letters()
            for i in range(3): word = word + randoms_end[i]
        else:
            word = word[::-1]
        end_str.append(word)
    print("Encoding successful!\n\nEncoded string:")
    print(' '.join(end_str))
elif num==2:
    print("\nDecode Mode Activated!\n")
    for word in words:
        if len(word)>=3:
            word = word[3:-3]
            word = word[-1] + word[:-1]
        else:
            word = word[::-1]
        end_str.append(word)
    print("Decoding successful!\n\nDecoded string:")
    print(' '.join(end_str))
else: print("Invalid input.")