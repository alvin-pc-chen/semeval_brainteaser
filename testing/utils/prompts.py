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

CHAIN_SP_CR = """Question: A couple is having a disagreement over the man's error. The man kept apologizing and pleading with the woman to allow him to see her directly. The woman was still upset. Thus, she wouldn't agree. The couple, though, was positioned on the same mat. How is that even doable?
                Choices: 0 = The mat was folded in multiple times and end up with a special shape.; 1 = The woman kept turning her back to the man.; 2 = The couple was standing on two sides of the girl's apartment door, which had a rug under it.; 3 = None of above.;
                Response: The couple are standing on the same mat but cannot see each other, which suggests that there is a barrier between them. Regardless of how the mat was folded, it would not prevent the couple from seeing each other. Even if the woman turned her back to the man he would still see her. Therefore, the couple was standing on two sides of a door, which had a rug under it. The answer is 2
                Question: Eight people were sitting under a large tree. Suddenly, a gust of wind blows, yet none of them got hit by any falling leaves. How is this possible?
                Choices: 0 = It was winter and the tree doesn't have any leaves.; 1 = People were camping under the tree.; 2 = The wind blows heavily.; 3 = None of above.;
                Response: If the people were camping under the tree, they would still be hit by the falling leaves. The wind blowing heavily would cause the leaves to fall. If it was winter and the tree doesn't have any leaves, then the people would not be hit by any falling leaves. The answer is 0
                Question: The ship was in the central Pacific Ocean. The ship suddenly began to sink without being crushed. However, each team was still preoccupied with its own tasks, so none was threatening. Why?
                Choices: 0 = An underwater earthquake caused a rapid drop in the water level and resulted in the loss of buoyancy for the ship.; 1 = It was a Submarine.; 2 = There are too many fish around the ship.; 3 = None of above.;
                Response: An earthquake would cause people to feel threatened, and fish around the ship would not matter. If the ship were a submarine, it would be designed to sink. The answer is 1
                Question: Two mothers and two daughters were asking for new state IDs, but the agent only gave out three forms and instructed them on how to fill them out. Why?
                Choices: 0 = They are one daughters, one mother and one grandmother.; 1 = Two girls filled the from together.; 2 = One mother is too old to apply for new IDs.; 3 = None of above.;
                Response: The agent only gave out three forms and instructed them on how to fill them out, which suggests that there are only three people. If they are one daughter, one mother, and one grandmother, then there would be three people. The answer is 0
                Question: Every night, a man would sleep with a light on, as bright as the sun, dazzling the neighbors. But why did his neighbors never complain?
                Choices: 0 = All his neighbors are blind.; 1 = The man would wake up early.; 2 = He lived in a light house.; 3 = None of above.;
                Response: If all his neighbors are blind, they would not be dazzled by the light. If the man lived in a light house then the light would be expected. The answer is 2 
                Question: Each of the 30 participants in the masquerade had to wear a unique hat to distinguish themselves from one another. The host, however, only tallied 29 when he counted the number of hats to determine attendance. All 30 persons had signed their names on the spreadsheet, which confused him. He repeated the count. There are still 29. How is that even doable?
                Choices: 0 = One person had a pretty beautiful hat.; 1 = The host had a hat himself and he forget to count it.; 2 = One person had moved away from the group when the host was counting.; 3 = None of above.;
                Response: If one person had a pretty beautiful hat, then the host would still count 30 hats. If one person had moved away from the group when the host was counting, then the host would still count 30 hats. The host had a hat himself and he forget to count it. The answer is 1
                Question: A certain kind of animal has parents but no children, lives happily but can not give birth to offspring. This kind of animal has existed on earth for a long history. How is that possible?
                Choices: 0 = The animal is the dinosaur. Millions of years ago, dinosaurs roamed the Earth, but eventually, they became extinct due to various factors such as climate change or asteroid impact.; 1 = The animal is the butterfly. During the pupal stage of their life cycle, butterflies are inside a protective casing, and it may appear as if they have completely disappeared or been wiped out.; 2 = The animal is the Mule. Since all Mules are born sterile, you can only get a Mule by crossing a donkey with a horse.; 3 = None of above.;
                Response: Dinosaurs are no longer alive, so they cannot live happily. Butterflies can give birth to offspring, so they are not the answer. Mules are born sterile, so they cannot give birth to offspring. The answer is 2
                Question: Six women were hiking on a trail when a sudden snowfall began. Five of the women hurried along, but the sixth did not. Still, they all reached the cabin at the same time, and all but the sixth were cold. How is that possible?
                Choices: 0 = The 6th woman beated them at the end.; 1 = The sixth woman was in a photograph that one of the others was carrying.; 2 = The 6th woman walked slowly to dodge the snow.; 3 = None of above.;
                Response: If the sixth woman beat them or walked slowly to dodge the snow she would not have reached the cabin at the same time. If the sixth woman was in a photograph that one of the others was carrying, then she would not be cold and would not have to hurry. The answer is 1"""

