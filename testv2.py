def my_custom_function(x):
    return x * x

import joblib

# # Save the function to a file
# joblib.dump(my_custom_function, 'my_custom_function.joblib')


# Load the function
loaded_function = joblib.load('my_custom_function.joblib')

# Use the loaded function
result = loaded_function(5)  # Should return 25
print(result)
