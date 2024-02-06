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
    print(style, message)

    print("#############################Submitting request to #####################################")
    print("#########################################################################################################")

    print(send_single_human_message(message))
    print("#########################################################################################################")
    print("#####################################Single human message completed.#####################################")
    print("#########################################################################################################")
    print()

    print(send_human_message_prompt_template(style, message))
    print("#########################################################################################################")
    print("#####################################Human message prompt template completed.############################")
    print("#########################################################################################################")
    print()

    print(send_multi_message_prompt_template(style, message))
    print("#########################################################################################################")
    print("#####################################Multi message prompt template completed.############################")
    print("#########################################################################################################")
    print()

    print(send_prompt_with_chat_memory(style, message))
    print("#########################################################################################################")
    print("#####################################Prompt with chat memory completed.###################################")
    print()

    print("#########################################################################################################")
    print("############################# END OF REQUEST #####################################")


if __name__ == "__main__":
    main()
