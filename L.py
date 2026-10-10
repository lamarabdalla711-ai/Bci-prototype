
#fp1/fp2/c3/c4/p3/p4/o1/o2
electrodes = ['fp1','fp2','c3','c4','p3','p4','o1','o2']
#importing
import numpy as np
import streamlit as st
import time
#variables
data = np.random.randint(5,50, size = 8)
signal = np.mean(data)
fp1=data[0]
fp2=data[1]
c3=data[2]
c4=data[3]
p3=data[4]
p4=data[5]
o1=data[6]
o2=data[7]
st.text(f'fp1 : {fp1}          fp2 : {fp2}/nc3 : {c3}          c4 : {c4}/np3 : {p3}          p4 : {p4}/no1 : {o1}          o2 : {o2}     ')
st.bar_chart(data)
if signal > 35 and signal < 45:
   st.text("I NEED HELP...")
   st.audio("alarm.mp3")
elif signal >= 35 and signal <= 45:
   st.text("I am focusing now...")
elif signal < 25 :
   st.text("I am calm...")
time.sleep(2)  
st.rerun()  
