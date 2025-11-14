instalo dependecias

pip install Flask Flask-SQLAlchemy PyMySQL python-dotenv Flask-Migrate SpeechRecognition PyAudio flet

# 🎙️ AsisVoice – Sistema de asistencia inteligente con reconocimiento de voz

## 🧩 Descripción general
**AsisVoice** es una aplicación educativa inteligente diseñada para automatizar la toma de asistencia en clases mediante **reconocimiento y síntesis de voz**.  
Combina tecnologías de **Python**, **Speech Recognition**, y **Text-to-Speech (TTS)** para ofrecer una experiencia fluida, moderna y eficiente tanto para docentes como para estudiantes.

---

## 🧠 Funcionamiento general
1. El docente abre la aplicación y selecciona la materia o curso.  
2. El sistema anuncia por voz:  
   > “Clase de Programación II iniciada. Comenzando la asistencia. Por favor respondan presente cuando escuchen su nombre.”  
3. La app nombra automáticamente a cada alumno (voz tipo Alexa).  
4. Cuando el alumno responde “presente”, el sistema lo reconoce mediante **reconocimiento de voz** y marca la asistencia.  
5. Al finalizar, la app anuncia:  
   > “Asistencia finalizada. 23 presentes, 2 ausentes.”  
6. Los datos de asistencia se guardan automáticamente en una base de datos o archivo.

---

## 📂 Carga automática de alumnos
- El docente puede **cargar una lista de alumnos directamente desde un archivo Excel (.xlsx) o CSV**.  
- El sistema procesa el archivo y genera automáticamente la lista de alumnos del curso.  
- Esto permite integrar fácilmente planillas ya existentes sin necesidad de ingresar datos manualmente.

---

## ⚙️ Tecnologías

### 🔹 Backend
- **Python** (Flask )

### 🔹 Reconocimiento de voz
- `SpeechRecognition`
- `OpenAI Whisper`
- `pyaudio`

### 🔹 Síntesis de voz
- `pyttsx3`
- `gTTS`
- APIs de voz neural (Azure / ElevenLabs / OpenAI TTS)

### 🔹 Interfaz gráfica 
- `Flet`
### 🔹 Base de datos
- `SQLite`
- `Google Sheets API`
- `Pandas + OpenPyXL` para manejo de Excel

---

## 🎯 Objetivo del proyecto
Desarrollar una herramienta útil, moderna y autónoma que:
- Optimice el tiempo de clase.
- Reduzca errores en el registro de asistencia.
- Integre tecnologías de IA en la práctica docente.
- Ofrezca una experiencia atractiva y profesional.

---

## 🚀 Futuras mejoras
- Generación de reportes automáticos de asistencia en PDF o Excel.  
- Integración con plataformas educativas (Google Classroom, Moodle, etc).  
- Identificación de voz individual por alumno (reconocimiento de hablantes).  
- Control por comandos de voz del docente:  
  > “Iniciar asistencia”, “Finalizar clase”, “Mostrar ausentes”.

---

## 🧑‍💻 Autor
**Pietro** – Profesor y desarrollador de software  
💡 Proyecto educativo para optimizar la gestión de asistencia mediante IA y herramientas open source.

---

## 🗓️ Versión
**v0.1 – Proyecto en desarrollo**
