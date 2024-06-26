import os
from typing import List

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder

llm = HuggingFaceEndpoint(
    endpoint_url=os.environ['LLM_ENDPOINT'],
     huggingfacehub_api_token = os.environ['HF_TOKEN'],
    task="text2text-generation",
    model_kwargs={
        "max_new_tokens": 200
    }
)

chat_model = ChatHuggingFace(llm=llm)
# ------------------------------------------------------------------------------
# TODO Functions - Implement the logic as per instructions
# ------------------------------------------------------------------------------


def send_single_human_message(message) -> BaseMessage:
    f"""
    TODO: Implement this method to use the ChatHuggingFace object(chat_model)  to invoke with a List containing a single HumanMessage.

    :param:
    message: Takes in user input about what they want to ask the LLM.

    :returns:
    AIMessage object containing the LLM's response.

    Instructions:
    - Create a new HumanMessage object called 'human_message' with the message variable provided via the arguments to this function.
    - Pass a list as an argument with the human_message to ChatHuggingFace object's invoke() method. I.e. chat_model.invoke([human_message])
    - Return the response from the invoke method.
    End TODO
    """
    # Write Code Below
    human_message = HumanMessage(content=message)
    
    # Replace with return statement
    return chat_model.invoke([human_message])


def send_human_message_prompt_template(message) -> BaseMessage:
    """
    TODO: Create a HumanPromptTemplate object from the prompt file, sending the HumanMesasge to the ChatHuggingFace object
            with the HumanPromptTemplate object's formatted messages.
    :param: 
    style: Takes in user input about what style they AI to respond in. (e.g. cheerful, formal, pirate, etc.)
    message: Takes in user input about what they want to ask the LLM.
    
    :returns: 
    AIMessage object containing the LLM's response.
    
    Instructions:
    - Create a new HumanMessagePromptTemplate object and use the from_template method with the message variable passed
        as an argument.
    - Use the new HumanMessagePromptTemplate object's .format_messages() method to be passed as an argument through the invoke
        method of the chat_model..
    - Return the response from the chat_model.
    
    End TODO
    """
    # Write Code Below
    human_message_prompt = HumanMessagePromptTemplate.from_template(message)
    
    return chat_model.invoke(human_message_prompt.format_messages())


def send_multi_message_prompt_template(style, message) -> BaseMessage:
    # System message prompt template
    file = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../templates/system_prompt.txt')))
    prompt_file = file.read()
    file.close()

    """
    TODO: Create a PromptTemplate object using both a HumanMessagePromptTemplate and a SystemMessagePromptTemplate object 
            using the 'system_prompt.txt' from the templates directory.
    
    :param: 
    style: Takes in user input about what style they AI to respond in. (e.g. cheerful, formal, pirate, etc.)
    message: Takes in user input about what they want to ask the LLM.
    
    :returns: 
    AIMessage object containing the LLM's response.
    
    Instructions:
    - Create a new HumanMessagePromptTemplate object and use the from_template method with the message variable passed 
        as an argument.
    - Create a new SystemMessagePromptTemplate object and use the from_template method with the prompt_file variable passed 
        as an argument.
    - Create a new ChatPromptTemplate object using the from_messages with a List containing the SystemMessagePromptTemplate  
        and HumanMessagePromptTemplate objects. NOTE: HumanMessage must be last in the list.
    - Send the formatted messages from PromptTemplate object to the chat_model via the invoke method, including 
        the style=style and message=message. 
    - Return the response from the chat_model.
    
    End TODO
    """
    # Write Code Below
    human_message_prompt = HumanMessagePromptTemplate.from_template(message)
    
    f = open("./templates/system_prompt.txt", "r")
    system_prompt = f.read()
    f.close()
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_prompt)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    # Replace with return statement
    return chat_model.invoke(chat_prompt.format_messages(message=message, style=style))


def send_prompt_with_chat_memory(style, message) -> List[BaseMessage]:
    system_ai_template = f"An AI that is here to help any human to answer any questions. Talks in a {style} tone."
    message2 = "What can birds do?"
    message3 = "How many messages have we exchanged? About what?"

    """
    TODO: The send_prompt_with_chat_memory function is designed to facilitate a conversation with the Language 
    Learning Model (LLM). Using the ChatHuggingFace object and a ChatPromptTemplate object, which includes a 
    SystemMessagePromptTemplate, a MessagesPlaceholder for history, and a HumanMessagePromptTemplate. The function 
    also initializes a ConversationBufferMemory object to store the conversation history. It then creates a 
    ConversationChain object and sends messages through the run method. Finally, it returns the conversation 
    history.

    :param: 
    style: Takes in user input about what style they AI to respond in. (e.g. cheerful, formal, pirate, etc.)
        message: Takes in user input about what they want to ask the LLM.

    :returns: 
    AIMessage object containing the LLM's response.

    Instructions:
        - Create a new ConversationBufferMemory object.
        - Create a new ConversationChain object with the ChatHuggingFace object(chat_model) for the 'llm' value and
            the ConversationBufferMemory object for the 'memory' value in the chain.
        - Using the ConversationChain object, send each message through the predict method 3x. I.e chain.predict(input=message) Inputting each message object:
            message, message2 and message3.
        - By using ConversationBufferMemory object's buffer_as_messages variable you can return a list of all messages 
            that transpired within the conversation.

    End TODO
    """
    # Write Code Below
    system_prompt = SystemMessagePromptTemplate.from_template(system_ai_template)
    chat_prompt = ChatPromptTemplate.from_messages(
                    [
                        system_prompt, 
                        MessagesPlaceholder(variable_name="chat_history"),
                        HumanMessagePromptTemplate.from_template("{input}")
                    ])

    conversation_buf = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    conversation_chain = ConversationChain(prompt=chat_prompt, llm=chat_model, memory=conversation_buf)

    conversation_chain.predict(input=message)
    conversation_chain.predict(input=message2)
    conversation_chain.predict(input=message3)


    # Replace with return statement
    return conversation_buf.buffer_as_messages
