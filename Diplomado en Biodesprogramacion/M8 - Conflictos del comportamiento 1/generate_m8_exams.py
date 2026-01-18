import os

# Data Definitions
# Request 1: Lenguaje Corporal
exams_lenguaje = [
    {
        "title": "EXAMEN: LENGUAJE CORPORAL",
        "url": "https://fernandosanchezinstituto.com.mx/examen-lenguaje-corporal/"
    }
]

# Request 2: Conflictos de Comportamiento I (5 exams)
exams_conflictos = [
    {
        "title": "EXAMEN: CONFLICTOS DE COMPORTAMIENTO",
        "url": "https://fernandosanchezinstituto.com.mx/examen-conflictos-de-comportamiento/"
    },
    {
        "title": "EXAMEN: CONFLICTOS DE COMPORTAMIENTO CASO 1",
        "url": "https://fernandosanchezinstituto.com.mx/examen-conflictos-de-comportamiento-caso-1/"
    },
    {
        "title": "EXAMEN: CONFLICTOS DE COMPORTAMIENTO CASO 2",
        "url": "https://fernandosanchezinstituto.com.mx/examen-conflictos-de-comportamiento-caso-2/"
    },
    {
        "title": "EXAMEN: CONFLICTOS DE COMPORTAMIENTO CASO 3",
        "url": "https://fernandosanchezinstituto.com.mx/examen-conflictos-de-comportamiento-caso-3/"
    },
    {
        "title": "EXAMEN: CONFLICTOS DE COMPORTAMIENTO CASO 4",
        "url": "https://fernandosanchezinstituto.com.mx/examen-conflictos-de-comportamiento-caso-4/"
    }
]

# HTML Template Generator
def generate_html(exams, title_text, exams_count_text):
    html_content = f"""<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>

<div class="bg-white rounded-2xl shadow-lg border border-gray-100 p-5 md:p-6 relative overflow-hidden group hover:border-blue-200 transition-all duration-300">
    <!-- Decorative background element -->
    <div class="absolute top-0 right-0 -mr-16 -mt-16 w-48 h-48 rounded-full bg-blue-50 opacity-50 blur-3xl group-hover:bg-blue-100 transition-colors"></div>

    <div class="relative z-10 flex flex-col">
        <!-- Header with Icon -->
        <div class="flex items-start justify-between mb-4">
            <div>
                <span class="inline-block px-2.5 py-0.5 bg-blue-100 text-[#233878] text-[10px] md:text-xs font-bold rounded-full uppercase tracking-wide mb-1.5">
                    Evaluaciones
                </span>
                <h2 class="text-lg md:text-2xl font-bold text-gray-800 leading-tight">
                    {title_text} <br>
                    <span class="text-[#233878]">{exams_count_text}</span>
                </h2>
                <p class="text-sm text-gray-500 mt-1">Selecciona el examen para entrar</p>
            </div>
            <div class="w-10 h-10 md:w-12 md:h-12 rounded-xl bg-blue-50 text-[#233878] flex items-center justify-center shadow-sm shrink-0">
                <!-- Exam/List Icon -->
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
                </svg>
            </div>
        </div>

        <!-- Scrollable List -->
        <div class="overflow-y-auto max-h-[400px] pr-2 space-y-2 custom-scrollbar">
"""
    items_html = ""
    for i, exam in enumerate(exams):
        # Alternate background slightly for readability
        bg_class = "bg-gray-50 hover:bg-blue-50" if i % 2 == 0 else "bg-white hover:bg-blue-50"
        
        item = f"""
            <a href="{exam['url']}" target="_blank" class="block {bg_class} border border-gray-100 rounded-lg p-3 transition-colors group/item">
                <div class="flex items-center gap-3">
                    <div class="w-6 h-6 rounded-full bg-blue-100 text-[#233878] flex items-center justify-center font-bold text-[10px] shrink-0 group-hover/item:bg-[#233878] group-hover/item:text-white transition-colors">
                        {i+1}
                    </div>
                    <div class="flex-1">
                        <h4 class="text-xs md:text-sm font-medium text-gray-700 group-hover/item:text-[#233878] transition-colors">
                            {exam['title']}
                        </h4>
                    </div>
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400 group-hover/item:text-[#233878] transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                    </svg>
                </div>
            </a>
        """
        items_html += item

    footer_content = """
        </div>
    </div>
</div>

<style>
    .custom-scrollbar::-webkit-scrollbar {
        width: 6px;
    }
    .custom-scrollbar::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 4px;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb:hover {
        background: #94a3b8;
    }
</style>
"""
    return html_content + items_html + footer_content

# Main execution
base_path = os.path.dirname(os.path.abspath(__file__))
# Navigate up 2 levels to reach panel root, then into Examenes
output_dir = os.path.abspath(os.path.join(base_path, "..", "..", "Examenes"))
os.makedirs(output_dir, exist_ok=True)

# Generate Snippet 1: Lenguaje Corporal
output_file_1 = os.path.join(output_dir, "snippet-examenes-lenguaje-corporal.html")
html_1 = generate_html(exams_lenguaje, "Esta materia contiene:", "1 examen")
with open(output_file_1, "w", encoding="utf-8") as f:
    f.write(html_1)
print(f"Generated: {output_file_1}")

# Generate Snippet 2: Conflictos de Comportamiento
output_file_2 = os.path.join(output_dir, "snippet-examenes-conflictos-comportamiento.html")
html_2 = generate_html(exams_conflictos, "Esta materia contiene:", "5 examenes")
with open(output_file_2, "w", encoding="utf-8") as f:
    f.write(html_2)
print(f"Generated: {output_file_2}")
