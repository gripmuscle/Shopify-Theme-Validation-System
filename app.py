import streamlit as st
import base64
import json
import random
import string
import time

# Function to generate a random string of a specified length
def generate_key(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to encode a string in base64
def encode_base64(s):
    return base64.b64encode(s.encode()).decode()

# Function to create a JSON data structure with valid keys
def generate_json_data(num_keys=10):
    data = {"validCodes": []}
    for _ in range(num_keys):
        key = generate_key()
        encoded_key = encode_base64(key)
        data["validCodes"].append(encoded_key)
    return data

# Streamlit UI
st.title('JSON Keys Generator')

# Sidebar for user input
st.sidebar.header('Settings')
num_keys = st.sidebar.slider('Number of Keys to Generate', min_value=1, max_value=100000, value=10000, step=1000)
key_length = st.sidebar.slider('Length of Each Key', min_value=8, max_value=64, value=16)
generate_button = st.sidebar.button('Generate Keys')

# Placeholder for displaying progress
progress_placeholder = st.empty()

if generate_button:
    with st.spinner('Generating keys...'):
        time.sleep(1)  # Simulate some processing time
        json_data = generate_json_data(num_keys)
        json_output = json.dumps(json_data, indent=4)
        
        # Update the progress placeholder
        progress_placeholder.empty()
        
        st.subheader('Generated JSON Data')
        
        # Textbox for displaying JSON data
        st.text_area('JSON Output', json_output, height=400)
        
        # Save to file
        json_file_name = f'generated_keys_{num_keys}.json'
        licenses_file_name = 'licenses.json'
        with open(json_file_name, 'w') as f:
            f.write(json_output)
        
        # Create a sample licenses.json file
        licenses_data = {"licenses": [{"id": i+1, "key": generate_key()} for i in range(num_keys)]}
        licenses_output = json.dumps(licenses_data, indent=4)
        with open(licenses_file_name, 'w') as f:
            f.write(licenses_output)
        
        st.success(f'JSON data has been saved to "{json_file_name}" and "{licenses_file_name}"')
        
        # Download options
        st.download_button(
            label='Download JSON file',
            data=json_output,
            file_name=json_file_name,
            mime='application/json'
        )
        
        st.download_button(
            label='Download licenses.json',
            data=licenses_output,
            file_name=licenses_file_name,
            mime='application/json'
        )

# Additional improvements and UI enhancements
st.sidebar.markdown("""
### Additional Features:
- **Generate Keys**: Specify the number of keys and their length.
- **Progress Indicator**: See a spinner while keys are being generated.
- **Download Options**: Download the generated JSON file and licenses file directly from the app.

If you encounter any issues or have suggestions, please let us know!
""")
