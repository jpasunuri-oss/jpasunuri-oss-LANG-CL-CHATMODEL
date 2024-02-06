import unittest
from typing import List
from langchain_core.messages import AIMessage, BaseMessage
from langchain_core.outputs import LLMResult

from src.main.lab import send_single_human_message, send_human_message_prompt_template, send_multi_message_prompt_template, \
    send_prompt_with_chat_memory
from src.utilities.llm_testing_util import llm_connection_check, llm_wakeup


class TestLLMResponses(unittest.TestCase):
    """
        This function is a sanity check for the Language Learning Model (LLM) connection.
        It attempts to generate a response from the LLM. If a 'Bad Gateway' error is encountered,
        it initiates the LLM wake-up process. This function is critical for ensuring the LLM is
        operational before running tests and should not be modified without understanding the
        implications.
        Raises:
            Exception: If any error other than 'Bad Gateway' is encountered, it is raised to the caller.
        """

    def test_llm_sanity_check(self):
        try:
            response = llm_connection_check()
            self.assertIsInstance(response, LLMResult)
        except Exception as e:
            if 'Bad Gateway' in str(e):
                llm_wakeup()
                self.fail("LLM is not awake. Please try again in 3-5 minutes.")

    def test_send_single_human_message(self):
        response = send_single_human_message("Hello, how are you?")
        self.assertIsInstance(response, BaseMessage)

    def test_send_human_message_prompt_template(self):
        response = send_human_message_prompt_template("goofy", "Hello, how are you?")
        self.assertIsInstance(response, BaseMessage)

    def test_send_multi_message_prompt_template(self):
        response = send_multi_message_prompt_template("Monty Python", "What is the air speed velocity of a laden swallow?")
        self.assertIsInstance(response, AIMessage)

    def test_send_prompt_with_chat_memory(self):
        response = send_prompt_with_chat_memory("pirate", "How much wood could a woodchuck chuck if a woodchuck could chuck wood?")
        self.assertIsInstance(response, List)
        self.assertIn("woodchuck", response[1].content.lower())


if __name__ == '__main__':
    unittest.main()
