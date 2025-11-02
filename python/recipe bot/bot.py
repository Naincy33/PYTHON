import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load your OpenAI API key from an environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_recipe(ingredients, dietary_preference="None"):
    """Generate a recipe using OpenAI's GPT model."""
    prompt = f"""
    You are a helpful AI chef. Suggest a recipe based on these ingredients: {', '.join(ingredients)}.
    Dietary Preference: {dietary_preference}.
    Include step-by-step instructions and estimated cooking time.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a chef assistant."},
                  {"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"].strip()

@app.route("/recipe", methods=["POST"])
def recipe_chatbot():
    data = request.json
    ingredients = data.get("ingredients", [])
    dietary_preference = data.get("dietary_preference", "None")
    
    if not ingredients:
        return jsonify({"error": "Please provide at least one ingredient."}), 400
    
    recipe = generate_recipe(ingredients, dietary_preference)
    return jsonify({"recipe": recipe})

if __name__ == "__main__":
    app.run(debug=True)