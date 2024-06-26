from llama_cpp import Llama
import gradio as gr
import json

# Load the Llama model
LLM = Llama(model_path="./llama-2-7b-chat.ggmlv3.q8_0.bin", verbose=True, n_ctx=4096)
print('Model loaded')

# Define the function to generate the response
def extract_info(conversation):
    prompt = f"This is a conversation between a customer and Agent for KYC Process. Extract the following information from the conversation and provide it in valid JSON format: customer Full Name, Location, Occupation, Income, Mother Name, Date of birth. \
    Conversation: {conversation} \
    Details to include: customer Full Name, Location, Occupation, Income, Mother Name, Date of birth. \
    Answer: "
    
    output = LLM(prompt)
    
    # Extract the JSON part of the response
    response_text = output["choices"][0]["text"]
    print(response_text)
    start_idx = response_text.find("{")
    end_idx = response_text.rfind("}") + 1
    json_output = response_text[start_idx:end_idx]
    response_json = json.loads(json_output)
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
