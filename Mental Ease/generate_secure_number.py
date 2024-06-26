# Import the secrets module
import secrets

# Define a function to generate a secure 12-digit decimal number
def generate_secure_number():
  # Generate a random 12-digit hexadecimal number using secrets.token_hex
  n = secrets.token_hex(6) # 6 bytes = 12 hex digits
  # Convert it to a decimal number using int with base 16
  n = int(n, 16)
  # Return the number as a string
  return str(n)

# Call the function and print the result
print(generate_secure_number())
