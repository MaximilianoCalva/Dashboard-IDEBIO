function doGet() {
    // 1. Intentar servir desde caché primero (Ultra-rápido)
    const cache = CacheService.getScriptCache();
    const cachedData = cache.get("ALL_SHEETS_JSON_V2");

    if (cachedData != null) {
        return ContentService.createTextOutput(cachedData)
            .setMimeType(ContentService.MimeType.JSON);
    }

    // 2. Si no hay caché, leer Google Sheets (Más lento, pero solo pasa cada 25 mins)
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const sheets = ss.getSheets();
    const responseObj = {};

    sheets.forEach(sheet => {
        const sheetName = sheet.getName();
        const data = sheet.getDataRange().getValues();

        if (data.length > 1) { // Solo si tiene datos más allá de la cabecera
            const headers = data.shift(); // Quitar cabecera

            // Mapear filas a objetos
            const rows = data.map(row => {
                return {
                    titulo: row[0],
                    vimeoUrl: row[1],
                    fecha: row[2] instanceof Date ? Utilities.formatDate(row[2], "GMT", "dd/MM/yyyy") : row[2],
                    profesor: row[3]
                };
            }).reverse(); // El más nuevo arriba

            responseObj[sheetName] = rows;
        }
    });

    const jsonString = JSON.stringify(responseObj);

    // 3. Guardar en caché por 1500 segundos (25 minutos)
    cache.put("ALL_SHEETS_JSON_V2", jsonString, 1500);

    return ContentService.createTextOutput(jsonString)
        .setMimeType(ContentService.MimeType.JSON);
}