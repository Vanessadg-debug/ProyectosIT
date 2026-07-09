## TC12 — Duplicados y faltantes
**Fecha:** 2026-07-01
**Decisión:** Filtrar lista cruda contra data_list ANTES de contar duplicados.
**Razón:** Evitar que columnas extra (ej. "Comentarios de Juan") contaminen el conteo de duplicados reales.
**Plan:**
1. Filtrar header crudo vs data_list -> separa extras (alimenta TC13) y lista limpia
2. Sobre lista limpia, usar Counter -> quedarse con count > 1 -> duplicados

**Pendiente:** data_list como parámetro explícito, no global (ver entrada de arquitectura general)

función contar_duplicados(clean_data):
    conteo = Counter(clean_data)
    duplicados = []
    para llave, valor en conteo.items():
        si valor > 1:
            agregar llave a duplicados
    regresar duplicados

    Pendiente: normalización en header_filter
1. Si pd.isna(value) → ignorar (comportamiento actual, sin cambios)
2. Si NO es NaN → aplicar str(value).lower().strip()
3. Comparar valor ya normalizado contra data_list
Razón: TC21 (headers en mayúsculas) ya funciona en read_header,
pero falla en header_filter porque la normalización no se propaga
tras la relectura del archivo.