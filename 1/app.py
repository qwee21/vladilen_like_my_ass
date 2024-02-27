import sys
from datetime import timedelta
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import auto


class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonGoToCity.clicked.connect(self.goToCity)
        self.buttonDistanceToPoint.clicked.connect(self.distanceToPoint)
        self.buttonCostOfTrip.clicked.connect(self.costOfTrip)
        self.buttonTimeOfTrip.clicked.connect(self.timeOfTrip)
        self.buttonPriceLoss.clicked.connect(self.priceLoss)

    def goToCity(self):
        auto = self.getAuto()
        if auto.go_to_city([self.boxGPSXGoToCity.value(), self.boxGPSYGoToCity.value()]):
            QMessageBox.about(self, "Предупреждение", "Вы доедете до города")
        else:
            QMessageBox.about(self, "Предупреждение", "У вас не хватит топлива")

    def distanceToPoint(self):
        auto = self.getAuto()
        QMessageBox.about(self, "Вычисление", f"До точки {auto.distance_to_gps_point([self.boxGPSXDistanceToPoint.value(), self.boxGPSYDistanceToPoint.value()])} км")

    def costOfTrip(self):
        auto = self.getAuto()
        QMessageBox.about(self, "Вычисление", f"Цена поездки ₽{auto.trip_cost([self.boxGPSXCostOfTrip.value(), self.boxGPSYCostOfTrip.value()], self.boxFuelCostCostOfTrip.value())}")

    def timeOfTrip(self):
        auto = self.getAuto()
        QMessageBox.about(self, "Проверка", f"Время поездки {auto.time_trip([self.boxGPSXTimeOfTrip.value(), self.boxGPSYTimeOfTrip.value()])} ч")

    def priceLoss(self):
        auto = self.getAuto()
        QMessageBox.about(self, "Проверка", f"Автомобиль потерял ₽{auto.price_loss()}")

    def getAuto(self):
        return auto.Auto(color=self.boxColor.text(),
                         model=self.boxBrand.text(),
                         type_of_drive=self.boxDriveType.text(),
                         mileage=self.boxMileage.value(),
                         price_new=self.boxNewCost.value(),
                         price_now=self.boxNowCost.value(),
                         gps_now=[self.boxGPSX.value(), self.boxGPSY.value()],
                         max_speed=self.boxMaxSpeed.value(),
                         type_engine=self.boxEngineType.text(),
                         petrol_now=self.boxRemaningFuel.value(),
                         fuel_consumption=self.boxFuelConsumption.value(),
                         interval_service=timedelta(days=int(self.boxServiceInterval.value())))


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()