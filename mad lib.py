import random

verb = input("type verb")
adj = input("type adj")
noun = input("type noun")
adverb = input("type adverb")
pronoun = input("type any pronoun")
preposition = input("type preposition")

stories = ["hi my name is" +noun+ "i am " + adj + "boy.I study btech at" + verb +"osmania university"+ adverb+ "I do electrical engineering" +pronoun+ "i like electrical circuits subject very much" +preposition+ "i hate power systems." ,
"flat earth is really" +adj+ "it really makes no sense " +verb+ "but still many people in america believe this theory" +noun+ "round earth is th einevitable truth" +adverb+ "flat earth theory was outdated " +pronoun+ "earth round shape makes it rvolve around sun" +preposition+ "so flat earth theory is disposed",
"life is said to be" +verb+ " happily we have to make ourselfs" +adj+ "happy and" +noun+ " around us happy by" +adverb+ " in the correct way sometimes life gives" +pronoun+ " us hard times but we have to face it with courage and bravery which" +preposition+ " to strengthen our character"]

randomstories= random.choice(stories)

print(randomstories)