FROM python:3.11-slim

#　作業ディレクトリ
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリのコードをコピー
COPY . .

# Streamlit 実行
EXPOSE 7001
CMD ["streamlit", "run", "app.py", "--server.port=7001", "--server.address=0.0.0.0"]
