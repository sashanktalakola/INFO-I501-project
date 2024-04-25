import streamlit as st
from utils import get_article_data
from entity import TopicClassification


st.set_page_config(layout="wide")


st.title("Articles Topic Classification")

with st.expander(label="**Manual Text Input**", expanded=False):
    with st.form(key="topic-classification-manual", clear_on_submit=False):

        topic_classification_object = TopicClassification()
        input_data = st.text_area(label="Input Article Data", height=350)
        topic_classification_object.classification_data = input_data

        submit = st.form_submit_button(label="Predict")

        if submit:
            if (input_data is not None) and (input_data != ""):

                with st.spinner('Application Generating Response ...'):
                    try:
                        response = topic_classification_object.get_response(topic_classification_object.classification_data)
                        st.success(f"Application Output - {response}")
                    except ConnectionError:
                        st.error("Please check your network conenction")
                    except:
                        st.write("Please re-check the entered input data")
            else:
                st.warning("Passed empty value for input! Please enter some information")
            response = None
            input_data = None
            topic_classification_object = None

with st.expander(label="**URL Input**", expanded=False):
    with st.form(key="topic-classification-url", clear_on_submit=False):
        input_url = st.text_input(label="Input Article URL")

        if input_url != "":
            with st.spinner('Obtaining Article Data'):
                page_data = get_article_data(input_url.strip())

                st.write("**Parsed Page Content**")
                page_data
        submit = st.form_submit_button(label="Predict")

        if submit:

            topic_classification_object = TopicClassification()
            topic_classification_object.classification_data = page_data

            with st.spinner('Application Generating Response ...'):
                try:
                    response = topic_classification_object.get_response(topic_classification_object.classification_data)
                    st.success(f"Application Output - {response}")
                except ConnectionError:
                    st.error("Please check your network conenction")
                except:
                    st.warning("Please re-check the entered input data")

st.write("GitHub Repo - https://github.com/sashanktalakola/INFO-I501-project/")
st.write("")
st.write("")
st.write("")
st.write("Note:")
st.markdown("* The **Manual Text Input** option is for entering the data of the article manually. In the text area provided you can enter the article data and upon entring the data, click **Predict** to perform classification on the data provided")
st.markdown("* In the **URL Input** option, you can enter a url for a website, and upon succesfully retreiving the contents of the page it will be displayed on the web interface and simulaneously the topic of the data will be classified. Please note, the parsing is based of `p` tags of the webpage, as they are often associated with content of the article and information in the rest of the tags will be not considered for prediction. When an invalid webpage is given as input the model returns `-1` indicating parsing the webpage, as warning will also be displayed.")
st.markdown("* Please note, the LLM API is based of an free service hence the number of requests it limited. And repeated requests can cause to slow down, and in certain cases the API does not send any response.")