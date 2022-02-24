from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9!</h1>"\
            "<img src= 'https://media.giphy.com/media/l378khQxt68syiWJy/giphy-downsized-large.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1> Your guess is too high! Try again!</h1>"\
               "<img src='https://media.giphy.com/media/d8EN0mls2eoAFLRiX8/giphy.gif'/>"

    elif guess < random_number:
        return "<h1>Your guess is too low! Try again!</h1>"\
               "<img src='https://media.giphy.com/media/Nieh7wqfcXSvu/giphy.gif'/>"

    else:
        return "<h1>Yay! Your guess was correct!</h1>"\
               "<img src='https://media.giphy.com/media/AhgQdQqF0nwPiZkGPc/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
