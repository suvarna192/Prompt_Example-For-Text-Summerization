from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# Initialize the ChatGroq model
chat = ChatGroq(temperature=0, groq_api_key="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", model_name="mixtral-8x7b-32768")

# Define the system and human prompt
system = "You are a helpful assistant."
human = """
This is a conversation between a customer and an agent for the KYC process. Extract the following information from the conversation and provide it in valid JSON format: customer Full Name, Location,last 4 digit of mobile number, Occupation, Income, Mother Name, Date of birth.
Conversation: {text}
Details to include: customer Full Name, Location, last 4 digit of mobile number,Occupation, Income, Mother Name, Date of birth.
Answer:
"""


# Create the ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

# Define the text to be analyzed
text="What is your date of birth? 12th July 1995 .What is your last 4 digit of mobile number? 9876..What is your annual income? 18 lakh..What is your name? Rahul Vishwas Patil.What is your occupation? Teacher.What is your location? Mumbai."
 # Combine the prompt and the model
chain = prompt | chat

# Invoke the model with the given text
response = chain.invoke({"text": text})

# Display the response
print(response)

