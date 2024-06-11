# ap-cs-principle-finalproject-year-
# Number-Guessing Game

This project is a simple number-guessing game implemented using Flask. Users can guess a single secret number or try to guess a number from a list of secret numbers.

## Features

- Guess a single secret number.
- Guess a number from a list of secret numbers.
- Reset the secret number.
- Informative feedback on guesses (too low, too high, correct).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/number-guessing-game.git
    cd number-guessing-game
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install Flask
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://localhost:2417`.

## Routes

- `/` : Displays a welcome message.
- `/reset` : Generates a new secret number.
- `/guess` : Handles guessing the single secret number. Supports both GET and POST requests.
- `/secret_numbers` : Handles guessing from a list of secret numbers. Supports both GET and POST requests.

## Code Explanation

- **Global Variables**:
  - `secret_number`: A single secret number to guess.
  - `secret_numbers`: A list of 10 secret numbers.

- **Functions**:
  - `guess_number_list(guess: int, secret_numbers: list[int]) -> str`: Checks if the guessed number is in the list of secret numbers.
  - `create_secret_numbers()`: Generates a new list of 10 random secret numbers.

- **Routes**:
  - `/`: Displays a welcome message.
  - `/reset`: Generates a new secret number.
  - `/guess`: Handles the guessing game for a single secret number.
  - `/secret_numbers`: Handles the guessing game for a list of secret numbers.

## Templates

- `guess.html`: A simple HTML form to input guesses and display feedback.

## Testing

The code has been thoroughly tested for:
- Correct initialization of the secret number and list of secret numbers.
- Proper handling of guesses, with informative feedback.
- Robustness against invalid inputs and edge cases.

## License

This project is licensed under the MIT License.
