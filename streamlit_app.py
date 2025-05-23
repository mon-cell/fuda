import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt #入れるとエラー
import numpy as np
from io import StringIO
from collections import Counter

st.set_page_config(page_title="top page", page_icon="")
st.title("top page")


def count_factor(i):
    data = i['順位'].value_counts()
    sum_data = data.sum()
    return sum_data

st.title('CSVアップロード')
uploaded_file = st.file_uploader('CSVファイルをアップロードしてください', type=["csv", "xlsx"])

# Check if file was uploaded
if uploaded_file:
    # Check MIME type of the uploaded file
    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.dataframe(df)
    st.success('ファイルを読み込みました')
    st.write('全対戦成績')
    
    op_list0 = [' ']
    op_list1 = df['相手1'].tolist() # 列からリストを取得
    op_list2 = df['相手2'].tolist()
    op_list3 = df['相手3'].tolist()

    combined = op_list1 + op_list2 + op_list3
    counter = Counter(combined)

    sorted_items = [item for item, count in counter.most_common()]
    sorted_items = op_list0 + sorted_items
    
    
    selected_name = st.selectbox('名前を選んでください', sorted_items)
    st.write(f'選択したのは: {selected_name}')

    op = selected_name

    if selected_name == ' ':
        df_cond = df
    else:
        df_cond = df[(df['相手1'] == op) | (df['相手2'] == op) | (df['相手3'] == op)]
    
    df_1st = df_cond[(df_cond['順位'] == 1)]
    df_2nd = df_cond[(df_cond['順位'] == 2)]
    df_3rd = df_cond[(df_cond['順位'] == 3)]
    df_4th = df_cond[(df_cond['順位'] == 4)]

    num_all = df_cond['順位'].count()
    num_1st = count_factor(df_1st)
    num_2nd = count_factor(df_2nd)
    num_3rd = count_factor(df_3rd)
    num_4th = count_factor(df_4th)

    rate_1st = 100 * num_1st / num_all
    rate_up_half = 100 * (num_1st + num_2nd) / num_all
    rate_4th = 100 * num_4th / num_all

    col_sum = df_cond['合計'].sum()
    col_mean = np.mean(df_cond['合計'])
    col_mean = round(float(col_mean), 1)
    
    col_stdv = np.std(df_cond['合計'])
    col_stdv = round(float(col_stdv), 1)
    
    st.dataframe(df_cond)
    st.write(op, f'との対戦数: ', num_all)

    st.write('対戦でのトップ数: ', num_1st, '(', rate_1st.round(1), '%)')
    st.write('対戦でのラス数: ', num_4th, '(', rate_4th.round(1), '%)')
    st.write('対戦での連帯率: ', rate_up_half.round(1), '%')
    st.write('対戦スコア合計: ', col_sum)
    st.write('対戦スコア平均: ', col_mean)
    st.write('対戦スコア標準偏差: ', col_stdv)
    
else:
    st.warning('No file uploaded.')
