import streamlit as st
import pandas as pd
import pydeck as pdk 

# Configuración de la página
st.set_page_config(page_title="SUR DAO | Centro de Mando", page_icon="🐋", layout="wide")

# 1. Fila superior: Logo y Título
col_logo, col_titulo = st.columns([0.15, 0.85]) 

with col_logo:
    # Asegúrate de tener la carpeta 'assets' en el mismo nivel que app.py
    st.image("assets/surdao.svg", width=180)

with col_titulo:
    st.write("")
    st.write("")
    st.write("")
    st.title("Auditoría Ciudadana en Tiempo Real")

# 2. Subtítulo centrado
st.markdown(
    "<h4 style='text-align: center; color: #a0a0a0;'>Infraestructura descentralizada de seguimiento de trayectorias.</h4>", 
    unsafe_allow_html=True
)

st.divider()

# Creamos las pestañas
tab1, tab2, tab3, tab4 = st.tabs(["📉 Fuga", "⚠️ Riesgo", "👨‍🏫 Sobrecarga", "🌍 Auditoría Territorial"])

# PESTAÑA 1: FUGA
with tab1:
    st.markdown("### Evolución Histórica de la Fuga de Talentos")
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
            st.error(f"Error al cargar: {e}")

# PESTAÑA 2: RIESGO
with tab2:
    anio_riesgo = st.selectbox("Año a escanear:", [str(y) for y in range(2025, 2011, -1)])
    if st.button("⚠️ Ejecutar Escáner de Riesgo", use_container_width=True, type="primary"):
        try:
            df_riesgo = pd.read_csv(f"data/volatilidad_riesgo_instituciones_{anio_riesgo}.csv")
            st.bar_chart(df_riesgo.head(10).set_index("NOM_RBD")["Volatilidad_Rendimiento"], color="#9D4EDD")
            st.dataframe(df_riesgo, use_container_width=True)
        except Exception as e:
            st.warning("No se encontró el archivo en la carpeta 'data/'.")

# PESTAÑA 3: DOCENTES
with tab3:
    st.markdown("### 👨‍🏫 Sobrecarga Docente")
    try:
        df_docentes = pd.read_csv("data/matriz_maestra_ratio_docentes.csv")
        anios_docentes = sorted(df_docentes['Anio'].unique(), reverse=True)
        for anio in anios_docentes:
            st.markdown(f"#### 🚨 Cohorte {anio}")
            df_anio = df_docentes[df_docentes['Anio'] == anio].nlargest(10, 'Ratio_Alumnos_Docente')
            st.bar_chart(df_anio.set_index("Nombre_Colegio")["Ratio_Alumnos_Docente"], color="#FF4B4B")
            st.divider()
    except:
        st.error("No se encontró el archivo matriz_maestra_ratio_docentes.csv")

# ==========================================
# ==========================================
# PESTAÑA 4: AUDITORÍA TERRITORIAL (MAPA INTELIGENTE)
# ==========================================
with tab4:
    st.markdown("### 🌍 Auditoría Territorial: Rendimiento vs. Gestión")
    
    @st.cache_data
    def get_master_data():
        return pd.read_parquet("data/master_surdao_2026.parquet")
    
    try:
        df_master = get_master_data()
        
        # Filtro de año (ya que ahora tienes la columna 'Anio' en tu master)
        anios_disponibles = sorted(df_master['Anio'].unique(), reverse=True)
        anio_sel = st.selectbox("Selecciona año para auditar:", anios_disponibles)
        df_filtrado = df_master[df_master['Anio'] == anio_sel].copy()
        
        opcion_mapa = st.radio("Visualizar por:", ["Tasa de Éxito", "Sobrecarga Docente"], horizontal=True)
        
        if opcion_mapa == "Tasa de Éxito":
            col_valor = 'Tasa_Exito'
            def color_func(val): return [231, 76, 60, 160] if val < 20 else [46, 204, 113, 160]
        else:
            col_valor = 'Ratio_Alumnos_Docente'
            def color_func(val): return [231, 76, 60, 160] if val > 25 else [46, 204, 113, 160]
        
        df_filtrado['color'] = df_filtrado[col_valor].apply(color_func)
        
        st.pydeck_chart(pdk.Deck(
            map_style="light",
            initial_view_state=pdk.ViewState(latitude=-33.45, longitude=-70.66, zoom=6),
            layers=[pdk.Layer(
                "ScatterplotLayer",
                df_filtrado,
                get_position='[LONGITUD, LATITUD]',
                get_color='color',
                get_radius=300,
                pickable=True
            )],
            tooltip={"html": "<b>{Nombre_Colegio}</b><br/>Éxito: {Tasa_Exito}%<br/>Sobrecarga: {Ratio_Alumnos_Docente}"}
        ))
        
        # Tabla sin la columna inexistente
        cols_mostrar = ['Nombre_Colegio', 'Tasa_Exito', 'Ratio_Alumnos_Docente', 'Total_Docentes']
        st.dataframe(df_filtrado[cols_mostrar].sort_values(by='Tasa_Exito', ascending=False), use_container_width=True)

    except Exception as e:
        st.error(f"Error en auditoría territorial: {e}")
