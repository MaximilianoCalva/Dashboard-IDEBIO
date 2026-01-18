import os

# Data Definitions
snippets_data = [
    {
        "filename": "snippet-paso-3-foro.html",
        "title": "Paso 3 de 4: Participa en tu foro",
        "subtitle": "Tu participación en foro forma el 20% de tu calificación total",
        "content": [
            "La información para participar en tu foro será proporcionado por tu docente",
        ],
        "button_text": "Selecciona aquí para entrar a tu apartado de Foro",
        "button_url": "https://fernandosanchezinstituto.com.mx/foros/",
        "icon": "chat",
        "type": "info"
    },
    {
        "filename": "snippet-paso-4-trabajo-final.html",
        "title": "Paso 4 de 4: Entrega tu trabajo final",
        "subtitle": "Último paso",
        "content": [
            "Tu entrega de trabajo final forma el 20% de tu calificación total.",
            "La validez de tu trabajo final estará condicionada únicamente a su envío a través de la plataforma designada. Cualquier otro medio de entrega no será considerado como válido para la evaluación del trabajo. Asegúrese de seguir las instrucciones detalladas y utilizar exclusivamente la plataforma indicada para garantizar la aceptación y consideración adecuada de su trabajo final.",
            "El periodo de evaluación de tu trabajo final es del día 21 al día 26 de cada mes.",
            "Al enviar tu trabajo final a través de la plataforma designada, recibirás una confirmación por correo electrónico. La evaluación de tu trabajo se llevará a cabo durante el periodo comprendido entre el día 21 y el día 26 de cada mes. Asegúrate de estar atento a tu correo electrónico para verificar la recepción de tu documento y ten en cuenta el plazo establecido para la evaluación."
        ],
        "button_text": "",
        "button_url": "",
        "icon": "document",
        "type": "warning"
    },
    {
        "filename": "snippet-apartado-abierto.html",
        "title": "Apartado abierto",
        "subtitle": "",
        "content": [
            "El periodo de entrega de trabajo final es del día 10 al día 20 de cada mes",
            "Es tiempo de enviar tu trabajo final"
        ],
        "button_text": "Selecciona aquí para crear o enviar tu trabajo final",
        "button_url": "https://fernandosanchezinstituto.com.mx/trabajo-final/",
        "icon": "check",
        "type": "success"
    },
    {
        "filename": "snippet-apartado-cerrado.html",
        "title": "Apartado cerrado",
        "subtitle": "",
        "content": [
            "El periodo de envío de tu trabajo final es del día 10 al 20 de cada mes"
        ],
        "button_text": "",
        "button_url": "",
        "icon": "lock",
        "type": "error"
    }
]

def get_icon_svg(icon_name):
    if icon_name == "chat":
        return """<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z" />
</svg>"""
    elif icon_name == "document":
        return """<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
</svg>"""
    elif icon_name == "check":
        return """<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
</svg>"""
    elif icon_name == "lock":
        return """<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
</svg>"""
    return ""

def get_colors(type):
    if type == "info":
        return "bg-blue-50 border-blue-100", "text-[#233878]", "bg-blue-100", "text-blue-600"
    elif type == "warning":
        return "bg-amber-50 border-amber-100", "text-amber-800", "bg-amber-100", "text-amber-600"
    elif type == "success":
        return "bg-green-50 border-green-100", "text-green-800", "bg-green-100", "text-green-600"
    elif type == "error":
        return "bg-red-50 border-red-100", "text-red-800", "bg-red-100", "text-red-600"
    else: # default
         return "bg-white border-gray-100", "text-gray-800", "bg-gray-100", "text-gray-600"


def generate_snippet(data, output_path):
    card_bg, title_color, icon_bg, icon_color = get_colors(data["type"])
    
    content_html = ""
    for paragraph in data["content"]:
        content_html += f'<p class="text-sm md:text-base text-gray-600 mb-3 last:mb-0 leading-relaxed">{paragraph}</p>'

    button_html = ""
    if data["button_text"] and data["button_url"]:
        button_html = f"""
        <div class="mt-6">
            <a href="{data["button_url"]}" target="_blank" class="inline-flex items-center justify-center px-6 py-3 border border-transparent text-sm font-medium rounded-lg text-white bg-[#233878] hover:bg-blue-800 transition-colors shadow-sm w-full md:w-auto">
                {data["button_text"]}
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
            </a>
        </div>
        """

    html_content = f"""<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>

<div class="{card_bg} rounded-2xl shadow-sm border p-6 md:p-8 relative overflow-hidden group hover:shadow-md transition-all duration-300">
    <div class="flex items-start gap-5">
        <div class="{icon_bg} {icon_color} w-12 h-12 rounded-xl flex items-center justify-center shrink-0 shadow-sm">
            {get_icon_svg(data["icon"])}
        </div>
        
        <div class="flex-1">
            <h2 class="text-xl md:text-2xl font-bold {title_color} mb-1">{data["title"]}</h2>
            {f'<h3 class="text-sm font-semibold uppercase tracking-wider text-gray-500 mb-4">{data["subtitle"]}</h3>' if data["subtitle"] else '<div class="mb-2"></div>'}
            
            <div class="prose prose-blue max-w-none">
                {content_html}
            </div>

            {button_html}
        </div>
    </div>
</div>
"""
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated: {output_path}")

# Main execution
base_path = "/Users/maximilianocalva/Documents/GitHub/IDEBIO/panel.fernandosanchezinstituto.com.mx/Trabajo final/"

# Create directory if it doesn't exist (just in case, though we checked)
os.makedirs(base_path, exist_ok=True)

for snippet in snippets_data:
    full_path = os.path.join(base_path, snippet["filename"])
    generate_snippet(snippet, full_path)

print("All snippets generated successfully.")
