from flask import Flask, request
import random

app = Flask(__name__)
number_to_guess = random.randint(1, 10)
guess_count = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    global guess_count
    message = ''
    wrong_guess = False
    success = False
    invalid_input = False
    
    if request.method == 'POST':
        user_input = request.form['guess']
        if not user_input.isdigit():
            invalid_input = True
            message = 'Invalid input! Please enter a valid number!'
            wrong_guess = True
        else:
            user_guess = int(user_input)
            if 1 <= user_guess <= 10:
                guess_count += 1
                if user_guess == number_to_guess:
                    message = 'Congratulations! You guessed the right number!'
                    success = True
                elif guess_count < 3:
                    if user_guess < number_to_guess:
                        message = 'Too low! Try again!'
                    else:
                        message = 'Too high! Try again!'
                    wrong_guess = True
                else:
                    message = 'Sorry, you have reached the maximum number of attempts! The number was ' + str(number_to_guess)
            else:
                message = 'Please enter a number between 1 and 10!'
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
        .confetti {
            position: fixed;
            width: 10px;
            height: 10px;
            border-radius: 50%;
        }
        <!-- Other styles here... -->
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
         <form action="/restart" method="POST">
        <button type="submit" class="btn btn-warning mt-3">Restart</button>
    </form>
        ''' + (f'<p class="mt-3 { "success" if success else "danger" }">{ message }</p>' if message else '') + '''
    </div>
    <script>
        const invalidInput = ''' + str(invalid_input).lower() + ''';
        if (invalidInput) {
            document.body.style.backgroundColor = '#ff0000'; // Change background to red
        }
        const success = ''' + str(success).lower() + ''';
        if (success) {
            // Create confetti elements
            for (let i = 0; i < 100; i++) {
                const confetti = document.createElement('div');
                confetti.className = 'confetti';
                confetti.style.top = Math.random() * 100 + 'vh';
                confetti.style.left = Math.random() * 100 + 'vw';
                confetti.style.backgroundColor = '#' + Math.floor(Math.random()*16777215).toString(16);
                confetti.style.transform = 'rotate(' + Math.random() * 360 + 'deg)';
                document.body.appendChild(confetti);
            }
            // Animate confetti falling
            const allConfetti = document.querySelectorAll('.confetti');
            allConfetti.forEach((el) => {
                el.style.transition = 'all 2s linear';
                el.style.top = (Math.random() * 100 + 100) + 'vh';
                el.style.opacity = 0;
            });
            // Remove confetti after animation ends
            setTimeout(() => {
                allConfetti.forEach((el) => el.remove());
            }, 2000);
        }
    </script>
    '''
@app.route('/restart', methods=['POST'])
def restart():
    global number_to_guess
    global guess_count
    number_to_guess = random.randint(1, 10)
    guess_count = 0
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
