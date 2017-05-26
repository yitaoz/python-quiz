import string

# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

easy_paragraph = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

easy_answers = ["function", "variables", "null", "arrays"]


medium_paragraph = '"Animals have played a major role in human\'s lives throughout history. Today, scientific research is trying to ___1___ the positive aspects of living with companion animals. Animals have been used as an ___2___ form of treatment for many years. More recently it has been discovered that owning a pet can help lower people\'s blood pressure, ___3___ the chances of living after a heart attack, keep people more active and provide more satisfaction with life. It is ___4___ that this happens because pets help people become more social, provide a means to give and receive ___5___, and help connect us with the natural world."'

medium_answers = ["discover", "alternative", "enhanced", "theorized","affection"]

hard_paragraph = '"Starting a ___1___ data entry business is easier than trying to work from job to job. Having a business means that people will come to your business whenever they need a service you ___2___. This also means that instead of having to always ___3___ for jobs on freelancing websites, you will be able to have clients come to you as needed. One important thing to ___4___ when starting a data entry business is that customer service is really important. \n\nIt\'s hard to get anywhere in the data entry field if you don\'t ___5___ your customers with all the services they need. It\'s important that you take your time to really care for your customers completely. Once you are ready to start your data entry business it\'s time to start building a great team. You want to have a team that can do a ___6___ range of tasks so that your business can fill customer\'s needs. You want to always test your team before giving them the task of working with a client."'

hard_answers = ["complete","offer","apply","remember","provide","wide"]

MAX_ATTEMPTS = 5
LAST_ATTEMPT = 1
NO_ATTEMPTS_LEFT = 0

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

"""
	Behavior: This function runs the easy version of the quiz
	Inputs: Takes no inputs
	Outputs: This function returns no value

"""
def run_easy_quiz():
	print "You've chosen easy!\n\nYou will get 5 guesses per problem\n\n"
	run_quiz(easy_paragraph,easy_answers)

"""
	Behavior: This function runs the medium version of the quiz
	Inputs: Takes no inputs
	Outputs: This function returns no value

"""
def run_medium_quiz():
	print "You've chosen medium!\n\nYou will get 5 guesses per problem\n\n"
	run_quiz(medium_paragraph,medium_answers)


"""
	Behavior: This function runs the hard version of the quiz
	Inputs: Takes no inputs
	Outputs: This function returns no value

"""
def run_hard_quiz():
	print "You've chosen hard!\n\nYou will get 5 guesses per problem\n\n"
	run_quiz(hard_paragraph,hard_answers)

"""
	Behavior: This function replaces the blank in the paragraph with the correct answer
	Inputs: The current paragraph text, the correct answer, the blank number that the answer is the replace
	Outputs: Updated paragraph text with the blank filled.

"""
def update_paragraph_text(paragraph_text,answer,position):
	token_to_replace = "___"+str(position)+"___"

	return paragraph_text.replace(token_to_replace,answer)

"""
	Behavior: This function runs a quiz given the paragraph and corresponding answers
	Inputs: Paragraph text with blanks, answers to the paragraph texts
	Outputs: No output

"""
def check_guesses_left(guesses):
	guesses-=1
	if guesses ==NO_ATTEMPTS_LEFT:
		print "You've failed too many straight guesses! Game Over!"
		return guesses
	if guesses ==LAST_ATTEMPT:
		print "That isn't the correct answer! Let's try again: you have 1 try left! Make it count!\n\n"
	else:
		print "That isn't the correct answer! Let's try again: you have " + str(guesses)+" trys left!\n\n"	

	return guesses

"""
	Behavior: This function runs a quiz given the paragraph and corresponding answers
	Inputs: Paragraph text with blanks, answers to the paragraph texts
	Outputs: No output

"""
def run_quiz(paragraph_text,paragraph_answers):
	
	guesses=MAX_ATTEMPTS

	for answer in paragraph_answers:
		while True:
			print "The current paragraph reads as such:"
			print paragraph_text
			user_answer = raw_input("\n\nWhat should be substituted in for __"+str(paragraph_answers.index(answer)+1)+"__? ")
			if user_answer == answer:
				paragraph_text=update_paragraph_text(paragraph_text,answer,paragraph_answers.index(answer)+1)
				guesses = MAX_ATTEMPTS
				print "\nCorrect!\n\n"
				break
			else:
				guesses = check_guesses_left(guesses)
				if guesses == NO_ATTEMPTS_LEFT:
					return

	print paragraph_text

	print "\n\nYou Won!"

"""
	Behavior: Initializes the quiz selection loop
	Inputs: Takes no inputs
	Outputs: Gives no outputs

"""
def init_quiz():
	user_choice = raw_input("Please select a game difficulty by typing it in! \nPossible choices include easy, medium and hard.\n")

	while True:

		if user_choice == "easy":
			run_easy_quiz()
			break
		elif user_choice == "medium":
			run_medium_quiz()
			break
		elif user_choice == "hard":
			run_hard_quiz()
			break
		else:
			user_choice = raw_input("Invalid selection! Please select either easy, medium or hard\n")


init_quiz()




