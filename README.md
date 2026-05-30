<p align="center">
  <img src="assets/surdao.svg" alt="SUR DAO Logo" width="250">
</p>


<p align="center">
  <img src="assets/surdao.svg" alt="SUR DAO Logo" width="250">
</p>

# Command Center: Territorial Citizen Audit

<p align="center">
  <a href="https://surdao.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🚀_Live_Command_Center-FF4B4B?style=for-the-badge" alt="Live Demo">
  </a>
</p>

<details>
<summary><b>🇺🇸 English Version (Click to expand)</b></summary>
<br>

This repository contains the initial architecture of the <b>SUR DAO Command Center</b>, an interactive platform designed to track, process, and analytically expose systemic failures through georeferenced data. This initial phase audits the territory of <b>Chile</b>, with a roadmap to scale to <b>Argentina</b> and the <b>Global South</b>.

> ⚠️ <b>Phase 0: Education</b> > This release focuses exclusively on the Chilean Educational System. Upcoming stages will integrate new datasets (starting with Health).

### ⚙️ Architecture and Tech Stack
* <b>Frontend / UI:</b> <code>Streamlit</code>
* <b>Massive Data Processing:</b> <code>Pandas</code> and <code>PyArrow</code> (Native high-performance engine for <code>.parquet</code> files).
* <b>Geospatial Engine:</b> <code>PyDeck</code> (Thermographic mapping in <i>Light Mode</i>).
* <b>Historical Queries:</b> <code>DuckDB</code>

### 🖥️ Audit Terminals (App Structure)
* <b>1. Historical "Brain Drain":</b> Evolution of student loss (2012-2023).
* <b>2. Risk Scanner:</b> Statistical anomalies in school grades and institutional performance.
* <b>3. Teacher Overload:</b> Ranking of establishments with the highest collapse in staff distribution.
* <b>4. Territorial Audit:</b> Interactive radar exposing structural collapse (Green/Yellow/Red zones).

<b>Phase 2</b> proposes a <b>Spiral Architecture</b> and a model of <b>Reciprocal Economy and Mutual Custody</b> to support the invisible work ("Shadow Layer") of those sustaining the network.

</details>

---

### *Infraestructura descentralizada de seguimiento.*

Este repositorio contiene la arquitectura inicial del **Centro de Mando de SUR DAO**, una plataforma web interactiva diseñada para rastrear, procesar y exponer de forma analítica y georreferenciada las fallas estructurales del sistema. Esta fase inicial audita el territorio de Chile, pero la arquitectura está diseñada para escalar próximamente a Argentina y, con la fuerza de la comunidad, a todo el Hemisferio Sur.

> ⚠️ **Fase 0: Educación** > Este lanzamiento representa únicamente la **Fase 0** de nuestro roadmap operativo, enfocada exclusivamente en el Sistema Educativo Chileno. En próximas etapas, la infraestructura escalará para integrar nuevas bases de datos y auditar otros sectores clave del territorio nacional, próximamente Salud.

---

## ⚙️ Arquitectura y Stack Tecnológico
Para garantizar el procesamiento in-memory de bases de datos masivas sin latencia en la nube, el Centro de Mando utiliza:
* **Frontend / UI:** `Streamlit`
* **Procesamiento de Datos Masivos:** `Pandas` y `PyArrow` (Motor nativo de alto rendimiento para archivos `.parquet`).
* **Motor Geoespacial:** `PyDeck` (Cartografía termográfica en capa *Light Mode*).
* **Consultas Históricas (Pre-procesamiento):** `DuckDB`

## 🗄️ Fuentes de Datos (Data Lake)

<details>
<summary><b>Click to view full list of data sources</b></summary>
Nuestra infraestructura no inventa los datos, procesa y transparenta lo que ya existe. La información utilizada en esta <b>Fase 0</b> proviene íntegramente de registros oficiales del MINEDUC:
<ul>
  <li>Rendimiento académico por estudiante (2002 - 2025)</li>
  <li>Matrícula por estudiante (2004 - 2025)</li>
  <li>Notas de enseñanza media y percentil (1990 - 2023)</li>
  <li>Alumnos preferentes, prioritarios y beneficiarios SEP (2008 - 2025)</li>
  <li>Sistema de Admisión Escolar (SAE) (2016 - 2023)</li>
  <li>Directorio de Establecimientos Educacionales (1992-2025)</li>
