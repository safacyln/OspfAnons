import streamlit as st
# import paramiko

st.title('OSPF Anons Software')

networkAddr = st.text_input('Anons edilmesini istediğiniz network adresini yazınız')
networkComment = st.text_input('Açıklama yazınız (Örn: Kurumsal)')
st.write('OSPF Network Address : ', networkAddr)
st.write('OSPF Network Comment : ', networkComment)

