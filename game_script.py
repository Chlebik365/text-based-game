import engine as game
from time import sleep

def red_text(string):
    return f"\033[31m{string}\033[0m"  # ANSI escape code for red text

def blue_text(string):
    return f"\033[34m{string}\033[0m"  # ANSI escape code for blue text

def green_text(string):
    return f"\033[32m{string}\033[0m"  # ANSI escape code for green text

def yellow_text(string):
    return f"\033[33m{string}\033[0m"  # ANSI escape code for yellow text

def purple_text(string):
    return f"\033[95m{string}\033[0m"  # ANSI escape code for light purple text



def title_screen():
    global player_name, player_sex
    
    while True:
        skip = (input("Do you want to skip dialogue? For the story I recommend to say no. Yes/No: "))
        print("\n")
        
        if skip.lower() == "no":
            print(f"Welcome, {blue_text("traveler")}.\n")
            sleep(2)
            print(f"{blue_text("You")} are lost in a {green_text("Dark Forest")}.")
            sleep(4)
            print(f"Oh, yes, {purple_text("I")} forgot to introduce {purple_text("myself")}.")
            sleep(4)
            print(f"{purple_text("I")} am {purple_text("Aetherion")}, the ruler of {green_text("Dark Forest")}.")
            sleep(4)
            player_name = input(f"How should {purple_text("I")} refer to {blue_text("you")}? ")
            sleep(1)
            player_sex = input(f"Are {blue_text("you")} male or female? ")
            sleep(1)
            print(f"Yet again, welcome, {blue_text(player_name)}.\n")
            sleep(4)
            print(f"{blue_text("You")} might be wondering why you're here.")
            sleep(4)
            print("One shall find the reason for struggle after they have defeated it.\n")
            sleep(4)
            print(f"There is a path out, but {blue_text("you")} can see a {yellow_text("shadowy figure")} ahead.")
            sleep(6)
            print(f"{blue_text("You")} identify the shadowy figure as a {yellow_text('skeleton')}.\n")
            sleep(4)
            print(f"You wield an old, {green_text("rusty sword")}.")
            sleep(4)
            print("It has definitely seen better days, but using it is your only option.")
            sleep(4)
            print(f"{blue_text(player_name)}, we shall meet again.")
            sleep(4)
            print(f"And there, {blue_text("your")} adventure starts.\n")
            sleep(8)
            break
        
        elif skip.lower() == "yes":
            print(f"{blue_text("You")} skipped the dialogue!")
            sleep(4)
            player_name = input("What is your name? ")
            sleep(1)
            player_sex = input(f"Are {blue_text("you")} male or female? ")
            sleep(4)
            print(f"And there, {blue_text("your")} adventure starts.\n")
            sleep(8)
            break

        else:
            print(red_text("Invalid input!"))
    

def initialize_game(player_name):
    global player, skeleton, zombie, rusty_sword, sword ,bare_hands

    player = game.Player(player_name, 100, 0, 5, 20, 50, 1, 0, 100)

    skeleton = game.Enemy("Skeleton", 50, 0, 10, 20, 50, 1, 40)
    zombie = game.Enemy("Zombie", 75, 0, 15, 25, 50, 1, 60)

    skeleton.is_alive = False
    zombie.is_alive = False

    rusty_sword = game.Weapon("Rusty Sword", 10, 20, 50, 1, 0, 75)
    sword = game.Weapon("Sword", 15, 30, 60, 1, 0, 80)
    bare_hands = game.bare_hands

    print(f"Here is {blue_text("your")} {green_text("sword")}.")
    player.obtain_item(bare_hands)
    player.obtain_item(rusty_sword)
   
    print(f"With this in mind, your first {red_text("fight")} shall come along.\n")
    sleep(4)

def first_kill():
    sleep(2)
    print(f"\n{blue_text("You")} killed the {yellow_text("skeleton")}!")
    sleep(6)
    print(f"Though {blue_text("you")} are now a {red_text("murderer")}, {blue_text("you")} are on the right path.")
    sleep(4)
    print(f"{purple_text("I")} shall reward you for your actions later, but for now, you may continue your journey.\n")
    sleep(8)

def second_kill():
    sleep(2)
    print(f"\nYet another {yellow_text("skeleton")} down!")
    sleep(2)
    print(f"{purple_text("I")} am impressed.")
    sleep(1)
    print(f"{blue_text(player.name)}, {blue_text("you")} are truly skilled.") # type: ignore
    sleep(4)
    print(f"Though {purple_text("I")} believe {blue_text("you")} are skilled, {purple_text("I")} have not yet decided whether {blue_text("you")} are worthy of {purple_text("my")} {green_text("sword")}.\n")
    sleep(8)

