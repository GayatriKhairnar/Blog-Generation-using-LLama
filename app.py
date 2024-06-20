import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text,keywords,blog_style):

    ### LLama2 model
    llm=CTransformers(model="models\llama-2-7b-chat.ggmlv3.q2_K.bin",
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
        Generate technical project ideas for {blog_style} job profile for a topic {input_text} with using these {keywords}.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'keywords'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,keywords=keywords))
    print(response)
    return response






st.set_page_config(page_title="Generate Project Idea",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Project Idea 🤖")

input_text=st.text_input("Enter the Topic")


## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('Keywords')
with col2:
    blog_style=st.selectbox('Generating project idea for',
                            ('Researchers','Data Scientist','Software Developer','Common People'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))
