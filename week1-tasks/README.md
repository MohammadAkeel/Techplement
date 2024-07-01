# Random Password Generator

Welcome to the Random Password Generator project! This program allows users to generate a random password based on specified criteria such as length, and the number of uppercase characters, lowercase characters, numbers, and special characters.

## Features

- Generates a random password of a specified length.
- Allows the user to specify the number of:
  - Uppercase characters
  - Lowercase characters
  - Numbers
  - Special characters
- Ensures the generated password meets the specified criteria without exceeding the total length.

Here's a brief overview of the code structure:

generate_password(length, sequence): Generates a random password segment of the given length from the provided sequence.
get_input(prompt): Prompts the user for input and validates it as a positive integer.
main(): Main function that handles the user inputs, validates them, and generates the final password.