def third_kill():
    sleep(2)
    print(f"\nYet another {yellow_text("skeleton")} down!")
    sleep(1)
    print(f"More worthy {yellow_text("opponents")} shall come.")
    sleep(5)
    print(f"{blue_text("You")} are in need of a better {green_text("weapon")}.")
    sleep(4)
    print(f"Thus, {purple_text("I")} reward {blue_text("you")} {purple_text("my")} {green_text("sword")}.\n")
    sleep(5)
    
    player.obtain_item(sword) # type: ignore

    answer = input(f"\nAnything you want to tell {purple_text("me")}? ")
    if answer.lower() == "aetherion":
        print(f"\n{blue_text("You")} may have noticed that {purple_text("I")} no longer take pauses in my speech.")
        sleep(2)
        print(f"This is caused purely by {purple_text("Philip")} being too lazy to put sleep() statements everywhere.")
        sleep(4)
        print(f"So me, {purple_text("Martin")}, fixed it for him.")
        sleep(2)
        print(f"{blue_text("You")}'re welcome!")
        sleep(4)
        print(f"But {purple_text("Martin")} also wrote speep(2) in second_kill(), so {purple_text("I")} ({purple_text("Philip")}) had to correct it.")
        sleep(2)
        print("This is hopefully the last time.")
        sleep(4)
        print(f"Your journey awaits {blue_text("you")}, {blue_text(player.name)}.\n") # type: ignore
        sleep(8)

    else:
        print("\nNothing?")
        sleep(6)
        print(f"{purple_text("I")} see.")
        sleep(2)
        print(f"Your journey awaits {blue_text("you")}, {blue_text(player.name)}.\n") # type: ignore
        sleep(8)

def fourth_kill():
    sleep(2)
    print(f"\n{blue_text(player.name)}, how did {blue_text("you")} fare in the battle?") # type: ignore
    sleep(4)
    print("Well, we see yet again, so your sword must've done wonders.")
    sleep(6)
    print(f"{purple_text("Philip")} is too lazy to make more stages, so in the meantime, enjoy leveling up and killing endless {yellow_text("zombies")} and {yellow_text("skeletons")}!")
    sleep(8)
    print(f"{purple_text("I")}, {purple_text("Aetherion")} will await our next encounter.")
    sleep(4)
    print("Until then, good luck.\n")
    sleep(10)

def spawn_enemies(enemies_to_spawn):
    global skeleton, zombie, player

    choices = 0

    if "skeleton" in enemies_to_spawn:
        choices += 1

    if "zombie" in enemies_to_spawn:
        choices += 1
    
    if choices == 2:
        if game.randint(0, 1) == 0 and not skeleton.is_alive:
            skeleton = game.Enemy("Skeleton", 50, 0, 10, 20, 50, player.level, 40)
        
        elif not zombie.is_alive:
            zombie = game.Enemy("Zombie", 75, 0, 15, 25, 50, player.level, 60)
    
    elif "skeleton" in enemies_to_spawn and not skeleton.is_alive:
        skeleton = game.Enemy("Skeleton", 50, 0, 10, 20, 50, player.level, 40)
        if zombie.is_alive:
            zombie.is_alive = False
    
    elif "zombie" in enemies_to_spawn and not zombie.is_alive:
        zombie = game.Enemy("Zombie", 75, 0, 15, 25, 50, player.level, 60)
        if skeleton.is_alive:
            skeleton.is_alive = False

title_screen()
initialize_game(player_name)

completed_stage_one = False
completed_stage_two = False
completed_stage_three = False
completed_stage_four = False

while True:

    if player.murder_count == 0: # type: ignore
        enemies_to_spawn = ["skeleton"]

    if player.murder_count == 1 and not completed_stage_one: # type: ignore
        first_kill()
        completed_stage_one = True

    if player.murder_count == 2 and not completed_stage_two: # type: ignore
        second_kill()
        completed_stage_two = True
    
    if player.murder_count == 3 and not completed_stage_three: # type: ignore
        third_kill()
        enemies_to_spawn = ["zombie"]
        completed_stage_three = True
        
    if player.murder_count == 4 and not completed_stage_four: # type: ignore
        fourth_kill()
        enemies_to_spawn = ["skeleton", "zombie"]
        completed_stage_four = True

    spawn_enemies(enemies_to_spawn)


    player.prompt_attack() # type: ignore

