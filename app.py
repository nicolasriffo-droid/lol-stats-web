import streamlit as st
import math

# ========================================================
# CONSTANTES Y DATOS DE TUS COMANDOS ORIGINALES
# ========================================================
roles_descripcion = {
    "TOP": "Te gustan los duelos y jugar independiente.\n\n**Campeones recomendados:** Darius, Sett, Garen",
    "JUNGLA": "Te gusta controlar el mapa y ayudar líneas.\n\n**Campeones recomendados:** Lee Sin, Kayn, Viego",
    "MID": "Te gusta hacer daño y carrear partidas.\n\n**Campeones recomendados:** Yasuo, Zed, Ahri",
    "ADC": "Te gusta escalar y ser el carry principal.\n\n**Campeones recomendados:** Jinx, Kai'Sa, Vayne",
    "SUPPORT": "Te gusta ayudar y proteger al equipo.\n\n**Campeones recomendados:** Thresh, Leona, Lulu"
}


def obtener_referencias_por_rol(rol):
    datos = {
        "top": {
            "Hierro": (4.5, 8.5, 4.0, 4.5, 0.3, 35), "Bronce": (5.0, 7.5, 4.5, 5.2, 0.4, 40),
            "Plata": (6.0, 6.5, 5.0, 5.8, 0.5, 43), "Oro": (7.0, 5.5, 5.5, 6.5, 0.6, 45),
            "Platino": (7.5, 4.5, 5.5, 7.0, 0.7, 48), "Esmeralda": (8.0, 4.5, 6.0, 7.3, 0.8, 50),
            "Diamante": (8.5, 3.5, 6.0, 7.8, 1.0, 52), "Maestro": (9.0, 3.5, 6.5, 8.2, 1.2, 55),
            "Gran Maestro": (9.5, 3.0, 7.0, 8.5, 1.3, 58), "Challenger": (10.0, 3.0, 7.0, 8.8, 1.5, 60)
        },
        "mid": {
            "Hierro": (5.0, 8.0, 4.5, 5.0, 0.4, 40), "Bronce": (5.5, 7.0, 5.0, 5.7, 0.5, 45),
            "Plata": (6.5, 6.5, 5.5, 6.3, 0.6, 48), "Oro": (7.5, 5.5, 6.0, 7.0, 0.8, 50),
            "Platino": (8.0, 4.5, 6.5, 7.5, 0.9, 52), "Esmeralda": (8.5, 4.5, 7.0, 7.8, 1.0, 54),
            "Diamante": (9.0, 3.5, 7.5, 8.3, 1.2, 56), "Maestro": (9.5, 3.5, 8.0, 8.7, 1.4, 58),
            "Gran Maestro": (10.0, 3.0, 8.5, 9.0, 1.5, 60), "Challenger": (10.5, 3.0, 9.0, 9.3, 1.7, 63)
        },
        "jungla": {
            "Hierro": (5.0, 7.5, 5.5, 4.0, 0.5, 45), "Bronce": (5.5, 7.0, 6.0, 4.5, 0.6, 48),
            "Plata": (6.0, 6.5, 6.5, 5.0, 0.7, 50), "Oro": (7.0, 5.5, 8.0, 5.5, 0.9, 53),
            "Platino": (8.0, 4.5, 9.0, 5.8, 1.0, 55), "Esmeralda": (8.5, 4.5, 10.0, 6.1, 1.1, 57),
            "Diamante": (9.0, 3.5, 11.0, 6.4, 1.3, 60), "Maestro": (10.0, 3.5, 12.0, 6.7, 1.5, 62),
            "Gran Maestro": (10.5, 3.0, 12.5, 7.0, 1.6, 64), "Challenger": (11.0, 3.0, 13.0, 7.3, 1.8, 66)
        },
        "adc": {
            "Hierro": (5.5, 8.0, 4.0, 5.0, 0.2, 35), "Bronce": (6.0, 7.0, 4.5, 5.8, 0.3, 38),
            "Plata": (6.8, 6.5, 5.0, 6.5, 0.4, 40), "Oro": (7.8, 5.5, 5.8, 7.3, 0.5, 43),
            "Platino": (8.3, 4.5, 6.2, 7.8, 0.5, 45), "Esmeralda": (8.8, 4.5, 6.6, 8.2, 0.6, 47),
            "Diamante": (9.3, 3.5, 7.0, 8.7, 0.7, 50), "Maestro": (9.8, 3.5, 7.5, 9.1, 0.8, 52),
            "Gran Maestro": (10.3, 3.0, 8.0, 9.4, 0.9, 54), "Challenger": (10.8, 3.0, 8.5, 9.8, 1.0, 56)
        },
        "support": {
            "Hierro": (1.5, 7.0, 7.0, 0.5, 1.0, 40), "Bronce": (2.0, 6.5, 8.0, 0.6, 1.2, 45),
            "Plata": (2.5, 6.0, 9.5, 0.6, 1.5, 48), "Oro": (2.8, 5.0, 11.0, 0.7, 1.8, 52),
            "Platino": (3.0, 4.5, 12.5, 0.7, 2.1, 55), "Esmeralda": (3.3, 4.5, 13.5, 0.8, 2.3, 58),
            "Diamante": (3.5, 3.5, 14.5, 0.8, 2.6, 61), "Maestro": (3.8, 3.5, 15.5, 0.9, 2.9, 64),
            "Gran Maestro": (4.0, 2.8, 16.5, 0.9, 3.1, 66), "Challenger": (4.3, 2.8, 17.5, 1.0, 3.4, 69)
        }
    }
    return datos.get(rol.strip().lower())


