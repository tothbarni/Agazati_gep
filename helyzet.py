class Helyzet:
    def __init__(self, id, hely, tipus, ipcim):
        self.id = int(id)
        self.hely = hely
        self.tipus = tipus
        self.ipcim = ipcim

    def __str__(self):
        return f"ID: {self.id}, Hely: {self.hely}, Típus: {self.tipus}, IP: {self.ipcim}"