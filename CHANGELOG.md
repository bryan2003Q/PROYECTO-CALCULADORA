# CHANGELOG

Todos los cambios notables en este proyecto se documentan en este archivo.

Se sigue el formato **Keep a Changelog** y **Semantic Versioning** (SemVer).

- **Formato:** `MAJOR.MINOR.PATCH`  
- **Reglas básicas:** los cambios incompatibles incrementan MAJOR, nuevas funcionalidades incrementan MINOR, correcciones incrementan PATCH.

---

## [Unreleased]
### Added
- (Lista los cambios en desarrollo aquí)

### Changed
- (Lista los cambios en desarrollo aquí)

### Fixed
- (Lista las correcciones en desarrollo aquí)

---

## [1.1.0] - 2025-11-26
**Tag:** `v1.1.0`  
**Commits incluidos (resumen):** `2405eef`, `5fda773`, `2f262ea`, `9f12df9`, `378d345`, `dbc7a0c`, `59fcc92`  
**Autores destacados:** Amwt24, AntonyC12, BryanQ, Tu Nombre

### Added
- Añadidas operaciones aritméticas: resta, multiplicación y división. (`59fcc92` — BryanQ)  
- Tests automatizados para las operaciones matemáticas. (`dbc7a0c` — BryanQ)  
- Implementación inicial de la interfaz y funciones del backend para la calculadora. (`9f12df9` — Tu Nombre)  
- Pipeline de control de calidad y validaciones internas implementadas. (`2f262ea` — AntonyC12)

### Changed
- Consolidación de features y ajustes de integración mediante merges de ramas de feature. (commits de integración: `5fda773`, `378d345`, `2405eef`)  
  *Nota:* estos merges integran la lógica del backend, tests y ajustes de UI/HTML.

### Fixed
- Correcciones derivadas del proceso de integración y tests (detalles en los commits de merge y en los tests añadidos).  
  - Ejemplos: ajustes en arranque y manejo de excepciones detectados por tests. (ver `2405eef`, `378d345`)

**Resumen:** v1.1.0 consolida la base funcional del proyecto (v1.0.0), añade nuevas operaciones y cobertura de tests, e introduce controles de calidad automáticos que mejoran la estabilidad para despliegues posteriores.

---

## [1.0.0] - 2025-11-26
**Tag:** `v1.0.0`  
**Commit tag asociado:** `71b16bc`  
**Commits clave previos al tag:** `6d7363b` (Initial commit), `99b9a91` (implementación backend), `71b16bc` (Fix: corrección de arranque en `app.py`)  
**Autores destacados:** Amwt24, Tu Nombre, AntonyC12, BryanQ

### Added
- Versión inicial del proyecto: estructura base del repositorio. (`6d7363b` — Initial commit)  
- Implementación básica del backend / API de la calculadora. (`99b9a91` — Tu Nombre)  
- Corrección del problema de arranque en `app.py` incluida en el tag inicial. (`71b16bc` — Amwt24)

### Changed
- (Versión inicial — sin cambios semánticos; solo estructura y primer despliegue)

### Fixed
- Fix: corrección del problema de arranque en `app.py` antes de publicar la versión inicial. (`71b16bc`)

---

## Notas sobre las fechas de los tags
- `v1.1.0` — 2025-11-26 10:56:26 -0500  
- `v1.0.0` — 2025-11-26 04:27:01 -0500

---