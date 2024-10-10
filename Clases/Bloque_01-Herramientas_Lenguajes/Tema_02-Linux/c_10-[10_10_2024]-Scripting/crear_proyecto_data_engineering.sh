#!/bin/bash

# Nombre del proyecto
proyecto="proyecto_data_engineering"

# Crear el directorio principal del proyecto
if [ ! -d "$proyecto" ]; then
  mkdir "$proyecto"
  echo "Directorio principal '$proyecto' creado."
else
  echo "El directorio principal '$proyecto' ya existe."
fi

# Crear los subdirectorios principales, incluyendo los nuevos
subdirectorios=("big_data/config" "big_data/data" "big_data/jobs" "big_data/scripts" "datos_brutos" "datos_procesados/batch" "datos_procesados/stream" "feature_engineering" "machine_learning" "machine_learning/pipelines" "machine_learning/generative_ai" "visualizations/powerbi" "docs/crisp_dm/1_comprension_negocio" "docs/crisp_dm/2_comprension_datos" "docs/crisp_dm/3_preparacion_datos" "docs/crisp_dm/4_modelado" "docs/crisp_dm/5_evaluacion" "docs/crisp_dm/6_despliegue" "scripts" "tests" "notebooks" "docs" "orquestacion" "dependencias" "logs" "configuracion" "resultados" "modelos")

for subdir in "${subdirectorios[@]}"; do
  ruta="$proyecto/$subdir"
  if [ ! -d "$ruta" ]; then
    mkdir -p "$ruta"
    echo "Subdirectorio '$subdir' creado en '$proyecto'."
  else
    echo "El subdirector...
fi

echo "Estructura de directorios para el proyecto de Data Engineering y CRISP-DM creada correctamente."

# Crear archivos de ejemplo en los nuevos subdirectorios para CRISP-DM
echo "Creando archivos de ejemplo para CRISP-DM..."

# Documentación para cada fase de CRISP-DM
crisp_dm_docs=("1_comprension_negocio/informe_comprension_negocio.md" "2_comprension_datos/informe_comprension_datos.md" "3_preparacion_datos/informe_preparacion_datos.md" "4_modelado/informe_modelado.md" "5_evaluacion/informe_evaluacion.md" "6_despliegue/informe_despliegue.md")

for doc in "${crisp_dm_docs[@]}"; do
  touch "$proyecto/docs/crisp_dm/$doc"
  echo "# Informe para ${doc//_/ }" > "$proyecto/docs/crisp_dm/$doc"
  echo "Este documento cubre la fase de ${doc//_/ }." >> "$proyecto/docs/crisp_dm/$doc"
done

echo "Archivos de ejemplo y estructura de directorios para CRISP-DM creada correctamente."
