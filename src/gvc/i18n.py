from __future__ import annotations

import os
import re
import sys

DEFAULT_LANGUAGE_LABEL = "English"

UI_TEXT = {
    "English": {
        "window_title": "Godot Video Converter",
        "add_files": "Add Files",
        "remove_selected": "Remove Selected",
        "clear": "Clear",
        "output": "Output:",
        "change_output": "Change Output",
        "open_output": "Open Output",
        "language": "Language:",
        "about": "About",
        "tab_convert": "Convert Video",
        "tab_atlas": "Generate Atlas",
        "engine_profile": "Engine Profile",
        "format": "Format",
        "quality": "Quality",
        "resolution": "Resolution",
        "keep_original": "Keep original",
        "fps": "FPS",
        "keep_audio": "Keep audio",
        "ogv_mode": "OGV mode",
        "frames": "Frames",
        "mode": "Mode",
        "backend": "Backend",
        "info_title": "Selected Video Info",
        "rec_title": "Information",
        "action_convert": "Convert Video",
        "action_atlas": "Generate Atlas",
        "cancel": "Cancel",
        "ready": "Ready",
        "done": "Done",
        "cancelled": "Cancelled",
        "cancelling": "Cancelling...",
        "operation_in_progress": "Operation in progress",
        "operation_in_progress_text": "A conversion is running. Do you want to cancel and exit?",
        "invalid_video_file": "Invalid video file: {name}",
        "no_recommendations": "No recommendations available",
        "resolution_info": "Resolution: {value}",
        "fps_info": "FPS: {value:.2f}",
        "duration_info": "Duration: {value:.2f}s",
        "video_codec_info": "Video codec: {value}",
        "audio_codec_info": "Audio codec: {value}",
        "audio_none": "Audio: none",
        "select_videos": "Select videos",
        "list_cleared": "List cleared",
        "select_output_folder": "Select output folder",
        "open_output_folder": "Open output folder",
        "open_output_folder_error": "Could not open output folder",
        "about_text": "Godot Video Converter is free and open-source software focused on video conversion and atlas generation for Godot and Love2D.\n\nVersion {version}\nDeveloper: Lextrack",
        "no_files_title": "No files",
        "no_files_text": "Add at least one video file",
        "invalid_fps_title": "Invalid FPS",
        "added_n_files": "Added {added} file(s)",
        "added_rejected": "Added {added} file(s), rejected {rejected} invalid file(s)",
        "no_valid_files_added": "No valid video files added",
        "converting_status": "Converting {index}/{total}: {name}",
        "atlas_status": "Atlas {index}/{total}: {name}",
        "ffmpeg_not_found": "FFmpeg not found",
    },
    "Español": {
        "window_title": "Godot Video Converter",
        "add_files": "Agregar Archivos",
        "remove_selected": "Eliminar Seleccionados",
        "clear": "Limpiar",
        "output": "Salida:",
        "change_output": "Cambiar Salida",
        "open_output": "Abrir Salida",
        "language": "Idioma:",
        "about": "Acerca de",
        "tab_convert": "Convertir Video",
        "tab_atlas": "Generar Atlas",
        "engine_profile": "Perfil de Motor",
        "format": "Formato",
        "quality": "Calidad",
        "resolution": "Resolución",
        "keep_original": "Mantener original",
        "fps": "FPS",
        "keep_audio": "Mantener audio",
        "ogv_mode": "Modo OGV",
        "frames": "Frames",
        "mode": "Modo",
        "backend": "Backend",
        "info_title": "Info del Video Seleccionado",
        "rec_title": "Informacion",
        "action_convert": "Convertir Video",
        "action_atlas": "Generar Atlas",
        "cancel": "Cancelar",
        "ready": "Listo",
        "done": "Terminado",
        "cancelled": "Cancelado",
        "cancelling": "Cancelando...",
        "operation_in_progress": "Operación en progreso",
        "operation_in_progress_text": "Hay una conversión en curso. ¿Quieres cancelar y salir?",
        "invalid_video_file": "Archivo de video inválido: {name}",
        "no_recommendations": "No hay recomendaciones disponibles",
        "resolution_info": "Resolución: {value}",
        "fps_info": "FPS: {value:.2f}",
        "duration_info": "Duración: {value:.2f}s",
        "video_codec_info": "Códec de vídeo: {value}",
        "audio_codec_info": "Códec de audio: {value}",
        "audio_none": "Audio: ninguno",
        "select_videos": "Seleccionar videos",
        "list_cleared": "Lista limpiada",
        "select_output_folder": "Seleccionar carpeta de salida",
        "open_output_folder": "Abrir carpeta de salida",
        "open_output_folder_error": "No se pudo abrir la carpeta de salida",
        "about_text": "Godot Video Converter es software gratuito y de codigo abierto enfocado en conversion de video y generacion de atlas para Godot y Love2D.\n\nVersion {version}\nDesarrollador: Lextrack",
        "no_files_title": "Sin archivos",
        "no_files_text": "Agrega al menos un archivo de video",
        "invalid_fps_title": "FPS inválido",
        "added_n_files": "Se agregaron {added} archivo(s)",
        "added_rejected": "Se agregaron {added} archivo(s), se rechazaron {rejected} inválidos",
        "no_valid_files_added": "No se agregaron archivos de video válidos",
        "converting_status": "Convirtiendo {index}/{total}: {name}",
        "atlas_status": "Atlas {index}/{total}: {name}",
        "ffmpeg_not_found": "FFmpeg no encontrado",
    },
    "Français": {
        "window_title": "Godot Video Converter",
        "add_files": "Ajouter des fichiers",
        "remove_selected": "Supprimer la sélection",
        "clear": "Effacer",
        "output": "Sortie :",
        "change_output": "Changer la sortie",
        "open_output": "Ouvrir la sortie",
        "language": "Langue :",
        "about": "À propos",
        "tab_convert": "Convertir la vidéo",
        "tab_atlas": "Générer un atlas",
        "engine_profile": "Profil du moteur",
        "format": "Format",
        "quality": "Qualité",
        "resolution": "Résolution",
        "keep_original": "Conserver l'original",
        "fps": "FPS",
        "keep_audio": "Conserver l'audio",
        "ogv_mode": "Mode OGV",
        "frames": "Images",
        "mode": "Mode",
        "backend": "Backend",
        "info_title": "Informations de la vidéo sélectionnée",
        "rec_title": "Informations",
        "action_convert": "Convertir la vidéo",
        "action_atlas": "Générer un atlas",
        "cancel": "Annuler",
        "ready": "Prêt",
        "done": "Terminé",
        "cancelled": "Annulé",
        "cancelling": "Annulation...",
        "operation_in_progress": "Opération en cours",
        "operation_in_progress_text": "Une conversion est en cours. Voulez-vous annuler et quitter ?",
        "invalid_video_file": "Fichier vidéo invalide : {name}",
        "no_recommendations": "Aucune recommandation disponible",
        "resolution_info": "Résolution : {value}",
        "fps_info": "FPS : {value:.2f}",
        "duration_info": "Durée : {value:.2f}s",
        "video_codec_info": "Codec vidéo : {value}",
        "audio_codec_info": "Codec audio : {value}",
        "audio_none": "Audio : aucun",
        "select_videos": "Sélectionner des vidéos",
        "list_cleared": "Liste effacée",
        "select_output_folder": "Sélectionner le dossier de sortie",
        "open_output_folder": "Ouvrir le dossier de sortie",
        "open_output_folder_error": "Impossible d'ouvrir le dossier de sortie",
        "about_text": "Godot Video Converter est un logiciel libre et open source axé sur la conversion vidéo et la génération d'atlas pour Godot et Love2D.\n\nVersion {version}\nDéveloppeur : Lextrack",
        "no_files_title": "Aucun fichier",
        "no_files_text": "Ajoutez au moins un fichier vidéo",
        "invalid_fps_title": "FPS invalide",
        "added_n_files": "{added} fichier(s) ajouté(s)",
        "added_rejected": "{added} fichier(s) ajouté(s), {rejected} fichier(s) invalide(s) rejeté(s)",
        "no_valid_files_added": "Aucun fichier vidéo valide ajouté",
        "converting_status": "Conversion {index}/{total} : {name}",
        "atlas_status": "Atlas {index}/{total} : {name}",
        "ffmpeg_not_found": "FFmpeg introuvable",
    },
    "Deutsch": {
        "window_title": "Godot Video Converter",
        "add_files": "Dateien hinzufügen",
        "remove_selected": "Auswahl entfernen",
        "clear": "Leeren",
        "output": "Ausgabe:",
        "change_output": "Ausgabe ändern",
        "open_output": "Ausgabe öffnen",
        "language": "Sprache:",
        "about": "Info",
        "tab_convert": "Video konvertieren",
        "tab_atlas": "Atlas erzeugen",
        "engine_profile": "Engine-Profil",
        "format": "Format",
        "quality": "Qualität",
        "resolution": "Auflösung",
        "keep_original": "Original beibehalten",
        "fps": "FPS",
        "keep_audio": "Audio beibehalten",
        "ogv_mode": "OGV-Modus",
        "frames": "Frames",
        "mode": "Modus",
        "backend": "Backend",
        "info_title": "Informationen zum ausgewählten Video",
        "rec_title": "Informationen",
        "action_convert": "Video konvertieren",
        "action_atlas": "Atlas erzeugen",
        "cancel": "Abbrechen",
        "ready": "Bereit",
        "done": "Fertig",
        "cancelled": "Abgebrochen",
        "cancelling": "Wird abgebrochen...",
        "operation_in_progress": "Vorgang läuft",
        "operation_in_progress_text": "Eine Konvertierung läuft gerade. Möchtest du abbrechen und beenden?",
        "invalid_video_file": "Ungültige Videodatei: {name}",
        "no_recommendations": "Keine Empfehlungen verfügbar",
        "resolution_info": "Auflösung: {value}",
        "fps_info": "FPS: {value:.2f}",
        "duration_info": "Dauer: {value:.2f}s",
        "video_codec_info": "Videocodec: {value}",
        "audio_codec_info": "Audiocodec: {value}",
        "audio_none": "Audio: keines",
        "select_videos": "Videos auswählen",
        "list_cleared": "Liste geleert",
        "select_output_folder": "Ausgabeordner auswählen",
        "open_output_folder": "Ausgabeordner öffnen",
        "open_output_folder_error": "Der Ausgabeordner konnte nicht geöffnet werden",
        "about_text": "Godot Video Converter ist freie Open-Source-Software mit Fokus auf Videokonvertierung und Atlas-Erzeugung für Godot und Love2D.\n\nVersion {version}\nEntwickler: Lextrack",
        "no_files_title": "Keine Dateien",
        "no_files_text": "Füge mindestens eine Videodatei hinzu",
        "invalid_fps_title": "Ungültige FPS",
        "added_n_files": "{added} Datei(en) hinzugefügt",
        "added_rejected": "{added} Datei(en) hinzugefügt, {rejected} ungültige Datei(en) verworfen",
        "no_valid_files_added": "Keine gültigen Videodateien hinzugefügt",
        "converting_status": "Konvertiere {index}/{total}: {name}",
        "atlas_status": "Atlas {index}/{total}: {name}",
        "ffmpeg_not_found": "FFmpeg nicht gefunden",
    },
}