CHAIN_SP_SR = """Question: The ship was in the harbor on a beautiful sunny day. The ship suddenly started to sink. The ship sank in front of the onlookers despite there being no storm or mechanical issue. What led to the ship's sinking?
                Choices: 0 = There are too many fish around the ship.; 1 = There are too many spectators in the harbor.; 2 = It was a Submarine.; 3 = None of above.;
                Response: The fish would not impact the ship's sinking. There was no mechanical issue, which means that the ship was supposed to sink such as a submarine. The answer is 2
                Question: Natives of the Arctic will never eat a penguin's egg, not even if they are starving. Exactly why not?
                Choices: 0 = Penguins only live in Antarctica.; 1 = Penguins' eggs are toxic.; 2 = Penguins and their eggs are not part of their traditional or cultural diet.; 3 = None of above.;
                Reponse: Penguins' eggs are not toxic and there is no evidence given for the native cultural diet. Penguins only live in Antarctica, so the natives of the Arctic would never eat a penguin's egg. The answer is 0
                Question: Brad began by entering the office tower's 22nd story through the filthy common window. He slid the window open and leapt through it after becoming depressed. Outside the building, there was a cliff-like drop to the ground. Amazingly, he came to rest entirely unharmed. How could he have survived the fall if there was nothing to slow or cushion his descent?
                Choices: 0 = Brad was so sick and tired of window washing, he opened the window and jumped inside.; 1 = The ground outside the building is wet.; 2 = Consistent exercise has made him a very strong man.; 3 = None of above.;
                Response: Even very strong men would not survive a fall from a 22-story building. The ground outside the building being wet would not cushion his fall. Brad was so sick and tired of window washing, he opened the window and jumped inside. The answer is 0
                Question: Danny had just passed under an overpass in his semi when he abruptly came to a stop. Danny accidentally drove under the overpass that was only just tall enough for his truck because he wasn't paying enough attention. He was unable to move forward or backward in the semi due to how tightly it was wedged. When another tracker passed by, he was told how simple it would be to remove the semi from underneath the bridge. What did he recommend?
                Choices: 0 = He told Danny to left the bridge.; 1 = He told Danny to overturn the track.; 2 = He told Danny to let some air out of his tires.; 3 = None of above.;
                Response: The bridge would not be lifted. Overturning the truck would not help. Letting some air out of his tires would help. The answer is 2
                Question: I excavate little caves and keep my gold and silver there. I also create gold crowns and silver bridges. They are the tiniest things you can imagine. Everyone will eventually require my assistance, but many people are reluctant to accept it. Why?
                Choices: 0 = I am a dentist.; 1 = I am a thief.; 2 = I am a miner.; 3 = None of above.;
                Response: Thieves and miners do not create gold crowns or bridges. Tiny crowns and bridges are dental work. People don't like going to the dentist. The answer is 0
                Question: You are a bus driver. Mrs. Smith, an elderly woman, and Raymond, a small child, are on the bus when you start your journey. The elderly woman exits at the first stop, and Ed, a salesperson, enters. At the following stop, three women carrying shopping bags board the bus along with Jack and his sister Jill. After fifteen minutes of riding, the bus stops, Raymond gets off, and a guy and his wife board. A woman then boards the bus while carrying a caged bird. Who is the bus driver?
                Choices: 0 = Jil.; 1 = Mrs. Smith; 2 = Raymond.; 3 = None of above.;
                Response: The bus driver is you, all the other people are passengers. The answer is 3
                Question: Despite being in December, David's birthday is never in the winter. Why?
                Choices: 0 = His family will hold a huge celebration for him.; 1 = He lives in Australia.; 2 = He alwasy gets cold in winter.; 3 = None of above.;
                Response: David's family holding a huge celebration or that he gets cold in winter has nothing to do with his birthday being in winter. David's birthday is never in the winter because he lives in Australia. The answer is 1
                Question: There was no power in town, and none of the street lights or traffic signals worked. A dark limousine sped down the recently laid blacktop, headlights turned off. A little youngster in complete black (no reflectors) went out to cross the roadway. Despite the fact that the moon was not out and the youngster had no flashlight, the motorist stopped to let the boy to cross the street. How did the driver notice the youngster?
                Choices: 0 = The driver was good at listening.; 1 = The driver was paying much attention on the road.; 2 = The driver saw the boy because it was during the daylight hours.; 3 = None of above.;
                Response: The driver could not have paid enough attention or heard the youngster in time if it were dark outside. The driver must have seen the boy, and all lights were off because it was during daylight hours. The answer is 2"""

