def extract_substring(input_string, delimiter, num_delimiters):
    # Split the input string by the specified delimiter
    parts = input_string.split(delimiter)
    
    # Join the required number of parts back together with the delimiter
    result = delimiter.join(parts[:num_delimiters])
    
    return result

# Examples
input_string1 = "module1/Group1/build"
input_string2 = "module1/Group1/tests/test1_42"

# Extract substrings
output1 = extract_substring(input_string1, "/", 2)
output2 = extract_substring(input_string2, "/", 2)

print(output1)  # Output: module1/Group1
print(output2)  # Output: module1/Group1
