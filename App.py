import os
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key in your environment variable (OPENAI_API_KEY)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the user's input as a prompt
        prompt = request.form.get("prompt")
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=500,
                n=1,
                stop=None,
                temperature=0.7
            )
            generated_resume = response.choices[0].text.strip()
        except Exception as e:
            generated_resume = f"Error generating resume: {e}"
        
        return render_template("result.html", resume=generated_resume, prompt=prompt)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
