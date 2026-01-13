# IDEBIO - Instituto de Biodesprogramación Fernando Sánchez

## Información Institucional

**Nombre Completo:** Instituto de Biodesprogramación Fernando Sánchez  
**Acrónimo:** IDEBIO  
**Sitio Web:** https://fernandosanchezinstituto.com.mx

## SEO y Metadata

### Dashboard (Panel de Estudiantes)
**Título del Sitio:** IDEBIO - Panel de Alumnos | Instituto de Biodesprogramación Fernando Sánchez
**Descripción Corta:** Plataforma exclusiva para alumnos de IDEBIO. Accede a tus diplomados en Biodesprogramación, material de estudio y certificaciones con Fernando Sánchez.

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

**WhatsApp Soporte:** +52 1 33 1429 0988  
**URL WhatsApp:** https://wa.me/5213334054655  
**Canal WhatsApp:** https://whatsapp.com/channel/0029Vb6g37Z3bbV3WXetDx2J

## URLs del Panel

- **Web Principal:** https://fernandosanchezinstituto.com.mx
- **Iniciar Sesión:** https://fernandosanchezinstituto.com.mx/iniciar-sesion/
- **Dashboard:** https://fernandosanchezinstituto.com.mx/panel-access/
- **Logout:** https://fernandosanchezinstituto.com.mx/panel-access/?action=logout&redirect_to=https%3A%2F%2Ffernandosanchezinstituto.com.mx

## Componentes: Headers & Navegación

### Headers (Optimizados Tablet/Mobile 1024px)
Sistema de headers responsivos con menú hamburguesa para dispositivos con ancho menor a 1024px (tablets y móviles).

#### 1. Header Logged In (Usuario Autenticado)
**Archivo:** `Header/header-logged-in-IDEBIO.html`

- **Marca:** Logo/Texto "IDEBIO" clickeable (redirige al home).
- **Desktop (>1024px):** Botones visibles:
  - 📊 Dashboard
  - 💬 Soporte (WhatsApp)
  - 🚪 Cerrar Sesión
- **Tablet/Móvil (≤1024px):** Menú hamburguesa lateral con overlay.

#### 2. Header Logged Out (Usuario No Autenticado)
**Archivo:** `Header/header-logged-out-IDEBIO.html`

- **Marca:** Logo/Texto clickeable.
- **Acción:** Botón "Acceso a tu diplomado".
- **Responsive:** Menú hamburguesa en tablet/móvil.

#### 3. Header Web Principal
**Archivo:** `header-idebio.html` (en repo web)
- Navegación completa del sitio web.
- Breakpoint 1024px para menú móvil.

### Implementación Técnica
- **Breakpoint JS/CSS:** 1024px.
- **Z-Index:** Header (1000), Overlay (998), Menú Lateral (999).
- **Scripts:** Auto-cierre al redimensionar a desktop y tecla ESC.

---

## Estructura de Sección Inicio (Dashboard)

La sección inicio está organizada en **13 componentes**:

### 1️⃣ Header y Bienvenida
- **01-dashboard-inicio-IDEBIO.html** - Título "DASHBOARD".
- **02-bienvenida-IDEBIO.html** - Mensaje de bienvenida.

### 2️⃣ Avisos y Accesos
- **03-aviso-admin-docentes-IDEBIO.html** 👥 - Aviso docentes.
- **04-accesos-rapidos-IDEBIO.html** ⚡ - Accesos rápidos.
- **05-aviso-solo-visualizacion-IDEBIO.html** 👁️ - Solo visualización.
- **06-reglamento-IDEBIO.html** - Reglamento.
- **07-plataforma-inactiva-IDEBIO.html** - Aviso inactiva.

### 3️⃣ Sección Administrativa
- **08-aviso-solo-administrativos-IDEBIO.html** 🔒 - Aviso admin.
- **09-informacion-chatbot-IDEBIO.html** - Chatbot.
- **10-oferta-activa-IDEBIO.html** - Tabla oferta activa.
- **11-requisiciones-IDEBIO.html** 📋 - Formularios requisiciones.
- **12-correos-activos-IDEBIO.html** 📧 - Correos activos.

### 4️⃣ Sección Estudiantil
- **13-aviso-dashboard-estudiantil-IDEBIO.html** 📚 - Aviso estudiantil.

---

## Recursos Adicionales (Extras)

### Carpeta: `Extras/`
**Archivo principal:** `extras-grid-idebio.html`

Grid de recursos con 6 secciones:
1. ⭐ Evaluación Docente
2. ❓ Dudas Frecuentes
3. 🏥 Consultorio
4. 📖 Biodiccionario
5. 📚 Bioteca
6. 🎥 Videoteca

---

## 🛠️ Cómo Usar en Elementor

1. **Editar Página**: Usar Elementor.
2. **Widget HTML**: Arrastrar widget HTML.
3. **Pegar Código**: Copiar TODO el contenido del archivo HTML (incluyendo `<style>` y `<script>`).
4. **Guardar**: Publicar cambios.

---

**Versión:** 4.0 (Update Headers 1024px)
**Fecha:** Enero 2026
