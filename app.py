from flask import Flask, render_template, request


import os
import google.generativeai as genai

API_KEY = "APIKEYHERE"
# Configure your API key
# It's recommended to set it as an environment variable (e.g., GOOGLE_API_KEY)
# You can also pass it directly, but for security, environment variables are better.
try:
    genai.configure(api_key=API_KEY)
except KeyError:
    print("Please set the GOOGLE_API_KEY environment variable.")
    exit()


app = Flask(__name__)

@app.route('/')
def index_page():
      return render_template("index.html")

def get_ai_response(user_inp):
     model = genai.GenerativeModel('gemini-1.5-flash') 
     prompt = user_inp
     response = model.generate_content(prompt)
     return response


@app.route('/process_form', methods=['POST'])
def process_form():
        user_query = request.form.get('user_input')
        print(user_query)

        ai_response = get_ai_response(user_query)
        print('---------------')
        print(ai_response.text)
        print('---------------')
        return render_template("index.html", output_here=ai_response.text)

if __name__ == '__main__':
    app.run(debug=True)