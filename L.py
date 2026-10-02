#BCI Perototype
#fp1/fp2/c3/c4/p3/p4/o1/o2
electrodes = ['fp1','fp2','c3','c4','p3','p4','o1','o2']
#importing
import winsound
import numpy as np
import streamlit as st
import time
#variables
data = np.random.randint(5,50, size = 8)
fp1=data[0]
fp2=data[1]
c3=data[2]
c4=data[3]
p3=data[4]
p4=data[5]
o1=data[6]
o2=data[7]
st.text(f'fp1 : {fp1}')
st.text(f'fp2 : {fp2}')
st.text(f'c3 : {c3}')
st.text(f'c4 : {c4}')
st.text(f'p3 : {p3}') 
st.text(f'p4 : {p4}')
st.text(f'o1 : {o1}')
st.text(f'o2 : {o2}')
signal = np.mean(data)
#Estimation and operation
st.title('status of the me....' )
if signal > 35:
   st.subheader('I need help!!') 
   winsound.Beep(500,2100) 
elif signal > 25 : 
   st.subheader('I am thisty🫗 ..')
else :
   st.subheader('I am fine..')    
time. sleep(3)
st.rerun()  