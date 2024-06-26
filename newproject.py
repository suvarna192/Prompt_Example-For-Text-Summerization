import gradio as gr
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import json

# Initialize the ChatGroq model
model = ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="mixtral-8x7b-32768"
)

# Define the system and human prompt
system = "You are a helpful assistant."
human = """
This is a conversation between a customer and an agent for the KYC process. Extract the following information from the conversation and provide it in valid JSON format: customer Full Name, Location, last 4 digit of mobile number, Occupation, Income, Mother Name, Date of birth.
Conversation: {text}
Details to include: customer Full Name, Location, last 4 digit of mobile number, Occupation, Income, Mother Name, Date of birth.
Answer:
"""

# Create the ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

# Define the function to process the text
def extract_info(text):
    # Combine the prompt and the model
    chain = prompt | model
    # Invoke the model with the given text
    response = chain.invoke({"text": text})
    # Extract the content from the response
    response_text = response.content.strip()  # Strip any extra whitespace
    # Find the start and end of the JSON object
    start_idx = response_text.find('{')
    end_idx = response_text.rfind('}') + 1
    # Extract the JSON object
    response_json_str = response_text[start_idx:end_idx]
    # Parse the response into JSON
    response_json = json.loads(response_json_str)
    # Re-format the response into a prettified JSON string
    return json.dumps(response_json, indent=4)

# Create the Gradio interface
demo = gr.Interface(
    fn=extract_info,
    inputs="text",
    outputs="json",
    title="KYC Information Extractor",
    description="Enter a conversation text to extract KYC information in JSON format."
)

# Launch the Gradio interface
if __name__ == "__main__":
    demo.launch()
