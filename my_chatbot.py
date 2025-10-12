# A very simple, rule-based chatbot

def college_chatbot():
    # Print a welcome message
    print("Hello! I am the College Enquiry Bot.\nHow can I help you today? 🙏")
    print("You can ask me about timings, Teachers ,location, or courses.")

    # Start an infinite loop to keep the conversation going
    while True:
        # Get input from the user and convert it to lowercase
        user_input = input("You: ").lower()

        # --- This is where our rules (if/elif/else) are ---

        # Rule 1: Check if the user wants to say hi
        if "hello" in user_input or "hi" in user_input or "whats up"  in user_input:
            print("Bot: Hi there! What can I help you with?")

        # Rule 2: Check for questions about college timings
        elif "timing" in user_input or "hours" in user_input:
            print("Bot: The college is open from 9 AM to 5 PM, [ Monday to Friday ].")

        elif "name" in user_input or "college name" in user_input:
            print("College name is : New Horizon College of engineering ")


        # Rule 3: Check for questions about the location
        elif "location" in user_input or "where" in user_input:
            print("Bot: The college is located at Marathalli , Bengaluru City.")

        # Rule 4: Check for questions about courses
        elif "courses" in user_input or "programs" in user_input:
            print("Bot: We offer courses in Artifical Intelligence ,Computer Science, Data science,Business etc .")

        elif "teachers" in user_input or "faculty" in user_input:
            print("Teachers are highly educated especially [ Shravya Shetty Mam ] (AI Teacher) 🚀")


        # Rule 5: Check if the user wants to exit
        elif "bye" in user_input or "exit"   in user_input or "ok" in user_input:
            print("Bot: Goodbye! Have a great day.🥰")
            break  # This keyword breaks the loop and ends the program

        # Rule 6 (Else): If the bot doesn't understand
        else:
            print("Bot: I'm sorry, I don't understand that. Please ask me about timings, location, or courses.")

# This line starts the chatbot function when the script is run
college_chatbot()


        