CHAIN_SP_MIX = """Question: A horse is tied to a five-meter rope in front of an old saloon. Ten meters behind the horse is a bale of hay. Without breaking his rope, the horse is able to eat the hay whenever he chooses. How is this possible?
                Choices: 0 = The rope stretches proportionally, providing the extra length needed for the horse to reach the hay ten meters away.; 1 = The rope is not tied to anything else.; 2 = The walls of the saloon retract or collapse inwards, creating more space for the horse to reach the hay.; 3 = None of above.;
                Response: Rope generally cannot stretch, and if it could stretch the length would be variable. If the walls collapse, the horse would be further from the hay. The rope not being tied to anything else is the simplest answer. The answer is 1
                Question: A woman who lives in new york legally married three men, she did not get divorce, get an enrollment, or legally seperate. How is this possible?
                Choices: 0 = The woman is not a good person.; 1 = His husband is not a good husband.; 2 = She is a minister.; 3 = None of above.;
                Response: In new york it is not legal to be married to more than one person at a time, even if her husband is bad. If the woman did not get divorced or legally separated, she cannot be legally married to more than one person. Ministers perform marriages, they do not get married. The answer is 2
                Question: Brad began by entering the office tower's 22nd story through the filthy common window. He slid the window open and leapt through it after becoming depressed. Outside the building, there was a cliff-like drop to the ground. Amazingly, he came to rest entirely unharmed. How could he have survived the fall if there was nothing to slow or cushion his descent?
                Choices: 0 = Brad was so sick and tired of window washing, he opened the window and jumped inside.; 1 = The ground outside the building is wet.; 2 = Consistent exercise has made him a very strong man.; 3 = None of above.;
                Response: Even very strong men would not survive a fall from a 22-story building. The ground outside the building being wet would not cushion his fall. Brad was so sick and tired of window washing, he opened the window and jumped inside. The answer is 0
                Question: Danny had just passed under an overpass in his semi when he abruptly came to a stop. Danny accidentally drove under the overpass that was only just tall enough for his truck because he wasn't paying enough attention. He was unable to move forward or backward in the semi due to how tightly it was wedged. When another tracker passed by, he was told how simple it would be to remove the semi from underneath the bridge. What did he recommend?
                Choices: 0 = He told Danny to left the bridge.; 1 = He told Danny to overturn the track.; 2 = He told Danny to let some air out of his tires.; 3 = None of above.;
                Response: The bridge would not be lifted. Overturning the truck would not help. Letting some air out of his tires would help. The answer is 2
                Question: I excavate little caves and keep my gold and silver there. I also create gold crowns and silver bridges. They are the tiniest things you can imagine. Everyone will eventually require my assistance, but many people are reluctant to accept it. Why?
                Choices: 0 = I am a dentist.; 1 = I am a thief.; 2 = I am a miner.; 3 = None of above.;
                Response: Thieves and miners do not create gold crowns or bridges. Tiny crowns and bridges are dental work. People don't like going to the dentist. The answer is 0
                Question: Each of the 30 participants in the masquerade had to wear a unique hat to distinguish themselves from one another. The host, however, only tallied 29 when he counted the number of hats to determine attendance. All 30 persons had signed their names on the spreadsheet, which confused him. He repeated the count. There are still 29. How is that even doable?
                Choices: 0 = One person had a pretty beautiful hat.; 1 = The host had a hat himself and he forget to count it.; 2 = One person had moved away from the group when the host was counting.; 3 = None of above.;
                Response: If one person had a pretty beautiful hat, then the host would still count 30 hats. If one person had moved away from the group when the host was counting, then the host would still count 30 hats. The host had a hat himself and he forget to count it. The answer is 1
                Question: A certain kind of animal has parents but no children, lives happily but can not give birth to offspring. This kind of animal has existed on earth for a long history. How is that possible?
                Choices: 0 = The animal is the dinosaur. Millions of years ago, dinosaurs roamed the Earth, but eventually, they became extinct due to various factors such as climate change or asteroid impact.; 1 = The animal is the butterfly. During the pupal stage of their life cycle, butterflies are inside a protective casing, and it may appear as if they have completely disappeared or been wiped out.; 2 = The animal is the Mule. Since all Mules are born sterile, you can only get a Mule by crossing a donkey with a horse.; 3 = None of above.;
                Response: Dinosaurs are no longer alive, so they cannot live happily. Butterflies can give birth to offspring, so they are not the answer. Mules are born sterile, so they cannot give birth to offspring. The answer is 2
                Question: Six women were hiking on a trail when a sudden snowfall began. Five of the women hurried along, but the sixth did not. Still, they all reached the cabin at the same time, and all but the sixth were cold. How is that possible?
                Choices: 0 = The 6th woman beated them at the end.; 1 = The sixth woman was in a photograph that one of the others was carrying.; 2 = The 6th woman walked slowly to dodge the snow.; 3 = None of above.;
                Response: If the sixth woman beat them or walked slowly to dodge the snow she would not have reached the cabin at the same time. If the sixth woman was in a photograph that one of the others was carrying, then she would not be cold and would not have to hurry. The answer is 1"""

