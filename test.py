import cx_Oracle
import io

cx_Oracle.init_oracle_client(lib_dir="/opt/oracle/instantclient_21_4")
connection = cx_Oracle.connect(user="system", password="oracle",
                               dsn="localhost",
                               encoding="UTF-8")
cursor = connection.cursor()

id_val = 3

cursor.execute("select id, dbms_lob.getlength(value) from test where id = :1",[id_val])
blob_size = cursor.fetchone()
print("DB Blob length:", blob_size)

cursor.execute("select value from test where id = :1",[id_val])
blob_data = cursor.fetchone()
print("Simple BLOB length:", blob_data[0].size())

binary_stream = io.BytesIO()
cursor.execute("select value from test where id = :1",[id_val])
blob, = cursor.fetchone()
offset = 1
num_bytes_in_chunk = 65536
while True:
    data = blob.read(offset, num_bytes_in_chunk)
    if data:
        binary_stream.write(data)
    if len(data) < num_bytes_in_chunk:
        break
    offset += len(data)
print("Stream BLOB length:", binary_stream.getbuffer().nbytes)

# id_val = 3
# lob_var = cursor.var(cx_Oracle.DB_TYPE_BLOB)
# cursor.execute("""
#         insert into test (id, value)
#         values (:1, empty_blob())
#         returning value into :2""", [id_val, lob_var])
# blob, = lob_var.getvalue()
# offset = 1
# num_bytes_in_chunk = 65536
# with open("test.tar", "rb") as f:
#     while True:
#         data = f.read(num_bytes_in_chunk)
#         if data:
#             blob.write(data, offset)
#         if len(data) < num_bytes_in_chunk:
#             break
#         offset += len(data)
# connection.commit()

# cursor.execute("select value from test where id = :1", [id_val])
# blob, = cursor.fetchone()
# offset = 1
# num_bytes_in_chunk = 65536
# with open("test_file_new.tar", "wb") as f:
#     while True:
#         data = blob.read(offset, num_bytes_in_chunk)
#         if data:
#             f.write(data)
#         if len(data) < num_bytes_in_chunk:
#             break
#         offset += len(data)