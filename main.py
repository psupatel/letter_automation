#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Open guest list and letter template
with open ("./Input/Names/invited_names.txt", "r") as guests:
    guest_list = guests.readlines()

# Name by name, open the letter template, add the name to the template and replace the sender, create a new title,
# and add the new letter to the output folder
with open ("./Input/Letters/starting_letter.txt") as letters:
    letter_template = letters.read()
    for name in guest_list:
        stripped_name = name.strip()
        new_letter = letter_template.replace("[name]", stripped_name)
        new_letter = new_letter.replace("Angela", "Sanjiv")
        new_file = "./Output/ReadyToSend/letter_to_" + name
        with open(new_file, "w") as file:
            file.write(new_letter)