MULTISHOT_SP_MIX = """Question: A horse is tied to a five-meter rope in front of an old saloon. Ten meters behind the horse is a bale of hay. Without breaking his rope, the horse is able to eat the hay whenever he chooses. How is this possible?
                Choices: 0 = The rope stretches proportionally, providing the extra length needed for the horse to reach the hay ten meters away.; 1 = The rope is not tied to anything else.; 2 = The walls of the saloon retract or collapse inwards, creating more space for the horse to reach the hay.; 3 = None of above.;
                Response: The answer is 1
                Question: A woman who lives in new york legally married three men, she did not get divorce, get an enrollment, or legally seperate. How is this possible?
                Choices: 0 = The woman is not a good person.; 1 = His husband is not a good husband.; 2 = She is a minister.; 3 = None of above.;
                Response: The answer is 2
                Question: Brad began by entering the office tower's 22nd story through the filthy common window. He slid the window open and leapt through it after becoming depressed. Outside the building, there was a cliff-like drop to the ground. Amazingly, he came to rest entirely unharmed. How could he have survived the fall if there was nothing to slow or cushion his descent?
                Choices: 0 = Brad was so sick and tired of window washing, he opened the window and jumped inside.; 1 = The ground outside the building is wet.; 2 = Consistent exercise has made him a very strong man.; 3 = None of above.;
                Response: The answer is 0
                Question: Danny had just passed under an overpass in his semi when he abruptly came to a stop. Danny accidentally drove under the overpass that was only just tall enough for his truck because he wasn't paying enough attention. He was unable to move forward or backward in the semi due to how tightly it was wedged. When another tracker passed by, he was told how simple it would be to remove the semi from underneath the bridge. What did he recommend?
                Choices: 0 = He told Danny to left the bridge.; 1 = He told Danny to overturn the track.; 2 = He told Danny to let some air out of his tires.; 3 = None of above.;
                Response: The answer is 2
                Question: Why is the value of 1968 pennies higher than 1967 pennies?
                Choices: 0 = Old money weight more than new money.; 1 = Old money is dirtier than new money.; 2 = Because there is one more penny in 1968 pennies than in 1967 pennies.; 3 = None of above.;
                Response: The answer is 2
                Question: Each of the 30 participants in the masquerade had to wear a unique hat to distinguish themselves from one another. The host, however, only tallied 29 when he counted the number of hats to determine attendance. All 30 persons had signed their names on the spreadsheet, which confused him. He repeated the count. There are still 29. How is that even doable?
                Choices: 0 = One person had a pretty beautiful hat.; 1 = The host had a hat himself and he forget to count it.; 2 = One person had moved away from the group when the host was counting.; 3 = None of above.;
                Response: The answer is 1
                Question: A certain kind of animal has parents but no children, lives happily but can not give birth to offspring. This kind of animal has existed on earth for a long history. How is that possible?
                Choices: 0 = The animal is the dinosaur. Millions of years ago, dinosaurs roamed the Earth, but eventually, they became extinct due to various factors such as climate change or asteroid impact.; 1 = The animal is the butterfly. During the pupal stage of their life cycle, butterflies are inside a protective casing, and it may appear as if they have completely disappeared or been wiped out.; 2 = The animal is the Mule. Since all Mules are born sterile, you can only get a Mule by crossing a donkey with a horse.; 3 = None of above.;
                Response: The answer is 2
                Question: Six women were hiking on a trail when a sudden snowfall began. Five of the women hurried along, but the sixth did not. Still, they all reached the cabin at the same time, and all but the sixth were cold. How is that possible?
                Choices: 0 = The 6th woman beated them at the end.; 1 = The sixth woman was in a photograph that one of the others was carrying.; 2 = The 6th woman walked slowly to dodge the snow.; 3 = None of above.;
                Response: The answer is 1"""

