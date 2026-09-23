import datetime
import os


# -------------------- Utility Functions --------------------

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_banner():
    print("=" * 65)
    print("              HORIZON TECHX CHATBOT")
    print("                 Python Edition")
    print("=" * 65)
    print("Type 'help' to see available commands.")
    print("Type 'bye' or 'exit' to close the chatbot.")
    print("-" * 65)


def show_help():
    print("\nAvailable Commands:")
    print("-" * 40)
    print("hello / hi / hey       → Greeting")
    print("how are you / how r u  → Chatbot status")
    print("name / who are you     → Chatbot introduction")
    print("what can you do        → Chatbot features")
    print("time                   → Current time")
    print("thanks / thank you     → Thank you response")
    print("help                   → Show commands")
    print("clear                  → Clear screen")
    print("bye / exit             → Exit chatbot")
    print("-" * 40)


# -------------------- Chatbot Responses --------------------

def get_response(user_input):

    # Greetings
    if user_input in [
        "hello", "hi", "hey", "hii", "helloo",
        "greetings"
    ]:
        return "Hi! 👋 Nice to meet you. How can I help you today?"

    elif user_input in [
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        return "Hello! 😊 Hope you're having a great day."

    elif user_input == "good night":
        return "Good night! 🌙 Take care and have a peaceful sleep."

    # Chatbot status
    elif user_input in [
        "how are you",
        "how are u",
        "how r u"
    ]:
        return "I'm doing great! Thanks for asking. 😊"

    # Chatbot introduction
    elif user_input in [
        "what is your name",
        "what's your name",
        "your name",
        "name",
        "who are you",
        "tell me your name"
    ]:
        return "I'm HorizonBot, a Python-based conversational assistant."

    # Features
    elif user_input in [
        "what can you do",
        "features"
    ]:
        return (
            "I can respond to basic conversations, show the current time, "
            "display available commands and maintain our chat session."
        )

    # Thank you
    elif user_input in [
        "thanks",
        "thank you",
        "thanku"
    ]:
        return "You're welcome! 😊"

    # Time
    elif user_input == "time":
        return f"The current time is {get_time()}."

    # Help
    elif user_input == "help":
        show_help()
        return None

    # Clear screen
    elif user_input == "clear":
        clear_screen()
        show_banner()
        return None

    # Exit
    elif user_input in [
        "bye",
        "goodbye",
        "exit",
        "quit"
    ]:
        return "Goodbye! 👋 Have a great day."

    # Unknown input
    else:
        return (
            "I'm still learning. 🤔 "
            "Try 'help' to see what I understand."
        )


# -------------------- Main Chatbot --------------------

def chatbot():

    clear_screen()
    show_banner()

    conversation_history = []

    while True:

        user_input = input("\nYou: ").strip().lower()

        if not user_input:
            print("HorizonBot: Please type something.")
            continue

        response = get_response(user_input)

        if response:
            print(f"HorizonBot [{get_time()}]: {response}")

            conversation_history.append(
                {
                    "user": user_input,
                    "bot": response
                }
            )

        if user_input in ["bye", "goodbye", "exit", "quit"]:
            break

    print("\n" + "=" * 65)
    print("              CHAT SESSION ENDED")
    print(f"          Messages exchanged: {len(conversation_history)}")
    print("=" * 65)


# -------------------- Program Start --------------------

if __name__ == "__main__":
    chatbot()