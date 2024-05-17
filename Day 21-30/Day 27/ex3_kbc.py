print("Welcome to KBC!\n")

questions = [
    ["Current Railway Minister of India is:\nA.Mamta Banarjee\nB.Ram Vilash\nC.Ashwini Vaishnaw\nD.Piyush Goyal","C"],
    ["What does not grow on tree according to a popular Hindi saying?\nA.Money\nB.Flowers\nC.Leaves\nD.Fruits", "A"],
    ["Which city is known as Pink City in India?\nA.Bangalore\nB.Mysore\nC.Jaipur\nD.Kochi", "C"],
    ["Who wrote India's National Anthem?\nA.Rabindranath Tagore\nB.Lal Bahadur Shastri\nC.Chetan Bhagat\nD.RK Narayan","A"],
    ["When is the National Hindi Diwas celebrated?\nA.13 September\nB.14 September\nC.14 July\nD.15 August", "B"],
    ["Where in India Gate located?\nA.Agra\nB.Mumbai\nC.Punjab\nD.New Delhi", "D"]
]

count = 0
winnings = 0

for i in range(6):
    print("\nQuestion", i+1, ":", questions[i][0])
    ans = input("Enter your option: ")
    if(ans.upper())==questions[i][1]:
        print("\nYou are correct!")
        count+=1
        winnings = count*1000
        print("You won", winnings, "till now!")
    else:
        print("\nIncorrect answer!")
        break
print("\n\nYou won", winnings, "in total and got", count, "answers correct!")
if(count==len(questions)): print("Congratulations! You answered ALL the questions correctly!")
print("\nThank you for playing!")