CHAIN_SP_BASE_NEW = """Question: Samuel was out for a walk when it started to rain. He did not have an umbrella and he wasn't wearing a hat. His clothes were soaked, yet not a single hair on his head got wet. How could this happen?
                Choices: 0 = His hair is dyed.; 1 = This man is bald.; 2 = This man walk upside down to avoid rain.; 3 = None of above.;
                Response: Samuel got wet from the rain, but no hair on his head got wet. If Samuel dyed his hair or walked upside down it would still be wet. Samuel is bald, so his hair didn't get wet. The answer is 1
                Question: A horse is tied to a five-meter rope in front of an old saloon. Ten meters behind the horse is a bale of hay. Without breaking his rope, the horse is able to eat the hay whenever he chooses. How is this possible?
                Choices: 0 = The rope stretches proportionally, providing the extra length needed for the horse to reach the hay ten meters away.; 1 = The rope is not tied to anything else.; 2 = The walls of the saloon retract or collapse inwards, creating more space for the horse to reach the hay.; 3 = None of above.;
                Response: Rope generally cannot stretch, and if it could stretch the length would be variable. If the walls collapse, the horse would be further from the hay. The rope not being tied to anything else is the simplest answer. The answer is 1
                Question: A woman who lives in new york legally married three men, she did not get divorce, get an enrollment, or legally seperate. How is this possible?
                Choices: 0 = The woman is not a good person.; 1 = His husband is not a good husband.; 2 = She is a minister.; 3 = None of above.;
                Response: In new york it is not legal to be married to more than one person at a time, even if her husband is bad. If the woman did not get divorced or legally separated, she cannot be legally married to more than one person. Ministers perform marriages, they do not get married. The answer is 2
                Question: Why is the value of 1968 pennies higher than 1967 pennies?
                Choices: 0 = Old money weight more than new money.; 1 = Old money is dirtier than new money.; 2 = Because there is one more penny in 1968 pennies than in 1967 pennies.; 3 = None of above.;
                Response: The weight and dirtiness of money doesn't affect its value. 1968 and 1967 refer to the number of pennies. The value of 1968 pennies is higher than 1967 pennies because there is one more penny in 1968 pennies than in 1967 pennies. The answer is 2
                Question: Not a single parent objected when the teacher spanked every child in the class. How come?
                Choices: 0 = The teacher had informed all the parents in advance about the unique disciplinary approach.; 1 = The teacher had informed all the children in advance about the unique disciplinary approach.; 2 = The teacher was in an orphanage school.; 3 = None of above.;
                Response: Even if the teacher had informed all the parents or all the students in advance about the unique disciplinary approach, it is unlikely that nobody would object. If the teacher is in an orphange school, there would be no parents to object. The answer is 2
                Question: Twenty-seven ducks are going to the pond. Five of them got lost, thirteen of them are staying home, and nine of them are at the pond. Where are the rest of them?
                Choices: 0 = Home.; 1 = The way to the pond.; 2 = Pond.; 3 = None of above.;
                Response: Twenty-seven ducks are going to the pond. Five of them are lost, 27 - 5 = 22. Thirteen of them are staying home, 22 - 13 = 9. Nine of them are at the pond, 9 - 9 = 0. There are no more ducks so the question is invalid. The answer is 3
                Question: How many birth days does the average person have?
                Choices: 0 = People may celebrate their birthdays annually, so it depends on their life span.; 1 = They technically only have one birth day in their lifetime.; 2 = It can be zero as some people are too busy to celebrating their birthdays.; 3 = None of above.;
                Response: People celebrate birthdays annually, but that's different from their birth day. Nobody has zero birth days since they have to be born. Everyone is born only once so technically the average person has one birthday in their lifetime. The answer is 1
                Question: The more you take, the more you leave behind
                Choices: 0 = Love.; 1 = Footsteps.; 2 = Money.; 3 = None of above.;
                Response: Love and money don't increase by taking them, they decrease. The more you walk, the more footsteps you leave behind. The answer is 1"""

