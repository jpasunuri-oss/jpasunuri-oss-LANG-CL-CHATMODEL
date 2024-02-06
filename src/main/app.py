from src.main.lab import send_single_human_message, send_human_message_prompt_template, \
    send_multi_message_prompt_template, send_prompt_with_chat_memory


# ------------------------------------------------------------------------------
# Starter Code - TOUCH AT YOUR OWN RISK!
# ------------------------------------------------------------------------------

"""
This file will contain an interactive way to test your LLM's responses you've created in the lab.py file. It will take 
in user input from the console and send it to the LLM, printing the response to the console. You may modify this file,
as it will not affect the test results. Strictly used for manual testing of your code.
"""

def user_input():
    user_input_style = input("Style: ")
    user_input_message = input("Message: ")

    return [user_input_style, user_input_message]


def main():
    style, message = user_input()
    print("Choose a method to test:")
    print("1. send_single_human_message")
    print("2. send_human_message_prompt_template")
    print("3. send_multi_message_prompt_template")
    print("4. send_prompt_with_chat_memory")
    choice = int(input("Enter your choice (1-4): "))
    result = switch_method(choice, style, message)
    print(result)


def switch_method(choice, style, message):
    if choice == 1:
        return send_single_human_message(message)
    elif choice == 2:
        return send_human_message_prompt_template(style, message)
    elif choice == 3:
        return send_multi_message_prompt_template(style, message)
    elif choice == 4:
        return send_prompt_with_chat_memory(style, message)
    else:
        return "Invalid choice"


if __name__ == "__main__":
    main()
