import streamlit as st
import pandas as pd
import requests
import time
import pydeck as pdk # <--- Asegúrate de tener también esto para el mapa

# Configuración de la página
st.set_page_config(page_title="SUR DAO | Centro de Mando", page_icon="🐋", layout="wide")

# 1. Fila superior: Logo y Título
col_logo, col_titulo = st.columns([0.15, 0.85]) 

with col_logo:
    st.image("assets/surdao.svg", width=180) # Esto busca dentro de la carpeta assets

with col_titulo:
    # Estos espacios empujan el título hacia abajo para que quede a la altura de la base del logo
    st.write("")
    st.write("")
    st.write("")
    st.title("Auditoría Ciudadana en Tiempo Real")

# 2. Subtítulo centrado forzado con HTML
st.markdown(
    "<h4 style='text-align: center; color: #a0a0a0;'>Infraestructura descentralizada de seguimiento de trayectorias.</h4>", 
    unsafe_allow_html=True
)

st.divider()
# Creamos las pestañas para unificar la app
tab1, tab2, tab3, tab4 = st.tabs(["📉 Fuga", "⚠️ Riesgo", "👨‍🏫 Sobrecarga", "🌍 Auditoría Territorial"])

# ==========================================
# PESTAÑA 1: FUGA DE TALENTOS
# ==========================================
with tab1:
    st.markdown("### Evolución Histórica de la Fuga de Talentos (2012 - 2023)")
    if st.button("🔥 Generar Radiografía Histórica", use_container_width=True, key="btn_fuga"):
        try:
            # Leemos el archivo único que tiene toda la historia
            df_fuga = pd.read_csv("data/fuga_talentos.csv")
            
            # Asegurarnos de que el índice sea el año para que los gráficos funcionen bien
            if "Año" in df_fuga.columns:
                df_fuga = df_fuga.set_index("Año")
                
            col1, col2 = st.columns(2)
            col1.line_chart(df_fuga["Tasa de Fuga (%)"], color="#FF4B4B")
            col2.bar_chart(df_fuga["Talentos Fugados"], color="#1f77b4")
            st.dataframe(df_fuga, use_container_width=True)
        except Exception as e:
            st.error(f"Error al cargar la matriz de fuga: {e}")

# ==========================================
# PESTAÑA 2: ESCÁNER DE RIESGO
# ==========================================
with tab2:
    anio_riesgo = st.selectbox("Año a escanear:", [str(y) for y in range(2025, 2011, -1)])
    if st.button("⚠️ Ejecutar Escáner de Riesgo", use_container_width=True, type="primary"):
        try:
            # Magia con f-strings: busca dinámicamente el archivo del año seleccionado
            ruta_archivo = f"data/volatilidad_riesgo_instituciones_{anio_riesgo}.csv"
            df_riesgo = pd.read_csv(ruta_archivo)
            
            st.bar_chart(df_riesgo.head(10).set_index("NOM_RBD")["Volatilidad_Rendimiento"], color="#9D4EDD")
            st.dataframe(df_riesgo, use_container_width=True)
        except Exception as e:
            st.warning(f"No se encontró el escáner de riesgo para el año {anio_riesgo}. Verifica la carpeta 'data/'.")

