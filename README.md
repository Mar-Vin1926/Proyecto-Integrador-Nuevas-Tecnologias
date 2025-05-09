```markdown
# Análisis de Suicidios en Antioquia (2005-2021)

## Descripción
Esta aplicación de Streamlit permite explorar y analizar datos sobre la cantidad de suicidios registrados en el departamento de Antioquia, Colombia, entre los años 2005 y 2021. La aplicación proporciona herramientas interactivas para filtrar los datos por año y región, y visualizaciones para identificar patrones y tendencias.

## Funcionalidades
* Filtro interactivo por rango de años.
* Filtro interactivo por región.
* Visualización de la tendencia anual de suicidios.
* Visualización de la distribución de suicidios por región.
* Visualización de la tendencia de suicidios por región a lo largo del tiempo.
* Mapa interactivo que muestra la ubicación aproximada de los casos.
* Tabla con los datos filtrados.

## Cómo ejecutar la aplicación
1.  Clona este repositorio (si aplica).
2.  Asegúrate de tener Python instalado.
3.  Crea un entorno virtual (recomendado):
    ```bash
    python -m venv .venv
    ```
    * Activa el entorno virtual:
        * En Windows: `.venv\Scripts\activate`
        * En macOS/Linux: `source .venv/bin/activate`
4.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
5.  Navega hasta el directorio del proyecto.
6.  Ejecuta la aplicación:
    ```bash
    streamlit run Inicio.py
    ```

## Estructura del proyecto
```
analisis_suicidios_streamlit/
├── .streamlit/
├── assets/
├── pages/
├── static/
│   └── datasets/
│       └── suicidios_antioquia.csv
├── .gitignore
├── Inicio.py
├── README.md
└── requirements.txt
```

## Datasets
* `static/datasets/suicidios_antioquia.csv`: Contiene datos sobre la cantidad de suicidios en Antioquia por año, región, y otras variables.

## Librerías utilizadas
* streamlit
* pandas
* plotly
* pydeck

## Autor
Marvin García
```
