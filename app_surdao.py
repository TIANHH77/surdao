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
tab1, tab2, tab3 = st.tabs([ "⚠️ Riesgo", "👨‍🏫 Sobrecarga", "🌍 Auditoría Territorial"])


# ==========================================
# PESTAÑA 1: ESCÁNER DE RIESGO
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
# PESTAÑA 2: CRISIS DE TALENTO DOCENTE
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
# ==========================================
# PESTAÑA 3: AUDITORÍA TERRITORIAL (MAPA INTELIGENTE Y TOP 50)
# ==========================================
with tab4:
    st.markdown("### 🌍 Mapa de Calor: Distribución de Presión Estructural")
    
    @st.cache_data
    def cargar_geo():
        # AHORA PANDAS LEE EL PARQUET DIRECTAMENTE
        return pd.read_parquet("data/matriz_final_geolocalizada.parquet", engine="pyarrow")
    
    try:
        df_pd = cargar_geo()
        
        anio_mapa = st.selectbox("Selecciona año para filtrar el mapa:", sorted(df_pd['Anio'].unique(), reverse=True))
        df_filtrado = df_pd[df_pd['Anio'] == anio_mapa].copy()
        
        def asignar_color(ratio):
            if pd.isna(ratio):
                return [150, 150, 150, 100]  
            elif ratio <= 20:
                return [46, 204, 113, 160]   
            elif ratio <= 30:
                return [241, 196, 15, 180]   
            else:
                return [255, 40, 40, 200]    
                
        df_filtrado['color'] = df_filtrado['Ratio_Alumnos_Docente'].apply(asignar_color)

        # ---------------------------------------------------------
        # MAGIA NUEVA: Extrayendo los 50 más críticos (Rojo/Amarillo)
        # ---------------------------------------------------------
        df_criticos = df_filtrado[df_filtrado['Ratio_Alumnos_Docente'] > 20].copy()
        
        # Validamos cómo se llaman tus columnas en el Parquet (Ajusta si son distintos)
        col_notas = "Promedio_Notas" if "Promedio_Notas" in df_criticos.columns else "Ratio_Alumnos_Docente"
        col_variacion = "Volatilidad_Rendimiento" if "Volatilidad_Rendimiento" in df_criticos.columns else "Ratio_Alumnos_Docente"
        
        # Obtenemos los 50 con mayor variación/riesgo
        df_top50 = df_criticos.nlargest(50, col_variacion)

        # ---------------------------------------------------------
        # CONFIGURACIÓN DEL TOOLTIP INTERACTIVO (HTML)
        # ---------------------------------------------------------
        tooltip_html = {
            "html": f"""
            <div style='font-family: sans-serif;'>
                <b style='font-size: 15px;'>{{Nombre_Colegio}}</b><br/>
                <hr style='margin: 5px 0; border-color: #555;'/>
                🔴 <b>Ratio (Alumnos/Docente):</b> {{Ratio_Alumnos_Docente}}<br/>
                📉 <b>Nota Promedio:</b> {{{col_notas}}}<br/>
                ⚠️ <b>Variación (Riesgo):</b> {{{col_variacion}}}
            </div>
            """,
            "style": {
                "backgroundColor": "#2E2E2E",
                "color": "white",
                "border": "1px solid #FF4B4B",
                "padding": "12px",
                "borderRadius": "6px",
                "boxShadow": "2px 2px 10px rgba(0,0,0,0.5)"
            }
        }

        # ---------------------------------------------------------
        # CAPAS DEL MAPA (General + Destacados Top 50)
        # ---------------------------------------------------------
        capa_general = pdk.Layer(
            "ScatterplotLayer",
            df_filtrado, 
            get_position='[LONGITUD, LATITUD]',
            get_color='color', 
            get_radius=200,
            radius_min_pixels=2,
            radius_max_pixels=6,
            pickable=True,
        )

        capa_top50 = pdk.Layer(
            "ScatterplotLayer",
            df_top50,
            get_position='[LONGITUD, LATITUD]',
            get_fill_color=[255, 0, 0, 255], # Rojo puro intenso
            get_line_color=[0, 0, 0, 255],   # Borde negro para que resalten
            stroked=True,
            line_width_min_pixels=1,         # Borde fino y elegante
            get_radius=350,                  # Tamaño ajustado para no ser grosero
            radius_min_pixels=4,
            radius_max_pixels=9,
            pickable=True,
        )

        # Dividimos la pantalla: Mapa a la izquierda (70%), Lista Crítica a la derecha (30%)
        col_mapa, col_lista = st.columns([2.5, 1])

        with col_mapa:
            st.pydeck_chart(pdk.Deck(
                map_style="light", 
                initial_view_state=pdk.ViewState(latitude=-33.45, longitude=-70.66, zoom=5, pitch=30), # Pitch 30 le da un leve efecto 3D
                layers=[capa_general, capa_top50], # Ponemos ambas capas
                tooltip=tooltip_html
            ))
            
        with col_lista:
            st.markdown("#### 🚨 Top 50 Alertas")
            st.caption("Instituciones con mayor volatilidad.")
            
            # Formateamos la tabla lateral dinámicamente para evitar columnas duplicadas
            columnas_tabla = ['Nombre_Colegio', 'Ratio_Alumnos_Docente']
            if col_variacion not in columnas_tabla:
                columnas_tabla.append(col_variacion)
                
            df_mostrar = df_top50[columnas_tabla].copy()
            
            # Redondeamos decimales solo si la columna es numérica y existe
            if col_variacion in df_mostrar.columns and pd.api.types.is_numeric_dtype(df_mostrar[col_variacion]):
                df_mostrar[col_variacion] = df_mostrar[col_variacion].round(2) 
            
            st.dataframe(df_mostrar, hide_index=True, use_container_width=True, height=450)

    except Exception as e:
        st.error(f"Error cargando el mapa. Asegúrate de que el archivo matriz_final_geolocalizada.parquet existe y contiene las columnas necesarias. Detalles: {e}")
