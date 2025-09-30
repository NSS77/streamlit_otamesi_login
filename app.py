import os
import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# --- ユーザー情報 ---
USER_DATA = {}
for key, value in os.environ.items():
    if key.startswith("USER"):
        username, password = value.split(":")
        USER_DATA[username] = password

# --- セッション初期化 ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# --- ログアウト関数 ---
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""

# --- ログインフォーム ---
if not st.session_state.logged_in:
    st.title("🎈 ログイン画面")
    username_input = st.text_input("ユーザーID")
    password_input = st.text_input("パスワード", type="password")
    if st.button("ログイン"):
        if username_input in USER_DATA and USER_DATA[username_input] == password_input:
            st.session_state.logged_in = True
            st.session_state.username = username_input
            st.balloons()
        else:
            st.error("ユーザーIDまたはパスワードが間違っています")

# --- ログイン後画面 ---
if st.session_state.logged_in:
    st.title(f"ようこそ {st.session_state.username} さん！")
    if st.button("ログアウト"):
        logout()

    st.write("---")
    # 時計更新
    st_autorefresh(interval=1000, key="clock_refresh")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"🕒 現在の時刻: **{now}**")
