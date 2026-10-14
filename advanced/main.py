import json

#json files
n = 1
json_file = "level_" + str(n) + "_character.json"

#messages for inputs
level_up = "Do you want to level up? Type yes or no.\n"
attribute_choice = """You have one point to increase you attributes. What would you like to increase?
Strength | Dexterity | Constitution | Intelligence | Wisdom | Charisma\n"""
weapon = """What weapon would you like to add?\n"""
add_weapon = "Should a weapon be added? Type yes or no\n"
add_skill = "Should a skill be added. Type yes or no\n"
skill = "What skill would you like to add?\n"


#list of attributes
attributes_list = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
]

#values for points
attribute_points = 1
selected_points = 0

#weapons you get upon leveling up
weapons = ["Shadow Dagger", "Greatsword", "Crossbow"]

#skills you can receive
skills = ["Investigation", "Survival", "Stealth"]

#reads the level 1 character jason file


#loop to ask and assign new values to file
while True:
    if n >= 4:
        print("Max level reached.")
        break
    else:
        with open(json_file, "r") as file:
            data = json.load(file)
        try:
            #while loops for checkpoints
            while True:
                print("type exit to quit")
                #level up section
                level_up_input = input(level_up).strip().lower()
                if level_up_input == "no":
                    print("You will remain at level", data["level"])
                    break
                elif level_up_input == "exit":
                    break
                elif level_up_input == "yes":
                    data["level"] += 1
                    data["armor_class"] += 1
                    print("You are now level", data["level"], "with an armor class of", data["armor_class"])
                    try:
                        while True:
                            #attribute select
                            attribute_select = input(attribute_choice).strip().lower()
                            if attribute_select in attributes_list:
                                data["attributes"][attribute_select] += 1
                                print("You have upgraded", attribute_select, "and are now at", data["attributes"][attribute_select])
                                break
                            else:
                                print("invalid input")
                    except ValueError:
                        print("Invalid input")
                    while True:
                        #Skill select
                        skill_input = input(skill).strip().title()
                        if skill_input.isdigit():
                            print("Invalid input")
                        else:
                            data["skills"].append(skill_input)
                            break
                    while True:
                        #Weapon select
                        weapon_input = input(add_weapon).strip().lower()
                        if weapon_input.isdigit():
                            print("Invalid command")
                        else:
                            if weapon_input == "yes":
                                weapon_select = input(weapon).strip().title()
                                if weapon_select.isdigit():
                                    print("Invalid command")
                                else:
                                    data["weapons"].append(weapon_select)
                                    print(f"You added a {weapon_select}")
                                    break
                            elif weapon_input == "no":
                                print("No weapon will be added")
                                break
                    n += 1
                    json_file = "level_" + str(n) + "_character.json"
                    with open(json_file, "w") as file:
                        json.dump(data, file, indent=4)
                    break
                else:
                    print("invalid input")
        except ValueError:
            print("Invalid input")