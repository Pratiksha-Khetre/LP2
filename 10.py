# AI Customer Support Chatbot

def chatbot():

    print("===================================")
    print("     WELCOME TO AI CHATBOT")
    print("===================================")

    name = input("Enter your name: ")

    print(f"\nHello {name}! How can I help you?")
    print("Type 'exit' to end the chat.\n")

    while True:

        user = input("You: ").lower()

        # Exit
        if user == "exit":
            print(f"Bot: Thank you {name}! Visit again.")
            break

        # Greeting
        elif "hello" in user or "hi" in user:
            print(f"Bot: Hello {name}! How are you today?")

        # Order Query
        elif "order" in user:
            print("Bot: Your order has been successfully placed.")

        # Payment Query
        elif "payment" in user:
            print("Bot: Please check your payment details and try again.")

        # Refund Query
        elif "refund" in user:
            print("Bot: Refund will be processed within 5 working days.")

        # Delivery Query
        elif "delivery" in user:
            print("Bot: Delivery usually takes 3 to 7 days.")

        # Help
        elif "help" in user:
            print("\nBot: I can help you with:")
            print("1. Order Status")
            print("2. Payment Issues")
            print("3. Refund")
            print("4. Delivery Information\n")

        # Thank You
        elif "thank" in user:
            print("Bot: You're welcome!")

        # Default Response
        else:
            print("Bot: Sorry! I did not understand your query.")


# Function Call
chatbot()