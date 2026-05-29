<p align="center">
  <img src="assets/surdao.svg" alt="SUR DAO Logo" width="250">
</p>

#  Centro de Mando: Auditoría Ciudadana Territorial

### *Infraestructura descentralizada de seguimiento.*

Este repositorio contiene la arquitectura inicial del **Centro de Mando de SUR DAO**, una plataforma web interactiva diseñada para rastrear, procesar y exponer de forma analítica y georreferenciada las fallas estructurales dentro del sistema chileno.

> ⚠️ **Fase 0: Educación** > Este lanzamiento representa únicamente la **Fase 0** de nuestro roadmap operativo, enfocada exclusivamente en el **Sistema Educativo Chileno**. En próximas etapas, la infraestructura escalará para integrar nuevas bases de datos y auditar otros sectores clave del territorio nacional.

---

## 🗄️ Fuentes de Datos (Data Lake)

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

## 🖥️ Terminales de Auditoría (Estructura de la App)

El dashboard actual unifica el análisis en 4 pestañas tácticas interactivas:

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

---

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
