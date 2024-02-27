import sys
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit
from PyQt6.QtGui import QDoubleValidator
from PyQt6 import QtWidgets

import task2


class App(design.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.distance_to_point_button.clicked.connect(self.distancetopoint)
        self.distance_to_origin_button.clicked.connect(self.distancetooriginpoint)
        self.closest_to_point_button.clicked.connect(self.closespoint)
        self.generate_rows.clicked.connect(self.generatetable)
        self.sherical_coordinat_button.clicked.connect(self.shericalcoordinat)
        self.cylindrical_coordinates_button.clicked.connect(self.cylindricalcoordinat)



    def distancetopoint(self):
        class_in = task2.Point3D(x = self.x1.value(), y = self.y1.value(), z = self.z1.value())
        QMessageBox.about(self, "Вычисление", f"Расстояние между точками = {class_in.distance_to_point([self.x2.value(), self.y2.value(), self.z2.value()])}")

    def distancetooriginpoint(self):
        class_in = task2.Point3D(x=self.x_distance_origin.value(), y=self.y_distance_origin.value(), z=self.z_distance_origin.value())
        QMessageBox.about(self, "Вычисление", f"Расстояние между до начала координат = {class_in.distance_to_origin()}")

    def generatetable(self):
        self.table_closest.clear()
        row_in_table = int(self.row_in_table.value())
        self.table_closest.setRowCount(row_in_table)
        double_validator = QDoubleValidator()
        self.table_closest.setColumnCount(3)
        column_labels = ['X', 'Y', 'Z']
        self.table_closest.setHorizontalHeaderLabels(column_labels)

        for row in range(row_in_table):
            for col in range(3):
                item = QLineEdit()
                item.setValidator(double_validator)
                self.table_closest.setCellWidget(row, col, item)

    def closespoint(self):
        class_in = task2.Point3D(x=self.x_closes_point.value(), y=self.y_closes_point.value(), z=self.z_closes_point.value())
        res = []

        for row in range(self.table_closest.rowCount()):
            x_item = self.table_closest.cellWidget(row, 0)
            y_item = self.table_closest.cellWidget(row, 1)
            z_item = self.table_closest.cellWidget(row, 2)
            if x_item is not None and y_item is not None and z_item is not None:
                x_text = x_item.text().strip().replace(",",".")
                y_text = y_item.text().strip().replace(",",".")
                z_text = z_item.text().strip().replace(",",".")
                if x_text != "" and y_text != "" and z_text != "":
                    res.append([float(x_text), float(y_text), float(z_text)])

        if res:
            closest_point = class_in.find_closest_point(res)
            QMessageBox.about(self, "Вычисление", f"Ближайшая точка это {closest_point}")
        else:
            QMessageBox.about(self, "Вычисление", "Введите координаты точек в таблицу.")

    def shericalcoordinat(self):
        class_in = task2.Point3D(x=self.sheric_x.value(), y=self.sheric_y.value(), z=self.sheric_z.value())
        QMessageBox.about(self,"Вычисление", f"Сферические координаты = {class_in.to_spherical_coordinates()}")

    def cylindricalcoordinat(self):
        class_in = task2.Point3D(x=self.cylindrical_x.value(), y=self.cylindrical_y.value(), z=self.cylindrical_z.value())
        QMessageBox.about(self, "Вычисление", f"Цилиндрические координаты = {class_in.to_spherical_coordinates()}")






def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()