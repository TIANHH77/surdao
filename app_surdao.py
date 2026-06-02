import streamlit as st
import pandas as pd
import time
import pydeck as pdk 

# Configuración de la página
st.set_page_config(page_title="SUR DAO | Centro de Mando", page_icon="🐋", layout="wide")

# 1. Fila superior: Logo y Título
col_logo, col_titulo = st.columns([0.15, 0.85]) 

with col_logo:
    # CORRECCIÓN 1: RUTA RELATIVA AL LOGO
    st.image("assets/surdao.svg", width=180)

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
            df_fuga = pd.read_csv("data/fuga_talentos.csv")
            
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
            ruta_archivo = f"data/volatilidad_riesgo_instituciones_{anio_riesgo}.csv"
            df_riesgo = pd.read_csv(ruta_archivo)
            
            st.bar_chart(df_riesgo.head(10).set_index("NOM_RBD")["Volatilidad_Rendimiento"], color="#9D4EDD")
            st.dataframe(df_riesgo, use_container_width=True)
        except Exception as e:
            st.warning(f"No se encontró el escáner de riesgo para el año {anio_riesgo}. Verifica la carpeta 'data/'.")

# ==========================================
# PESTAÑA 3: CRISIS DE TALENTO DOCENTE
# ==========================================
with tab3:
    st.markdown("### 👨‍🏫 Sobrecarga Docente: La Falla Estructural")
    st.markdown("Los 10 establecimientos más críticos por año. Cuando el ratio de **Alumnos por Docente** se rompe, el sistema colapsa.")
    
    @st.cache_data
    def cargar_datos_docentes():
        try:
            # CORRECCIÓN 2: RUTA RELATIVA A DATA/
            return pd.read_csv("data/matriz_maestra_ratio_docentes.csv")
        except:
            return pd.DataFrame()
            
    df_docentes = cargar_datos_docentes()
    
    if not df_docentes.empty:
        anios_docentes = sorted(df_docentes['Anio'].unique(), reverse=True)
        
        for anio in anios_docentes:
            st.markdown(f"#### 🚨 Cohorte {anio}")
            
            df_anio = df_docentes[df_docentes['Anio'] == anio]
            df_top10_docentes = df_anio.nlargest(10, 'Ratio_Alumnos_Docente')
            
            col_grafico, col_tabla = st.columns([2, 1])
            
            with col_grafico:
                st.bar_chart(df_top10_docentes.set_index("Nombre_Colegio")["Ratio_Alumnos_Docente"], color="#FF4B4B")
                
            with col_tabla:
                df_mostrar = df_top10_docentes[['Nombre_Colegio', 'Ratio_Alumnos_Docente', 'Promedio_Notas']].rename(
                    columns={"Ratio_Alumnos_Docente": "Alumnos x Prof.", "Promedio_Notas": "Nota Prom."}
                )
                st.dataframe(df_mostrar, hide_index=True, use_container_width=True)
            
            st.divider() 
    else:
        st.error("No se encontró el archivo matriz_maestra_ratio_docentes.csv o está vacío.")


# # ==========================================
# PESTAÑA 4: AUDITORÍA TERRITORIAL (MAPA INTELIGENTE)
# ==========================================
with tab4:
    st.markdown("### 🌍 Auditoría Territorial: Rendimiento vs. Gestión")
    
    # Esta es la única forma correcta de cargar los datos
    @st.cache_data
    def get_data():
        # Asegúrate de que esta ruta coincida exactamente con donde está tu master
        return pd.read_parquet("data/master_surdao_2026.parquet")
    
    try:
        df_master = get_data()
        
        # Selector de métrica
        opcion_mapa = st.radio("Visualizar por:", ["Tasa de Éxito", "Sobrecarga Docente"], horizontal=True)
        
        # Lógica de color
        if opcion_mapa == "Tasa de Éxito":
            col_valor = 'Tasa_Exito'
            def color_func(val):
                return [231, 76, 60, 160] if val < 20 else [46, 204, 113, 160]
        else:
            col_valor = 'Ratio_Alumnos_Docente'
            def color_func(val):
                return [231, 76, 60, 160] if val > 25 else [46, 204, 113, 160]
        
        df_master['color'] = df_master[col_valor].apply(color_func)
        
        # Mapa
        st.pydeck_chart(pdk.Deck(
            map_style="light",
            initial_view_state=pdk.ViewState(latitude=-33.45, longitude=-70.66, zoom=6),
            layers=[pdk.Layer(
                "ScatterplotLayer",
                df_master,
                get_position='[LONGITUD, LATITUD]',
                get_color='color',
                get_radius=300,
                pickable=True
            )],
            tooltip={"html": "<b>{Nombre_Colegio}</b><br/>Éxito: {Tasa_Exito}%<br/>Sobrecarga: {Ratio_Alumnos_Docente}"}
        ))
        
        # Tabla de datos
        st.dataframe(df_master[['Nombre_Colegio', 'Tasa_Exito', 'Ratio_Alumnos_Docente', 'Puntaje_Docente_Promedio']].sort_values(by='Tasa_Exito', ascending=False), use_container_width=True)

    except Exception as e:
        st.error(f"Error en la auditoría territorial: {e}")
