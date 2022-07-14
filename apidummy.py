from connection import con_dummy
from flask import Flask, request
import sett 



app = Flask(__name__)

@app.route('/post/apidummy/', methods=['POST'])
def getUser():
    data = request.get_json()
    # print(data)
    id_user = str(data['id_user'])
    user_name = str(data['user_name'])
    tgl_buat = str(data['tgl_buat'])

    conn = con_dummy.connection()
    status = {}
 
    try:
        cur = conn.cursor()

        select = """ SELECT 'IDUSR'||LPAD(COUNT(1)+1,3,'0') AS no_id FROM MS_MASTER_USER """
     
        cur.execute(select)
        nomor_id = cur.fetchone()
        no_id_user = nomor_id[0] + id_user
    
        insert_user = """ INSERT INTO MS_MASTER_USER (ID_USER, NAMA_USER, TGL_BUAT) VALUES (:no_id_user, :user_name, :tgl_buat) """
        cur.execute(insert_user,(no_id_user, user_name, tgl_buat,)) 
        hasil = conn.commit()

        status = {'eror' :'0','message' : " "}
        return status
        cur.close()
        conn.close()
    except Exception as e:
        # print('Error', str(e))
        status = {'status' :'fail','message' : str(e)}
        conn.rollback()
        cur.close()
        conn.close()
    return status 


