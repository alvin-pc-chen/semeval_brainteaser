# Zero shot - Sentence
ZERO_SP_BASE = "Using commonsense reasoning, find the best choice for the following question:\n"
# Chain of Thought - Sentence
CHAIN_SYSTEM = {"role": "system", 
                 "content": "You are a Question Answering Model that answers questions by finding logical entailments between the question and answer choices."}
CHAIN_SP_BASE = """Question: Samuel was out for a walk when it started to rain. He did not have an umbrella and he wasn't wearing a hat. His clothes were soaked, yet not a single hair on his head got wet. How could this happen?
                Choices: 0 = His hair is dyed.; 1 = This man is bald.; 2 = This man walk upside down to avoid rain.; 3 = None of above.;
                Response: Samuel got wet from the rain, but no hair on his head got wet. If Samuel dyed his hair it would still be wet. Samuel is bald, so his hair didn't get wet. The answer is 1
                Question: A horse is tied to a five-meter rope in front of an old saloon. Ten meters behind the horse is a bale of hay. Without breaking his rope, the horse is able to eat the hay whenever he chooses. How is this possible?
                Choices: 0 = The rope stretches proportionally, providing the extra length needed for the horse to reach the hay ten meters away.; 1 = The rope is not tied to anything else.; 2 = The walls of the saloon retract or collapse inwards, creating more space for the horse to reach the hay.; 3 = None of above.;
                Response: That the rope is not tied to anything else is the simplest choice. The horse can reach the hay whenever he chooses. The answer is 1
                Question: A woman who lives in new york legally married three men, she did not get divorce, get an enrollment, or legally seperate. How is this possible?
                Choices: 0 = The woman is not a good person.; 1 = His husband is not a good husband.; 2 = She is a minister.; 3 = None of above.;
                Response: In new york it is not legal to be married to more than one person at a time. If the woman did not get divorced or legally separated, she cannot be legally married to more than one person. Ministers perform marriages, they do not get married. The answer is 2
                Question: Why is the value of 1968 pennies higher than 1967 pennies?
                Choices: 0 = Old money weight more than new money.; 1 = Old money is dirtier than new money.; 2 = Because there is one more penny in 1968 pennies than in 1967 pennies.; 3 = None of above.;
                Response: 1968 and 1967 refer to the number of pennies. The value of 1968 pennies is higher than 1967 pennies because there is one more penny in 1968 pennies than in 1967 pennies. The answer is 2
                Question: Not a single parent objected when the teacher spanked every child in the class. How come?
                Choices: 0 = The teacher had informed all the parents in advance about the unique disciplinary approach.; 1 = The teacher had informed all the children in advance about the unique disciplinary approach.; 2 = The teacher was in an orphanage school.; 3 = None of above.;
                Response: Even if the teacher had informed all the parents or all the students in advance about the unique disciplinary approach, it is unlikely that nobody would object. If the teacher is in an orphange school, there would be no parents to object. The answer is 2
                Question: Twenty-seven ducks are going to the pond. Five of them got lost, thirteen of them are staying home, and nine of them are at the pond. Where are the rest of them?
                Choices: 0 = Home.; 1 = The way to the pond.; 2 = Pond.; 3 = None of above.;
                Response: Twenty-seven ducks are going to the pond. Five of them are lost, 27 - 5 = 22. Thirteen of them are staying home, 22 - 13 = 9. Nine of them are at the pond, 9 - 9 = 0. There are no more ducks so the question is invalid. The answer is 3
                Question: How many birth days does the average person have?
                Choices: 0 = People may celebrate their birthdays annually, so it depends on their life span.; 1 = They technically only have one birth day in their lifetime.; 2 = It can be zero as some people are too busy to celebrating their birthdays.; 3 = None of above.;
                Response: Everyone is born only once so technically the average person has one birthday in their lifetime. The answer is 1
                Question: The more you take, the more you leave behind
                Choices: 0 = Love.; 1 = Footsteps.; 2 = Money.; 3 = None of above.;
                Response: Footsteps. The more you walk, the more footsteps you leave behind. The answer is 1"""