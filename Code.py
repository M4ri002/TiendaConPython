# CREAMOS Y GUARDAMOS EL OBJETO USUARIO PRIVADO
class Usuario:
    def __init__(self, nombre, apellido, usuario, password):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__password = password

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, apellido):
        self.__apellido = apellido
    def get_usuario(self):
        return self.__usuario
    def set_usuario(self, usuario):
        self.__usuario = usuario
    def get_password(self):
        return self.__password
    def set_password(self, password):
        self.__password = password

Actual_User = Usuario('','','','')

def Registrar_user():
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    usuario = input("Introduce el nombre de usuario: ")
    password = input("Introduce tu contraseña: ")
    if ((usuario and password) == "Admin"):
        print("(No puedes registrar un Administrador)")
    else:
        User = Usuario(nombre, apellido, usuario,password)
        guardar_user(User)
#GUARDA EL USUARIO EN EL TXT
def guardar_user(Usuario):
    with open('Usuarios.txt','a') as archivo:
        archivo.write(f"{Usuario.get_nombre()},{Usuario.get_apellido()},{Usuario.get_usuario()},{Usuario.get_password()}\n")
    print("\nRegistrado correctamente...")

def login_user():
    user = input("\nUSUARIO: ")
    passw = input("PASSWORD: ")
    with open('Usuarios.txt', 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(', ')
            # print(partes)
            usuario_archivo = partes[0].split(',')[2] #Si no hago esto no me coge el valor del array que quiero
            password_archivo = partes[0].split(',')[3]

            if((user == usuario_archivo) and (passw == password_archivo)):
                if ((usuario_archivo == "Admin") and (password_archivo == "Admin")):
                    return "A"
                else:
                    Actual_User.set_nombre(partes[0].split(',')[0])
                    Actual_User.set_apellido(partes[0].split(',')[1])
                    Actual_User.set_usuario(partes[0].split(',')[2])
                    Actual_User.set_password(partes[0].split(',')[3])
                    return "C"
        else:
            print("\n\t***NO ESTAS REGISTRADO***\n \n")


def mostrar_usuarios():
    with open('Usuarios.txt', 'r') as archivo:
        lineas = archivo.readlines()
        print(f"\n{'NOMBRE':<18}{'APELLIDO':<15}{'USUARIO':<20}\n")
        for linea in lineas:
            campos = linea.strip().split(',')
            print(f"{campos[0]:<20}{campos[1]:<14}{campos[2]:<20}")
#BUSCA Y ELIMINA USUARIOS
def buscar_user():
    mostrar_usuarios()
    user = input("\nEscriba el USERNAME del usuario a eliminar: ")
    with open('Usuarios.txt', 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(', ')
            # print(partes)
            usuario_archivo = partes[0].split(',')[2]
            if(user == usuario_archivo):
                eliminar_usuario(user)
                return
def eliminar_usuario(user):
    resp = input("¿Desea eliminar el usuario?(s,n)\n>")
    if(resp == "s"):
        with open('Usuarios.txt', 'r+') as archivo:
            lineas = archivo.readlines()
            for indice, linea in enumerate(lineas):
                if user in linea:
                    lineas.pop(indice)
            archivo.seek(0)
            archivo.writelines(lineas)
            archivo.truncate()
            archivo.close()
    else:
        return

#MODIFICA LOS DATOS DEL OBJETO Y DESPUES EN EL TXT
def modificar_datos():
    opcion = input("\nQue desea modificar? (nº)\n1- Nombre\n2- Apellido\n3- Usuario\n4- Contraseña\n>")
    if(opcion == "1"):
        New = input("¿Cual sera su nuevo nombre?: ")
        Pivot_user = Actual_User.get_nombre()
        Actual_User.set_nombre(New)
        casilla = 0
    elif(opcion == "2"):
        New = input("¿Cual sera su nuevo Apellido?: ")
        Pivot_user = Actual_User.get_apellido()
        Actual_User.set_apellido(New)
        casilla = 1
    elif(opcion == "3"):
        New = input("¿Cual sera su nuevo Usuario?: ")
        Pivot_user = Actual_User.get_usuario()
        Actual_User.set_usuario(New)
        casilla = 2
    elif(opcion == "4"):
        New = input("¿Cual sera su nueva Contraseña?: ")
        Pivot_user = Actual_User.get_password()
        Actual_User.set_password(New)
        casilla = 3
    else:
            print("\n\t***Opcion incorrecta***\n")
            return
    with open('Usuarios.txt', 'r+') as archivo:
        lineas = archivo.readlines()
        for indice, linea in enumerate(lineas):
            campos = linea.strip().split(',')
            if (campos[casilla] == Pivot_user):
                campos[casilla] = New
                lineas[indice] = ','.join(campos) + '\n'
                break
        archivo.seek(0)
        archivo.writelines(lineas)
        archivo.truncate()
        archivo.close()



# CREAMOS Y GUARDAMOS EL OBJETO PRODUCTO PRIVADO
class Producto:
    def __init__(self, ID, nombre, precio):
        self.__ID = ID
        self.__nombre = nombre
        self.__precio = precio

    def get_ID(self):
        return self.__ID
    def set_ID(self, ID):
        self.__ID = ID
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio = precio

#GUARDA 
def introduce_producto():
    ID = "x" #(Esta programado como un valor autoincremental)
    nombre = input("Introduce el nombre : ")
    precio = input("Introduce el precio: ")

    product = Producto(ID,nombre,precio)
    guardar_datos(product)

def guardar_datos(Producto):
    with open('Productos.txt','r+') as archivo:
        lineas = archivo.readlines()
        if lineas:
            ultimo_id = int(lineas[-1].split(',')[0])
            nuevo_id = ultimo_id + 1
        # Establecer el primer ID como 1 si el archivo está vacío
        else:
            nuevo_id = 1

        archivo.write(f"{nuevo_id},{Producto.get_nombre()},{Producto.get_precio()}\n")


#BUSCA UN PRODUCTO PARA MODIFICARLO
def buscar_producto():
    opcion = input("\nQue desea modificar? (nº)\n1- ID\n2- PRODUCTO\n3- PRECIO\n>")
    if(opcion == "1"):
        prod = input("¿De que producto?: ")
        casilla = 0
    elif(opcion == "2"):
        prod = input("¿Que producto desea cambiar?: ")
        casilla = 1
    elif(opcion == "3"):
        prod = input("¿De que producto?: ")
        casilla = 2
    else:
            print("\n\t***Producto no encontrado***\n")
            return
    with open('Productos.txt', 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(', ')
            # print(partes)
            producto_archivo = partes[0].split(',')[1]
            val = partes[0].split(',')[casilla]

            if((prod == producto_archivo)):
                modificar_producto(val,casilla)
                return
        else:
            print("\n\t***Producto no encontrado***\n")
            return


#MODIFICA EL PRODUCTO
def modificar_producto(val,casilla):
    New = input("Escriba el nuevo valor: ")
    with open('Productos.txt', 'r+') as archivo:
        lineas = archivo.readlines()
        for indice, linea in enumerate(lineas):
            campos = linea.strip().split(',')
            if campos[casilla] == val:
                campos[casilla] = New
                lineas[indice] = ','.join(campos) + '\n'
                break
        archivo.seek(0)
        archivo.writelines(lineas)
        archivo.truncate()
        archivo.close()

def mostrar_productos():
    with open('Productos.txt', 'r') as archivo:
        lineas = archivo.readlines()
        print(f"{'ID':<5}{'PRODUCTO':<15}{'PRECIO':<8}\n")
        for linea in lineas:
            campos = linea.strip().split(',')
            print(f"{campos[0]:<5}{campos[1]:<15}{campos[2]:<8}")


#FACTURACION TOTAL
def fact_total():
    usr = input("1- Ver facturacion total\n2- Ver facturas de un usuario\n>")
    if(usr == "1"):
        total = 0
        with open('Facturas.txt', 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(', ')
                precio = float(partes[0].split(',')[2])
                total += precio
        print("\n\tTotal: ",total,"€")
        return total
    elif (usr == "2"):
        mostrar_usuarios()
        user = input("De que usuario las quieres ver?")
        with open('Facturas.txt', 'r') as archivo:
            lineas = archivo.readlines()
            print(f"{'ID':<5}{'USUARIO':<15}{'PRECIO':<8}\n")
            for linea in lineas:
                campos = linea.strip().split(',')
                if (user == campos[0]):

                    print(f"{campos[0]:<5}{campos[1]:<15}{campos[2]:<8}")
    else:
        print("**Opcion no valida**")
        return

def comprar_prod(user):
    val = input("Escriba el ID del producto que desea comprar (nº)\n>")
    with open('Productos.txt', 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(', ')
            # print(partes)
            producto_archivo = partes[0].split(',')[1]
            id_prod = partes[0].split(',')[0]
            precio_prod = partes[0].split(',')[2]
            if((val == id_prod)):
                with open('Facturas.txt', 'a') as archivo:
                    archivo.write(f"{user},{producto_archivo},{precio_prod}\n")
                    print("PRODUCTO ADQUIRIDO\n")
                return
        else:
            print("\n\t***Producto no encontrado***\n")
            return






Bool_Log = True
Bool_Cliente = False
Bool_Admin = False

#PANTALLA LOGIN
while Bool_Log == True:
    print("\nSeleccione una opción (nº)")
    opcion = input("\n1- LOGIN\n2- REGISTRARTE\n3- SALIR\n> ")
    if (opcion == "1"):
        Login_result = login_user()
        if (Login_result == "A"):
            print("(Estas logeado como Administrador)")
            Bool_Admin = True;
            Bool_Log=False;
            #MENU ADMIN
            while Bool_Admin == True:
                var = input("\n1- CREAR PRODUCTO\n2- MODIFICAR PRODUCTOS\n3- ELIMINAR USUARIOS\n4- FACTURACION TOTAL\n5- SALIR\n> ")
                if(var == "1"):
                    introduce_producto()
                if (var == "2"):
                    buscar_producto()
                if (var == "3"):
                    buscar_user()
                if (var == "4"):
                    fact_total()
                if (var == "5"):
                    Bool_Admin = False
                    Bool_Log = True
        if (Login_result == "C"):
            print("(Estas logeado como Cliente)")
            Bool_Cliente = True;
            Bool_Log=False;
            #MENU CLIENTES
            while Bool_Cliente == True:
                var = input("\n1- VER PRODUCTOS\n2- COMPRAR PRODUCTOS\n3- MODIFICAR MIS DATOS\n4- ATRÁS\n> ")
                if(var == "1"):
                    mostrar_productos();
                if (var == "2"):
                    comprar_prod(Actual_User.get_usuario())
                if (var == "3"):
                    modificar_datos()
                if (var == "4"):
                    Bool_Log = True
                    Bool_Cliente = False
    if (opcion == "2"):
        Registrar_user()
    if (opcion == "3"):
        Bool_Log = False