import streamlit as st
import pickle

pickle_in = open("D:\\temp\\My_Work\\knn.pkl","rb")
knn = pickle.load(pickle_in)

def predict(experience,testScore,interviewScore):
    result = knn.predict([[experience,testScore,interviewScore]])
    return result

def main():
    st.title("Salary Prediction")
    name = st.text_input("Enter name","")
    experience = st.number_input("Enter experience in Years")
    testScore = st.slider("Select Test Score", 0, 10)
    intervieScore = st.text_input("Enter Number of Interviews","")

    if(st.button('Predict')):
        name1 = name.title()
        result = predict(int(experience),int(testScore),int(intervieScore))
        st.success("Hello {} your salary could be {} approx".format(name1,result[0][0]))

if __name__=='__main__':
    main()