def calcular_mi_rango(kills, deaths, assists, cs_min, vision_min, kp_pct, rol):
    rangos_referencia = obtener_referencias_por_rol(rol)
    if not rangos_referencia: return "Rol no válido"
    kda_jugador = (kills + assists) / max(deaths, 1)
    puntuaciones_rango = {}
    for rango, (k_ref, d_ref, a_ref, cs_ref, vis_ref, kp_ref) in rangos_referencia.items():
        kda_ref = (k_ref + a_ref) / max(d_ref, 1)
        desv_kda = abs(kda_jugador - kda_ref) / kda_ref
        desv_cs = abs(cs_min - cs_ref) / cs_ref
        desv_vision = abs(vision_min - vis_ref) / vis_ref
        desv_kp = abs(kp_pct - kp_ref) / kp_ref
        distancia_proporcional = math.sqrt((desv_kda ** 2) + (desv_cs ** 2) + (desv_vision ** 2) + (desv_kp ** 2))
        puntuaciones_rango[rango] = distancia_proporcional
    return min(puntuaciones_rango, key=puntuaciones_rango.get)


# ========================================================
# CONTROL DE SESIÓN WEB
# ========================================================
if "logeado" not in st.session_state:
    st.session_state.logeado = False

# --- PANTALLA 1: LOGIN WEB ---
if not st.session_state.logeado:
    st.title("🔒 League Stats Login")
    st.write("Por favor, inicia sesión para acceder al panel.")

    usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión", use_container_width=True):
        if usuario.strip() == "admin" and contraseña.strip() == "1234":
            st.session_state.logeado = True
            st.success("¡Login correcto!")
            st.rerun()  # Recarga la página para mostrar el panel
        else:
            st.error("Usuario o contraseña incorrectos")

