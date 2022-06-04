import enum
import time
import webbrowser
import os

from todoist_api_python.api import TodoistAPI

from compartido import PEQUEÑO_DESCANSO


todoist = TodoistAPI(os.environ["TODOIST_TOKEN"])


def organizarme_la_semana():
    print("Hola, bienvenido a su organización de la semana.")
    time.sleep(PEQUEÑO_DESCANSO)

    print("\nPrimero, vamos a abrir su lista de quehaceres.")
    webbrowser.open_new("https://todoist.com/app/upcoming")

    print("También, vamos a abrir su calendario. Considerelo.")
    webbrowser.open_new("https://outlook.office.com/calendar/view/week")

    print("Por favor, coloque las ventanas para poder ver las dos a la vez.")

    time.sleep(PEQUEÑO_DESCANSO)

    print("\nAhora, por favor (presione Enter cuando haya cumplido cada instrucción):")
    input("- vea las tareas atrasadas. Elija nuevas fechas de vencamiento para ellas.")
    input(
        "- también vea las tareas de hoy y próximo, asegúrese que las fechas estén razonables"
    )
    input(
        "- añada etiqueta @schedule_me a las tareas que quiere agregar a tu calendario"
    )

    tareas_todoist = [
        tarea.content + "\n- desde Todoist"
        for tarea in todoist.get_tasks(filter="@regular")
    ]

    tareas_otro = [
        "ir al gymnasio\n- no después de las 9",
        "Duolingo",
        "cocinar\n- también decida cuándo ir de compras, y qué hacer",
        "esto, organizarte la semana",
    ]

    todas_las_tareas = tareas_todoist + tareas_otro

    print("\nVamos a mostrarle tareas que usted tiene que hacer.")
    print(
        "Al mostrarselo, añada un evento a tu calendario con úbicacion que le dirá dónde y cuándo hacerlo."
    )
    print(
        "Puede que tenga que hacer la tarea mas que una vez en la semana (por ejemplo, cocinar)"
    )

    for i, tarea in enumerate(todas_las_tareas):
        input(f"\n{i+1}. {tarea}")

    print("\nHecho, gracias. Que tengas una semana organizada.")
