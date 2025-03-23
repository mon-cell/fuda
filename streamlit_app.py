import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

class Hai_List():
    list_hai = [] # クラス属性　全てのインスタンスで共有
    def __init__(self, name, cat, no, dora): # 属性に値を一括で設定するメソッドを定義
        self.name = name # selfには実際にはインスタンスが入る
        self.cat = cat
        self.no = no
        self.dora = dora
        
     # 各属性の値をprint
    def print_hai(self):
        print('{},{},{},{}'.format(self.name, self.cat, self.no, self.dora))

    def get_hai_name(hai):
        return hai.name
    
    def get_hai_no(hai):
        return hai.no

    def hai_display(i):
        if i == m5r:
            print(RED + chr(int(i.name, 16)), end='')
        elif i == p5r:
            print(RED + chr(int(i.name, 16)), end='')
        elif i == s5r:
            print(RED + chr(int(i.name, 16)), end='')
        else:
            print(BLACK + chr(int(i.name, 16)), end='')

    def hai_list_display(l):
        for i in l:
            Hai_List.hai_display(i)
        print('')

    
    def hai_display_call(i, j):
        #print(BLACK + chr(int(i.name, 16)))
        Hai_List.hai_display(i)
        print('')        
        if j == 'pon':
            print(GRAY + 'ポン', end='')
        elif j == 'che':
            print(GRAY + 'チー', end='')
        elif j == 'kan':
            print(GRAY + 'カン', end='')
        elif j == 'reach':
            print(GRAY + 'リーチ', end='')
        elif j == 'tsumo':
            print(GRAY + 'ツモ', end='')
        elif j == 'ron':
            print(GRAY + 'ロン', end='')
        elif j == 'dora':
            print(GRAY + 'ドラ', end='')
        print('')

    def add_hai(l, i):
        l.append(i)
        sorted_l = sorted(l, key=lambda x: x.no) # noでリストを昇順に並べ替え
        for j in sorted_l: # 並べ替えたリストを表示
            #print(BLACK + chr(int(j.name, 16)), end='')
            Hai_List.hai_display(j)

    def sort_hai(l, i):
        l.append(i)
        sorted_l = sorted(l, key=lambda x: x.no) # noでリストを昇順に並べ替え
        return sorted_l

    def reorder_hai(l):
        sorted_l = sorted(l, key=lambda x: x.no) # noでリストを昇順に並べ替え
        for j in sorted_l: # 並べ替えたリストを表示
            Hai_List.hai_display(j)

# 入力した文字列を並べ替えて表示する
    def order_text(l):
        Hai_List.reorder_hai(l)
        st.write(st.session_state[l])

BLACK = '\033[0;30m'
RED = '\033[31m'
GRAY = '\033[37m'
BLUE = '\033[34m'
  
# 萬子
m1 = Hai_List('1F007', 'manzu', 1, '')
m2 = Hai_List('1F008', 'manzu', 2, '')
m3 = Hai_List('1F009', 'manzu', 3, '')
m4 = Hai_List('1F00A', 'manzu', 4, '')
m5 = Hai_List('1F00B', 'manzu', 5, '')
m6 = Hai_List('1F00C', 'manzu', 6, '')
m7 = Hai_List('1F00D', 'manzu', 7, '')
m8 = Hai_List('1F00E', 'manzu', 8, '')
m9 = Hai_List('1F00F', 'manzu', 9, '')
m5r = Hai_List('1F00B', 'manzu', 5.1, 'dora')

# 筒子
p1 = Hai_List('1F019', 'pinzu', 11, '')
p2 = Hai_List('1F01A', 'pinzu', 12, '')
p3 = Hai_List('1F01B', 'pinzu', 13, '')
p4 = Hai_List('1F01C', 'pinzu', 14, '')
p5 = Hai_List('1F01D', 'pinzu', 15, '')
p6 = Hai_List('1F01E', 'pinzu', 16, '')
p7 = Hai_List('1F01F', 'pinzu', 17, '')
p8 = Hai_List('1F020', 'pinzu', 18, '')
p9 = Hai_List('1F021', 'pinzu', 19, '')
p5r = Hai_List('1F01D', 'pinzu', 15.1, 'dora')

# 索子
s1 = Hai_List('1F010', 'souzu', 21, '')
s2 = Hai_List('1F011', 'souzu', 22, '')
s3 = Hai_List('1F012', 'souzu', 23, '')
s4 = Hai_List('1F013', 'souzu', 24, '')
s5 = Hai_List('1F014', 'souzu', 25, '')
s6 = Hai_List('1F015', 'souzu', 26, '')
s7 = Hai_List('1F016', 'souzu', 27, '')
s8 = Hai_List('1F017', 'souzu', 28, '')
s9 = Hai_List('1F018', 'souzu', 29, '')
s5r = Hai_List('1F014', 'souzu', 25.1, 'dora')

