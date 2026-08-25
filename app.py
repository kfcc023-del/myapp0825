import streamlit as st

st.title("새마을금고중앙회~글씨가 많아지면 알아서 줄바꿈이 될런지 궁금해서 그냥 쭉 한번 써봄 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

if st.button("Send balloons!"):
    st.balloons()
