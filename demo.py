# load the large language model file
from llama_cpp import Llama
LLM = Llama(model_path="./llama-2-7b-chat.ggmlv3.q8_0.bin", verbose=True, n_ctx=4096)
print('model loaded')
# create a text prompt
text="I'm talking to Mr. Priyanka from Bajaj Housing Finance Company.  Mr. Ashutosh had asked for loan through our application.  I had called him regarding this.  You can search for properties to buy.  How many lakhs do you require?  You are talking to Latur from out of city.  Where do you want to buy the property?  How do you feel comfortable in Marathi?  It's okay.  If you have any 5 Lakhs requirement for construction,  where exactly is your plot?  Do you have land or property in the Gram Panchayat?  I don't have land.  I have agriculture property.  Okay.  But if you want to do construction,  you have land in the Gram Panchayat, right?  Okay.  Can you please tell me the PIN code  for construction of your area?  What do you all do? What is your job?  How much salary do you get?  Do you serve your teachers?  How much salary do you get?  You get 32,000  How much do you get?  Do you get 16,000?  It doesn't matter  Today I want to discuss with you about our rights, do you have 5 lakhs?  No problem, I have my income source with me.  Do you have a shop act license or an ITR?  Do you pay the ITR?  If you don't have an ITR, do you have a current account or income proof?  Do you have a shop act license?  It's okay. I will discuss it with Adhikara. If it's possible for me, I will call you back.  Thank you."

prompt = "This is a conversation between a customer and Bajaj Finance Company. Extract the following information from the conversation and provide it in valid JSON format: greeting (good morning, hello, hi, good evening, good afternoon), customer name, customer bank name (if mentioned), and home loan amount. \
          Conversation: {text} \
          Details to include: customer name, customer bank name, home loan amount. \
          Answer: "


        
# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])