</ul>
</details>

---

## 🖥️ Terminales de Auditoría (Estructura de la App)
El dashboard actual unifica el análisis en 4 pestañas tácticas interactivas:

* **📉 1. Histórico Fuga:** Volumen de cerebros perdidos y tasa porcentual de fuga sistémica.
* **⚠️ 2. Escáner de Riesgo:** Identificación de instituciones con comportamientos altamente volátiles.
* **👨‍🏫 3. Sobrecarga Docente:** Ranking de colapso en la distribución de la planta docente.
* **🌍 4. Auditoría Territorial (Mapa Termográfico):** Radar espacial basado en el ratio Alumnos/Docente.

---

## 📚 La Visión: Hacia la Gobernanza Descentralizada
Este dashboard es solo la auditoría de la realidad (Fase 0). La **Fase 2** propone una **Arquitectura de Espiral** y un modelo de **Economía Recíproca**. Buscamos reconocer ("Proof of Contribution") el trabajo invisible de quienes sostienen la red educativa desde la *Capa de Sombra*.

> 🚨 **Próximo Despliegue:** El Código de la Educación Superior. El sistema ve matrículas, mas no trayectorias. Hallazgos próximamente.

---

## 🗺️ Estructura del Repositorio

<details>
<summary><b>Click to see file hierarchy</b></summary>

