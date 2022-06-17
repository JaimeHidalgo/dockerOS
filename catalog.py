import requests
import streamlit as st
import pandas as pd

def startStreamLit():
    pf= pd.read_csv(r'/home/fa5/Desktop/ocean/missions/rtkft/maidenVoyage/docker/nftDocker/nftCollections.csv')
    print(pf)
    st.text("meow meow")
    st.table(pf)

if __name__ =='__main__':
    startStreamLit()