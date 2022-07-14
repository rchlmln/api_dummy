from apidummy import app

# file support untuk menjalankan instance di production (WSGI) menggunakan gunicorn
# sebelumnya jangan lupa di env production dilakukan install gunicorn 'pip install gunicorn'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2031, debug=True)

