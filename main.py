
def start_jarvis():
    print("================================")
    print("       JARVIS AI ONLINE")
    print("================================")
    print("Hello! I am your personal AI assistant.")
    print("Type 'exit' to shut me down.")

    while True:
        command = input("\nYou: ")

        if command.lower() == "hello":
            print("JARVIS: Hello! How can I help you?")

        elif command.lower() == "how are you":
            print("JARVIS: All systems are running perfectly!")

        elif command.lower() == "your name":
            print("JARVIS: I am JARVIS, your personal AI.")

        elif command.lower() == "exit":
            print("JARVIS: Goodbye, Sir!")
            break

        else:
            print("JARVIS: I am still learning. Please teach me!")

start_jarvis()

