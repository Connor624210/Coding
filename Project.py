''' An educational quiz python program about plastic pollution in our oceans
Made by Connor Nesdale
Date created: 6th May 2026 '''


import random

quiz = [
    {
        "question": "How much garbage enters the ocean every minute?",
        "options": ["A) Roughtly 20 tones", "B) 100kgs", "C) Roughly 1 garbage truckload", "D) 357kgs"],
        "answer": "C",
        "further_explanation": "The one garbage truckload per minute figure is a visual tool used by scientists to represent the roughly 8 to 11 million metric tons of plastic that leak into our oceans annually. This number is calculated by dividing that massive yearly total by the minutes in a year, resulting in about 15 metric tons per minute—the average capacity of a standard industrial garbage truck. This waste doesn't typically come from literal trucks dumping into the sea, but rather from mismanaged landfills, litter washed into storm drains, and rivers acting as conveyor belts for inland trash. Without major changes to global waste infrastructure, researchers warn this rate could accelerate to two truckloads per minute by 2030 and four by 2050."
    },
    {
        "question": "What percent of people are aware of microplastics and reported being very farmilar with them according to a US study?",
        "options": ["A) 80%", "B) 5%", "C) 76%", "D) 18%"],
        "answer": "D",
        "further_explanation": "The 18(%) statistic highlights that while a vast majority of Americans have heard the term microplastics, only a small portion—less than one-fifth—feel truly knowledgeable about them. This awareness-literacy gap reveals that while public concern is rising due to media coverage of plastics in the human food supply, deep understanding of their specific origins and health impacts remains low. Most citizens know that plastic pollution exists but cannot identify how these microscopic particles detach from everyday synthetic clothing, car tyres, or breaking-down bottles. While basic recognition is high, this lack of deep familiarity is particularly challenging because it prevents consumers from making informed purchasing choices and weakens public support for stricter plastic regulation policies."
    },
    {
        "question": "Roughly what percent of plastic pollution enters the ocean from ocean based soruces like fishing and cargo boats?",
        "options": ["A) 80%", "B) 5%", "C) 11.5%", "D) 20%"],
        "answer": "D",
        "further_explanation": "The 20(%) statistic highlights that while the vast majority of ocean plastic starts on land, a significant portion—about one-fifth—is dumped or lost directly at sea by marine industries. This ocean-based pollution primarily consists of fishing gear, such as nets, lines, and traps, which are often referred to as ghost gear because they continue to trap and kill marine life long after they are abandoned. Other contributors include cargo ships that lose containers during storms and offshore platforms that accidentally release waste or industrial materials. While this 20% might seem smaller than land-based totals, these plastics are particularly harmful because they are released far from shore, where they can bypass coastal cleanup efforts and immediately enter deep-sea ecosystems"
    },
    {
        "question": "How long does plastic take to break down?",
        "options": ["A) Forever", "B) 450 years", "C) 1000 years", "D) 100 years"],
        "answer": "A",
        "further_explanation": "Because plastic is synthetic and not found in nature, most bacteria cannot decompose it; instead, it undergoes photodegradation, where sunlight slowly weakens the material until it shatters into microscopic fragments. These resulting microplastics never truly disappear or return to the earth as nutrients, meaning every piece of plastic ever made still exists in some form today. This permanent presence in the environment is why plastic is considered one of the most persistent pollutants on the planet, as it continues to accumulate in our soil and oceans indefinitely."
    },
    {
        "question": "Many people believe that plastic pollution is only an issue if marine animals eat it, however thats not true what other issues does it cause?",
        "options": ["A) plastic acts as a toxic sponge which soaks up chemicals from the water which allows the chemicals to enter the food chain", 
        "B) Plastic debris can carry diseases and invasive species to new environments", 
        "C) Plastic pollution causes over $10 billion in annual economic losses to marine ecosystems, impacting tourism, fishing, and shipping industries.", "D) Its good for the environment"],
        "answer": ["A", "B", "C","ABC"],
        "further_explanation": "Beyond the physical danger to animals, plastic pollution acts as a toxic sponge by absorbing harmful industrial chemicals from the water, which then move up the food chain and can eventually reach humans. Floating plastic also serves as a high-speed transport system for diseases and invasive species, allowing them to cross entire oceans and devastate new ecosystems. On a global scale, this trash causes over $10 billion in annual economic damage by clogging shipping routes, damaging fishing equipment, and devaluing coastal tourism destinations. Collectively, these factors show that plastic isn't just a litter problem, but a complex threat to global health, biodiversity, and the economy."
    }

]

random.shuffle(quiz)
total_points = 0

user_name = input("What is your user name? ")
print()

while True:
    add_question = input("Would you like to create a question? (Y/N): ").upper().replace(" ","")
    print()
    if add_question not in ['YES', 'Y']:
        break
        
    print() 
    new_question = input("What's your question for the quiz? ")
    print() 
    
    new_option1 = input("What's your first option? ")
    new_option2 = input("What's your second option? ")
    new_option3 = input("What's your third option? ")
    new_option4 = input("What's your fourth option? ")
    
    print() 
    new_options = [f"A) {new_option1}", f"B) {new_option2}", f"C) {new_option3}", f"D) {new_option4}"]
    
    new_answer = input("What is the correct answer? (A, B, C, or D): ").upper().replace(" ","")
    print()
    new_further_explanation = input("Enter a further explanation for this answer: ")
    print() 
        
    quiz.append({
        "question": new_question, 
        "options": new_options, 
        "answer": new_answer, 
        "further_explanation": new_further_explanation 
    })


for item in quiz:
    print(item["question"])

    print()

    for option in item["options"]:
        print(option)

    print()

    guess = input("Your answer (A, B, C, or D): ").upper().replace(" ", "")

    print()

    print(item["further_explanation"])
    
    print()

    if guess in item["answer"]:
        print("Correct")
        total_points += 100
    
    else:
        print("Incorrect")

    print()
    print("****************************************************************************************************************************************************************************************************************")
    print()

print(f"{user_name} your total points is: {total_points}")
print("Thank you for trying out my eductional quiz about plastic pollution in our oceans, I hope you learned something new")