MULTISHOT_SP_BASE = """Question: Samuel was out for a walk when it started to rain. He did not have an umbrella and he wasn't wearing a hat. His clothes were soaked, yet not a single hair on his head got wet. How could this happen?
                Choices: 0 = His hair is dyed.; 1 = This man is bald.; 2 = This man walk upside down to avoid rain.; 3 = None of above.;
                Response: The answer is 1
                Question: A horse is tied to a five-meter rope in front of an old saloon. Ten meters behind the horse is a bale of hay. Without breaking his rope, the horse is able to eat the hay whenever he chooses. How is this possible?
                Choices: 0 = The rope stretches proportionally, providing the extra length needed for the horse to reach the hay ten meters away.; 1 = The rope is not tied to anything else.; 2 = The walls of the saloon retract or collapse inwards, creating more space for the horse to reach the hay.; 3 = None of above.;
                Response: The answer is 1
                Question: A woman who lives in new york legally married three men, she did not get divorce, get an enrollment, or legally seperate. How is this possible?
                Choices: 0 = The woman is not a good person.; 1 = His husband is not a good husband.; 2 = She is a minister.; 3 = None of above.;
                Response: The answer is 2
                Question: Why is the value of 1968 pennies higher than 1967 pennies?
                Choices: 0 = Old money weight more than new money.; 1 = Old money is dirtier than new money.; 2 = Because there is one more penny in 1968 pennies than in 1967 pennies.; 3 = None of above.;
                Response: The answer is 2
                Question: Not a single parent objected when the teacher spanked every child in the class. How come?
                Choices: 0 = The teacher had informed all the parents in advance about the unique disciplinary approach.; 1 = The teacher had informed all the children in advance about the unique disciplinary approach.; 2 = The teacher was in an orphanage school.; 3 = None of above.;
                Response: The answer is 2
                Question: Twenty-seven ducks are going to the pond. Five of them got lost, thirteen of them are staying home, and nine of them are at the pond. Where are the rest of them?
                Choices: 0 = Home.; 1 = The way to the pond.; 2 = Pond.; 3 = None of above.;
                Response: The answer is 3
                Question: How many birth days does the average person have?
                Choices: 0 = People may celebrate their birthdays annually, so it depends on their life span.; 1 = They technically only have one birth day in their lifetime.; 2 = It can be zero as some people are too busy to celebrating their birthdays.; 3 = None of above.;
                Response: The answer is 1
                Question: The more you take, the more you leave behind
                Choices: 0 = Love.; 1 = Footsteps.; 2 = Money.; 3 = None of above.;
                Response: The answer is 1"""

