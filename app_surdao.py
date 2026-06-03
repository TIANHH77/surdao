import streamlit as st
import pandas as pd
import duckdb
import pydeck as pdk 

# Configuración maestra de la página
st.set_page_config(page_title="SUR DAO | Centro de Mando", page_icon="🐋", layout="wide")

# Ruta oficial a tu cerebro de datos indexado
DB_PATH = r"C:\SURDAO_CENTRO_MANDO\palacio_memoria\maestros\SURDAO_LAKEHOUSE.duckdb"

# Función de conexión segura de alto rendimiento
def ejecutar_consulta(query: str) -> pd.DataFrame:
    # Abrimos en modo lectura para permitir concurrencia masiva de usuarios
    con = duckdb.connect(DB_PATH, read_only=True)
    try:
        df = con.execute(query).df()
        return df
    except Exception as e:
        st.error(f"Error en motor DuckDB: {e}")
        return pd.DataFrame()
    finally:
        con.close()

# 1. Fila superior: Logo y Título
col_logo, col_titulo = st.columns([0.15, 0.85]) 

with col_logo:
    st.image("assets/surdao.svg", width=180)

with col_titulo:
    st.write("")
    st.write("")
    st.write("")
    st.title("Auditoría Ciudadana en Tiempo Real")

# 2. Subtítulo corporativo
st.markdown(
    "<h4 style='text-align: center; color: #a0a0a0;'>Infraestructura descentralizada de seguimiento de trayectorias longitudinales.</h4>", 
    unsafe_allow_html=True
)

st.divider()

# Orquestación de Pestañas Analíticas
tab1, tab2, tab3, tab4 = st.tabs(["📉 Fuga (Transición)", "⚠️ Escáner de Riesgo", "👨‍🏫 Sobrecarga Docente", "🌍 Auditoría Territorial"])

# ==========================================
# PESTAÑA 1: FUGA DE TALENTOS (Tasa de Transición Real)
# ==========================================
with tab1:
    st.markdown("### Evolución Histórica de la Fuga de Talentos Escolares")
    st.caption("Cruce longitudinal en tiempo real de la matrícula media frente al ingreso efectivo a la Educación Superior.")
    
    if st.button("🔥 Generar Radiografía Histórica", use_container_width=True, key="btn_fuga"):
        with st.spinner("Computando trayectorias longitudinales sobre el Data Lake..."):
            # SQL puro para cruzar cohortes históricas al vuelo
            query_fuga = """
                WITH Cohortes AS (
                    SELECT AGNO, COUNT(DISTINCT MRUN) AS Matricula_Media
                    FROM VIEW_BM_MATRICULA
                    WHERE COD_GRADO IN ('12', '4') -- Filtro de 4to Medio según codificación Mineduc
                    GROUP BY 1
                ),
                Transicionados AS (
                    SELECT B.AGNO, COUNT(DISTINCT S.MRUN) AS Ingreso_Superior
                    FROM VIEW_BM_MATRICULA B
                    INNER JOIN VIEW_SUP_MATRICULA S ON B.MRUN = S.MRUN
                    WHERE B.COD_GRADO IN ('12', '4')
                    GROUP BY 1
                )
                SELECT 
                    C.AGNO AS Anio,
                    C.Matricula_Media AS [Egresados 4to Medio],
                    COALESCE(T.Ingreso_Superior, 0) AS [Ingresaron a la U],
                    (100.0 - (COALESCE(T.Ingreso_Superior, 0) * 100.0 / C.Matricula_Media)) AS [Tasa de Fuga (%)]
                FROM Cohortes C
                LEFT JOIN Transicionados T ON C.AGNO = T.AGNO
                ORDER BY C.AGNO ASC
            """
            df_fuga = ejecutar_consulta(query_fuga)
            
            if not df_fuga.empty:
                df_grafico = df_fuga.set_index("Anio")
                col1, col2 = st.columns(2)
                col1.line_chart(df_grafico["Tasa de Fuga (%)"], color="#FF4B4B")
                col2.bar_chart(df_grafico["Ingresaron a la U"], color="#1f77b4")
                st.dataframe(df_fuga, use_container_width=True, hide_index=True)

# ==========================================
# PESTAÑA 2: ESCÁNER DE RIESGO ACADÉMICO
# ==========================================
with tab2:
    st.markdown("### Escáner de Volatilidad y Riesgo de Rendimiento")
    # Generar años dinámicamente consultando los datos reales disponibles
    anio_riesgo = st.selectbox("Selecciona el Año a escanear:", [str(y) for y in range(2024, 2011, -1)])
    
    if st.button("⚠️ Ejecutar Escáner de Riesgo", use_container_width=True, type="primary"):
        with st.spinner(f"Analizando desviaciones estándar de notas para el periodo {anio_riesgo}..."):
            query_riesgo = f"""
                SELECT 
                    NOM_RBD,
                    COUNT(DISTINCT MRUN) AS Total_Alumnos,
                    STDDEV(TRY_CAST(REPLACE(PROM_GRAL, ',', '.') AS DOUBLE)) AS Volatilidad_Rendimiento,
                    AVG(TRY_CAST(REPLACE(PROM_GRAL, ',', '.') AS DOUBLE)) AS Promedio_General
                FROM VIEW_BM_RENDIMIENTO
                WHERE AGNO = '{anio_riesgo}' AND PROM_GRAL IS NOT NULL
                GROUP BY NOM_RBD
                HAVING COUNT(DISTINCT MRUN) > 30 -- Filtro estadístico para evitar muestras pequeñas
                ORDER BY Volatilidad_Rendimiento DESC
                LIMIT 15
            """
            df_riesgo = ejecutar_consulta(query_riesgo)
            
            if not df_riesgo.empty:
                st.bar_chart(df_riesgo.set_index("NOM_RBD")["Volatilidad_Rendimiento"], color="#9D4EDD")
                st.dataframe(df_riesgo, use_container_width=True, hide_index=True)

