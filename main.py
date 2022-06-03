import inquirer

from organizarme_la_semana import organizarme_la_semana
from standup_diario import standup_diario


def main():
    programa_elejido = inquirer.list_input(
        "Que quieres hacer?",
        choices=[
            ("Standup diario", standup_diario),
            ("Organizarme la semana", organizarme_la_semana),
        ],
    )

    programa_elejido()


if __name__ == "__main__":
    main()
