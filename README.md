# INFO-I501-project

## Overview
This project aimed to develop a web application capable of automatically classifying articles into relevant topics using natural language processing (NLP) techniques. Through the integration of advanced machine learning algorithms, the application analyzes the content of each article and assigns it to one or multiple predefined categories. The primary outcome of our project is an efficient and accurate tool for organizing and categorizing large volumes of articles, enhancing content discoverability and facilitating targeted content delivery. Stakeholders such as content publishers, researchers, and online platforms can benefit from this tool by streamlining content management, improving searchability, and enhancing user engagement.

Stakeholders, including content publishers, researchers, and online platforms, would find our tool immensely useful for several reasons - **Efficient Content Organization** and **Targeted Content Delivery**

## Data Description
* **title** [*string*]: The title of the article.
* **text** [*string*]: The text content of the article.
* **url** [*string*]: The URL associated to the article.
* **authors** [*list of string*]: The article authors.
* **timestamp** [*string*]: The publication datetime of the article.
* **tags** [*list of string*]: List of tags associated to the article.

#### Data Cleaning
* The original dataset contains `192368` article, from these `5000` articles have been selected.
* Columns `title`, `url`, `authors` and `timestamp` have been removed as they provide no significant information while predicting the Topic of the Article.
* The `text` column required text cleaning for removing urls, non-ascii characters.
  * URLs have been removed using regular expressions, where the text that starts with `https://` or `http://` have been removed.
  * Non-ascii charcaters are removed using comparision with the `ascii_letters` and `digits` from the `string` package.
  * Further, the article text contained `\n\n` to seperate paragraphs instead, it has been replaced with `\n`. This ensures that the page structure is still maintained while reducing the number of tokens that LLM need to process.

## Algorithm Description
This project utilizes the `streamlit` framework from front-end and back-end purposes. Topic Classification is done using an API to LlaMa2 LLM using the `replicate` API service. Upon the user request, an API call is made by the streamlit application to the `replicate` servers, which returns the LlaMa API output. Ultimately, the response that has been received undergoes processing to be shown on the web interface. In case of error has occured the the web interface displays an error warning.

## Tools Used
Programming Language - `python`
Front-end and back-end - `streamlit`
Data Processing - `pandas`
Application Testing - `unittest`
URL Parsing - `requests` and `BeautifulSoup`
Application Hosting - `Docker` and `Google Cloud Run`

## Ethical Concerns
Automated content classification using natural language processing (NLP) techniques can introduce several ethical and societal implications that need to be carefully addressed. Few of the concerns would be -
* **Bias in Classification** - NLP models trained on biased datasets may perpetuate existing biases in content classification, leading to unfair or discriminatory outcomes. This can be mitigated by ensuring there is **diversity in training data to minimize bias** and regularly auditing and updating the model to identify and mitigate bias.
* **Privacy Concerns** - Analyzing the content of articles may raise privacy concerns if sensitive or personally identifiable information is processed without consent. Mitigation strategies could include implementing robust **data anonymization techniques** to protect user privacy and Obtaining **explicit consent from users** before processing their data.
* **Unintended Consequences** - Automated content classification may have unintended consequences, such as amplifying misinformation or suppressing certain viewpoints. This can be mitigated by implementing human oversight to review and validate classification results, developing robust mechanisms to detect and address misinformation or biased content