LANGUAGE_LABELS = tuple(UI_TEXT.keys())
LANGUAGE_CODES = {
    "English": "en",
    "Español": "es",
    "Français": "fr",
    "Deutsch": "de",
}
REQUIRED_UI_KEYS = frozenset(UI_TEXT[DEFAULT_LANGUAGE_LABEL].keys())
_REPORTED_MISSING: set[tuple[str, str]] = set()

RECOMMENDATIONS_ES_REPLACEMENTS = {
    "Invalid video file": "Archivo de video inválido",
    "WHAT THIS VIDEO HAS": "LO QUE TIENE ESTE VIDEO",
    "RECOMMENDED NEXT STEP": "QUE TE CONVIENE HACER",
    "Short video (0-10s) - Perfect for UI animations or button effects": "Video corto (0-10s) - Perfecto para animaciones de UI o efectos de botones",
    "Use 'Ideal Loop' for videos that need to repeat smoothly": "Usa 'Ideal Loop' para videos que deben repetirse de forma fluida",
    "Increase to 30 FPS for smoother UI animations": "Sube a 30 FPS para animaciones de UI más fluidas",
    "Medium video (10-30s) - Ideal for character animations or environmental loops": "Video medio (10-30s) - Ideal para animaciones de personajes o bucles de entorno",
    "Try 'Official Godot' as the recommended starting point": "Prueba 'Official Godot' como punto de partida recomendado",
    "Long video (30-60s) - Great for cutscenes or character intros": "Video largo (30-60s) - Excelente para cinemáticas o intros de personajes",
    "Use 'High Compression' if you want a smaller file and do not need fast jumps": "Usa 'High Compression' si quieres un archivo mas pequeno y no necesitas saltos rapidos",
    "Extended video (60-180s) - Suitable for intro cinematics or tutorials": "Video extendido (60-180s) - Adecuado para cinemáticas introductorias o tutoriales",
    "Split into shorter clips for faster loading in Godot": "Divide en clips más cortos para cargar más rápido en Godot",
    "Use 'Mobile Optimized' for more stable playback on weaker devices": "Usa 'Mobile Optimized' para una reproduccion mas estable en equipos modestos",
    "Very long video (180s+) - May impact loading times": "Video muy largo (180s+) - Puede afectar los tiempos de carga",
    "Large files possible with OGV; reduce resolution or FPS": "Con OGV pueden generarse archivos grandes; reduce resolución o FPS",
    "Split into smaller clips or stream externally": "Divide en clips más pequeños o reprodúcelos externamente",
    "High resolution detected": "Resolución alta detectada",
    "Large files possible with OGV; try 1080p or 720p to save space": "Con OGV pueden generarse archivos grandes; prueba 1080p o 720p para ahorrar espacio",
    "High-res is fine for short splash screens or cutscenes": "Alta resolución va bien para pantallas splash o cinemáticas cortas",
    "Use 1080p for most Godot projects, or 720p for mobiles": "Usa 1080p para la mayoría de proyectos Godot, o 720p para móviles",
    "Low resolution - Great for mobile or retro-style games": "Baja resolución - Excelente para móviles o juegos estilo retro",
    "Use 'Mobile Optimized' for more predictable playback": "Usa 'Mobile Optimized' para una reproduccion mas predecible",
    "Standard resolution - Suitable for most Godot projects": "Resolución estándar - Adecuada para la mayoría de proyectos Godot",
    "Try 720p for mobiles or 1080p for desktop": "Prueba 720p para móviles o 1080p para escritorio",
    "High FPS short clip - Great for smooth UI effects": "Clip corto con FPS altos - Excelente para efectos fluidos de UI",
    "High FPS detected": "FPS altos detectados",
    "Reduce to 30 FPS to save space with OGV": "Reduce a 30 FPS para ahorrar espacio con OGV",
    "Low FPS detected": "FPS bajos detectados",
    "Use 24-30 FPS for smooth cinematics or gameplay": "Usa 24-30 FPS para cinemáticas o gameplay más fluidos",
    "24-30 FPS is ideal for OGV in Godot - balances smoothness and size": "24-30 FPS es ideal para OGV en Godot: equilibra fluidez y tamaño",
    "Short video with audio (0-5s) - Perfect for UI sounds or effects": "Video corto con audio (0-5s) - Perfecto para sonidos o efectos de UI",
    "Long video with audio - Great for cutscenes": "Video largo con audio - Excelente para cinemáticas",
    "Extract audio as OGG for better control in Godot": "Extrae el audio como OGG para mejor control en Godot",
    "Audio included - Good for character dialogues or ambient scenes": "Audio incluido - Bueno para diálogos de personajes o escenas ambientales",
    "Consider extracting audio as OGG for flexible control in Godot": "Considera extraer el audio como OGG para un control más flexible en Godot",
    "Audio will be removed because keep_audio is disabled": "El audio será removido porque keep_audio está desactivado",
    "No audio - Ideal for background loops or visual effects": "Sin audio - Ideal para bucles de fondo o efectos visuales",
    "Use OGV for best compatibility in Godot": "Usa OGV para mejor compatibilidad en Godot",
    "Source video codec: unknown": "Codec de video de origen: desconocido",
    "Source audio codec: unknown": "Codec de audio de origen: desconocido",
    "Widescreen (16:9) - Easy fit for fullscreen scenes and cutscenes": "Panoramico (16:9) - Se adapta facilmente a escenas a pantalla completa y cinematicas",
    "Classic 4:3 - Useful for retro presentation or stylized UI": "Clasico 4:3 - Util para una presentacion retro o una UI estilizada",
    "Square (1:1) - Useful for UI, icons, or centered loops": "Cuadrado (1:1) - Util para UI, iconos o bucles centrados",
    "Ultra-wide (21:9) - May need letterboxing or careful layout": "Ultra panoramico (21:9) - Puede necesitar bandas o una composicion cuidada",
    "Non-standard aspect ratio - May need cropping, padding, or a custom layout": "Relacion de aspecto no estandar - Puede necesitar recorte, relleno o una composicion personalizada",
    "MP4 output selected. This is fine for general use, but OGV is recommended for Godot runtime compatibility": "Salida MP4 seleccionada. Sirve para uso general, pero se recomienda OGV para compatibilidad de ejecución en Godot",
    "WebM output selected. This is fine for general use, but OGV is recommended for Godot runtime compatibility": "Salida WebM seleccionada. Sirve para uso general, pero se recomienda OGV para compatibilidad de ejecución en Godot",
    "GIF output selected. Useful for previews/UI loops, but OGV is recommended for in-game video playback in Godot": "Salida GIF seleccionada. Útil para previews/bucles de UI, pero se recomienda OGV para reproducción de video dentro del juego en Godot",
    "OGV is the format natively supported by Godot": "OGV es el formato soportado de forma nativa por Godot",
    "Video looks good for Godot. Use OGV for best compatibility.": "El video se ve bien para Godot. Usa OGV para mejor compatibilidad.",
    "Use 'Seek Friendly' if the video needs to start from different points": "Usa 'Seek Friendly' si el video necesita empezar desde distintos puntos",
    "You may not need to reconvert unless you want a different size or preset": "Puede que no necesites reconvertirlo salvo que quieras otro tamano o preset",
    "H.264/AVC sources usually convert cleanly to Godot-oriented OGV": "Las fuentes H.264/AVC suelen convertirse bien a OGV orientado a Godot",
    "WebM sources can work as inputs, but OGV is the safer final target for Godot": "Las fuentes WebM pueden usarse como entrada, pero OGV es el destino final mas seguro para Godot",
    "Animated GIF sources usually benefit from lower resolution or lower FPS before export": "Las fuentes GIF animadas suelen beneficiarse de una menor resolucion o menos FPS antes de exportar",
    "Short video (0-10s) - Good for loops, UI effects, or stylized inserts": "Video corto (0-10s) - Bueno para bucles, efectos de UI o inserts estilizados",
    "Medium video (10-60s) - Suitable for in-game scenes or animated screens": "Video medio (10-60s) - Adecuado para escenas dentro del juego o pantallas animadas",
    "Long video (60s+) - Test playback early on target hardware": "Video largo (60s+) - Prueba la reproduccion temprano en el hardware objetivo",
    "Long videos are easier to manage when split into shorter scenes": "Los videos largos se manejan mejor si se dividen en escenas mas cortas",
    "Prefer 1080p or 720p unless the game really needs a larger source": "Prefiere 1080p o 720p salvo que el juego realmente necesite una fuente mayor",
    "Low resolution - Good fit for lightweight 2D projects": "Resolucion baja - Buena opcion para proyectos 2D livianos",
    "Standard resolution - Good baseline for Love2D playback": "Resolucion estandar - Buena base para reproduccion en Love2D",
    "Reduce to 24-30 FPS if you want a lighter OGV for Love2D": "Reduce a 24-30 FPS si quieres un OGV mas liviano para Love2D",
    "Very low FPS may look choppy; 24-30 FPS is a safer default": "Un FPS muy bajo puede verse entrecortado; 24-30 FPS es un valor mas seguro",
    "24-30 FPS is a practical target for Love2D video playback": "24-30 FPS es un objetivo practico para reproduccion de video en Love2D",
    "Embedded audio is supported, but test sync and volume on target platforms": "El audio embebido esta soportado, pero prueba sincronizacion y volumen en las plataformas objetivo",
    "No audio - Good for decorative loops or background motion": "Sin audio - Bueno para bucles decorativos o movimiento de fondo",
    "MP4 output selected. Keep OGV for the final Love2D playback path": "Salida MP4 seleccionada. Mantén OGV para la ruta final de reproduccion en Love2D",
    "WebM output selected. Keep OGV for the final Love2D playback path": "Salida WebM seleccionada. Mantén OGV para la ruta final de reproduccion en Love2D",
    "GIF output selected. Fine for previews, but not as a Love2D video replacement": "Salida GIF seleccionada. Sirve para previews, pero no como reemplazo de video en Love2D",
    "OGV is the main engine-oriented target for Love2D video playback": "OGV es el objetivo principal orientado al motor para reproduccion de video en Love2D",
    "If a file fails in Love2D, try 'Love2D Compatibility' first": "Si un archivo falla en Love2D, prueba primero 'Love2D Compatibility'",
    "Use 'Ideal Loop' for videos that need to repeat smoothly": "Usa 'Ideal Loop' para videos que deben repetirse de forma fluida",
    "Use 'Lightweight' if you want a smaller file": "Usa 'Lightweight' si quieres un archivo mas pequeno",
    "You may not need to reconvert unless you want a smaller file or a different preset": "Puede que no necesites reconvertirlo salvo que quieras un archivo mas pequeno o un preset distinto",
    "H.264/AVC sources are a practical starting point before converting to OGV": "Las fuentes H.264/AVC son un punto de partida practico antes de convertir a OGV",
    "WebM sources are fine as inputs, but OGV is the safer final target for Love2D": "Las fuentes WebM sirven como entrada, pero OGV es el destino final mas seguro para Love2D",
    "Video looks good for Love2D. Use OGV for best compatibility.": "El video se ve bien para Love2D. Usa OGV para mejor compatibilidad.",
}

