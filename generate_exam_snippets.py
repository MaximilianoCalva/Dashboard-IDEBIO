import os

# Data Definitions
links = [
    "https://fernandosanchezinstituto.com.mx/curso/3100/",
    "https://fernandosanchezinstituto.com.mx/curso/3200/",
    "https://fernandosanchezinstituto.com.mx/curso/3300/",
    "https://fernandosanchezinstituto.com.mx/curso/3400/",
    "https://fernandosanchezinstituto.com.mx/curso/3500/",
    "https://fernandosanchezinstituto.com.mx/curso/3600/",
    "https://fernandosanchezinstituto.com.mx/curso/3700/",
    "https://fernandosanchezinstituto.com.mx/curso/3800/",
    "https://fernandosanchezinstituto.com.mx/curso/3900/",
    "https://fernandosanchezinstituto.com.mx/curso/31000/",
    "https://fernandosanchezinstituto.com.mx/curso/31100/",
    "https://fernandosanchezinstituto.com.mx/curso/31200/",
    "https://fernandosanchezinstituto.com.mx/curso/31300/",
    "https://fernandosanchezinstituto.com.mx/curso/31400/",
    "https://fernandosanchezinstituto.com.mx/curso/31500/",
    "https://fernandosanchezinstituto.com.mx/curso/31600/",
    "https://fernandosanchezinstituto.com.mx/curso/31700/",
    "https://fernandosanchezinstituto.com.mx/curso/31800/",
    "https://fernandosanchezinstituto.com.mx/curso/31900/",
    "https://fernandosanchezinstituto.com.mx/curso/32000/",
    "https://fernandosanchezinstituto.com.mx/curso/32100/",
    "https://fernandosanchezinstituto.com.mx/curso/32200/",
    "https://fernandosanchezinstituto.com.mx/curso/32300/",
    "https://fernandosanchezinstituto.com.mx/curso/32400/"
]

plan_4_titles = [
    "INTRODUCCIÓN A LA BIODESPROGRAMACIÓN",
    "LA NUEVA MEDICINA GERMÁNICA 1",
    "LA NUEVA MEDICINA GERMÁNICA 2",
    "BIOPSICOLOGÍA",
    "ÓRGANOS Y EMOCIONES: CONFLICTO POR CAPAS EMBRIONARIAS",
    "ÓRGANOS Y EMOCIONES II: CONFLICTO POR CAPAS EMBRIONARIAS",
    "ÓRGANOS Y EMOCIONES III: CONFLICTO POR CAPAS EMBRIONARIAS",
    "CONFLICTOS DE COMPORTAMIENTO",
    "CONFLICTOS DE COMPORTAMIENTO II",
    "TIPOS DE CUERPO Y ALIMENTOS EN BIODESPROGRAMACIÓN",
    "PROYECTO SENTIDO",
    "ÁRBOL TRANSGENERACIONAL",
    "ACOMPAÑAMIENTO AL INCONSCIENTE PARA LA BIODESPROGRAMACIÓN",
    "PRINCIPIOS DE PNL",
    "PNL E HIPNOSIS",
    "HIPNOSIS",
    "PROTOCOLOS: ACTOS SIMBÓLICOS",
    "ADICCIONES Y SUICIDIOS EN BIODESPROGRAMACIÓN",
    "AMOR Y RELACIONES",
    "ABUNDANCIA Y PROSPERIDAD",
    "CONFLICTOS BUCALES EN BIODESPROGRAMACIÓN",
    "LENGUAJE CORPORAL",
    "ANÁLISIS DEL ROSTRO Y CUERPO",
    "COACHING APLICADO A LA BIODESPROGRAMACIÓN"
]

