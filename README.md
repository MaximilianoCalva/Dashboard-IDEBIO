# IDEBIO - Instituto de Biodesprogramación Fernando Sánchez

## Información Institucional

**Nombre Completo:** Instituto de Biodesprogramación Fernando Sánchez  
**Acrónimo:** IDEBIO  
**Sitio Web:** https://fernandosanchezinstituto.com.mx

## SEO y Metadata

### Dashboard (Panel de Estudiantes)
**Título del Sitio:** IDEBIO - Mi Dashboard | Plataforma de Aprendizaje  
**Descripción Corta:** Accede a tu plataforma de aprendizaje de Biodesprogramación. Consulta tus cursos, diplomados, certificados y avanza en tu formación profesional con IDEBIO.

## Colores Institucionales

### Paleta de Colores
- **Azul Primario Oscuro:** `#233878`
- **Azul Primario Medio:** `#2863A4`
- **Azul Primario Claro:** `#3A7BC8`
- **Gradiente Principal:** `linear-gradient(135deg, #233878 0%, #2863A4 100%)`

### Colores de Sistema
- **Blanco:** `#FFFFFF`
- **Gris Claro:** `#F5F5F5`
- **Éxito (Verde):** `#10b981`
- **Advertencia (Amarillo):** `#f59e0b`
- **Peligro (Rojo):** `#ef4444`

## Contacto

**WhatsApp Soporte:** +52 1 33 3405 4655  
**URL WhatsApp:** https://wa.me/5213334054655  
**Canal WhatsApp:** https://whatsapp.com/channel/0029Vb6g37Z3bbV3WXetDx2J

## Redes Sociales

**Imagen de Cuentas Oficiales:** https://fernandosanchezinstituto.com.mx/wp-content/uploads/2023/08/Cuentas-reales-Post-03.jpg

## URLs del Panel

- **Mi Cuenta:** https://fernandosanchezinstituto.com.mx/mi-cuenta/
- **Iniciar Sesión:** https://fernandosanchezinstituto.com.mx/iniciar-sesion/
- **Panel Access:** https://fernandosanchezinstituto.com.mx/panel-access/
- **Logout:** https://fernandosanchezinstituto.com.mx/panel-access/?action=logout&redirect_to=https%3A%2Ffernandosanchezinstituto.com.mx

## Recursos Visuales

### Logo
**URL:** https://fernandosanchezinstituto.com.mx/wp-content/uploads/2021/06/Recurso-3-scaled.png

### Dimensiones del Logo
- **Desktop:** 30px altura
- **Mobile:** 25px altura
- **Max Width:** 150px

## Componentes del Dashboard

### Headers
- `Header/header-logged-in-IDEBIO.html` - Header para usuarios autenticados
- `Header/header-logged-out-IDEBIO.html` - Header para usuarios no autenticados

### Especificaciones del Header
- **Padding:** 3px 10px
- **Ancho:** 100% (full width)
- **Altura Mínima:** 50px
- **Font Size Brand:** 18px (desktop), 16px (mobile)
- **Font Size Subtitle:** 9px (desktop), 8px (mobile)

## Notas de Diseño

- Los headers usan texto "IDEBIO" en lugar de logo
- El texto del brand usa el gradiente institucional
- Diseño responsive con breakpoints en 768px y 480px
- Botones compactos con iconos de 14px
- Sombras suaves con opacidad del color institucional

---

## 🛠️ Plataforma y Tecnología

### Stack Tecnológico
- **CMS**: WordPress
- **LMS**: LearnDash / Tutor LMS
- **Constructor**: Elementor Pro
- **Hosting**: https://fernandosanchezinstituto.com.mx

### Implementación de Componentes HTML

Todos los componentes HTML de este proyecto están diseñados para ser implementados en **Elementor** usando el widget HTML.

#### Cómo Usar en Elementor:

1. **Editar Página/Template**
   - Ir a la página del dashboard que deseas editar
   - Abrir con Elementor

2. **Agregar Widget HTML**
   - Buscar "HTML" en el panel de widgets de Elementor
   - Arrastrar el widget a la sección deseada