# ==========================================
# PESTAÑA 3: CRISIS DE TALENTO DOCENTE (Sobrecarga)
# ==========================================
with tab3:
    st.markdown("### 👨‍🏫 Sobrecarga Docente: La Falla Estructural")
    st.markdown("Análisis dinámico de la relación Alumnos por cada Profesor en funciones.")
    
    anio_docentes = st.selectbox("Selecciona Año de Análisis Docente:", [str(y) for y in range(2024, 2011, -1)], key="sel_doc")
    
    if st.button("🚨 Calcular Ratios de Presión", use_container_width=True):
        with st.spinner("Procesando nóminas docentes vs registros de matrícula escolar..."):
            query_docentes = f"""
                WITH Alumnos AS (
                    SELECT AGNO, RBD, NOM_RBD, COUNT(DISTINCT MRUN) AS Total_Alumnos
                    FROM VIEW_BM_MATRICULA
                    WHERE AGNO = {anio_docentes}
                    GROUP BY 1, 2, 3
                )
                SELECT 
                    A.NOM_RBD AS [Nombre Colegio],
                    A.Total_Alumnos AS [Alumnos Matriculados],
                    TRY_CAST(D.DC_TOT AS INTEGER) AS [Total Docentes],
                    ROUND(A.Total_Alumnos / NULLIF(TRY_CAST(D.DC_TOT AS DOUBLE), 0), 1) AS [Ratio Alumnos x Prof]
                FROM Alumnos A
                INNER JOIN VIEW_CH_DOCENTES D ON A.RBD = D.RBD AND A.AGNO = D.AGNO
                ORDER BY [Ratio Alumnos x Prof] DESC
                LIMIT 10
            """
            df_docentes = ejecutar_consulta(query_docentes)
            
            if not df_docentes.empty:
                col_grafico, col_tabla = st.columns([2, 1])
                with col_grafico:
                    st.bar_chart(df_docentes.set_index("Nombre Colegio")["Ratio Alumnos x Prof"], color="#FF4B4B")
                with col_tabla:
                    st.dataframe(df_docentes, hide_index=True, use_container_width=True)

# ==========================================
# PESTAÑA 4: AUDITORÍA TERRITORIAL (Geolocalización Completa)
# ==========================================
with tab4:
    st.markdown("### 🌍 Mapa de Calor: Distribución Geográfica de la Presión Estructural")
    
    anio_mapa = st.selectbox("Selecciona año para filtrar el mapa territorial:", [str(y) for y in range(2024, 2011, -1)], key="sel_map")
    
    with st.spinner("Generando coordenadas de geolocalización institucional..."):
        # Extraemos coordenadas reales cruzando el Directorio de Establecimientos
        query_geo = f"""
            WITH Presion AS (
                SELECT RBD, COUNT(DISTINCT MRUN) AS Alumnos
                FROM VIEW_BM_MATRICULA
                WHERE AGNO = {anio_mapa}
                GROUP BY 1
            )
            SELECT 
                E.NOM_RBD AS Nombre_Colegio,
                TRY_CAST(E.LATITUD AS DOUBLE) AS LATITUD,
                TRY_CAST(E.LONGITUD AS DOUBLE) AS LONGITUD,
                P.Alumnos AS Matricula_Total
            FROM VIEW_TR_ESTABLECIMIENTOS E
            INNER JOIN Presion P ON E.RBD = P.RBD
            WHERE E.LATITUD IS NOT NULL AND E.LONGITUD IS NOT NULL 
              AND TRY_CAST(E.LATITUD AS DOUBLE) BETWEEN -56.0 AND -17.0 -- Filtro de coordenadas de Chile
        """
        df_geo = ejecutar_consulta(query_geo)
        
        if not df_geo.empty:
            # Configuración dinámica del color (Escala de calor según tamaño de matrícula)
            df_geo['color_r'] = df_geo['Matricula_Total'].apply(lambda x: min(255, int(x / 5)))
            df_geo['color'] = df_geo['color_r'].apply(lambda r: [r, 50, 150, 160])
            
            tooltip_html = {
                "html": """
                <div style='font-family: sans-serif; background-color: #2E2E2E; color: white; padding: 10px; border-radius: 5px;'>
                    <b>{Nombre_Colegio}</b><br/>
                    <hr style='margin: 5px 0;'/>
                    👥 <b>Matrícula Total:</b> {Matricula_Total} alumnos
                </div>
                """,
                "style": {"color": "white"}
            }
            
            capa_general = pdk.Layer(
                "ScatterplotLayer",
                df_geo, 
                get_position='[LONGITUD, LATITUD]',
                get_color='color', 
                get_radius=300,
                radius_min_pixels=3,
                radius_max_pixels=12,
                pickable=True,
            )
            
            col_mapa, col_lista = st.columns([2.5, 1])
            
            with col_mapa:
                st.pydeck_chart(pdk.Deck(
                    map_style="mapbox://styles/mapbox/dark-v10", 
                    initial_view_state=pdk.ViewState(latitude=-33.45, longitude=-70.66, zoom=6, pitch=40),
                    layers=[capa_general],
                    tooltip=tooltip_html
                ))
                
            with col_lista:
                st.markdown("#### 📊 Distribución de Datos")
                st.caption(f"Se geolocalizaron {len(df_geo):,} colegios activos.")
                st.dataframe(df_geo[['Nombre_Colegio', 'Matricula_Total']].sort_values(by="Matricula_Total", ascending=False), hide_index=True, use_container_width=True, height=400)