RECOMMENDATIONS_FR_REPLACEMENTS = {
    "Invalid video file": "Fichier vidéo invalide",
    "WHAT THIS VIDEO HAS": "CE QUE CETTE VIDEO CONTIENT",
    "RECOMMENDED NEXT STEP": "ÉTAPE SUIVANTE RECOMMANDÉE",
    "Short video (0-10s) - Perfect for UI animations or button effects": "Vidéo courte (0-10s) - Parfaite pour les animations d'interface ou les effets de boutons",
    "Use 'Ideal Loop' for videos that need to repeat smoothly": "Utilisez 'Ideal Loop' pour les vidéos qui doivent se répéter en douceur",
    "Increase to 30 FPS for smoother UI animations": "Passez à 30 FPS pour des animations d'interface plus fluides",
    "Medium video (10-30s) - Ideal for character animations or environmental loops": "Vidéo moyenne (10-30s) - Idéale pour les animations de personnages ou les boucles d'environnement",
    "Try 'Official Godot' as the recommended starting point": "Essayez 'Official Godot' comme point de départ recommandé",
    "Long video (30-60s) - Great for cutscenes or character intros": "Vidéo longue (30-60s) - Très adaptée aux cinématiques ou aux introductions de personnages",
    "Use 'High Compression' if you want a smaller file and do not need fast jumps": "Utilisez 'High Compression' si vous voulez un fichier plus petit et n'avez pas besoin de sauts rapides",
    "Extended video (60-180s) - Suitable for intro cinematics or tutorials": "Vidéo étendue (60-180s) - Adaptée aux cinématiques d'introduction ou aux tutoriels",
    "Split into shorter clips for faster loading in Godot": "Découpez en clips plus courts pour un chargement plus rapide dans Godot",
    "Use 'Mobile Optimized' for more stable playback on weaker devices": "Utilisez 'Mobile Optimized' pour une lecture plus stable sur des appareils modestes",
    "Very long video (180s+) - May impact loading times": "Très longue vidéo (180s+) - Peut affecter les temps de chargement",
    "Large files possible with OGV; reduce resolution or FPS": "Avec OGV, les fichiers peuvent être volumineux ; réduisez la résolution ou les FPS",
    "Split into smaller clips or stream externally": "Découpez en clips plus petits ou lisez la vidéo en externe",
    "High resolution detected": "Haute résolution détectée",
    "Large files possible with OGV; try 1080p or 720p to save space": "Avec OGV, les fichiers peuvent être volumineux ; essayez 1080p ou 720p pour gagner de la place",
    "High-res is fine for short splash screens or cutscenes": "Une haute résolution convient bien aux écrans splash courts ou aux cinématiques",
    "Use 1080p for most Godot projects, or 720p for mobiles": "Utilisez 1080p pour la plupart des projets Godot, ou 720p pour les mobiles",
    "Low resolution - Great for mobile or retro-style games": "Basse résolution - Très adaptée aux jeux mobiles ou au style rétro",
    "Use 'Mobile Optimized' for more predictable playback": "Utilisez 'Mobile Optimized' pour une lecture plus prévisible",
    "Standard resolution - Suitable for most Godot projects": "Résolution standard - Adaptée à la plupart des projets Godot",
    "Try 720p for mobiles or 1080p for desktop": "Essayez 720p pour le mobile ou 1080p pour le bureau",
    "High FPS short clip - Great for smooth UI effects": "Clip court à FPS élevés - Idéal pour des effets d'interface fluides",
    "High FPS detected": "FPS élevés détectés",
    "Reduce to 30 FPS to save space with OGV": "Réduisez à 30 FPS pour économiser de l'espace avec OGV",
    "Low FPS detected": "FPS faibles détectés",
    "Use 24-30 FPS for smooth cinematics or gameplay": "Utilisez 24-30 FPS pour des cinématiques ou un gameplay fluide",
    "24-30 FPS is ideal for OGV in Godot - balances smoothness and size": "24-30 FPS est idéal pour OGV dans Godot - bon équilibre entre fluidité et taille",
    "Short video with audio (0-5s) - Perfect for UI sounds or effects": "Vidéo courte avec audio (0-5s) - Parfaite pour les sons ou effets d'interface",
    "Long video with audio - Great for cutscenes": "Vidéo longue avec audio - Très adaptée aux cinématiques",
    "Extract audio as OGG for better control in Godot": "Extrayez l'audio en OGG pour un meilleur contrôle dans Godot",
    "Audio included - Good for character dialogues or ambient scenes": "Audio inclus - Bien adapté aux dialogues de personnages ou aux scènes d'ambiance",
    "Consider extracting audio as OGG for flexible control in Godot": "Pensez à extraire l'audio en OGG pour un contrôle plus souple dans Godot",
    "Audio will be removed because keep_audio is disabled": "L'audio sera supprimé car l'option de conservation est désactivée",
    "No audio - Ideal for background loops or visual effects": "Pas d'audio - Idéal pour les boucles d'arrière-plan ou les effets visuels",
    "Use OGV for best compatibility in Godot": "Utilisez OGV pour la meilleure compatibilité dans Godot",
    "Source video codec: unknown": "Codec vidéo source : inconnu",
    "Source audio codec: unknown": "Codec audio source : inconnu",
    "Widescreen (16:9) - Easy fit for fullscreen scenes and cutscenes": "Format large (16:9) - S'adapte facilement aux scènes plein écran et aux cinématiques",
    "Classic 4:3 - Useful for retro presentation or stylized UI": "Format classique 4:3 - Utile pour une présentation rétro ou une interface stylisée",
    "Square (1:1) - Useful for UI, icons, or centered loops": "Format carré (1:1) - Utile pour l'interface, les icônes ou les boucles centrées",
    "Ultra-wide (21:9) - May need letterboxing or careful layout": "Ultra-large (21:9) - Peut nécessiter des bandes noires ou une mise en page soignée",
    "Non-standard aspect ratio - May need cropping, padding, or a custom layout": "Format non standard - Peut nécessiter un recadrage, des marges ou une mise en page personnalisée",
    "MP4 output selected. This is fine for general use, but OGV is recommended for Godot runtime compatibility": "Sortie MP4 sélectionnée. C'est correct pour un usage général, mais OGV est recommandé pour la compatibilité d'exécution dans Godot",
    "WebM output selected. This is fine for general use, but OGV is recommended for Godot runtime compatibility": "Sortie WebM sélectionnée. C'est correct pour un usage général, mais OGV est recommandé pour la compatibilité d'exécution dans Godot",
    "GIF output selected. Useful for previews/UI loops, but OGV is recommended for in-game video playback in Godot": "Sortie GIF sélectionnée. Utile pour les aperçus ou les boucles d'interface, mais OGV est recommandé pour la lecture vidéo dans Godot",
    "OGV is the format natively supported by Godot": "OGV est le format pris en charge nativement par Godot",
    "Video looks good for Godot. Use OGV for best compatibility.": "La vidéo semble correcte pour Godot. Utilisez OGV pour une meilleure compatibilité.",
    "Use 'Seek Friendly' if the video needs to start from different points": "Utilisez 'Seek Friendly' si la vidéo doit démarrer depuis différents points",
    "You may not need to reconvert unless you want a different size or preset": "Il n'est peut-être pas nécessaire de reconvertir sauf si vous voulez une autre taille ou un autre preset",
    "H.264/AVC sources usually convert cleanly to Godot-oriented OGV": "Les sources H.264/AVC se convertissent généralement bien vers un OGV orienté Godot",
    "WebM sources can work as inputs, but OGV is the safer final target for Godot": "Les sources WebM peuvent servir d'entrée, mais OGV est la cible finale la plus sûre pour Godot",
    "Animated GIF sources usually benefit from lower resolution or lower FPS before export": "Les sources GIF animées bénéficient souvent d'une résolution ou de FPS plus faibles avant l'export",
    "Short video (0-10s) - Good for loops, UI effects, or stylized inserts": "Vidéo courte (0-10s) - Bien adaptée aux boucles, effets d'interface ou inserts stylisés",
    "Medium video (10-60s) - Suitable for in-game scenes or animated screens": "Vidéo moyenne (10-60s) - Adaptée aux scènes en jeu ou aux écrans animés",
    "Long video (60s+) - Test playback early on target hardware": "Vidéo longue (60s+) - Testez la lecture tôt sur le matériel cible",
    "Long videos are easier to manage when split into shorter scenes": "Les longues vidéos sont plus faciles à gérer lorsqu'elles sont divisées en scènes plus courtes",
    "Prefer 1080p or 720p unless the game really needs a larger source": "Préférez 1080p ou 720p sauf si le jeu a vraiment besoin d'une source plus grande",
    "Low resolution - Good fit for lightweight 2D projects": "Basse résolution - Bien adaptée aux projets 2D légers",
    "Standard resolution - Good baseline for Love2D playback": "Résolution standard - Bonne base pour la lecture dans Love2D",
    "Reduce to 24-30 FPS if you want a lighter OGV for Love2D": "Réduisez à 24-30 FPS si vous voulez un OGV plus léger pour Love2D",
    "Very low FPS may look choppy; 24-30 FPS is a safer default": "Des FPS très faibles peuvent sembler saccadés ; 24-30 FPS est une valeur plus sûre",
    "24-30 FPS is a practical target for Love2D video playback": "24-30 FPS est une cible pratique pour la lecture vidéo dans Love2D",
    "Embedded audio is supported, but test sync and volume on target platforms": "L'audio intégré est pris en charge, mais testez la synchronisation et le volume sur les plateformes cibles",
    "No audio - Good for decorative loops or background motion": "Pas d'audio - Bien adapté aux boucles décoratives ou aux mouvements d'arrière-plan",
    "MP4 output selected. Keep OGV for the final Love2D playback path": "Sortie MP4 sélectionnée. Gardez OGV pour la lecture finale dans Love2D",
    "WebM output selected. Keep OGV for the final Love2D playback path": "Sortie WebM sélectionnée. Gardez OGV pour la lecture finale dans Love2D",
    "GIF output selected. Fine for previews, but not as a Love2D video replacement": "Sortie GIF sélectionnée. Correcte pour les aperçus, mais pas comme remplacement vidéo dans Love2D",
    "OGV is the main engine-oriented target for Love2D video playback": "OGV est la principale cible orientée moteur pour la lecture vidéo dans Love2D",
    "If a file fails in Love2D, try 'Love2D Compatibility' first": "Si un fichier échoue dans Love2D, essayez d'abord 'Love2D Compatibility'",
    "Use 'Lightweight' if you want a smaller file": "Utilisez 'Lightweight' si vous voulez un fichier plus petit",
    "You may not need to reconvert unless you want a smaller file or a different preset": "Il n'est peut-être pas nécessaire de reconvertir sauf si vous voulez un fichier plus petit ou un preset différent",
    "H.264/AVC sources are a practical starting point before converting to OGV": "Les sources H.264/AVC constituent un point de départ pratique avant la conversion en OGV",
    "WebM sources are fine as inputs, but OGV is the safer final target for Love2D": "Les sources WebM conviennent en entrée, mais OGV reste la cible finale la plus sûre pour Love2D",
    "Video looks good for Love2D. Use OGV for best compatibility.": "La vidéo semble correcte pour Love2D. Utilisez OGV pour une meilleure compatibilité.",
}

