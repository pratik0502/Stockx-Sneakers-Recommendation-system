import streamlit as st
import pickle
import pandas as pd

# def shoe_img(product_id):
#

def recommend(shoe):
    shoe_index = shoes[shoes['product_name'] == shoe].index[0]
    distance = similarity[shoe_index]
    shoes_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_shoes = []
    shoe_img_url = []
    try:
        for i in shoes_list:

            recommended_shoes.append(shoes.iloc[i[0]].product_name)
            shoe_img_url.append(shoes.iloc[i[0]].product_img_url)
    except:
        pass
    try:
        for x,y in zip(shoe_img_url,recommended_shoes):

             st.image(x, caption=y)
    except:
        pass
    # return recommended_shoes


shoes_dict = pickle.load(open('shoe.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


shoes = pd.DataFrame(shoes_dict)
st.title("stockX's  Shoes Recommender System")

selected_shoe_name = st.selectbox(
    'select shoes name.',shoes['product_name'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_shoe_name)
    try:
        for i in recommendations:

            st.write(i)
    except:
        pass