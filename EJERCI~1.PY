class TicketMachine:
    def __init__(self):
        self.destinations = ["Destino A", "Destino B", "Destino C"]
        self.prices = {"Destino A": 10, "Destino B": 15, "Destino C": 20}

    def display_menu(self):
        print("Seleccione su destino:")
        for index, destination in enumerate(self.destinations, start=1):
            print(f"{index}. {destination}")

    def select_destination(self):
        while True:
            self.display_menu()
            choice = input("Elija el número de su destino: ")
            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(self.destinations):
                    return self.destinations[choice_idx]
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Introduzca un número.")

    def process_payment(self, amount):
        # Simulamos el proceso de pago
        card_number = input("Ingrese el número de tarjeta de crédito: ")
        pin = input("Ingrese su PIN: ")
        # Aquí se verificaría la validez de la tarjeta y el PIN
        print(f"Se ha realizado un pago de ${amount} a través de la tarjeta {card_number}.")

    def issue_ticket(self, destination, amount):
        print(f"Billete para {destination} emitido.")
        print(f"Importe: ${amount}")
        print("¡Disfrute de su viaje!")

    def start(self):
        print("Bienvenido al sistema de expedición de billetes de tren.")
        destination = self.select_destination()
        amount = self.prices[destination]
        print(f"El importe del billete para {destination} es ${amount}.")
        self.process_payment(amount)
        self.issue_ticket(destination, amount)


# Crear una instancia de TicketMachine y comenzar el proceso
ticket_machine = TicketMachine()
ticket_machine.start()
