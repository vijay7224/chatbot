import pandas as pd 
import streamlit as st
data=pd.read_csv("C:\\Users\\payal\\Desktop\\col.csv")
y=data[["placement"]]
from sklearn.preprocessing import OneHotEncoder
lb=OneHotEncoder()
z=lb.fit_transform(y).toarray()
v=z[:,1]
data["place"]=v
dataset=data.drop(columns=["placement"])
x=dataset.iloc[:,-4:-1]
y=dataset[["place"]]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=1000000)
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)
st.title("STUDENT PLACEMENT PREDICTION")
e=st.number_input("ENTER THE STUDENT IQ",value=100)
f=st.number_input("ENTER THE STUDENT 10TH MARKES",value=33)
g=st.number_input("ENTER THE STUDENT 12TH MARKES",value=33)

if st.button("SUBMIT"):
  a=[[e,f,g]]
  b=lr.predict(a)
  c=b[0]
  b=int(c)
  if b==0:
    st.subheader("you are not place")
  else:
    st.subheader("your are place")