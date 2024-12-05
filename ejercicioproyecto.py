from datetime import date
from typing import List

class Usuario:
    def _init_(self, id: int, nombre: str, direccion: str, telefono: str, email: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.prestamos: List[Prestamo] = []

    def registrar_usuario(self):
        print(f"Usuario {self.nombre} registrado correctamente.")

    def actualizar_datos(self, nueva_direccion: str = None, nuevo_telefono: str = None):
        if nueva_direccion:
            self.direccion = nueva_direccion
        if nuevo_telefono:
            self.telefono = nuevo_telefono
        print(f"Datos del usuario {self.nombre} actualizados.")


class Bibliotecario:
    def _init_(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

    def validar_registro(self, usuario: Usuario) -> bool:
        if usuario.nombre and usuario.email:
            print(f"Usuario {usuario.nombre} validado.")
            return True
        print(f"Usuario {usuario.nombre} no validado.")
        return False

    def gestionar_base_datos(self, articulo: 'Articulo'):
        print(f"Artículo {articulo.titulo} gestionado en la base de datos.")

    def validar_prestamo(self, prestamo: 'Prestamo') -> bool:
        if prestamo.usuario and prestamo.articulo.disponible:
            print(f"Préstamo validado para el usuario {prestamo.usuario.nombre}.")
            return True
        print(f"Préstamo no válido para el usuario {prestamo.usuario.nombre}.")
        return False

    def registrar_articulo(self, articulo: 'Articulo'):
        print(f"Artículo {articulo.titulo} registrado en el catálogo.")

    def generar_reportes(self) -> 'Reporte':
        print("Generando reporte...")
        return Reporte(id=1, fecha_generacion=date.today(), contenido="Reporte generado.")


class Articulo:
    def _init_(self, id: int, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def registrar(self):
        print(f"Artículo {self.titulo} registrado correctamente.")

    def actualizar(self, nuevo_titulo: str = None, nuevo_autor: str = None):
        if nuevo_titulo:
            self.titulo = nuevo_titulo
        if nuevo_autor:
            self.autor = nuevo_autor
        print(f"Artículo {self.titulo} actualizado.")


class Prestamo:
    def _init_(self, id: int, fecha_inicio: date, fecha_fin: date, usuario: Usuario, articulo: Articulo):
        self.id = id
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.usuario = usuario
        self.articulo = articulo

    def realizar_prestamo(self) -> bool:
        if self.articulo.disponible:
            self.articulo.disponible = False
            print(f"Préstamo realizado para el usuario {self.usuario.nombre} del artículo {self.articulo.titulo}.")
            return True
        print(f"El artículo {self.articulo.titulo} no está disponible.")
        return False

    def finalizar_prestamo(self):
        self.articulo.disponible = True
        print(f"Préstamo del artículo {self.articulo.titulo} finalizado.")


class Reporte:
    def _init_(self, id: int, fecha_generacion: date, contenido: str):
        self.id = id
        self.fecha_generacion = fecha_generacion
        self.contenido = contenido

    def generar(self):
        print(f"Reporte ID: {self.id} generado el {self.fecha_generacion}.")