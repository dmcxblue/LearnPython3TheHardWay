# /bin/python3.7

from sys import argv

script, user_name, last_name = argv
prompt = '>>>> '

print(f"Hi {user_name} {last_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name} {last_name}?")
likes = input(prompt)

print(f"Where do you live {user_name} {last_name}?")
lives = input(prompt)

print(f"What kind of computer you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