# --- PANTALLA 2: PANEL DE LEAGUE OF LEGENDS ---
else:
    st.title("🏆 PANEL DE ESTADÍSTICAS LOL 🏆")
    st.write("¡Bienvenido al analizador táctico!")

    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.logeado = False
        st.rerun()

    # Creamos pestañas para que la página web se vea organizada
    pestana1, pestana2 = st.tabs(["🎯 Test de Línea", "📊 Calculador de Rango"])

    # --- PESTAÑA 1: TEST DE LINEA ---
    with pestana1:
        st.header("Descubre tu rol ideal")
        st.write("Responde estas preguntas del 1 (No me gusta nada) al 5 (Me encanta):")

        preguntas = [
            "¿Te gusta hacer mucho daño?", "¿Te gusta ayudar a tu equipo?", "¿Te gusta controlar objetivos?",
            "¿Te gustan los duelos 1v1?", "¿Te gusta carrear partidas?", "¿Te gusta moverte por todo el mapa?",
            "¿Te gusta iniciar peleas?", "¿Te gusta proteger aliados?", "¿Te gusta jugar agresivo?",
            "¿Te gusta farmear tranquilo?", "¿Te gusta tener mucho control del mapa?",
            "¿Te frustras si dependes de otros?",
            "¿Te gusta emboscar enemigos?", "¿Te gusta jugar campeones difíciles?", "¿Te gusta jugar peleas largas?",
            "¿Te gusta burstear enemigos rápidamente?", "¿Te gusta depender de posicionamiento?",
            "¿Te gusta iniciar teamfights?", "¿Te gusta splitpushear?", "¿Te gusta controlar el ritmo de la partida?"
        ]

        respuestas = []
        # En la web usamos Sliders (barras deslizantes), ¡se ve increíble!
        for i, preg in enumerate(preguntas, 1):
            resp = st.slider(f"{i}. {preg}", min_value=1, max_value=5, value=3, key=f"p_{i}")
            respuestas.append(resp)

        if st.button("Calcular mi Rol Táctico", type="primary"):
            roles = {"TOP": 0, "JUNGLA": 0, "MID": 0, "ADC": 0, "SUPPORT": 0}

            for i, resp in enumerate(respuestas, 1):
                if i in [1, 5, 14]: roles["MID"] += resp * 2; roles["ADC"] += resp * (2 if i != 14 else 1)
                if i in [2, 8, 11, 18]: roles["SUPPORT"] += resp * (3 if i in [2, 8] else 2)
                if i in [3, 6, 13, 20]: roles["JUNGLA"] += resp * 3
                if i in [4, 19]: roles["TOP"] += resp * 3
                if i in [7, 15, 18]: roles["TOP"] += resp * 2
                if i == 7: roles["SUPPORT"] += resp * 2
                if i == 9: roles["MID"] += resp * 2; roles["TOP"] += resp
                if i == 10: roles["ADC"] += resp * 3
                if i == 11: roles["JUNGLA"] += resp * 3
                if i == 12: roles["TOP"] += resp * 2; roles["MID"] += resp * 2
                if i == 16: roles["MID"] += resp * 3
                if i == 17: roles["ADC"] += resp * 3

            roles_ordenados = sorted(roles.items(), key=lambda x: x[1], reverse=True)
            mejor_rol = roles_ordenados[0][0]

            st.balloons()  # ¡Animación de globos por ganar!
            st.success(f"### 🔥 Tu mejor rol es: **{mejor_rol}**")
            st.info(roles_descripcion[mejor_rol])

    # --- PESTAÑA 2: CALCULADOR DE RANGO ---
    with pestana2:
        st.header("Analizador de Rango por KDA y Macro")
        st.write("Introduce los datos de tu última partida:")

        col1, col2 = st.columns(2)
        with col1:
            minutos = st.number_input("Duración de partida (minutos)", min_value=1.0, value=30.0)
            kills = st.number_input("Asesinatos (Kills)", min_value=0.0, value=5.0)
            deaths = st.number_input("Muertes (Deaths)", min_value=0.0, value=4.0)
            assists = st.number_input("Asistencias (Assists)", min_value=0.0, value=7.0)
        with col2:
            cs_total = st.number_input("Farming Total (CS)", min_value=0.0, value=180.0)
            vision_total = st.number_input("Puntuación de Visión", min_value=0.0, value=25.0)
            kills_totales_equipo = st.number_input("Kills Totales de tu Equipo", min_value=1.0, value=25.0)
            rol = st.selectbox("Tu Rol en esa partida", ["Top", "Mid", "Jungla", "Adc", "Support"])

        if st.button("Estimar mi Rango", type="primary"):
            cs_min = cs_total / minutos
            vision_min = vision_total / minutos
            kp_pct = ((kills + assists) / max(kills_totales_equipo, 1)) * 100

            rango_final = calcular_mi_rango(kills, deaths, assists, cs_min, vision_min, kp_pct, rol)

            st.metric(label="🏆 Tu Rango Estimado es:", value=rango_final)
            st.write(f"**Tus estadísticas por minuto:**")
            st.write(f"• CS/Min: {cs_min:.1f} | Visión/Min: {vision_min:.2f} | Participación: {kp_pct:.1f}%")