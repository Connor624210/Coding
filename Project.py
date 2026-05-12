import random

quiz = [
    {
        "question": "How much garbage enters the ocean every minute?",
        "options": ["A) Roughtly 20 tones", "B) 100kgs", "C) Roughly 1 garbage truckload", "D) 357kgs"],
        "answer": "C",
        "furter_explanation": ""
    },
    {
        "question": "What percent of people are aware of microplastics and reported being very farmilar with them according to a US study?",
        "options": ["A) 80%", "B) 5%", "C) 76%", "D) 18%"],
        "answer": "D",
        "furter_explanation": ""
    },
    {
        "question": "Roughly what percent of plastic pollution enters the ocean from ocean based soruces like fishing and cargo boats?",
        "options": ["A) 80%", "B) 5%", "C) 11.5%", "D) 20%"],
        "answer": "D",
        "furter_explanation": ""
    },
    {
        "question": "How long does plastic take to break down?",
        "options": ["A) Forever", "B) 450 years", "C) 1000 years", "D) 100 years"],
        "answer": "A",
        "furter_explanation": ""
    },
    {
        "question": "Many people believe that plastic pollution is only an issue if marine animals eat it, however thats not true what other issues does it cause",
        "options": ["A) plastic acts as a toxic sponge which soaks up chemicals from the water which allows the chemicals to enter the food chain", 
        "B) Plastic debris can carry diseases and invasive species to new environments", 
        "C) Plastic pollution causes over $10 billion in annual economic losses to marine ecosystems, impacting tourism, fishing, and shipping industries.", "D) Its good for the environment"],
        "answer": ["A", "B", "C"],
        "furter_explanation": ""
    }

]

random.shuffle(quiz)
total_points = 0

user_name = input("What is your user name? ")

for item in quiz:
    print(item["question"])

    for option in item["options"]:
        print(option)

    guess = input("Your answer (A, B, C, or D): ").upper()

    print(item["furter_explanation"])
    
    if guess in item["answer"]:
        print("Correct")
        total_points += 100
    
    else:
        print("Incorrect")

print(f"{user_name} your total points is: {total_points}")