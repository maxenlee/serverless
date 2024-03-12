import os

def get_last_4_digits_of_env_var(event, context):
    # Fetch the value of the environment variable
    env_var_value = os.environ["PICKLEJAR_ACCESS"]

    # Extract the last 4 digits
    last_4_digits = env_var_value[-4:]

    # # Check if the last 4 characters are digits, to ensure the operation's correctness
    # if last_4_digits.isdigit():
    #     result = f"The last 4 digits of TARGET_ENV_VAR are: {last_4_digits}"
    # else:
    #     result = "The TARGET_ENV_VAR does not have 4 digits at its end."

    result = f"The last 4 digits of TARGET_ENV_VAR are: {last_4_digits}"
    return {
        "statusCode": 200,
        "body": result
    }

if __name__ == "__main__":
    # Create dummy event and context
    event = {}  # You can simulate event data here if needed
    context = None  # Context is often not used when running locally

    # Call the function
    result = get_last_4_digits_of_env_var(event, context)
    print(result)
