import streamlit as st
st.set_page_config('secundária')

tab01, tab02, tab03 = st.tabs(['pagina 1', 'pagina 2 com o video', 'pagina 3 com a foto'])

with tab01:
    st.write('aba 01')


with tab02:
    st.video('https://youtu.be/K1bqiC8UkZc?si=b-2x3afwY_vecKMI')


with tab03:
    st.image('https://www.petz.com.br/blog/wp-content/uploads/2021/08/pato-de-estimacao.jpg')
    st.image('https://www.petz.com.br/blog/wp-content/uploads/2021/08/pato-de-estimacao.jpg')


