"""Educational Quiz: Ocean Plastic Pollution.

A Python-based interactive quiz designed to test and improve
user knowledge regarding plastic pollution in marine environments.

Author: Connor Nesdale
Date: 2026-05-06
"""


import random
#Main question bank where all the pre loaded questions are stored
#Correct answers and educational facts are also stored here
quiz = [
    {
        "question": "How much garbage enters the ocean every minute?",
        "options": ["A) Roughtly 20 tones", "B) 100kgs", "C) Roughly 1 garbage truckload", "D) 357kgs"],
        "answer": ["C"],
        "further_explanation": "The one garbage truckload per minute figure is a visual tool used by scientists to represent the roughly 8 to 11 million metric tons of plastic that"
        "leak into our oceans annually. This number is calculated by dividing that massive yearly total by the minutes in a year, resulting in about 15 metric tons per minute—the"
        "average capacity of a standard industrial garbage truck. This waste doesn't typically come from literal trucks dumping into the sea, but rather from mismanaged landfills,"
        "litter washed into storm drains, and rivers acting as conveyor belts for inland trash. Without major changes to global waste infrastructure, researchers warn this rate could"
        "accelerate to two truckloads per minute by 2030 and four by 2050."
    },
    {
        "question": "What percent of people are aware of microplastics and reported being very farmilar with them according to a US study?",
        "options": ["A) 80%", "B) 5%", "C) 76%", "D) 18%"],
        "answer": ["D"],
        "further_explanation": "The 18(%) statistic highlights that while a vast majority of Americans have heard the term microplastics, only a small portion—less than one-fifth—feel"
        "truly knowledgeable about them. This awareness-literacy gap reveals that while public concern is rising due to media coverage of plastics in the human food supply, deep"
        "understanding of their specific origins and health impacts remains low. Most citizens know that plastic pollution exists but cannot identify how these microscopic particles"
        "detach from everyday synthetic clothing, car tyres, or breaking-down bottles. While basic recognition is high, this lack of deep familiarity is particularly challenging"
        "because it prevents consumers from making informed purchasing choices and weakens public support for stricter plastic regulation policies."
    },
    {
        "question": "Roughly what percent of plastic pollution enters the ocean from ocean based soruces like fishing and cargo boats?",
        "options": ["A) 80%", "B) 5%", "C) 11.5%", "D) 20%"],
        "answer": ["D"],
        "further_explanation": "The 20(%) statistic highlights that while the vast majority of ocean plastic starts on land, a significant portion—about one-fifth—is dumped or lost"
        "directly at sea by marine industries. This ocean-based pollution primarily consists of fishing gear, such as nets, lines, and traps, which are often referred to as ghost"
        "gear because they continue to trap and kill marine life long after they are abandoned. Other contributors include cargo ships that lose containers during storms and offshore"
        "platforms that accidentally release waste or industrial materials. While this 20% might seem smaller than land-based totals, these plastics are particularly harmful because"
        "they are released far from shore, where they can bypass coastal cleanup efforts and immediately enter deep-sea ecosystems"
    },
    {
        "question": "How long does plastic take to break down?",
        "options": ["A) Forever", "B) 450 years", "C) 1000 years", "D) 100 years"],
        "answer": ["A"],
        "further_explanation": "Because plastic is synthetic and not found in nature, most bacteria cannot decompose it; instead, it undergoes photodegradation, where sunlight slowly"
        "weakens the material until it shatters into microscopic fragments. These resulting microplastics never truly disappear or return to the earth as nutrients, meaning every"
        "piece of plastic ever made still exists in some form today. This permanent presence in the environment is why plastic is considered one of the most persistent pollutants on"
        "the planet, as it continues to accumulate in our soil and oceans indefinitely."
    },
    {
        "question": "Many people believe that plastic pollution is only an issue if marine animals eat it, however thats not true what other issues does it cause?",
        "options": ["A) plastic acts as a toxic sponge which soaks up chemicals from the water which allows the chemicals to enter the food chain", "B) Plastic debris can carry diseases and invasive species to new environments",
        "C) Plastic pollution causes over $10 billion in annual economic losses to marine ecosystems, impacting tourism, fishing, and shipping industries.", "D) Its good for the environment"],
        "answer": ["A", "B", "C", "ABC"],
        "further_explanation": "Beyond the physical danger to animals, plastic pollution acts as a toxic sponge by absorbing harmful industrial chemicals from the water, which then"
        "move up the food chain and can eventually reach humans. Floating plastic also serves as a high-speed transport system for diseases and invasive species, allowing them to"
        "cross entire oceans and devastate new ecosystems. On a global scale, this trash causes over $10 billion in annual economic damage by clogging shipping routes, damaging"
        "fishing equipment, and devaluing coastal tourism destinations. Collectively, these factors show that plastic isn't just a litter problem, but a complex threat to global"
        "health, biodiversity, and the economy."
    }

]

