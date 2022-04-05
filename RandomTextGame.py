print("Welcome to the game. Your goal is to reach the town, have fun!")
name = input("What is your name? ")
age = int(input("How old are you? "))

if age >= 18:
	print("You are old enough for this game")

	wants_to_play = input("Do you want to play the game? ").capitalize()
	if wants_to_play == "Yes":
		print("Let's start!")
		health = 50
		print(f"You start with {health}, and you will gain or lose more as your journey progresses")

		forwards_or_backwards = input("Do you want to forwards or backwards(forwards/backwards)? ")
		if forwards_or_backwards == "forwards":
			ans = input("You made it a past a tree with a weird, angelic looking statue next to it. "
						"Do you inspect it or do you continue on with your journey(inspect/continue)? ")
			if ans == 'inspect':
				print("As you inspect the statue, it starts to glow. "
					  "You close your eyes, and your max health increases by 30.")
				health == 80

				ans = input("You see the town in the horizon, but before you reach the town, "
							"a woman approaches you and asks you to help her wash her clothes, do you(yes/no)? ")
				if ans == 'yes':
					print("You get your shit kicked in by the woman who turns out to be the tree from earlier")
					health == 30
					print("You made it to the town with a few bruises, but you are alive.")

				else:
					print("You continue on with your journey and make it to the town without a single scratch on your body, congrats.")


			elif ans == 'continue':
				print(
					"You continue on with your journey. A little while after you leave the tree, the angelic statue starts to glow.")

				ans = input("You notice a beautiful lady on the edge of the river washing her clothes, do you approach her(yes/no)? ")
				if ans == 'yes':
					print("You get your shit kicked in by the lady who turns out to be the tree from earlier")
					health -= 50

				else:
					print("You ignore the lady and carry on with your journey")
					print("You reach the town and thus the game has ended, hope you had fun.")

			else:
				print("You get your shit kicked in by the tree while you stood there helpless, game over.")
		else:
			print("Leaving the game so quickly, are you not good enough? ")
	else:
		print("Goodbye then")
else:
	print("Sorry, you are too young to play this game.")
