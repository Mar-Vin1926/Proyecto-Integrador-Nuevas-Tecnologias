import streamlit as st
import base64
from pathlib import Path

# --- Configuración de la página ---
st.set_page_config(
    page_title="Proyecto Python - Nuevas Tecnologías",
    page_icon="🚀",
    layout="wide"
)

# --- Estilos personalizados ---
st.markdown(f"""
    <style>
        .main-header {{
            font-size: 3rem;
            color: #2E86C1; /* Un azul más vibrante */
            text-align: center;
            margin-bottom: 1.5rem;
            font-family: 'Arial Black', sans-serif; /* Ejemplo de fuente */
        }}
        .sub-header {{
            font-size: 2rem;
            color: #5DADE2; /* Un tono de azul más claro */
            text-align: center;
            margin-bottom: 2.5rem;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Otra fuente */
            font-style: italic;
        }}
        .section-title {{
            font-size: 2.2rem;
            color: #2E86C1;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #D4E6F1;
            padding-bottom: 0.5rem;
        }}
        .student-info-container {{
            background-color: #EBF5FB; /* Fondo suave */
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.08);
            margin-bottom: 30px;
        }}
        .student-name {{
            color: #2E86C1;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .student-detail {{
            color: #5DADE2;
            font-size: 1.1rem;
            margin-bottom: 8px;
        }}
        .github-link {{
            color: #2E86C1 !important;
            font-weight: bold;
            text-decoration: none !important;
        }}
        .github-link:hover {{
            text-decoration: underline !important;
        }}
        .stButton > button {{
            background-color: #2E86C1;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.7rem 1.5rem;
            border: none;
            transition: background-color 0.3s ease;
        }}
        .stButton > button:hover {{
            background-color: #1C395A; /* Un tono más oscuro al pasar el ratón */
        }}
        .logo-cesde {{
            width: 250px; /* Ajusta el ancho según sea necesario */
            margin-bottom: 20px; /* Espacio debajo del logo */
        }}
        .logo-python {{
            width: 100px; /* Ajusta el ancho según sea necesario */
            margin-left: 20px; /* Espacio a la izquierda del logo */
            margin-bottom: 20px;
        }}
        .logos-container {{
            display: flex;
            justify-content: flex-start; /* Alinea los logos a la izquierda */
            align-items: center; /* Centra los logos verticalmente */
            gap: 2em; /* Espacio entre los logos */
            margin-bottom: 2em;
        }}
        .logo {{
            display: inline-block;
            width: auto;
            height: auto;
        }}
    </style>
""", unsafe_allow_html=True)

# --- Función para cargar y mostrar el logo SVG ---
def show_svg(filepath, width=None):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            svg_content = f.read()
        if width:
            svg_content = svg_content.replace('<svg', f'<svg width="{width}"')
        st.markdown(f"<div class='logo'>{svg_content}</div>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"No se encontró el archivo: {filepath}")
    except Exception as e:
        st.error(f"Error al cargar el archivo SVG: {e}")

# --- Sección de logos ---
st.markdown('<div class="logos-container">', unsafe_allow_html=True)

# Mostrar el logo de CESDE (SVG)
show_svg("assets/logo-Cesde-2023.svg", width=250)

# Mostrar el logo de Python (PNG)
try:
    st.image("assets/logo-python.png", width=100)
except FileNotFoundError:
    st.error("No se encontró el archivo: assets/logo-python.png")

st.markdown('</div>', unsafe_allow_html=True)

# --- Encabezados ---
st.markdown('<h1 class="main-header">¡Análisis de las causas de suicidio en Antioquia!</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">Explorando las Nuevas Tecnologías con un DataSet</h2>', unsafe_allow_html=True)

# --- Sección de información del estudiante con diseño mejorado ---
st.markdown('<h2 class="section-title">Desarrolladores</h2>', unsafe_allow_html=True)
st.markdown(f"""
    <div class="student-info-container">
        <div style="display: flex; align-items: center;">
            <div style="margin-right: 30px;">
                <img src="https://avatars.githubusercontent.com/u/12345679?v=4" alt="Foto de perfil" style="border-radius: 50%; width: 150px; height: 150px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
            </div>
            <div>
                <p class="student-name">Kevin Olivella, Marvin García y Paola Murillo</p>
                <p class="student-detail">Programa: <span style="font-weight: bold;">Desarrollo de Software: Nuevas Tecnologías</span></p>
                <p class="student-detail">Semestre: <span style="font-weight: bold;">2025-1</span></p>
                <p class="student-detail">Repositorio: <a href="https://github.com/Kevolive/proyecto-integrador.git" target="_blank" class="github-link">GitHub</a></p>
                <p class="student-detail">¡Apasionados por la creación de soluciones innovadoras con tecnología de punta!</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Introducción interactiva (ejemplo) ---
st.markdown('<h2 class="section-title">¿Qué te interesa explorar hoy?</h2>', unsafe_allow_html=True)
opcion = st.radio(
    "Selecciona un tema:",
    ("Inteligencia Artificial", "Desarrollo Web Moderno", "Análisis de Datos")
)

if opcion == "Inteligencia Artificial":
    st.write("¡Excelente elección! En las siguientes páginas encontrarás información sobre IA.")
elif opcion == "Desarrollo Web Moderno":
    st.write("El desarrollo web está en constante evolución. ¡Descubre las últimas tendencias!")
elif opcion == "Análisis de Datos":
    st.write("El poder de los datos para tomar decisiones informadas. ¡Exploremos!")

# --- Pie de página personalizado ---
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #777; font-size: 0.9rem; padding-top: 10px;">
        © 2025 Kevin Olivella - Marvin Garcia - Paola Murillo - Proyecto para Nuevas Tecnologías de Programación
    </div>
""", unsafe_allow_html=True)
