from flask import Flask, request
from random import choice

app = Flask(__name__)
#compliments = ['coolio', 'smashing', 'neato', 'fantabulous']

#@app.route('/compliment')
#def get_compliment():
    #"""Give the user a compliment"""
    #name = request.args.get('name')
    #compliment = choice(compliments)
    #return f'Hello there, {name}! You are so {compliment}!'

horoscopes = [
'You will have a restful night', 'The sky will fall tommorrow'
'Someone mysterious will greet you', 'A red car will honk at you']

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return """
    <form action='/horoscope'>
        <p>
            What is your name?
            <input type="text" name="name"></input>
        </p>
        <p>
            <input type+"checkbox" name="show_horoscopes"/>
            Show Horoscopes
        <p>
            How many Horoscopes?
            <select name="num_horoscopes">
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
            </select>
        </p>
            <input type="submit">
    </form>
    """

@app.route('/horoscope')
def get_horoscope():
    """Give the user a horoscope"""
    name = request.args.get('name')
    num_horocopes = int(request.args.get('num_horoscopes'))
    show_horoscopes = request.args.get('show_horoscopes')
    nice_things = ', '.join(sample(horoscopes, num_horoscopes))

    if show_horoscopes:
        return f'Here is your horoscope, {name}! {show_horoscope}!'
    else:
        return f'Hello there, {name}! Have a nice day!'

if __name__ == "__main__":
   app.run(debug=True)
