import json

naked_configurations = ''
with open("configurations.json","r") as f:
    naked_configurations = f.readline()
configurations = json.loads(naked_configurations)

while True:
    bruh = input("what ")
    if bruh == "name":
        print(configurations["name"])
    elif bruh == "age":
        print(configurations["age"])
    elif bruh == "occupation":
        print(configurations["occupation"])
    elif bruh == "no":
        bruh = input("why ")
        if bruh == "name":
            bruh = input("then ")
            configurations['name'] = bruh
            with open("configurations.json","w") as f:
                naked_configurations = json.dumps(configurations)
                f.write(naked_configurations)
                f.close()
        elif bruh == "age":
            bruh = input("then ")
            configurations['age'] = bruh
            with open("configurations.json","w") as f:
                naked_configurations = json.dumps(configurations)
                f.write(naked_configurations)
                f.close()
        elif bruh == "occupation":
            bruh = input("then ")
            configurations['occupation'] = bruh
            with open("configurations.json","w") as f:
                naked_configurations = json.dumps(configurations)
                f.write(naked_configurations)
                f.close()
    elif bruh == "nvm":
        quit()
    else:
        print("what?")

