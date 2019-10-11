from textwrap import dedent
from random import randint
from game_45_b import Engine

starvation_level = 80

class Scene(object):
    
    hunger_quips = [
        "You are dangerously close to giving in to the power of kale.",
        "Kale is calling your name.",
        "I foresee kale in your future.",
        "You are doing great! If you are actually trying to eat kale.",
        "If you aren't careful, you will be swimming in kale shortly.",
    ]
    
    def hunger_update(self):
        print(f"Your stomach rumbles, your starvation level has increased to {starvation_level}! ")
        if starvation_level >= 100:
            return 'death'
        print(Scene.hunger_quips[randint(0, len(self.hunger_quips)-1)]) 
    
class Defeat(Scene):
    
    def enter(self):
        print(dedent("""
            Your starvation level has reached 100, the hunger is too much to bare. You walk to 
            the fridge and take out the cranberry walnut kale salad your 'loving' wife made for
            you. After eating your salad, your starvation level only drops to 95, you decide to steal 
            someones lunch from the fridge. That person catches you and you get fired. Your wife thinks 
            you are a loser for getting fired and actually eating the kale salad she made for you,
            she said it was a prank. She leaves you and takes the house. You are now single, homeless
            and jobless. All because you ate a kale salad...you deserve it.
            """))
        exit(1)    

class Cubicle(Scene):
    
    def enter(self):
        global starvation_level

        print(dedent(f"""
            You are sitting at your desk, 30 minutes until lunch...your starvation level has 
            hit {starvation_level}. Once you hit 100, you will give up and eat kale salad.
            Your co-worker, Mike, is eating BBQ ribs and it is driving you crazy. Your stomach rumbles. 
            Do you 'ask for a bite', 'eat your kale salad' or 'get up and walk away'? 
            """))
        
        action = input("Tough choice, but you choose to: ")

        if action == "ask for a bite":
            print("What have you done, it is so good, it makes you even hungier! You need to walk away.")
            print("before you push him to the gound and take all of his BBQ ribs.")
            
            starvation_level += 10
            hungry_employee.hunger_update() 
            
            return 'break_room'
        
        elif action == "eat your kale salad":
            print("What! You have lost control! No sane person would make this choice, you need help. ")
            
            starvation_level += 20
            if starvation_level >= 100:
                return 'defeat' 
        
        elif action == "get up and walk away":
            print(dedent("""
                Wise move but that did not solve your hunger issue. Although, it may have saved Mike
                from getting punched in the face. 
            """))
            
            starvation_level += 5
            hungry_employee.hunger_update()
            
            return 'break_room'      
        
        else: 
            print("That was not an option, you are so hungry you are delirious and can't read")
            
            starvation_level += 5
            hungry_employee.hunger_update()
            
            return 'cubicle'
           
    
class BreakRoom(Scene):
    
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def enter(self):
        global starvation_level
        print(dedent("""
            You wonder into the break room, to escape the sweet smell of BBQ sauce. You overhear 2 co-workers
            talking about food leftover from a meeting. Your co-worker can see despiration in your eyes
            and decides to play a game with you and make you guess what food it is and where it is located. 
            You are in no mood for guessing games but you are at the mercy this heartless bastard. 
            """))
        
        question_prompts = [
        "What food is leftover?\n(a) Pizza\n(b) Sandwiches \n(c) Burrito Bar\n Answer:",
        "What room has the leftovers?\n(a) Dev Office\n(b) Lunch Room\n(c) 3rd Floor Meeting Room\n Answer:",
        ]

        questions = [
        BreakRoom(question_prompts[0], "a"), # assign a prompt and an answer to each element in the array (class parameters are prompt, answer)
        BreakRoom(question_prompts[1], "b"),
        ]
        
        score = 0
        
        while score <2:
            print("You aren't going anywhere until you get these 2 questions right")           
            score = 0            
            for question in questions:
                answer = input(question.prompt)           
                if answer == question.answer: 
                    score +=1
            
        starvation_level += 5
            
        if starvation_level >= 100:
            return 'defeat'

        print("\nGood job, now you know there is pizza in the lunch room!")
        hungry_employee.hunger_update()
        
        return 'lunch_room'                

class LunchRoom(Scene):
    
    def enter(self):
        global starvation_level
        print(dedent("""
            You speed walk to the lunch room as your starvation level nears 100 and peek through the window 
            on the door. There sits a pizza on the table with 3 slices left! Your stomach groans as you 
            reach for your badge to unlock the lunch room door. Crap on a cracker! You realize you left your badge 
            at your desk! Going back now is too risky, the pizza could be gone by the time you return. 
            There is a keypad on the door, it is 4-digits but it has been so long since you have had to 
            use it you can only remember the first 3 digits so you will have to guess on the last digit. 
            If you fail 4 times the keypad will disable for 5 minutes and you will be knee deep in kale, 
            can you crack the code?
        """))
        
        mystery_number = "4"
        guess = ""
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False

        while guess != mystery_number and not (out_of_guesses):
            if guess_count < guess_limit:
                guess = input("You enter \"123\" for the 1st 3 digits. Enter guess for the last digit: ")
                guess_count += 1
                if guess != mystery_number:
                    print("Shoots! That's not it!")
                    starvation_level += 5
                    hungry_employee.hunger_update()
                if starvation_level >= 100:
                    return 'defeat'
            else:
                out_of_guesses = True

        if out_of_guesses:
            print(dedent("""
                The keypad reads \"Error\" and your heart sinks, you look through the window on the door.
                You see Kevin, from accounting, spot the pizza. He smiles as he throws his Weight Watchers 
                microwavable lunch into the garbage and scoops up the 3 remaining pieces of pizza.                  
                """))
            
            return 'defeat'
        
        else:
            print("Whoa, lucky guess! The keypad reads \"Success\" and the door unlocks.")
            
            return 'victory'

class Victory(Scene):
    
    def enter(self):
        print(dedent("""
            Woo hoo! All of your hard work and determination have paid off. You scoop up the remaining
            pieces of pizza and head back to your desk. Victory has never been soooo cheesy!
            """))
        
        exit(1)

class SceneDirector(Scene):

    scenes = {
        'cubicle' : Cubicle(),
        'break_room' : BreakRoom("prompt", "answer"),
        'lunch_room' : LunchRoom(),
        'victory' : Victory(),
        'defeat' : Defeat(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = SceneDirector.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

hungry_employee = SceneDirector('cubicle')
lunch_time = Engine(hungry_employee)
lunch_time.play()    