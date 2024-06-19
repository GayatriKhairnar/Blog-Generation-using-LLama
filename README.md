# Blog-Generation-using-LLama

This project utilizes the LLama 2 model from Hugging Face to generate blog posts based on user input. LLama 2 is a language model known for its capabilities in natural language generation tasks.

Usage
To use this application, follow these steps:

1. Setup

Ensure you have Python installed on your system.
- Install the necessary dependencies by running:
  pip install -r requirements.txt
- Run the app.py script using Streamlit:
  streamlit run app.py
- This will start a local server and open the application in your default web browser.

2. Generating Blogs

Once the application interface loads:
- Enter the topic for your blog in the "Enter the Blog Topic" text input.
- Specify the number of words you want the blog to be in the "No of Words" field.
- Choose the target audience for the blog from the dropdown list under "Writing the blog for".
- Click on the "Generate" button to initiate the blog generation process.
![image](https://github.com/GayatriKhairnar/Blog-Generation-using-LLama/assets/45005641/bc389591-34f1-47ce-8039-338a146a4c1e)


3. Output

- The generated blog post will be displayed below the input fields once the "Generate" button is clicked.

4. Components
- LLama 2 Model: The core of this project is the LLama 2 model from Hugging Face, which is used for generating text based on user prompts.
- Link for model : https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q2_K.bin
- Streamlit: The web application is built using Streamlit, which provides an intuitive and interactive interface for users to input parameters and view generated content.

5. Code Overview
The main functionality of the application is defined in app.py, which includes:

- Importing necessary libraries such as Streamlit and components from LangChain.
- Defining a function getLLamaresponse to interact with the LLama 2 model and generate blog content based on user inputs.
- Setting up the Streamlit interface with input fields for blog topic, word count, and audience selection.
- Displaying the generated blog post on the web interface upon user request.


