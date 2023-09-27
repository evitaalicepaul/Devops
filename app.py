from flask import Flask, request
import random

app = Flask(__name__)

# Generate a random number between 1 and 10
number_to_guess = random.randint(1, 10)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    wrong_guess = False
    if request.method == 'POST':
        user_guess = int(request.form['guess'])
        if user_guess == number_to_guess:
            message = 'Congratulations! You guessed the right number!'
        else:
            message = 'Sorry, try again!'
            wrong_guess = True
            
    return '''
    <!doctype html>
    <title>Guess the Number</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <style>
        body {
            background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
            height: 100vh;
            margin: 0;
            font-family: 'Arial', sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 15px 5px rgba(0, 0, 0, 0.1);
            ''' + ('animation: shake 0.5s;' if wrong_guess else '') + '''
        }
        @keyframes shake {
            0% { transform: translate(1px, 1px) rotate(0deg); }
            10% { transform: translate(-1px, -2px) rotate(-1deg); }
            20% { transform: translate(-3px, 0px) rotate(1deg); }
            30% { transform: translate(3px, 2px) rotate(0deg); }
            40% { transform: translate(1px, -1px) rotate(1deg); }
            50% { transform: translate(-1px, 2px) rotate(-1deg); }
            60% { transform: translate(-3px, 1px) rotate(0deg); }
            70% { transform: translate(3px, 1px) rotate(-1deg); }
            80% { transform: translate(-1px, -1px) rotate(1deg); }
            90% { transform: translate(1px, 2px) rotate(0deg); }
            100% { transform: translate(1px, -2px) rotate(-1deg); }
        }
        h2 {
            margin-bottom: 20px;
            font-size: 2em;
            font-weight: bold;
        }
        p {
            font-size: 1em;
        }
        .form-group {
            margin-bottom: 1em;
        }
        input[type="text"] {
            width: 50%; 
            margin: auto;
            display: block;
            font-size: 0.9em;
        }
        .success {
            color: #28a745;
        }
        .danger {
            color: #dc3545;
        }
        button {
            transition: all 0.3s;
            font-size: 1em;
        }
        button:hover {
            transform: scale(1.05);
        }
    </style>
    <div class="container">
        <h2>Guess the Number!</h2>
        <p>Guess a number between 1 and 10</p>
        <form method="POST" action="/">
            <div class="form-group">
                <input type="text" class="form-control" name="guess" placeholder="Enter your guess" required>
            </div>
            <button type="submit" class="btn btn-primary">Guess</button>
        </form>
        ''' + (f'<p class="mt-3 { "success" if message.startswith("Congratulations") else "danger" }">{ message }</p>' if message else '') + '''
    </div>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
