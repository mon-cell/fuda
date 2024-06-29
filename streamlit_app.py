import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

# テキスト入力ボックス
text_input = st.text_input('対局名', 'テキストを入力')


# カテゴリ
options = st.multiselect(
    '対局カテゴリ',
    ['練習', '公式戦', 'リーグ戦', 'トーナメント'],
    default=['練習'] # デフォルトの設定
)

input_num = st.number_input('対局節', value=1)
result = input_num
st.write('節: ', result)

# ルール
st.radio("ルール", ('Aルール: aaa, bbb, ccc',
                 'Bルール: aaa, bbb, ccc',
                 'Cルール: aaa, bbb, ccc',
                'その他のルール'))

# その他のルール
text_area = st.text_area('その他のルール詳細', 'テキストを入力')

# 順位
option = st.selectbox(
    '順位', 
    ['1', '2', '3', '4']
)

# スコア
value = st.slider('Select a value', -100, 0, 100) # min, max, default

# 記録を表示
df = pd.DataFrame({'col1': [1,2,3]})
df

 
    

    
if st.checkbox('Aルール'):
    st.write('aaa, bbb, ccc')


# データをメールで送信、CSVと結合
if st.button('入力データを表示'):
    st.write('データを送信しました')

# arr = np.random.normal(1, 1, size=100)
# fig, ax = plt.subplots()
# ax.hist(arr, bins=20)

# fig


# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     st.write(uploaded_file)