# 字牌
east = Hai_List('1F000', 'jihai', 31, '')
south = Hai_List('1F001', 'jihai', 32, '')
west = Hai_List('1F002', 'jihai', 33, '')
north = Hai_List('1F003', 'jihai', 34, '')
chun = Hai_List('1F004', 'jihai', 35, '')
hatsu = Hai_List('1F005', 'jihai', 36, '')
haku = Hai_List('1F006', 'jihai', 37, '')

# 特殊
ume = Hai_List('1F022', 'special', '', '') # 梅
ran = Hai_List('1F023', 'special', '', '') # 蘭
take = Hai_List('1F024', 'special', '', '') # 竹
kiku = Hai_List('1F025', 'special', '', '') # 菊
shun = Hai_List('1F026', 'special', '', '') # 春
ka = Hai_List('1F027', 'special', '', '') # 夏
shu = Hai_List('1F028', 'special', '', '') # 秋
toh = Hai_List('1F029', 'special', '', '') # 冬
baida = Hai_List('1F02A', 'special', '', '') # 百搭ばいだオールマイティー

ura = Hai_List('1F02B', 'special', 41, '') # 裏面
batsu = Hai_List('1F02C', 'special', 51, '') # ばつ
none = Hai_List(' ', 'special', 61, '') # 空欄


# def insert_text(seq_obj):
#     if 'seq_list' not in st.session_state:
#         st.session_state['seq_list'] = []
#     st.session_state['seq_list'].append(seq_obj)
#     st.session_state['text'] += seq_obj.name


# 入力をそのまま表示する文字列
def insert_name(hai_name):
    if st.session_state['text']:
        st.session_state['text'] += hai_name
    else: st.session_state['text'] = hai_name

        
# 入力をそのまま表示する文字列
def insert_no(hai_no):
    if st.session_state['seq_list']:
        st.session_state['seq_list'] += hai_name
    else: st.session_state['seq_list'] = hai_name


def order_text():
    seq_list = ['text']
    sorted_list = sorted(st.session_state['text'], key=lambda x: x.no)
    seq_list = seq_list.join([seq.name for seq in sorted_list])
    print(seq_list)
    return seq_list


def combine_seq(h):
    insert_name(chr(int(h.name, 16)))
    hai_seq.append(Hai_List.hai_display(h))    
    
def combine_no(h):
    insert_no(chr(int(h.no, 16)))
    hai_seq.append(Hai_List.hai_display(h))    


hai_seq = []


if 'text' not in st.session_state:
    st.session_state['text'] = ''

st.text_area("表示したい配列を入力してください", key='text', height=150)


st.button(chr(int(m1.name, 16)), on_click=lambda: combine_seq(m1))
st.button(chr(int(p1.name, 16)), on_click=lambda: combine_seq(p1))
st.button(chr(int(p4.name, 16)), on_click=lambda: combine_seq(p4))

st.button('Order', on_click=lambda: order_text)


# 押すと二つ取得する関数
# 表示する関数
# 並べ替える関数
# ボタン作る関数


# def reset_text():
#     st.session_state['text'] = []
#クリックしたら関数を実行するボタンを作る関数

    


#st.button('Space', on_click=lambda: Hai_List.insert_text(' '))
#st.button('Reset', on_click=lambda: reset_text)

st.button('Show', on_click=lambda: Hai_List.add_hai(hai_seq, none))

# col_m1, col_m2, col_m3 = st.columns(3)
# with col_m1:
#      hai_button(chr(int(m3.name, 16)))    
# with col_m2:
#      hai_button(chr(int(m4.name, 16)))
# with col_m3:
#      hai_button(chr(int(m5.name, 16)))


        
if st.button('Delete'):
    st.session_state['text'].remove(text)
    


#if st.button('Display'):
#    st.write(st.session_state[hai_seq])



    
# text = st.text_input("表示したい単語を入力してください")

# col1, col2 = st.columns(2)

# with col1:
#     if st.button("追加", key=2):
#         st.session_state["hai_list"].append(text)

# with col2:
#     if st.button("削除", key=3): 
#         st.session_state["hai_list"].remove(text)

# for output_text in st.session_state["hai_list"]:
#     st.write("", output_text)



# テキスト入力ボックス
text_input = st.text_input('対局名', 'テキストを入力')
















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




