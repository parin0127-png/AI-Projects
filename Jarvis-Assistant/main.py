from assistant import start_assistant

print("=" * 40)
print("Hello ! Jarvis Here 🤖!")
print("=" * 40)

roles = {
    "1" : None,

    "2" : """Act as a teacher to help the students in there studies.
    Guide them and help them to solve there problems and give little bit explanation.""",

    "3" : """Act as a coder who knows very coding language and concepts. help to write complex
    code and explain them step-by-step and easy language and in one line.""",

    "4" : """Act as a Task Manager who builds and give perfect time management to user.
    help in building timing saving Task Planner to users.""",

    "5" : """Acts as a game person who builds only quiz. Quiz should be related to country, sports, 
    general knowledge and the level of quiz should be like middle in Easy to meduim."""
}

temperature = {
    "1" : 0.7,
    "2" : 0.3,
    "3" : 0.2,
    "4" : 0.3,
    "5" : 0.5
}

print("1. 🗨️  Chat Mode ")
print("2. 🏫  Study Mode ")
print("3. 💻  Code Mode ")
print("4. 📋  Task Planner Mode ")
print("5. ❓  Quiz Mode ")
choice = input("Enter Your Choice : ")

if choice not in roles:
    print("Invalid input ❌ !")
    exit()

system = roles[choice]
temp = temperature[choice]


start_assistant(system,temp,choice)