RECOMMENDATIONS_DE_REPLACEMENTS = {
    "Invalid video file": "Ungültige Videodatei",
    "WHAT THIS VIDEO HAS": "WAS DIESES VIDEO HAT",
    "RECOMMENDED NEXT STEP": "EMPFOHLENER NÄCHSTER SCHRITT",
    "Short video (0-10s) - Perfect for UI animations or button effects": "Kurzes Video (0-10s) - Ideal für UI-Animationen oder Schaltflächeneffekte",
    "Use 'Ideal Loop' for videos that need to repeat smoothly": "Verwende 'Ideal Loop' für Videos, die flüssig wiederholt werden sollen",
    "Increase to 30 FPS for smoother UI animations": "Erhöhe auf 30 FPS für flüssigere UI-Animationen",
    "Medium video (10-30s) - Ideal for character animations or environmental loops": "Mittellanges Video (10-30s) - Ideal für Charakteranimationen oder Umgebungsloops",
    "Try 'Official Godot' as the recommended starting point": "Versuche 'Official Godot' als empfohlenen Ausgangspunkt",
    "Long video (30-60s) - Great for cutscenes or character intros": "Langes Video (30-60s) - Gut geeignet für Zwischensequenzen oder Charakter-Intros",
    "Use 'High Compression' if you want a smaller file and do not need fast jumps": "Verwende 'High Compression', wenn du eine kleinere Datei willst und keine schnellen Sprünge brauchst",
    "Extended video (60-180s) - Suitable for intro cinematics or tutorials": "Längeres Video (60-180s) - Geeignet für Intro-Cinematics oder Tutorials",
    "Split into shorter clips for faster loading in Godot": "Teile es in kürzere Clips für schnelleres Laden in Godot",
    "Use 'Mobile Optimized' for more stable playback on weaker devices": "Verwende 'Mobile Optimized' für stabilere Wiedergabe auf schwächeren Geräten",
    "Very long video (180s+) - May impact loading times": "Sehr langes Video (180s+) - Kann die Ladezeiten beeinflussen",
    "Large files possible with OGV; reduce resolution or FPS": "Mit OGV sind große Dateien möglich; reduziere Auflösung oder FPS",
    "Split into smaller clips or stream externally": "Teile es in kleinere Clips oder streame es extern",
    "High resolution detected": "Hohe Auflösung erkannt",
    "Large files possible with OGV; try 1080p or 720p to save space": "Mit OGV sind große Dateien möglich; versuche 1080p oder 720p, um Platz zu sparen",
    "High-res is fine for short splash screens or cutscenes": "Hohe Auflösung ist für kurze Splash-Screens oder Zwischensequenzen in Ordnung",
    "Use 1080p for most Godot projects, or 720p for mobiles": "Verwende 1080p für die meisten Godot-Projekte oder 720p für Mobilgeräte",
    "Low resolution - Great for mobile or retro-style games": "Niedrige Auflösung - Gut für Mobil- oder Retro-Spiele",
    "Use 'Mobile Optimized' for more predictable playback": "Verwende 'Mobile Optimized' für besser vorhersehbare Wiedergabe",
    "Standard resolution - Suitable for most Godot projects": "Standardauflösung - Für die meisten Godot-Projekte geeignet",
    "Try 720p for mobiles or 1080p for desktop": "Versuche 720p für Mobilgeräte oder 1080p für Desktop",
    "High FPS short clip - Great for smooth UI effects": "Kurzer Clip mit hohen FPS - Ideal für flüssige UI-Effekte",
    "High FPS detected": "Hohe FPS erkannt",
    "Reduce to 30 FPS to save space with OGV": "Reduziere auf 30 FPS, um mit OGV Platz zu sparen",
    "Low FPS detected": "Niedrige FPS erkannt",
    "Use 24-30 FPS for smooth cinematics or gameplay": "Verwende 24-30 FPS für flüssige Zwischensequenzen oder Gameplay",
    "24-30 FPS is ideal for OGV in Godot - balances smoothness and size": "24-30 FPS sind ideal für OGV in Godot - guter Ausgleich zwischen Flüssigkeit und Dateigröße",
    "Short video with audio (0-5s) - Perfect for UI sounds or effects": "Kurzes Video mit Audio (0-5s) - Ideal für UI-Sounds oder Effekte",
    "Long video with audio - Great for cutscenes": "Langes Video mit Audio - Gut geeignet für Zwischensequenzen",
    "Extract audio as OGG for better control in Godot": "Extrahiere Audio als OGG für bessere Kontrolle in Godot",
    "Audio included - Good for character dialogues or ambient scenes": "Audio enthalten - Gut für Charakterdialoge oder stimmungsvolle Szenen",
    "Consider extracting audio as OGG for flexible control in Godot": "Erwäge, Audio als OGG zu extrahieren, um es in Godot flexibler zu steuern",
    "Audio will be removed because keep_audio is disabled": "Audio wird entfernt, weil 'Audio beibehalten' deaktiviert ist",
    "No audio - Ideal for background loops or visual effects": "Kein Audio - Ideal für Hintergrundloops oder visuelle Effekte",
    "Use OGV for best compatibility in Godot": "Verwende OGV für die beste Kompatibilität in Godot",
    "Source video codec: unknown": "Quell-Videocodec: unbekannt",
    "Source audio codec: unknown": "Quell-Audiocodec: unbekannt",
    "Widescreen (16:9) - Easy fit for fullscreen scenes and cutscenes": "Breitbild (16:9) - Passt gut zu Vollbildszenen und Zwischensequenzen",
    "Classic 4:3 - Useful for retro presentation or stylized UI": "Klassisches 4:3 - Nützlich für Retro-Präsentation oder stilisierte UI",
    "Square (1:1) - Useful for UI, icons, or centered loops": "Quadratisch (1:1) - Nützlich für UI, Icons oder zentrierte Loops",
    "Ultra-wide (21:9) - May need letterboxing or careful layout": "Ultra-Breitbild (21:9) - Kann Letterboxing oder ein sorgfältiges Layout brauchen",
    "Non-standard aspect ratio - May need cropping, padding, or a custom layout": "Ungewöhnliches Seitenverhältnis - Kann Zuschnitt, Padding oder ein eigenes Layout erfordern",
    "MP4 output selected. This is fine for general use, but OGV is recommended for Godot runtime compatibility": "MP4-Ausgabe gewählt. Für allgemeinen Gebrauch ist das in Ordnung, aber OGV wird für die Laufzeitkompatibilität in Godot empfohlen",
    "WebM output selected. This is fine for general use, but OGV is recommended for Godot runtime compatibility": "WebM-Ausgabe gewählt. Für allgemeinen Gebrauch ist das in Ordnung, aber OGV wird für die Laufzeitkompatibilität in Godot empfohlen",
    "GIF output selected. Useful for previews/UI loops, but OGV is recommended for in-game video playback in Godot": "GIF-Ausgabe gewählt. Nützlich für Vorschauen oder UI-Loops, aber OGV wird für Ingame-Videowiedergabe in Godot empfohlen",
    "OGV is the format natively supported by Godot": "OGV ist das von Godot nativ unterstützte Format",
    "Video looks good for Godot. Use OGV for best compatibility.": "Das Video sieht für Godot gut aus. Verwende OGV für die beste Kompatibilität.",
    "Use 'Seek Friendly' if the video needs to start from different points": "Verwende 'Seek Friendly', wenn das Video von verschiedenen Punkten starten soll",
    "You may not need to reconvert unless you want a different size or preset": "Du musst es möglicherweise nicht neu konvertieren, außer du möchtest eine andere Größe oder ein anderes Preset",
    "H.264/AVC sources usually convert cleanly to Godot-oriented OGV": "H.264/AVC-Quellen lassen sich meist sauber in Godot-orientiertes OGV umwandeln",
    "WebM sources can work as inputs, but OGV is the safer final target for Godot": "WebM-Quellen funktionieren als Eingabe, aber OGV ist das sicherere endgültige Zielformat für Godot",
    "Animated GIF sources usually benefit from lower resolution or lower FPS before export": "Animierte GIF-Quellen profitieren meist von geringerer Auflösung oder weniger FPS vor dem Export",
    "Short video (0-10s) - Good for loops, UI effects, or stylized inserts": "Kurzes Video (0-10s) - Gut für Loops, UI-Effekte oder stilisierte Einblendungen",
    "Medium video (10-60s) - Suitable for in-game scenes or animated screens": "Mittellanges Video (10-60s) - Geeignet für Spielszenen oder animierte Bildschirme",
    "Long video (60s+) - Test playback early on target hardware": "Langes Video (60s+) - Teste die Wiedergabe früh auf der Zielhardware",
    "Long videos are easier to manage when split into shorter scenes": "Lange Videos lassen sich leichter verwalten, wenn sie in kürzere Szenen aufgeteilt werden",
    "Prefer 1080p or 720p unless the game really needs a larger source": "Bevorzuge 1080p oder 720p, außer das Spiel braucht wirklich eine größere Quelle",
    "Low resolution - Good fit for lightweight 2D projects": "Niedrige Auflösung - Gut geeignet für leichte 2D-Projekte",
    "Standard resolution - Good baseline for Love2D playback": "Standardauflösung - Gute Basis für die Wiedergabe in Love2D",
    "Reduce to 24-30 FPS if you want a lighter OGV for Love2D": "Reduziere auf 24-30 FPS, wenn du ein leichteres OGV für Love2D möchtest",
    "Very low FPS may look choppy; 24-30 FPS is a safer default": "Sehr niedrige FPS können ruckelig wirken; 24-30 FPS sind ein sicherer Standard",
    "24-30 FPS is a practical target for Love2D video playback": "24-30 FPS sind ein praktikables Ziel für Videowiedergabe in Love2D",
    "Embedded audio is supported, but test sync and volume on target platforms": "Eingebettetes Audio wird unterstützt, aber teste Synchronität und Lautstärke auf den Zielplattformen",
    "No audio - Good for decorative loops or background motion": "Kein Audio - Gut für dekorative Loops oder Hintergrundbewegung",
    "MP4 output selected. Keep OGV for the final Love2D playback path": "MP4-Ausgabe gewählt. Nutze OGV für die endgültige Wiedergabe in Love2D",
    "WebM output selected. Keep OGV for the final Love2D playback path": "WebM-Ausgabe gewählt. Nutze OGV für die endgültige Wiedergabe in Love2D",
    "GIF output selected. Fine for previews, but not as a Love2D video replacement": "GIF-Ausgabe gewählt. Gut für Vorschauen, aber kein Ersatz für Video in Love2D",
    "OGV is the main engine-oriented target for Love2D video playback": "OGV ist das wichtigste engine-orientierte Zielformat für Videowiedergabe in Love2D",
    "If a file fails in Love2D, try 'Love2D Compatibility' first": "Wenn eine Datei in Love2D nicht funktioniert, versuche zuerst 'Love2D Compatibility'",
    "Use 'Lightweight' if you want a smaller file": "Verwende 'Lightweight', wenn du eine kleinere Datei möchtest",
    "You may not need to reconvert unless you want a smaller file or a different preset": "Du musst es möglicherweise nicht neu konvertieren, außer du möchtest eine kleinere Datei oder ein anderes Preset",
    "H.264/AVC sources are a practical starting point before converting to OGV": "H.264/AVC-Quellen sind ein praktischer Ausgangspunkt vor der Umwandlung in OGV",
    "WebM sources are fine as inputs, but OGV is the safer final target for Love2D": "WebM-Quellen sind als Eingabe in Ordnung, aber OGV ist das sicherere endgültige Zielformat für Love2D",
    "Video looks good for Love2D. Use OGV for best compatibility.": "Das Video sieht für Love2D gut aus. Verwende OGV für die beste Kompatibilität.",
}


