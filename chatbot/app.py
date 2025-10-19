from flask import Flask, render_template, request

app = Flask(__name__)

response = {
    "hi": "hello i am siranjeevi bot how can i help you",
    "how are you?": "I'm doing great, thanks for asking!",
    "bye": "Goodbye! Have a great day!"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    bot_response = ''
    
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        if user_input in response:
            bot_response = response[user_input]
        else:
            bot_response = "I can't understand that."

        if user_input.lower() == 'bye':
            bot_response = "Goodbye! Have a great day!"
    
    return render_template('chat.html', user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
