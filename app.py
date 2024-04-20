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
                    st.write("Please re-check the entered input data")

st.write("GitHub Repo - https://github.com/sashanktalakola/INFO-I501-project/")