from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Function to generate response from the model
def generate_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt", max_length=1024, truncation=True)
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, temperature=0.7)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Main function to simulate conversation
def main():
    print("Bot: Hello! Welcome to our testing service.")

    while True:
        user_message = input("User: ")

        # Check if user's message contains a pricing inquiry
        if "pricing" in user_message.lower():
            bot_response = generate_response("Bot: Could you please share your name and email with us?")
            print(bot_response)
            
            user_info = input("User: ")
            
            # Check if user's message contains name and email
            if "@" in user_info:
                confirmation = generate_response("Bot: Thanks for sharing your information with us!")
                print(confirmation)
                break  # End conversation
            else:
                print("Bot: Sorry, I didn't catch that. Can you please provide your name and email?")
        else:
            # Default bot response for non-pricing inquiries
            bot_response = generate_response("Bot: Welcome! How can I assist you today?")
            print(bot_response)

# Start the conversation
if __name__ == "__main__":
    main()