```text
surdao-centro-mando/
├── README.md                # El manifiesto y guía técnica
├── app_surdao.py            # Aplicación principal de Streamlit
├── assets/                  # Logo oficial de SUR DAO
├── data/                    # Data Lake (Parquet/CSV)
└── analytics/               # Módulos de procesamiento
#  Centro de Mando: Auditoría Ciudadana Territorial

<p align="center">
  <a href="https://surdao.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🚀_Probar_Centro_de_Mando_en_Vivo-FF4B4B?style=for-the-badge" alt="Live Demo">
  </a>
</p>

### *Infraestructura descentralizada de seguimiento.*

Este repositorio contiene la arquitectura inicial del Centro de Mando de SUR DAO, una plataforma web interactiva diseñada para rastrear, procesar y exponer de forma analítica y georreferenciada las fallas estructurales del sistema. Esta fase inicial audita el territorio de Chile, pero la arquitectura está diseñada para escalar próximamente a Argentina y, con la fuerza de la comunidad, a todo el Hemisferio Sur.

> ⚠️ **Fase 0: Educación** > Este lanzamiento representa únicamente la **Fase 0** de nuestro roadmap operativo, enfocada exclusivamente en el **Sistema Educativo Chileno**. En próximas etapas, la infraestructura escalará para integrar nuevas bases de datos y auditar otros sectores clave del territorio nacional, proximamente Salud.


## ⚙️ Arquitectura y Stack Tecnológico
Para garantizar el procesamiento in-memory de bases de datos masivas sin latencia en la nube, el Centro de Mando utiliza:
* **Frontend / UI:** `Streamlit`
* **Procesamiento de Datos Masivos:** `Pandas` y `PyArrow` (Motor nativo de alto rendimiento para archivos `.parquet`).
* **Motor Geoespacial:** `PyDeck` (Cartografía termográfica en capa *Light Mode*).
* **Consultas Históricas (Pre-procesamiento):** `DuckDB`


Nuestra infraestructura no inventa los datos, procesa y transparenta lo que ya existe. La información utilizada en esta **Fase 0** proviene íntegramente de registros oficiales gubernamentales procesados para su visualización masiva:

**Fuente Oficial:** [Datos Abiertos MINEDUC (Ministerio de Educación)](https://datosabiertos.mineduc.cl/)
* **Rendimiento académico por estudiante** (2002 - 2025)
* **Matrícula por estudiante** (2004 - 2025)
* **Notas de enseñanza media y percentil jóvenes** (1990 - 2023)
* **Notas de enseñanza media y percentil adultos** (1990 - 2023)
* **Alumnos preferentes, prioritarios y beneficiarios SEP** (2008 - 2025)
* **Sistema de Admisión Escolar (SAE)** (2016 - 2023)
* **Practicantes y titulados Técnico Profesional** (2013 - 2024)
* **Registro Público Digital – Anótate en la Lista** (2025)
* **Directorio de Establecimientos Educacionales** (1992-2025)

---

## 📚 La Visión: Hacia la Gobernanza Descentralizada (Fase 1 ➔ Fase 2)
Este dashboard es solo la auditoría de la realidad (Fase 0). El sistema educativo no se arregla solo mirándolo. 
El dashboard actual unifica el análisis en 4 pestañas tácticas interactivas:

## 🖥️ Terminales de Auditoría (Estructura de la App)
### 📉 1. Histórico Fuga
* **Propósito:** Muestra la evolución estructural de la pérdida de alumnos de excelencia académica en Chile entre los años 2012 y 2023.
* **Métricas:** Volumen de cerebros perdidos y tasa porcentual de fuga sistémica conectada a una infraestructura DuckDB.

### ⚠️ 2. Escáner de Riesgo
* **Propósito:** Detecta anomalías estadísticas en las calificaciones escolares filtradas por año.
* **Métricas:** Evalúa la desviación estándar del rendimiento. Identifica instituciones con comportamientos altamente volátiles que reflejan ecosistemas críticos.

### 👨‍🏫 3. Sobrecarga Docente
* **Propósito:** Expone el ranking anual de los 10 establecimientos con mayor colapso en la distribución de su planta docente.
* **Visualización:** Gráficos de barras en "rojo de alerta" que revelan la crisis de horas y dotación.

### 🌍 4. Auditoría Territorial (El Mapa Termográfico)
* **Propósito:** Traduce más de 120,000 registros tabulares en un radar espacial interactivo utilizando `PyDeck` en modo de alto contraste (`Light Mode`).
* **Lógica Científica del Semáforo de Presión:**
  * 🟢 **Verde (Ratio ≤ 20):** Zona Óptima/Tolerable según estándares OCDE. Pedagogía viable y seguimiento personalizado.
  * 🟡 **Amarillo (Ratio 21 - 30):** Zona de Alerta. Alta carga administrativa, estrés docente latente y gestión masiva de aula.
  * 🔴 **Rojo Sangre (Ratio > 30):** Colapso Estructural. El sistema supera los límites de resiliencia. Espacios de contención de crisis, no de aprendizaje.

La **Fase 2** de SUR DAO propone una **Arquitectura de Espiral** y un modelo de **Economía Recíproca y Custodia Mutua**. A través de una infraestructura descentralizada, buscamos reconocer y respaldar ("Proof of Contribution") el trabajo invisible de quienes sostienen la red educativa desde las trincheras, operando en lo que llamamos la *Capa de Sombra*, toda esa data no puede quedar oculta entre los promedios.

> 🚨 **Próximo Despliegue: El Código de la Educación Superior**
> Nuestros hallazgos sobre la educación superior se publicarán pronto en este mismo espacio. Como adelanto: en el caso de Chile, el sistema de convalidación de créditos y competencias sigue respondiendo a lógicas de 1983. Su "actualización" en 2018 no es más que maquillaje institucional para ocultar su mayor falla estructural: **el sistema ve matrículas, no trayectorias educativas.**


Si quieres entender el rediseño sistémico completo detrás de este código, te invitamos a explorar nuestros manifiestos fundacionales en la carpeta `/manifestos`:
1. `#1 Gobernanza Descentralizada, Economía Recíproca y Custodia Mutua`
2. `#2 Trayectorias Acompañadas`
3. `#3 Democracia Descentralizada DAO`

---
*No pedimos permiso para auditar, construimos los datos que exponen la realidad. El código es libre y el control territorial es ciudadano.* 

## 🗺️ Estructura del Repositorio

```text
surdao-centro-mando/
├── README.md                # El manifiesto y guía técnica del proyecto
├── app_surdao.py            # Aplicación principal de Streamlit (Interfaz y Control)
├── assets/                  # Identidad visual del proyecto
│   └── surdao.svg           # Logo vectorizado oficial de SUR DAO
├── data/                    # Data Lake Local (Archivos excluidos por peso)
│   ├── matriz_final_geolocalizada.parquet   
│   └── matriz_maestra_ratio_docentes.csv     
└── analytics/               # Módulos y scripts de procesamiento previos
