import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import pickle

#----------------------LOAD MODEL--------------------
model = pickle.load(open('ExpressoChurn1.pkl', "rb"))

st.markdown("<h1 style = 'text-align: centre; color: #435334'>START UP PROJECT</h1> ", unsafe_allow_html = True)
st.markdown("<h3 style = ''text-align: centre; text-align: right; color: #FFC436'>Built By Hope In GoMyCode Sanaith Wizard</h3>", unsafe_allow_html= True)

st.image('pngwing.com (9).png', width=700)

st.markdown("<h1 style = 'top_margin: 0rem; text-align: centre; color: #FE7BE5'>PROJECT SUMMARY</h1>", unsafe_allow_html= True)

st.markdown("<p style = 'top_margin: 0rem; text-align: justify; color: #8CABFF'>The telecommunications industry is a vast sector that encompasses the transmission of data, voice, and video over long distances, using a variety of technologies. It plays a crucial role in connecting people, businesses, and devices worldwide. The telecommunications industry is vital in the modern world, facilitating global communication and driving technological advancements. It continues to adapt and evolve in response to changing consumer needs and emerging technologies</p>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html= True)

username = st.text_input('Enter your name')
if st.button('submit name'):
    st.success(f"Welcome {username}. Pls use according to usage guidelines")

data = pd.read_csv('sampled_data.csv')
st.write(data.sample(10))

st.sidebar.image('pngwing.com (10).png', caption= f'Welcome {username}')
input_type = st.sidebar.selectbox('Select Your Prefered Input Type', ['Slider Input', 'Number Input'])

['REGULARITY', 'DATA_VOLUME', 'FREQUENCE', 'FREQ_TOP_PACK', 'FREQUENCE_RECH', 'ON_NET', 'REVENUE']
if input_type == 'Slider Input':
    regularity = st.sidebar.slider('REGULARITY', data['REGULARITY'].min(), data['REGULARITY'].max())
    data_vol = st.sidebar.slider('DATA_VOLUME', data['DATA_VOLUME'].min(), data['DATA_VOLUME'].max())
    frequency = st.sidebar.slider('FREQUENCE', data['FREQUENCE'].min(), data['FREQUENCE'].max())
    freqTop = st.sidebar.slider('FREQ_TOP_PACK', data['FREQ_TOP_PACK'].min(), data['FREQ_TOP_PACK'].max())
    freqRech = st.sidebar.slider('FREQUENCE_RECH', data['FREQUENCE_RECH'].min(), data['FREQUENCE_RECH'].max())
    onNet = st.sidebar.slider('ON_NET', data['ON_NET'].min(), data['ON_NET'].max())
    revenue = st.sidebar.slider('REVENUE', data['REVENUE'].min(), data['REVENUE'].max())

else:
    regularity = st.sidebar.number_input('REGULARITY', data['REGULARITY'].min(), data['REGULARITY'].max())
    data_vol = st.sidebar.number_input('DATA_VOLUME', data['DATA_VOLUME'].min(), data['DATA_VOLUME'].max())
    frequency = st.sidebar.number_input('FREQUENCE', data['FREQUENCE'].min(), data['FREQUENCE'].max())
    freqTop = st.sidebar.number_input('FREQ_TOP_PACK', data['FREQ_TOP_PACK'].min(), data['FREQ_TOP_PACK'].max())
    freqRech = st.sidebar.number_input('FREQUENCE_RECH', data['FREQUENCE_RECH'].min(), data['FREQUENCE_RECH'].max())
    onNet = st.sidebar.number_input('ON_NET', data['ON_NET'].min(), data['ON_NET'].max())
    revenue = st.sidebar.number_input('REVENUE', data['REVENUE'].min(), data['REVENUE'].max())

    st.markdown("<br>", unsafe_allow_html= True)

    # Bring all the inputs into a dataframe
input_variable = pd.DataFrame([{'REGULARITY' : regularity, 'DATA_VOLUME' : data_vol, 'FREQUENCE' : frequency, 'FREQ_TOP_PACK' : freqTop, 'FREQUENCE_RECH' : freqRech, 'ON_NET' : onNet, 'REVENUE' : revenue}])
st.write(input_variable)

# Create a tab for prediction and interpretation
pred_result, interpret = st.tabs(["Prediction Tab", "Interpretation Tab"])
prediction = None
with pred_result:
    if st.button('PREDICT'):
        st.markdown("<br>", unsafe_allow_html= True)
        prediction = model.predict(input_variable)
        st.write("Churn Status :", prediction)
        st.toast('Input is Predicted')
    else:
        st.write('Pls press the predict button for prediction')
    

with interpret:
    st.subheader('Model Interpretation')
    if prediction == 0:
        st.write(['This customer is not liable to continue service with the company.'])
    elif prediction == 1:
        st.write(['This customer is liable to continue service with the company'])    

    # st.write(f"CHURN = {model.round(2)} + {model.coef_[0].round(2)} REGULARITY + {model.coef_[1].round(2)} DATA_VOLUME + {model.coef_[2].round(2)} FREQUENCE + {model.coef_[2].round(2)} FREQ_TOP_PACK + {model.coef_[2].round(2)} FREQUENCE_RECH + {model.coef_[2].round(2)} ON_NET + {model.coef_[2].round(2)} REVENUE")

    
