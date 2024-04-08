import streamlit as st
from utils import get_prompt, get_response

st.set_page_config(layout="wide")


st.title("Articles Topic Classification")

with st.form(key="topic-classification", clear_on_submit=False):
    input_data = st.text_area(label="Input Article Data", height=350)
    submit = st.form_submit_button(label="Predict")

    if submit:
        if (input_data is not None) and (input_data != ""):

            input_data = input_data.strip()

            prompt = get_prompt(input_data)
            response = get_response(prompt)
            st.success(f"Application Output - {response}")
        else:
            st.warning("Passed empty value for input! Please enter some information")
        response = None
        input_data = None

with st.expander(label="**Issues**"):
    st.markdown('''
    - Further, due to the LLM API token limit, the application can only handle a limited number of tokens, to handle the issue in the future, the provided data is split among multiple chucks which will be streamed to the API, and prediction can be made of the result from each chunk.
    - In certain cases the the output from the LLM API is being unpredictable from scraping the class name from the output response, i.e, the response also contains information about why the API classified the input data as a particular class. To overcome this error we could use regualr expression on limited tokens output, then we could find the possible classes if they were part of the output. Or they output from the model can be passes to another API to just predict the classes from the output. The formed approach would result in a complex solution for multi-class classification, while the later suits for the multi-class classification and single-class classfication.
    ''')


with st.expander(label="**Next Steps**"):
    st.markdown('''
    - Currently the application only makes prediction on the classes - ["Data Science", "Cryptocurrency", "Bitcoin", "Poetry", "Life"]. This will be expanded to the entire set of classes.
    - The input text area currently only accepts text from the article, this will be further updated to handle either a URL to the article or the text from the article. User will have an option to chose the type of input being provided.
    - The application currently only supports single-class classification, this will be further expanded to multi-class classification.
    - The application currently uses open-source LLM, Llama 2, in the future user will have the option to choose their classification algorithm of their choice, or a prediction based of all set of algorithms.
    ''')