import streamlit as st
import pickle

fileName = "XGBModel.sav"

loadedModel = pickle.load(open(fileName, 'rb'))

predictions = loadedModel.predict([1,1,180000.0,1,1])

st.write(predictions)



# Use the terminal to 
'''
import streamlit as st
 
st.title('My First Streamlit App')

user_input = st.text_input("Enter some text:")

# Slider input
number = st.slider("Pick a number:", 0, 100, 50)

# Checkbox input
agree = st.checkbox("I agree")

# Display results based on inputs
st.write("You entered:", user_input)
st.write("You selected number:", number)

if agree:
    st.write("Thank you for agreeing!")
else:
    st.write("You didn't agree.")

# Simple button
if st.button("Click me"):
    st.write("Button clicked!")

# Selectbox input
option = st.selectbox(
    "Choose an option:",
    ["Option 1", "Option 2", "Option 3"]
)
st.write("You selected:", option)

# Multi-select input
options = st.multiselect(
    "Choose multiple options:",
    ["Option A", "Option B", "Option C", "Option D"]
)
st.write("You selected:", options)
'''










