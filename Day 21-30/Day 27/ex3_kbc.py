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
        if(count<6):
            print("You won", count*1000, "till now!")
        
    else:
        print("\nIncorrect answer!")
        break
if(count==2 or count==3):
    winnings = 2000
    print("\n\nYou won", winnings, "in total and got", count, "answers correct!")
elif(count==4 or count==5):
    winnings = 4000
    print("\n\nYou won", winnings, "in total and got", count, "answers correct!")
elif(count==len(questions)): print("Congratulations! You answered ALL the questions correctly and won 1000000!")
else: print("\nUnfortunately, you win nothing.")
print("\nThank you for playing!")