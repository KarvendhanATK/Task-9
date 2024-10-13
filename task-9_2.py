#Task-9.2
#Write a Python code using Lambda function to check every element of a List is an Integer or String?

data = [1, 'hello', 10, 'world', 25, 'i am using', 50, 'python']

# Use lambda 
result = list(map(lambda x: (x, 'Integer') if isinstance(x, int) else (x, 'String' if isinstance(x, str) else 'Other'), data))

# Print result
for item in result:
    print(item)