def normalize_language_label(language: str) -> str:
    return language if language in UI_TEXT else DEFAULT_LANGUAGE_LABEL


def language_label_to_code(language: str) -> str:
    label = normalize_language_label(language)
    return LANGUAGE_CODES.get(label, "en")


def validate_ui_catalog() -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    missing: dict[str, list[str]] = {}
    extra: dict[str, list[str]] = {}
    for label, table in UI_TEXT.items():
        keys = set(table.keys())
        missing_keys = sorted(REQUIRED_UI_KEYS - keys)
        if missing_keys:
            missing[label] = missing_keys
        extra_keys = sorted(keys - REQUIRED_UI_KEYS)
        if extra_keys:
            extra[label] = extra_keys
    return missing, extra


def _report_catalog_issues_once() -> None:
    missing, extra = validate_ui_catalog()
    if not missing and not extra:
        return

    lines = ["[gvc.i18n] Translation catalog issues detected:"]
    for label, keys in missing.items():
        lines.append(f"  - {label}: missing keys -> {', '.join(keys)}")
    for label, keys in extra.items():
        lines.append(f"  - {label}: extra keys -> {', '.join(keys)}")
    message = "\n".join(lines)

    if os.getenv("GVC_I18N_STRICT", "").lower() in {"1", "true", "yes"}:
        raise KeyError(message)

    if os.getenv("GVC_I18N_WARN", "1").lower() not in {"0", "false", "no"}:
        print(message, file=sys.stderr)


