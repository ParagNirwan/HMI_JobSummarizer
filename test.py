# Open the file
with open('./Assets/dummy.txt', 'r') as f:
    # Read the contents of the file
    contents = f.read()

    # Split the contents into lines
    lines = contents.splitlines()

    # Initialize an empty list to store the dictionaries
    data = []

    # Loop through each line and split it into key-value pairs
    for line in lines:
        if(line != ""):
            parts = line.split(':')
            key = parts[0]
            values = ''
            if(len(parts)>1):
                values = parts[1]
                # values = [v.strip() for v in values]

        # Create a new dictionary and add the key-value pairs
        d = {}
        d['key'] = key
        d['values'] = values

        # Append the new dictionary to the list
        data.append(d)

# Print the resulting data
print(data)