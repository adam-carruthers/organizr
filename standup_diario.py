import time
import webbrowser
import datetime as dt

PEQUEÑO_DESCANSO = 0.4


def standup_diario():
    print("Hola, bienvenido a su standup.")
    time.sleep(PEQUEÑO_DESCANSO)

    print("\nPrimero, vamos a abrir su lista de quehaceres.")
    webbrowser.open_new("https://todoist.com/app/upcoming")

    print("También, vamos a abrir su horario. Considerelo.")
    webbrowser.open_new("https://outlook.office.com/calendar/view/week")

    print("Por favor, coloque las ventanas para poder ver las dos a la vez.")

    time.sleep(PEQUEÑO_DESCANSO)

    print("\nAhora, por favor (presione Enter cuando haya cumplido cada instrucción):")
    input("- vea las tareas atrasadas. Elija nuevas fechas de vencamiento para ellas.")
    input(
        "- compruebe que la lista de hoy sea correcta, y las tareas del trabajo estén marcadas correctamente con @work."
    )
    input(
        "- cambie a ver solo las tareas del trabajo hoy (@work). Quiteles la prioritización y elegir nuevas prioritizaciónes."
    )
    input("- mueva a mañana las tareas que parezcan no realizable hoy")

    print("\nYa que hemos organizado las tareas, le vamos a abrir el tablero sprint.")
    webbrowser.open_new(
        "https://nhsd-jira.digital.nhs.uk/secure/RapidBoard.jspa?rapidView=4652&projectKey=ASCS"
    )

    print("\nOtra vez, cumpla las instrucciónes, y presione Enter una vez termindado:")
    input(
        "- compruebe que la lista sea correcta, especialmente el estado de los tickets suyos"
    )
    input(
        "- si vas a trabajar en un ticket hoy, assigneselo, y pongalo en la columna 'in progress'"
    )

    print("\nPor fin, estamos en el parte normal de standup. Responde las preguntas.")

    ayer = input("\n¿Qué hizo usted ayer?\n")

    hoy = input("\n¿Qué va a hacer hoy?\n")

    bloqueadores = input("\n¿Qué le bloquea?\n")

    hora_ahora = dt.datetime.now()

    registro = f"""\
===================
Registro de standup
===================

Hora de standup: {str(hora_ahora)}

¿Qué hizo usted ayer?
---------------------
{ayer}

¿Qué va a hacer hoy?
---------------------
{hoy}

¿Qué le bloquea?
---------------------
{bloqueadores}
"""

    with open(f"standups/{str(hora_ahora.date())}.txt", "w", encoding="utf8") as f:
        f.write(registro)

    print("\nGracias por haber completado el standup de hoy.")