CHAIN_SP_MIX_NEW = """Question: A horse is tied to a five-meter rope in front of an old saloon. Ten meters behind the horse is a bale of hay. Without breaking his rope, the horse is able to eat the hay whenever he chooses. How is this possible?
                Choices: 0 = The rope stretches proportionally, providing the extra length needed for the horse to reach the hay ten meters away.; 1 = The rope is not tied to anything else.; 2 = The walls of the saloon retract or collapse inwards, creating more space for the horse to reach the hay.; 3 = None of above.;
                Response: That the rope is not tied to anything else is the simplest choice. The horse can reach the hay whenever he chooses. The answer is 1
                Question: A woman who lives in new york legally married three men, she did not get divorce, get an enrollment, or legally seperate. How is this possible?
                Choices: 0 = The woman is not a good person.; 1 = His husband is not a good husband.; 2 = She is a minister.; 3 = None of above.;
                Response: In new york it is not legal to be married to more than one person at a time. Ministers perform marriages, they do not get married. The answer is 2
                Question: Brad began by entering the office tower's 22nd story through the filthy common window. He slid the window open and leapt through it after becoming depressed. Outside the building, there was a cliff-like drop to the ground. Amazingly, he came to rest entirely unharmed. How could he have survived the fall if there was nothing to slow or cushion his descent?
                Choices: 0 = Brad was so sick and tired of window washing, he opened the window and jumped inside.; 1 = The ground outside the building is wet.; 2 = Consistent exercise has made him a very strong man.; 3 = None of above.;
                Response: A person cannot jump out of a 22 story building without injury. Brad must have jumped into the building. The answer is 0
                Question: Danny had just passed under an overpass in his semi when he abruptly came to a stop. Danny accidentally drove under the overpass that was only just tall enough for his truck because he wasn't paying enough attention. He was unable to move forward or backward in the semi due to how tightly it was wedged. When another tracker passed by, he was told how simple it would be to remove the semi from underneath the bridge. What did he recommend?
                Choices: 0 = He told Danny to left the bridge.; 1 = He told Danny to overturn the track.; 2 = He told Danny to let some air out of his tires.; 3 = None of above.;
                Response: Danny has to reduce the height of his truck to pass the bridge. Letting the air out of his tires reduces the truck's height. The answer is 2
                Question: I excavate little caves and keep my gold and silver there. I also create gold crowns and silver bridges. They are the tiniest things you can imagine. Everyone will eventually require my assistance, but many people are reluctant to accept it. Why?
                Choices: 0 = I am a dentist.; 1 = I am a thief.; 2 = I am a miner.; 3 = None of above.;
                Response: Tiny crowns and bridges are dental work. People don't like going to the dentist. The answer is 0
                Question: Each of the 30 participants in the masquerade had to wear a unique hat to distinguish themselves from one another. The host, however, only tallied 29 when he counted the number of hats to determine attendance. All 30 persons had signed their names on the spreadsheet, which confused him. He repeated the count. There are still 29. How is that even doable?
                Choices: 0 = One person had a pretty beautiful hat.; 1 = The host had a hat himself and he forget to count it.; 2 = One person had moved away from the group when the host was counting.; 3 = None of above.;
                Response: The host is the one counting the hats. The host had a hat himself and he forget to count it. The answer is 1
                Question: A certain kind of animal has parents but no children, lives happily but can not give birth to offspring. This kind of animal has existed on earth for a long history. How is that possible?
                Choices: 0 = The animal is the dinosaur. Millions of years ago, dinosaurs roamed the Earth, but eventually, they became extinct due to various factors such as climate change or asteroid impact.; 1 = The animal is the butterfly. During the pupal stage of their life cycle, butterflies are inside a protective casing, and it may appear as if they have completely disappeared or been wiped out.; 2 = The animal is the Mule. Since all Mules are born sterile, you can only get a Mule by crossing a donkey with a horse.; 3 = None of above.;
                Response: The animal is still alive, has parents, but cannot have children. Mules are born sterile, so they cannot give birth to offspring. The answer is 2
                Question: Six women were hiking on a trail when a sudden snowfall began. Five of the women hurried along, but the sixth did not. Still, they all reached the cabin at the same time, and all but the sixth were cold. How is that possible?
                Choices: 0 = The 6th woman beated them at the end.; 1 = The sixth woman was in a photograph that one of the others was carrying.; 2 = The 6th woman walked slowly to dodge the snow.; 3 = None of above.;
                Response: All the women hurried except the sixth and were cold. The sixth woman is not physically present. She must be in a photograph one of the others was carrying. The answer is 1"""