3. **Copiar y Pegar Código**
   - Abrir el archivo HTML del componente
   - Copiar TODO el contenido (incluyendo `<style>` y `<script>`)
   - Pegar en el widget HTML de Elementor

4. **Guardar y Publicar**
   - Guardar cambios en Elementor
   - Publicar la página

#### Componentes Disponibles:

**Headers**:
- `Header/header-logged-in-IDEBIO.html` - Header para usuarios autenticados
- `Header/header-logged-out-IDEBIO.html` - Header para usuarios no autenticados

**Sección Inicio**:
- `Seccion inicio/01-dashboard-inicio-IDEBIO.html` - Cápsula de bienvenida
- `Seccion inicio/02-bienvenida-IDEBIO.html` - Mensaje de bienvenida (si existe)
- `Seccion inicio/03-reglamento-IDEBIO.html` - Reglamento institucional
- `Seccion inicio/04-plataforma-inactiva-IDEBIO.html` - Mensaje de plataforma inactiva
- `Seccion inicio/05-informacion-chatbot-IDEBIO.html` - Información del chatbot
- `Seccion inicio/06-oferta-activa-IDEBIO.html` - Ofertas activas
- `Seccion inicio/07-accesos-rapidos-IDEBIO.html` - Accesos rápidos

**Extras**:
- `Extras/extras-grid-idebio.html` - Grid de recursos adicionales

**Footer**:
- `Footer/footer-dashboard-idebio-snippet.html` - Footer del dashboard

**Acceso**:
- `Acceso a dashboard/login-idebio-snippet.html` - Página de login
- `Acceso a dashboard/logout-idebio-snippet.html` - Página de logout

---

## Última Actualización

Fecha: 2025-12-30  
Versión: 1.0

## Archivos de Acceso al Dashboard

### Carpeta: `Acceso a dashboard/`

**Para usuarios autenticados (logged-in):**
- `login-idebio-snippet.html` - Página de bienvenida con botón "Ir al Dashboard"
  - Redirige a: `https://fernandosanchezinstituto.com.mx/mi-cuenta/`

**Para usuarios NO autenticados (logged-out):**
- `logout-idebio-snippet.html` - Formulario de inicio de sesión
  - Contiene shortcode: `[profilepress-login id="1"]`
  - Incluye instrucciones para el usuario

**Uso en WordPress:**
- Copiar y pegar el contenido completo en un widget HTML de Elementor
- Los snippets no afectan el diseño de la página existente
- Usan clases CSS únicas para evitar conflictos

## Recursos Adicionales (Extras)

### Carpeta: `Extras/`

**Archivo principal:** `extras-grid-idebio.html`

Grid de recursos adicionales con 6 secciones de acceso rápido:

1. **⭐ Evaluación Docente**
   - Permite a los estudiantes evaluar a sus docentes
   - Integración con Elementor template ID: 141396
   
2. **❓ Dudas Frecuentes**
   - URL: https://fernandosanchezinstituto.com.mx/extra-dudas-frecuentes-de-alumnos-de-biodesprogramacion/
   - Respuestas a preguntas comunes de estudiantes

3. **🏥 Consultorio**
   - URL: https://fernandosanchezinstituto.com.mx/extras-consultorio/
   - Acceso al consultorio virtual

4. **📖 Biodiccionario**
   - URL: https://fernandosanchezinstituto.com.mx/Biodiccionario/
   - Diccionario especializado de Biodesprogramación

5. **📚 Bioteca**
   - URL: https://fernandosanchezinstituto.com.mx/bioteca
   - Biblioteca de recursos y materiales educativos

6. **🎥 Videoteca**
   - URL: https://fernandosanchezinstituto.com.mx/videoteca/
   - Biblioteca de videos educativos

### Diseño de Extras
- **Colores**: Gradiente azul IDEBIO (#233878 a #2863A4)
- **Layout**: Grid responsive (3 columnas desktop, 1 mobile)
- **Interactividad**: Hover effects con elevación y sombra
- **Iconos**: Emojis para identificación visual rápida
