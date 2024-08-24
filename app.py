import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# funtion to get response from Llama 2 modelgit co
def getLLamaresponse(input_text, no_Jokes, audience):
    llm = CTransformers(model= "models/llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type = "llama",
                        config = {"max_new_tokens":256, 'temperature': 0.01}) 
    # in config we can also give top_k, top_p, repetition_penalty, batch_size etc link: https://github.com/marella/ctransformers#config
    template = """
                You are an AI that generates Jokes content based on the following inputs:
                
                Generate {no_Jokes} jokes based on the following input text: {input_text}. The jokes should be suitable for the target
                audience, which is {audience}, and should have a moderate tone. Additionally, include relevant images to enhance the content

                """
    prompt = PromptTemplate(input_variables=['audience', 'input_text', 'no_Jokes'], template=template)

    response = llm(prompt.format(audience=audience, input_text=input_text, no_Jokes=no_Jokes))
    # print(response)
    return response



st.set_page_config(page_title="Stress Buster 😊",
                    page_icon='',   
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Stress Buster 😊")

input_text=st.text_input("Enter the Topic you want to crack Jokes on")


col1,col2=st.columns([5,5])


with col1:
    no_Jokes=st.number_input('No of Jokes', min_value=1, step=1)
with col2:
    audience=st.selectbox(' Target Audience',
                            ('Researchers/scientists','children','Adult people'),index=0)

    
submit=st.button("Generate")

## Final response
if submit:
    if not input_text or not no_Jokes:
        st.error("Please provide both a topic and the number of jokes.")
    else:
        response = getLLamaresponse(input_text, no_Jokes, audience)
        st.write(response)


