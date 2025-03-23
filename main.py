import google.generativeai as genai
from langchain_community.embeddings import OllamaEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = api_key)

#Loading the Model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Generate Responses

def generate_response(user_query):
    """
    Calls the Gemini API to generate a response based on user input.
    
    Parameters:
        user_query (str): The input query from the user.

    Returns:
        str: The AI-generated response.
    """
    try:
        response = model.generate_content(user_query)  # Send query to Gemini
        return response.text  # Extract and return text response
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Function for the Text Embeddings
def get_text_embeddings(text):
    """
    Converts text into an embedding vector using Ollama.

    Parameters:
        text (str): The input text.

    Returns:
        List[float]: The embedding vector.
    """
    embeddings = OllamaEmbeddings()
    return embeddings.embed_query(text)