def ui_text(language: str, key: str, **kwargs) -> str:
    label = normalize_language_label(language)
    default_table = UI_TEXT[DEFAULT_LANGUAGE_LABEL]
    localized_table = UI_TEXT[label]

    if key not in default_table:
        text = f"[missing-default:{key}]"
    elif key in localized_table:
        text = localized_table[key]
    else:
        text = default_table[key]
        report_key = (label, key)
        if report_key not in _REPORTED_MISSING:
            _REPORTED_MISSING.add(report_key)
            if os.getenv("GVC_I18N_WARN", "1").lower() not in {"0", "false", "no"}:
                print(
                    f"[gvc.i18n] Missing translation key '{key}' for language '{label}', using English fallback.",
                    file=sys.stderr,
                )
    return text.format(**kwargs) if kwargs else text


def translate_recommendations(text: str, language: str) -> str:
    if language == "de":
        out = text
        for en_text, de_text in RECOMMENDATIONS_DE_REPLACEMENTS.items():
            out = out.replace(en_text, de_text)

        out = re.sub(
            r"Source codec \((.+?)\) is already OGV-compatible for Godot",
            r"Der Quellcodec (\1) ist bereits OGV-kompatibel für Godot",
            out,
        )
        out = re.sub(
            r"Converting from (.+?) to OGV is recommended for Godot compatibility",
            r"Die Umwandlung von \1 nach OGV wird für die Kompatibilität mit Godot empfohlen",
            out,
        )
        out = re.sub(
            r"Source video codec: (.+?) - already in the OGV/Theora family",
            r"Quell-Videocodec: \1 - bereits in der OGV/Theora-Familie",
            out,
        )
        out = re.sub(
            r"Source video codec: (.+?) - common source format for exported videos",
            r"Quell-Videocodec: \1 - gängiges Quellformat für exportierte Videos",
            out,
        )
        out = re.sub(
            r"Source video codec: (.+?) - web-oriented source video format",
            r"Quell-Videocodec: \1 - weborientiertes Videoformat",
            out,
        )
        out = re.sub(
            r"Source video codec: (.+?) - animated image style source",
            r"Quell-Videocodec: \1 - Quelle im Stil eines animierten Bildes",
            out,
        )
        out = re.sub(
            r"Source video codec: (.+)",
            r"Quell-Videocodec: \1",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+?) - common in MP4 exports",
            r"Quell-Audiocodec: \1 - häufig in MP4-Exporten",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+?) - already close to OGV workflows",
            r"Quell-Audiocodec: \1 - bereits nah an OGV-Workflows",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+?) - efficient web-oriented audio",
            r"Quell-Audiocodec: \1 - effizientes weborientiertes Audio",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+?) - common compressed audio",
            r"Quell-Audiocodec: \1 - gängiges komprimiertes Audio",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+?) - uncompressed or near-uncompressed audio",
            r"Quell-Audiocodec: \1 - unkomprimiertes oder nahezu unkomprimiertes Audio",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+)",
            r"Quell-Audiocodec: \1",
            out,
        )
        out = re.sub(
            r"Source codec \((.+?)\) is already OGV-compatible for Love2D",
            r"Der Quellcodec (\1) ist bereits OGV-kompatibel für Love2D",
            out,
        )
        out = re.sub(
            r"Converting from (.+?) to OGV is recommended for Love2D compatibility",
            r"Die Umwandlung von \1 nach OGV wird für die Kompatibilität mit Love2D empfohlen",
            out,
        )
        return out

    if language == "fr":
        out = text
        for en_text, fr_text in RECOMMENDATIONS_FR_REPLACEMENTS.items():
            out = out.replace(en_text, fr_text)

        out = re.sub(
            r"Source codec \((.+?)\) is already OGV-compatible for Godot",
            r"Le codec source (\1) est deja compatible OGV pour Godot",
            out,
        )
        out = re.sub(
            r"Converting from (.+?) to OGV is recommended for Godot compatibility",
            r"La conversion de \1 vers OGV est recommandée pour la compatibilité avec Godot",
            out,
        )
        out = re.sub(
            r"Source video codec: (.+?) - already in the OGV/Theora family",
            r"Codec vidéo source : \1 - déjà dans la famille OGV/Theora",
            out,
        )
        out = re.sub(
            r"Source video codec: (.+?) - common source format for exported videos",
            r"Codec vidéo source : \1 - format source courant pour les vidéos exportées",
            out,
        )
        out = re.sub(
            r"Source video codec: (.+?) - web-oriented source video format",
            r"Codec vidéo source : \1 - format vidéo orienté web",
            out,
        )
        out = re.sub(
            r"Source video codec: (.+?) - animated image style source",
            r"Codec vidéo source : \1 - source de type image animée",
            out,
        )
        out = re.sub(
            r"Source video codec: (.+)",
            r"Codec vidéo source : \1",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+?) - common in MP4 exports",
            r"Codec audio source : \1 - courant dans les exports MP4",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+?) - already close to OGV workflows",
            r"Codec audio source : \1 - déjà proche des flux OGV",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+?) - efficient web-oriented audio",
            r"Codec audio source : \1 - audio efficace orienté web",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+?) - common compressed audio",
            r"Codec audio source : \1 - audio compresse courant",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+?) - uncompressed or near-uncompressed audio",
            r"Codec audio source : \1 - audio non compresse ou presque",
            out,
        )
        out = re.sub(
            r"Source audio codec: (.+)",
            r"Codec audio source : \1",
            out,
        )
        out = re.sub(
            r"Source codec \((.+?)\) is already OGV-compatible for Love2D",
            r"Le codec source (\1) est deja compatible OGV pour Love2D",
            out,
        )
        out = re.sub(
            r"Converting from (.+?) to OGV is recommended for Love2D compatibility",
            r"La conversion de \1 vers OGV est recommandée pour la compatibilité avec Love2D",
            out,
        )
        return out

    if language != "es":
        return text

    out = text
    for en_text, es_text in RECOMMENDATIONS_ES_REPLACEMENTS.items():
        out = out.replace(en_text, es_text)

    out = re.sub(
        r"Source codec \((.+?)\) is already OGV-compatible for Godot",
        r"El códec de origen (\1) ya es compatible con OGV para Godot",
        out,
    )
    out = re.sub(
        r"Converting from (.+?) to OGV is recommended for Godot compatibility",
        r"Se recomienda convertir de \1 a OGV para compatibilidad con Godot",
        out,
    )
    out = re.sub(
        r"Source video codec: (.+?) - already in the OGV/Theora family",
        r"Codec de video de origen: \1 - ya esta en la familia OGV/Theora",
        out,
    )
    out = re.sub(
        r"Source video codec: (.+?) - common source format for exported videos",
        r"Codec de video de origen: \1 - formato de origen comun en videos exportados",
        out,
    )
    out = re.sub(
        r"Source video codec: (.+?) - web-oriented source video format",
        r"Codec de video de origen: \1 - formato de video orientado a web",
        out,
    )
    out = re.sub(
        r"Source video codec: (.+?) - animated image style source",
        r"Codec de video de origen: \1 - fuente de estilo imagen animada",
        out,
    )
    out = re.sub(
        r"Source video codec: (.+)",
        r"Codec de video de origen: \1",
        out,
    )
    out = re.sub(
        r"Source audio codec: (.+?) - common in MP4 exports",
        r"Codec de audio de origen: \1 - comun en exportaciones MP4",
        out,
    )
    out = re.sub(
        r"Source audio codec: (.+?) - already close to OGV workflows",
        r"Codec de audio de origen: \1 - ya esta cerca de los flujos OGV",
        out,
    )
    out = re.sub(
        r"Source audio codec: (.+?) - efficient web-oriented audio",
        r"Codec de audio de origen: \1 - audio eficiente orientado a web",
        out,
    )
    out = re.sub(
        r"Source audio codec: (.+?) - common compressed audio",
        r"Codec de audio de origen: \1 - audio comprimido comun",
        out,
    )
    out = re.sub(
        r"Source audio codec: (.+?) - uncompressed or near-uncompressed audio",
        r"Codec de audio de origen: \1 - audio sin comprimir o casi sin comprimir",
        out,
    )
    out = re.sub(
        r"Source audio codec: (.+)",
        r"Codec de audio de origen: \1",
        out,
    )
    out = re.sub(
        r"Source codec \((.+?)\) is already OGV-compatible for Love2D",
        r"El codec de origen (\1) ya es compatible con OGV para Love2D",
        out,
    )
    out = re.sub(
        r"Converting from (.+?) to OGV is recommended for Love2D compatibility",
        r"Se recomienda convertir de \1 a OGV para compatibilidad con Love2D",
        out,
    )
    return out


_report_catalog_issues_once()
