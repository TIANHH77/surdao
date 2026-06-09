<p align="center">
  <img src="assets/surdao.svg" alt="SUR DAO Logo" width="250">
</p>

# Centro de Mando: Auditoría Ciudadana Territorial

[![Clones](https://img.shields.io/badge/dynamic/json?color=2ea043&label=Clones&query=count&logo=github&url=https%3A%2F%2Fgist.githubusercontent.com%2FTIANHH77%2F0259cb9b2d97bab774a666c4003eb5a3%2Fraw%2Fclone.json)](https://github.com/TIANHH77/surdao)

<p align="center">
  <a href="https://surdao.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🚀_Probar_Centro_de_Mando_en_Vivo-FF4B4B?style=for-the-badge" alt="Live Demo">
  </a>
</p>

<details>
<summary><b>🇺🇸 English Version (Click to expand)</b></summary>

This repository contains the architecture of the **SUR DAO Command Center**, an interactive platform to track and expose systemic failures via georeferenced data. This phase audits **Chile**, with a roadmap to scale to **Argentina** and the **Global South**.

> ⚠️ **Phase 0:** Focusing on the Chilean Educational System.

### ⚙️ Tech Stack
* **Frontend:** `Streamlit`
* **Data Processing:** `Pandas` + `PyArrow`
* **Geospatial:** `PyDeck`
* **Historical Queries:** `DuckDB`

### 🖥️ Audit Terminals
1. **Brain Drain:** Student loss evolution (2012-2023).
2. **Risk Scanner:** Statistical performance anomalies.
3. **Teacher Overload:** Staffing collapse rankings.
4. **Territorial Audit:** Interactive heat map of structural collapse.

**Phase 2** proposes a **Spiral Architecture** to support the "Shadow Layer" of educators. Our upcoming Higher Education report reveals: *the system sees enrollments, not trajectories.*
</details>

---

### *Infraestructura descentralizada de seguimiento.*

Este repositorio contiene la arquitectura inicial del **Centro de Mando de SUR DAO**, una plataforma web interactiva diseñada para rastrear, procesar y exponer de forma analítica y georreferenciada las fallas estructurales del sistema. Esta fase inicial audita el territorio de Chile, pero la arquitectura está diseñada para escalar próximamente a Argentina y, con la fuerza de la comunidad, a todo el Hemisferio Sur.

> ⚠️ **Fase 0: Educación** > Este lanzamiento representa únicamente la **Fase 0** de nuestro roadmap operativo, enfocada exclusivamente en el **Sistema Educativo Chileno**. En próximas etapas, la infraestructura escalará para integrar nuevas bases de datos y auditar otros sectores clave del territorio nacional, próximamente Salud.

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
  <li>Notas de enseñanza media y percentil jóvenes/adultos (1990 - 2023)</li>
  <li>Alumnos preferentes, prioritarios y beneficiarios SEP (2008 - 2025)</li>
  <li>Sistema de Admisión Escolar (SAE) (2016 - 2023)</li>
  <li>Directorio de Establecimientos Educacionales (1992-2025)</li>
</ul>
</details>

---

## 📚 La Visión: Hacia la Gobernanza Descentralizada (Fase 1 ➔ Fase 2)
Este dashboard es solo la auditoría de la realidad (Fase 0). El sistema educativo no se arregla solo mirándolo. 

## 🖥️ Terminales de Auditoría (Estructura de la App)
### 📉 1. Histórico Fuga
* **Propósito:** Evolución estructural de la pérdida de alumnos de excelencia académica (2012-2023).
* **Fuga de talentos del sistema educativo.

### ⚠️ 2. Escáner de Riesgo
* **Propósito:** Detecta anomalías estadísticas en calificaciones escolares y volatilidad institucional.
* **Métricas:** Evalúa la desviación estándar del rendimiento. Identifica instituciones con comportamientos altamente volátiles que reflejan ecosistemas críticos.

### 👨‍🏫 3. Sobrecarga Docente
* **Propósito:** Ranking anual de los 10 establecimientos con mayor colapso en la distribución de su planta docente.

### 🌍 4. Auditoría Territorial (El Mapa Termográfico)

* **Propósito:** Traduce más de 120,000 registros tabulares en un radar espacial interactivo utilizando `PyDeck` en modo de alto contraste (`Light Mode`).

* **Lógica Científica del Semáforo de Presión:**

* 🟢 **Verde (Ratio ≤ 20):** Zona Óptima/Tolerable según estándares OCDE. Pedagogía viable y seguimiento personalizado.

* 🟡 **Amarillo (Ratio 21 - 30):** Zona de Alerta. Alta carga administrativa, estrés docente latente y gestión masiva de aula.

* 🔴 **Rojo Sangre (Ratio > 30):** Colapso Estructural. El sistema supera los límites de resiliencia. Espacios de contención de crisis, no de aprendizaje

La **Fase 2** de SUR DAO propone una **Arquitectura de Espiral** y un modelo de **Economía Recíproca**. Buscamos reconocer ("Proof of Contribution") el trabajo invisible de quienes sostienen la red educativa desde la *Capa de Sombra*.

> 🚨 **Próximo Despliegue: El Código de la Educación Superior**
> El sistema ve matrículas, no trayectorias. Hallazgos próximamente.

Si quieres entender el rediseño sistémico completo detrás de este código, te invitamos a explorar nuestros manifiestos fundacionales en la carpeta `/manifestos`.

---
*No pedimos permiso para auditar, construimos los datos que exponen la realidad. El código es libre y el control territorial es ciudadano.* 🐋

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
