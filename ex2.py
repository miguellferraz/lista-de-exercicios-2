class Motor:
    def status(self):
        return "Motor: funcionando corretamente"

class Pneu:
    def status(self):
        return "Pneus: cheios e prontos para rodar"

class Veiculo(Motor, Pneu):
    def status(self):
        statusMotor = super().status()
        statusPneu = Pneu.status(self)

        return f"{statusMotor}\n{statusPneu}"

veiculo = Veiculo()
print(veiculo.status())