plan_3_titles = [
    "INTRODUCCIÓN A LA BIODESPROGRAMACIÓN",
    "LA NUEVA MEDICINA GERMÁNICA 1",
    "LA NUEVA MEDICINA GERMÁNICA 2",
    "BIOPSICOLOGÍA",
    "ÓRGANOS Y EMOCIONES I: CONFLICTO POR CAPAS EMBRIONARIAS",
    "ÓRGANOS Y EMOCIONES II: CONFLICTO POR CAPAS EMBRIONARIAS",
    "ÓRGANOS Y EMOCIONES III: CONFLICTO POR CAPAS EMBRIONARIAS",
    "CONFLICTOS DE COMPORTAMIENTO",
    "CONFLICTOS DE COMPORTAMIENTO II",
    "TIPOS DE CUERPO Y ALIMENTOS EN BIODESPROGRAMACIÓN",
    "PROYECTO SENTIDO",
    "ÁRBOL TRANSGENERACIONAL",
    "ACOMPAÑAMIENTO AL INCONSCIENTE PARA LA BIODESPROGRAMACIÓN",
    "PRINCIPIOS DE PNL",
    "PNL E HIPNOSIS",
    "HIPNOSIS",
    "PROTOCOLOS: ACTOS SIMBÓLICOS",
    "ADICCIONES Y SUICIDIOS EN BIODESPROGRAMACIÓN",
    "AMOR Y RELACIONES",
    "ABUNDANCIA Y PROSPERIDAD",
    "CONFLICTOS BUCALES EN BIODESPROGRAMACIÓN",
    "LENGUAJE CORPORAL",
    "ANÁLISIS DEL ROSTRO Y CUERPO",
    "COACHING APLICADO A LA BIODESPROGRAMACIÓN"
]

# HTML Template for Module Hub (Grid)
template_header_4to = """<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>

<div class="bg-white rounded-2xl shadow-lg border border-gray-100 p-6 md:p-8">
    <!-- Header -->
    <div class="text-center mb-8">
        <span class="inline-block px-3 py-1 bg-blue-100 text-[#233878] text-xs font-bold rounded-full uppercase tracking-wide mb-3">
            Diplomado en Biodesprogramación
        </span>
        <h2 class="text-2xl md:text-3xl font-bold text-gray-800 leading-tight">
            Materias
        </h2>
        <p class="text-gray-500 text-sm mt-3 max-w-2xl mx-auto">
            Dentro de la materia podrás encontrar los 4 pasos para concluir satisfactoriamente la materia.
        </p>
    </div>

    <!-- Warning Alert -->
    <div class="bg-amber-50 border-l-4 border-amber-400 p-4 mb-8 rounded-r-lg max-w-3xl mx-auto">
        <div class="flex items-center justify-center">
             <svg class="h-5 w-5 text-amber-400 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
            <p class="text-sm font-bold text-amber-900">
                Fecha límite: Día 15 de cada mes
            </p>
        </div>
    </div>

    <!-- Grid Container -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
"""

template_header_3er = template_header_4to.replace("4to Plan", "3er Plan")

template_footer = """
    </div>
</div>
"""

def generate_html(titles, filename, header_template):
    content = header_template
    for i, title in enumerate(titles):
        url = links[i]
        module_num = i + 1
        
        # Card HTML
        item_html = f"""
        <a href="{url}" target="_blank" class="group relative bg-white rounded-xl border border-gray-200 p-5 hover:shadow-xl hover:border-blue-200 transition-all duration-300 flex flex-col h-full overflow-hidden">
            <!-- Hover Gradient Background -->
            <div class="absolute inset-0 bg-gradient-to-br from-blue-50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            
            <div class="relative z-10 flex items-start justify-between mb-3">
                 <div class="w-8 h-8 rounded-lg bg-blue-100 text-[#233878] flex items-center justify-center font-bold text-sm group-hover:bg-[#233878] group-hover:text-white transition-colors">
                    {module_num}
                </div>
                <!-- Status Dot (Visual only) -->
                <div class="w-2 h-2 rounded-full bg-gray-300 group-hover:bg-green-400 transition-colors"></div>
            </div>
            
            <div class="relative z-10 flex-1">
                <h3 class="text-sm font-bold text-gray-800 leading-snug group-hover:text-[#233878] transition-colors mb-2">
                    {title}
                </h3>
            </div>
            
            <div class="relative z-10 mt-4 flex items-center text-xs font-semibold text-gray-400 group-hover:text-[#233878] transition-colors">
                <span>Realizar examen</span>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 ml-1 transform group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
            </div>
        </a>
        """
        content += item_html
    content += template_footer
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

# Generate files
base_path = "/Users/maximilianocalva/Documents/GitHub/IDEBIO/panel.fernandosanchezinstituto.com.mx/Dashboard/Seccion 03/Hub-Materias/"

# Ensure directory exists
os.makedirs(base_path, exist_ok=True)

generate_html(plan_4_titles, os.path.join(base_path, "snippet-hub-materias-4to-plan.html"), template_header_4to)
generate_html(plan_3_titles, os.path.join(base_path, "snippet-hub-materias-3er-plan.html"), template_header_3er)

print("Files generated successfully.")
