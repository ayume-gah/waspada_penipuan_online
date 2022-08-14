from asyncore import write
import streamlit as st
import re #regex
import random

st.sidebar.markdown("# Password Checker")
st.sidebar.image('password.svg')
st.header('Password Strong Checker')
st.write('''Password harus minimal 8 karakter dan maksimal 20 karakter. Dan terdiri dari kombinasi huruf
besar, huruf kecil dan angka.''')
st.write('\n')

password=st.text_input('Masukkan password','')
if len(password)>20:
    st.markdown('<p style="color:Red;font-size:20px;"><strong>Password terlalu panjang!</strong></p>',
    unsafe_allow_html=True)
    #st.write('**Password terlalu panjang!**')
elif len(password)<8:
    st.markdown('<p style="color:Red;font-size:20px;"><strong>Password terlalu pendek!</strong></p>',
    unsafe_allow_html=True)
    #st.write('**Password terlalu pendek!**')
elif len(password)>=8 and len(password)<=20:
    st.markdown('<p style="color:Green;font-size:20px;"><strong>Password OK!</strong></p>',
    unsafe_allow_html=True)
    #st.write('**Password OK!**')

password_scores={1:'Kekuatan password: **Lemah**',2:'Kekuatan password: **Sedang**',3:'Kekuatan password: **Kuat**'}
a=0
if re.search(r"[A-Z]", password):
    a+=1
if re.search(r"[a-z]", password):
    a+=1
if re.search(r"[0-9]", password):
    a+=1
st.write(password_scores.get(a))

st.write('-------------------------------------------------')
#st.write('###### Apakah Anda ingin password random yang kuat?')
#col1,col2=st.columns([2,8])
#ya=col1.button('Ya')
#tidak=col2.button('Tidak')

st.write('## Password Random Rekomendasi')
lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nomer='0123456789'
simbol='@#$&_-()+%*:/!?+.'
kata=lower+upper+nomer+simbol
panjang=st.slider('Tentukan panjang karakter yang diinginkan?',value=8,min_value=8,max_value=20,step=1)
password=''.join(random.sample(kata,panjang))
#st.code('Password baru anda : ' + password)
st.warning('Password baru anda : ' + password)