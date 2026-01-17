import os

# Data Definitions

# 4to Plan Titles (Definitive List)
# 4to Plan Titles (Definitive List)
# 4to Plan Titles (Definitive List from User Step 863)
plan_4_titles = [
    "INTRODUCCIÓN A LA BIODESPROGRAMACIÓN",
    "LA NUEVA MEDICINA GERMÁNICA I",
    "LA NUEVA MEDICINA GERMÁNICA II",
    "BIOPSICOLOGÍA",
    "ÓRGANOS Y EMOCIONES I: CONFLICTO POR CAPAS EMBRIONARIAS",
    "ÓRGANOS Y EMOCIONES II: CONFLICTO POR CAPAS EMBRIONARIAS",
    "ÓRGANOS Y EMOCIONES III: CONFLICTO POR CAPAS EMBRIONARIAS",
    "CONFLICTOS DE COMPORTAMIENTO I",
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

# 3er Plan Titles (Definitive List from User Step 863)
plan_3_titles = [
    "INTRODUCCIÓN A LA BIODESPROGRAMACIÓN",
    "LA NUEVA MEDICINA GERMÁNICA I",
    "LA NUEVA MEDICINA GERMÁNICA II",
    "ANATOMIA",
    "BIOPSICOLOGÍA",
    "ÓRGANOS Y EMOCIONES I: CONFLICTO POR CAPAS EMBRIONARIAS",
    "ÓRGANOS Y EMOCIONES II: CONFLICTO POR CAPAS EMBRIONARIAS",
    "CONFLICTOS DE COMPORTAMIENTO I",
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

def get_url(plan_type, index):
    # index is 0-based
    module_num = index + 1
    
    if plan_type == "4to":
        # 4to Plan Table Mapping:
        # 1-3: 3100, 3200, 3300
        # 4: Bio -> 3400
        # 5: Org I -> 3500
        # 6: Org II -> 3600
        # 7: Org III -> 3700
        # 8: Conflictos I -> 3800
        # 9: Conflictos II -> 3900
        # 10: Tipos -> 31000
        # ... Sequential
        # NOTE: 1-4 are sequential 3100-3400.
        # 5 is 3500.
        # So 4to plan is purely sequential logic for the URL number?
        # Let's check:
        # 1->3100. 2->3200. 3->3300. 4->3400. 5->3500. 6->3600. 7->3700. 8->3800.
        # Yes, 4to Plan URLs are strictly sequential based on index+1.
        return f"https://fernandosanchezinstituto.com.mx/curso/3{module_num}00/"

    elif plan_type == "3er":
        # 3er Plan Table Mapping:
        # 1: Intro -> 3100
        # 2: NMG I -> 3200
        # 3: NMG II -> 3300
        # 4: Anatomia -> 3500 (Override)
        # 5: Bio -> 3400 (Override)
        # 6: Org I -> 3600
        # 7: Org II -> 3700
        # 8: Conflictos I -> 3800
        # ...
        # So 1-3 sequential.
        # 4 is 3500.
        # 5 is 3400.
        # 6 is 3600.
        # 7 is 3700.
        # 8 is 3800.
        # So essentially, apart from 4 and 5 swapping URLs, it follows the module_num pattern.
        
        if module_num == 4: return "https://fernandosanchezinstituto.com.mx/curso/3500/"
        if module_num == 5: return "https://fernandosanchezinstituto.com.mx/curso/3400/"
        
        return f"https://fernandosanchezinstituto.com.mx/curso/3{module_num}00/"

    return "#"



def get_header_html(plan_name):
    return f"""<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>
<style>
    @keyframes blob {{
        0% {{ transform: translate(0px, 0px) scale(1); }}
        33% {{ transform: translate(30px, -50px) scale(1.1); }}
        66% {{ transform: translate(-20px, 20px) scale(0.9); }}
        100% {{ transform: translate(0px, 0px) scale(1); }}
    }}
    .animate-blob {{
        animation: blob 7s infinite;
    }}
    .animation-delay-2000 {{
        animation-delay: 2s;
    }}
    .animation-delay-4000 {{
        animation-delay: 4s;
    }}
</style>

<div class="bg-white rounded-2xl shadow-lg border border-gray-100 p-6 md:p-8 relative overflow-hidden">
    <!-- Dynamic Background Elements -->
    <div class="absolute inset-0 overflow-hidden rounded-2xl pointer-events-none">
        <div class="absolute top-0 left-0 -ml-10 -mt-10 w-64 h-64 bg-blue-100 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob"></div>
        <div class="absolute top-0 right-0 -mr-10 -mt-10 w-64 h-64 bg-purple-100 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob animation-delay-2000"></div>
        <div class="absolute -bottom-32 left-20 w-64 h-64 bg-pink-100 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob animation-delay-4000"></div>
    </div>

    <!-- Header -->
    <div class="relative z-10 text-center mb-8">
        <span class="inline-block px-3 py-1 bg-white/80 backdrop-blur-sm border border-blue-100 text-[#233878] text-xs font-bold rounded-full uppercase tracking-wide mb-3 shadow-sm">
            Diplomado en Biodesprogramación
        </span>
        <h2 class="text-2xl md:text-3xl font-bold text-gray-800 leading-tight">
            Materias <span class="text-sm font-normal text-gray-400 block md:inline-block md:ml-2">({plan_name})</span>
        </h2>
        <p class="text-gray-500 text-sm mt-3 max-w-2xl mx-auto">
            Dentro de la materia podrás encontrar los 4 pasos para concluir satisfactoriamente la materia.
        </p>
    </div>

    <!-- Warning Alert -->
    <div class="relative z-10 bg-amber-50/90 backdrop-blur-sm border-l-4 border-amber-400 p-4 mb-8 rounded-r-lg max-w-3xl mx-auto shadow-sm">
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
    <div class="relative z-10 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
"""

footer_html = """
    </div>
</div>
"""

def generate_html(titles, filename, plan_name):
    content = get_header_html(plan_name)
    
    # Clean check for url logic
    clean_type = "4to" if "4to" in plan_name else "3er"

    colors = [
        {'border': 'border-pink-500', 'text': 'text-pink-600', 'bg': 'bg-pink-100', 'hover_border': 'hover:border-pink-300'}, 
        {'border': 'border-blue-500', 'text': 'text-[#233878]', 'bg': 'bg-blue-100', 'hover_border': 'hover:border-blue-300'}, 
        {'border': 'border-purple-500', 'text': 'text-purple-600', 'bg': 'bg-purple-100', 'hover_border': 'hover:border-purple-300'}, 
        {'border': 'border-indigo-500', 'text': 'text-indigo-600', 'bg': 'bg-indigo-100', 'hover_border': 'hover:border-indigo-300'},
        {'border': 'border-teal-500', 'text': 'text-teal-600', 'bg': 'bg-teal-100', 'hover_border': 'hover:border-teal-300'},
        {'border': 'border-amber-500', 'text': 'text-amber-600', 'bg': 'bg-amber-100', 'hover_border': 'hover:border-amber-300'}
    ]

    for i, title in enumerate(titles):
        url = get_url(clean_type, i)
        module_num = i + 1
        
        # Color Cycle
        c = colors[i % len(colors)]
        
        # Consistent Card HTML with User's Design
        item_html = f'''
        <a href="{url}" target="_blank" class="group relative bg-white rounded-xl border border-gray-200 p-5 hover:shadow-xl transition-all duration-300 flex flex-col h-full overflow-hidden border-t-4 {c['border']} {c['hover_border']}">
            <!-- Hover Gradient Background -->
            <div class="absolute inset-0 bg-gradient-to-br from-blue-50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            
            <div class="relative z-10 flex items-start justify-between mb-3">
                 <div class="w-8 h-8 rounded-lg {c['bg']} {c['text']} flex items-center justify-center font-bold text-sm group-hover:bg-[#233878] group-hover:text-white transition-colors">
                    {module_num}
                </div>
                <!-- Status Dot -->
                <div class="w-2 h-2 rounded-full bg-gray-300 group-hover:bg-green-400 transition-colors"></div>
            </div>
            
            <div class="relative z-10 flex-1">
                <h3 class="text-xs md:text-sm font-bold text-gray-800 leading-snug group-hover:text-[#233878] transition-colors mb-2 uppercase">
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
        '''
        content += item_html
    
    content += footer_html
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

# Generate files
base_path = "/Users/maximilianocalva/Documents/GitHub/IDEBIO/panel.fernandosanchezinstituto.com.mx/Dashboard/Seccion 03/Hub-Materias/"
os.makedirs(base_path, exist_ok=True)

generate_html(plan_4_titles, os.path.join(base_path, "snippet-hub-materias-4to-plan.html"), "4to Plan")
generate_html(plan_3_titles, os.path.join(base_path, "snippet-hub-materias-3er-plan.html"), "3er Plan")

print("Files generated successfully.")
