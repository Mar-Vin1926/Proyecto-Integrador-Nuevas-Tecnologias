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
            color: #2E86C1;
            text-align: center;
            margin-bottom: 1.5rem;
            font-family: 'Arial Black', sans-serif;
        }}
        .sub-header {{
            font-size: 2rem;
            color: #5DADE2;
            text-align: center;
            margin-bottom: 2.5rem;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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
            background-color: #EBF5FB;
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
            background-color: #1C395A;
        }}
        .logos-container {{
            display: flex;
            justify-content: center; /* Centra los logos horizontalmente */
            align-items: center; /* Alinea los logos verticalmente */
            gap: 2em; /* Espacio entre los logos */
            margin-bottom: 2em;
        }}
        .logo {{
            display: inline-block;
            width: auto;
            height: auto;
        }}
        .logo-cesde {{
            width: 300px; /* Ajusta el ancho del logo de CESDE */
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

# Renderiza el logo de CESDE usando la función show_svg
show_svg("assets/logo-Cesde-2023.svg", width=120)

st.markdown('</div>', unsafe_allow_html=True)

# --- CSS para centrar y ajustar el tamaño del logo ---
st.markdown("""
<style>
.logos-container {
    display: flex;
    justify-content: center; /* Centra el logo horizontalmente */
    align-items: center; /* Centra el logo verticalmente */
    margin-bottom: 2em;
}
.logo {
    width: 120px; /* Ajusta el tamaño del logo de CESDE */
    height: auto;
    border-radius: 100px; /* Bordes redondeados */
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])  # Ajusta las proporciones de las columnas

with col1:
    # Mostrar la imagen con bordes redondeados y sombra
    st.image("assets/foto-perfil.jpg", width=150, caption="",)

with col2:
    # Mostrar la información del estudiante
    st.markdown("""
        <div>
            <p class="student-name">Kevin Olivella, Marvin García y Paola Murillo</p>
            <p class="student-detail">Programa: <span style="font-weight: bold;">Desarrollo de Software: Nuevas Tecnologías</span></p>
            <p class="student-detail">Semestre: <span style="font-weight: bold;">2025-1</span></p>
            <p class="student-detail">Repositorio: <a href="https://github.com/Mar-Vin1926/Proyecto-Integrador-Nuevas-Tecnologias.git" target="_blank" class="github-link">GitHub</a></p>
            <p class="student-detail">¡Apasionados por la creación de soluciones innovadoras con tecnología de punta!</p>
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
