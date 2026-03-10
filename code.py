import streamlit as st

st.title("LearnSphere")
st.subheader("Generative AI–Powered Machine Learning Learning System")

st.write("Learn machine learning concepts interactively.")

topic = st.selectbox(
    "Select Topic",
    ["Linear Regression", "Decision Tree", "Neural Network"]
)

style = st.radio(
    "Choose Learning Style",
    ["Explanation", "Code"]
)

if topic == "Linear Regression":

    if style == "Explanation":
        st.write("Linear Regression predicts continuous values using a best-fit line.")

    if style == "Code":
        st.code("""
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)
""")

elif topic == "Decision Tree":
    st.write("Decision Trees classify data using a tree-like structure.")

elif topic == "Neural Network":
    st.write("Neural Networks mimic the human brain using layers of neurons.")

st.success("LearnSphere is running successfully!")