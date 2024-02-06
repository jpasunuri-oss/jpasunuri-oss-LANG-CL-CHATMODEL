# Chat Model Lab
The [`lab.py`](src/main/lab.py) file is the centerpiece of the Chat Model Lab, where you will be implementing and interacting with chat_model 
classes provided by LangChain. The lab is designed to enhance your skills in handling prompt templates, managing chat 
history buffer memory, and utilizing conversation chains. It connects to an external ChatGPT for practical application of 
these concepts. The ultimate goal of the lab is to pass all test cases provided in [`src/test/test_lab.py`](./src/test/test_lab.py).

# Files to modify
The code you should modify, as well as the instructions for completing the lab, are in [`src/main/lab.py`](src/main/lab.py). Take notice of
the TODO comments in the file, this contains all instructions for the implementations required to complete the lab.

You may modify [`app.py`](src/main/app.py), which is provided for manual testing.

You should ***NOT*** modify [`src/test/test_lab.py`](src/test/test_lab.py). You must pass all test cases provided to pass the lab.

# LLM Connection Overview
This lab leverages an external connection to a hosted LLM. It is possible that it may become inaccessible due to an 
invalid API key or the service being unavailable. **PRIOR** to beginning the labs you should run the `test_llm_connection` 
test case in [`src/test/test_lab.py`](src/test/test_lab.py). The environment variables you should use for the connection should either be 
automatically configured for you upon opening the lab, or will be explicitly provided.