#This is where the user is able to create their own questions thats added to the quiz if they choose to 
#The while True, loops until it reveives vaild input "Yes", or "No"
def user_question():
    while True:

        add_question = input("Would you like to create a question? (Y/N): ").upper().replace(" ", "")
        print()

        if add_question in ['YES', 'Y', "NO", "N"]:
            break

        print("Answer is not vaild. Vaild answers include: Y or N")

    if add_question in ['NO', 'N']:
        return
#Here is where I collect the users custom question and possible answers
    print()
    new_question = input("What's your question for the quiz? ")
    print()

    new_option1 = input("What's your first option? ")
    new_option2 = input("What's your second option? ")
    new_option3 = input("What's your third option? ")
    new_option4 = input("What's your fourth option? ")
#This is where the custom question possible answers are randomly shuffled and labled with letters 
    print()
    new_options = [f"A) {new_option1}", f"B) {new_option2}", f"C) {new_option3}", f"D) {new_option4}"]
    random.shuffle(new_options)
#This is where I validate the users custom question correct answer by making sure its either A,B,C,D
#Otherwise it loops until it recevies the proper input
    while True:
        new_answer = input("What is the correct answer? (A, B, C, or D): ").upper().replace(" ", "")
        print()

        if new_answer in ['A', 'B', 'C', 'D']:
            break

        print("Answer is not vaild. Vaild answers include: A, B, C, D")
#This is where I get the user to provide extra infomation about why the answer to their question is that 
    new_further_explanation = input("Enter a further explanation for this answer: ")
    print()
#This is the place I add the users custom question into the main list "quiz"
    quiz.append({
        "question": new_question,
        "options": new_options,
        "answer": new_answer,
        "further_explanation": new_further_explanation
    })

#This is where the quiz starts
def start_quiz():

    random.shuffle(quiz)
    total_points = 0
#Here is where the program loops through each question and possible answers 
    for item in quiz:
        print(item["question"])

        print()
        for option in item["options"]:
            print(option)
#Here is where the program asks for the users answer to the question 
        while True:
            print()
            guess = input("Your answer (A, B, C, or D): ").upper().replace(" ", "")
            print()
#This is where the program checks if the users answer is vaild else it loops until a vaild reponse is given
            if guess in ["A", "B", "C", "D"]:
                break

            else:
                print("Answer is not vaild. Vaild answers include: A, B, C, D")
#This is where the program prints the further explanation to explain to the user why the answer is that
        print(item["further_explanation"])
        print()
#This is where the program sees if the user got the question correct
#This is where the program gives the user points depending if they got the question right or not
        if guess in item["answer"]:
            print("Correct")
            total_points += 100

        else:
            print("Incorrect")

        print()
        print("****************************************************************************************************************************************************************************************************************")
        print()
#This is where the program asigns the user a title depending on how many question they got right
        percentage = total_points / len(quiz)

        if percentage == 100:
            rank = "Master"
        elif percentage >= 80:
            rank = "Pro"
        else:
            rank = "Noob"

    return total_points, rank

#This code illistrates how the program is run and what fuctions are run before others
def main():
#This is where the program asks the user for their username
    user_name = input("What is your user name? ")
    print()
#This is where the program runs the user_question code which is when the program asks if the user wants to create their own question 
    user_question()
#This is where the program runs the start_quiz code which is when the program starts asking the user questions
    total_points, rank = start_quiz()
#This is where the program dispalys the users total points and their rank, and the thank you message 
    print(f"{user_name} your total points is: {total_points} Your rank is: {rank}")
    print("Thank you for trying out my eductional quiz about plastic pollution in our oceans, I hope you learned something new")

if __name__ == "__main__":
    main()
