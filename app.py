import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from PIL import Image
import time
import json

# Cargar credenciales desde secrets
if not firebase_admin._apps:
    firebase_info = st.secrets["firebase"]
    cred = credentials.Certificate(firebase_info)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Parámetros de Firebase
collection_name = "KISS"
document_name = "CLc5jpvARY1LOvqjZWpx"
campo = "Cantidad"

st.title("¿Quieres un besito? 👀💘")

# Leer el valor actual desde Firestore
doc_ref = db.collection(collection_name).document(document_name)
doc = doc_ref.get()

if doc.exists:
    cantidad_actual = doc.to_dict().get(campo, 0)
else:
    cantidad_actual = 0
    doc_ref.set({campo: cantidad_actual})

st.write(f"Besitos que te debo: **{cantidad_actual}**")

# Botón para incrementar
if st.button("¡Quiero besito!"):
    nueva_cantidad = cantidad_actual + 1
    doc_ref.update({campo: nueva_cantidad})
    
    st.success(f"Cantidad de besitos actualizada a {nueva_cantidad}")
    
    st.image("Aq.gif", caption="¡Listo!", use_column_width=True)
    
    time.sleep(2.9)
    st.rerun()