# ==========================================
# PESTAÑA 3: CRISIS DE TALENTO DOCENTE (CASCADA HISTÓRICA)
# ==========================================
with tab3:
    st.markdown("### 👨‍🏫 Sobrecarga Docente: La Falla Estructural")
    st.markdown("Los 10 establecimientos más críticos por año. Cuando el ratio de **Alumnos por Docente** se rompe, el sistema colapsa.")
    
    # Truco de magia: Cacheamos los 120.000 registros
    @st.cache_data
    def cargar_datos_docentes():
        try:
            # RUTA RELATIVA: Esto funcionará en cualquier lugar (tu PC y la nube)
            return pd.read_csv("data/matriz_maestra_ratio_docentes.csv")
        except:
            return pd.DataFrame()
            
    # 🔥 AQUÍ ESTABA EL ERROR: Faltaba esta línea para ejecutar la función
    df_docentes = cargar_datos_docentes()
    
    if not df_docentes.empty:
        # Obtenemos todos los años únicos, ordenados desde el más reciente al más antiguo
        anios_docentes = sorted(df_docentes['Anio'].unique(), reverse=True)
        
        # Generamos la cascada visual año por año
        for anio in anios_docentes:
            st.markdown(f"#### 🚨 Cohorte {anio}")
            
            # Filtramos el año y sacamos el Top 10 con peor ratio
            df_anio = df_docentes[df_docentes['Anio'] == anio]
            df_top10_docentes = df_anio.nlargest(10, 'Ratio_Alumnos_Docente')
            
            # Dividimos la pantalla: Gráfico a la izquierda, métricas a la derecha
            col_grafico, col_tabla = st.columns([2, 1])
            
            with col_grafico:
                # Un gráfico de barras rojo sangre para la alerta
                st.bar_chart(df_top10_docentes.set_index("Nombre_Colegio")["Ratio_Alumnos_Docente"], color="#FF4B4B")
                
            with col_tabla:
                # Mostramos la tabla resumen para los curiosos
                df_mostrar = df_top10_docentes[['Nombre_Colegio', 'Ratio_Alumnos_Docente', 'Promedio_Notas']].rename(
                    columns={"Ratio_Alumnos_Docente": "Alumnos x Prof.", "Promedio_Notas": "Nota Prom."}
                )
                st.dataframe(df_mostrar, hide_index=True, use_container_width=True)
            
            st.divider() # Línea separadora entre años
    else:
        st.error("No se encontró el archivo matriz_maestra_ratio_docentes.csv o está vacío.")

## ==========================================
# ==========================================
# PESTAÑA 4: AUDITORÍA TERRITORIAL (MAPA Y TOP 50)
# ==========================================
with tab4:
    st.markdown("### 🌍 Mapa de Calor: Distribución de Presión Estructural")
    
    @st.cache_data
    def cargar_datos():
        # Cargamos los dos archivos base
        df_geo = pd.read_parquet("data/matriz_final_geolocalizada.parquet")
        df_ratios = pd.read_csv("data/matriz_maestra_ratio_docentes.csv")
        # Cruzamos para asegurar que tenemos el nombre y el ratio del colegio
        return pd.merge(df_geo, df_ratios, on=['RBD', 'Anio'], how='left')
    
    try:
        df_completo = cargar_datos()
        
        anio_mapa = st.selectbox("Selecciona año:", sorted(df_completo['Anio'].unique(), reverse=True))
        df_filtrado = df_completo[df_completo['Anio'] == anio_mapa].copy()
        
        # Filtro de Top 50 basado en la estructura de tu archivo
        df_top50 = df_filtrado.nlargest(50, 'Ratio_Alumnos_Docente')

        col_mapa, col_lista = st.columns([2.5, 1])

        with col_mapa:
            st.pydeck_chart(pdk.Deck(
                map_style="light",
                initial_view_state=pdk.ViewState(latitude=-33.45, longitude=-70.66, zoom=5),
                layers=[
                    pdk.Layer("ScatterplotLayer", df_filtrado, get_position='[LONGITUD, LATITUD]', 
                              get_radius=200, get_color=[50, 200, 100, 150], pickable=True),
                    pdk.Layer("ScatterplotLayer", df_top50, get_position='[LONGITUD, LATITUD]', 
                              get_radius=200, get_fill_color=[230, 80, 80, 200], pickable=True)
                ],
                tooltip={"html": "<b>{Nombre_Colegio}</b><br/>Ratio: {Ratio_Alumnos_Docente}<br/>Nota: {Promedio_Notas}"}
            ))
            
        with col_lista:
            st.markdown("#### 🚨 Top 50 Alertas")
            # Mostramos los datos que sí existen en tu CSV
            st.dataframe(df_top50[['Nombre_Colegio', 'Ratio_Alumnos_Docente', 'Promedio_Notas']], 
                         hide_index=True, use_container_width=True, height=450)

    except Exception as e:
        st.error(f"Error en la auditoría: {e}")

