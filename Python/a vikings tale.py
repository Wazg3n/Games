# define the different locations in the game
village = "village"
forest = "forest"
ocean = "ocean"

# define the initial state of the game
location = village
enemies_defeated = 0

# define the main game loop
while True:
  # display the current location and the number of enemies defeated
  print(f"You are in the {location}.")
  print(f"You have defeated {enemies_defeated} enemies.")
  
  # get the player's next action
  action = input("What would you like to do? (fight/run/hide): ")
  
  # handle the fight action
  if action == "fight":
    enemies_defeated += 1
    print("You have defeated an enemy!")
  
  # handle the run action
  elif action == "run":
    print("You run away from the enemy.")
    location = ocean
  
  # handle the hide action
  elif action == "hide":
    print("You hide in the forest and wait for the enemy to pass.")
    location = forest
  
  # handle invalid actions
  else:
    print("Invalid action. Please try again.")
    
  # check if the player has won the game
  if enemies_defeated == 3:
    print("You have defeated all of the enemies and protected your village!")
    
    # interactive story begins
    print("As you stand victorious, you can't help but think about your family. As you look around, you realize that your wife and children are nowhere to be found. You frantically search for them, but eventually learn that they were killed during the raid.")
    action = input("Do you stay in the village to rebuild or do you set out on a quest for revenge? (stay/revenge): ")
    
    if action == "stay":
      print("You stay in the village and work hard to rebuild and honor your family's memory. Though the pain of their loss will always be with you, you find solace in the sense of community and purpose that rebuilding brings.")
      break
    elif action == "revenge":
      print("Devastated by the loss of your loved ones, you are filled with a burning desire for revenge. You set out to track down the raiders and bring them to justice. Your journey takes you across the ocean, where you encounter many challenges and make new allies. Eventually, you track down the raiders who attack your village and bring them to justice. Though you can never bring your family back, you find some sense of closure knowing that the perpetrators have been punished.")
      
      # plot twist begins
      print("As you return home to your village, you are greeted with a hero's welcome. The villagers shower you with praise and gratitude for defending them against the raiders.. However, something doesn't feel right. You soon discover that the raiders who attacked your village were actually hired by a rival village, and that your own village leaders were in on the plot. Enraged by this betrayal, you must decide whether to forgive and rebuild, or seek further vengeance.")
      action = input("Do you forgive and rebuild or seek further vengeance? (forgive/vengeance): ")
      
      if action == "forgive":
        print("You choose to forgive and rebuild, hoping to use this experience to bring about peace between the two villages. Though it is a difficult path, you are eventually able to broker a treaty and bring an end to the cycle of violence. You find solace in the knowledge.")
        break
    elif action == "revenge":
      print("You are filled with anger and betrayal as you realize that you have been fighting for a cause that was not just. But rather than succumb to despair, you decide to seek further justice.")

print("You gather your allies and set out to confront the rival village, determined to bring an end to their deceit and betrayal once and for all.")
print("After a long and grueling battle, the viking and his allies finally confront the rival village and bring an end to their deceit and betrayal. The viking is hailed as a hero once again, and the villagers express their gratitude and admiration for his bravery and determination. But despite his victories, the viking is left with a heavy heart. The loss of his wife and children weighs heavily on him, and he feels a sense of emptiness and sadness that he cannot shake. As he reflects on the events of the past, the viking realizes that his quest for justice has cost him everything. He has lost his family, his home, and his sense of purpose. Feeling defeated and alone, the viking decides to leave his village behind and set out on a journey of self-discovery. He wanders the land, searching for a sense of belonging and meaning in a world that seems to have betrayed him. As he travels, the viking encounters many challenges and hardships. But he remains determined and resolute, driven by the memory of his loved ones and the desire to honor their legacy. In the end, the viking finds peace and acceptance in a new land, surrounded by a community of like-minded individuals who understand his pain and support his journey. But even as he finds happiness in his new life, the viking never forgets the tragedy that led him there. And as he looks back on his journey, he realizes that the road to justice is often a long and difficult one, filled with heartache and loss.")