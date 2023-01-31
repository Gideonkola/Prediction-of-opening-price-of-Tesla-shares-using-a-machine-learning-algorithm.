import streamlit as st
import pickle

model = pickle.load(open('random_forest_model.pkl','rb'))

def main():
    st.title('Tesla Opening Price Prediction')

    #input variables 
    Year=st.text_input('Year')
    High=st.text_input('High')
    Low=st.text_input('Low')
    Close=st.text_input('Close')
    Adj_Close=st.text_input('Adj_Close')
    Volume=st.text_input('Volume')
    
    

    #prediction code
    if st.button('Predict'):
        makeprediction=model.predict([[Year, High, Low, Close, Adj_Close, Volume]])
        output=round(makeprediction[0],2) 
        st.success('You can sell your shares for {}'.format(output))  

if __name__=='__main__':
    main()
