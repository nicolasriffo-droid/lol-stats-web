import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import math

# ========================================================
# CONSTANTES Y DATOS DE TUS COMANDOS ORIGINALES
# ========================================================
roles_descripcion = {
    "TOP": "Te gustan los duelos y jugar independiente.\nCampeones: Darius, Sett, Garen",
    "JUNGLA": "Te gusta controlar el mapa y ayudar líneas.\nCampeones: Lee Sin, Kayn, Viego",
    "MID": "Te gusta hacer daño y carrear partidas.\nCampeones: Yasuo, Zed, Ahri",
    "ADC": "Te gusta escalar y ser el carry principal.\nCampeones: Jinx, Kai'Sa, Vayne",
    "SUPPORT": "Te gusta ayudar y proteger al equipo.\nCampeones: Thresh, Leona, Lulu"
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
# CONFIGURACIÓN DE LA INTERFAZ
# ========================================================
ventana = tk.Tk()
ventana.title("League of Legends Stats Panel")
ventana.geometry("450x450")

frame_login = tk.Frame(ventana)
frame_login.pack(pady=40)

label_resultado = tk.Label(frame_login, text="Esperando login...", font=("Arial", 12))
label_resultado.pack(pady=10)

tk.Label(frame_login, text="Usuario").pack()
entry_user = tk.Entry(frame_login)
entry_user.pack(pady=5)

tk.Label(frame_login, text="Contraseña").pack()
entry_pass = tk.Entry(frame_login, show="*")
entry_pass.pack(pady=5)

# Variables globales para guardar los resultados del usuario
res_linea = tk.StringVar(value="No calculado")
res_rango = tk.StringVar(value="No calculado")


# LÓGICA DE EJECUCIÓN VISUAL DEL TEST DE ROL
def ejecutar_test_linea():
    preguntas = [
        "¿Te gusta hacer mucho daño?",
        "¿Te gusta ayudar a tu equipo?",
        "¿Te gusta controlar objetivos?",
        "¿Te gustan los duelos 1v1?",
        "¿Te gusta carrear partidas?",
        "¿Te gusta moverte por todo el mapa?",
        "¿Te gusta iniciar peleas?",
        "¿Te gusta proteger aliados?",
        "¿Te gusta jugar agresivo?",
        "¿Te gusta farmear tranquilo?",
        "¿Te gusta tener mucho control del mapa?",
        "¿Te frustras si dependes de otros?",
        "¿Te gusta emboscar enemigos?",
        "¿Te gusta jugar campeones difíciles?",
        "¿Te gusta jugar peleas largas?",
        "¿Te gusta burstear enemigos rápidamente?\n(Burstear: Hacer mucho daño masivo en muy poco tiempo)",
        "¿Te gusta depender de posicionamiento?",
        "¿Te gusta iniciar teamfights?\n(Teamfights: Peleas grupales de varios integrantes de ambos equipos)",
        "¿Te gusta splitpushear?\n(Splitpushear: Presionar y destruir torretas solo en una línea alejada)",
        "¿Te gusta controlar el ritmo de la partida?"
    ]

    roles = {"TOP": 0, "JUNGLA": 0, "MID": 0, "ADC": 0, "SUPPORT": 0}
    messagebox.showinfo("Test de Rol", "A continuación se harán 20 preguntas rápidas. Responde de 1 a 5.")

    for i, preg in enumerate(preguntas, 1):
        while True:
            resp = simpledialog.askinteger(f"Pregunta {i}/20", f"{preg}\n(Responde del 1 al 5):", minvalue=1,
                                           maxvalue=5)
            if resp is not None:
                # Mapeo de puntajes idéntico a tus comandos
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
                break
            else:
                return  # Si cancela, sale del test

    roles_ordenados = sorted(roles.items(), key=lambda x: x[1], reverse=True)
    mejor_rol = roles_ordenados[0][0]

    res_linea.set(f"{mejor_rol}")
    messagebox.showinfo("Resultado del Test", f"Tu rol ideal es: {mejor_rol}\n\n{roles_descripcion[mejor_rol]}")


# LÓGICA DE EJECUCIÓN VISUAL DEL CALCULADOR DE RANGO
def ejecutar_calculador_rango():
    try:
        minutos = simpledialog.askfloat("Datos", "Minutos de duración de la partida:")
        if not minutos: return
        kills = simpledialog.askfloat("Datos", "Kills:")
        deaths = simpledialog.askfloat("Datos", "Deaths:")
        assists = simpledialog.askfloat("Datos", "Assists:")
        cs_total = simpledialog.askfloat("Datos", "Farming (CS Total):")
        vision_total = simpledialog.askfloat("Datos", "Puntuación de Visión Total:")
        kills_totales_equipo = simpledialog.askfloat("Datos", "Asesinatos totales de TU equipo:")
        rol = simpledialog.askstring("Datos", "Rol (top, mid, jungla, adc, support):").strip().lower()

        if rol not in ["top", "mid", "jungla", "adc", "support"]:
            messagebox.showerror("Error", "Rol no válido.")
            return

        cs_min = cs_total / minutos
        vision_min = vision_total / minutos
        kp_pct = ((kills + assists) / max(kills_totales_equipo, 1)) * 100

        resultado = calcular_mi_rango(kills, deaths, assists, cs_min, vision_min, kp_pct, rol)

        res_rango.set(f"{resultado}")
        messagebox.showinfo("Rango Estimado",
                            f"Basado en tus estadísticas por minuto como {rol.upper()},\ntu rango aproximado es: {resultado}")
    except Exception as e:
        messagebox.showerror("Error", f"Ingresaste datos inválidos: {e}")


# --- PANTALLA PRINCIPAL DE ESTADÍSTICAS LOL ---
def mostrar_pantalla_lol():
    frame_login.destroy()

    frame_lol = tk.Frame(ventana)
    frame_lol.pack(pady=20)

    tk.Label(frame_lol, text="🏆 PANEL DE ESTADÍSTICAS LOL 🏆", font=("Arial", 14, "bold"), fg="purple").pack(pady=15)

    # Textos que se actualizan de forma dinámica mediante las variables StringVar
    tk.Label(frame_lol, text="Mejor Línea sugerida:", font=("Arial", 10)).pack()
    tk.Label(frame_lol, textvariable=res_linea, font=("Arial", 12, "bold"), fg="blue").pack(pady=2)

    tk.Label(frame_lol, text="Rango aproximado por KDA:", font=("Arial", 10)).pack()
    tk.Label(frame_lol, textvariable=res_rango, font=("Arial", 12, "bold"), fg="darkgreen").pack(pady=2)

    # Botones interactivos para llamar a los algoritmos que hiciste
    tk.Button(frame_lol, text="🎯 Ejecutar Test de Línea", command=ejecutar_test_linea, width=25, bg="lightblue").pack(
        pady=10)
    tk.Button(frame_lol, text="📊 Calcular Rango (KDA/Stats)", command=ejecutar_calculador_rango, width=25,
              bg="lightgreen").pack(pady=5)

    ventana.update()


def login():
    usuario = entry_user.get().strip()
    contraseña = entry_pass.get().strip()

    if usuario == "admin" and contraseña == "1234":
        label_resultado.config(text="LOGIN CORRECTO", fg="green")
        ventana.update_idletasks()
        messagebox.showinfo("Éxito", "¡Inicio de sesión correcto!")
        mostrar_pantalla_lol()
    else:
        label_resultado.config(text="LOGIN INCORRECTO", fg="red")
        ventana.update_idletasks()
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


boton = tk.Button(frame_login, text="Iniciar sesión", command=login)
boton.pack(pady=15)

ventana.mainloop()