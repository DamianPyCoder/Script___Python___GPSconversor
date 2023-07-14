# NOTAS DE INTERÉS

## Instalaciones previas  
#### Python:
Entra en la web: https://www.python.org/downloads  
Importante: Cuando estés instalando marca la casilla "Agregar Python al PATH" para que configure automáticamente las variables de entorno.  

#### Paquetes:  
pip install googlemaps  
pip install requests

#### Para que se ejecute en excel:  
pip install pywin32

#### Registro en la api de Google  
https://developers.google.com/maps/documentation/geocoding/get-api-key






## Ejemplo de como ejecutar scripts de python en Excel:  
- Instala la librería "pywin32" en tu entorno Python. Puedes hacerlo usando el administrador de paquetes "pip".  
- Abre Excel y crea un nuevo archivo de hoja de cálculo.
- Haz clic en la pestaña "Archivo" y selecciona "Opciones".
- En la ventana de opciones, selecciona "Personalizar cinta de opciones" en el panel izquierdo.
- En la lista de pestañas principales, marca la casilla "Desarrollador" y haz clic en "Aceptar".
- Ahora deberías tener una nueva pestaña "Desarrollador" en la cinta de opciones de Excel. Haz clic en ella.
- En la pestaña "Desarrollador", haz clic en el botón "Insertar" en el grupo "Controles".
- En la lista de controles, selecciona "Botón" bajo la sección "Controles de formulario".
- Haz clic y arrastra en la hoja de cálculo para crear el botón.
- Se abrirá el cuadro de diálogo "Asignar macro". Haz clic en "Nuevo" para crear una nueva macro.
- Se abrirá el editor de VBA (Visual Basic for Applications). En el editor de VBA, puedes escribir tu código Python utilizando la librería "pywin32"  


      # Ejemplo de script
      import win32com.client as win32
  
      def ejecutar_python():
      # Código de Python
       resultado = mi_funcion_python()

      # Escribir el resultado en una celda de Excel
       excel = win32.gencache.EnsureDispatch('Excel.Application')
       workbook = excel.ActiveWorkbook
       worksheet = workbook.ActiveSheet
       cell = worksheet.Range('A1')
       cell.Value = resultado

       # Cerrar Excel
       excel.Quit()

       ejecutar_python()


 

- Guarda el código VBA y cierra el editor de VBA.
- Ahora, cuando hagas clic en el botón que creaste en la hoja de cálculo, se ejecutará el código Python y el resultado se escribirá en la celda A1 de la hoja de cálculo.




## Ejemplo de como ejecutar scripts de python en Libre Office:  
  
- Abre LibreOffice Calc y crea un nuevo archivo de hoja de cálculo.
- Haz clic en la pestaña "Herramientas" y selecciona "Macros" y luego "Editar macros".
- Se abrirá el editor de macros de LibreOffice Basic. En el editor de macros, puedes escribir tu código Python utilizando la interfaz de Python para LibreOffice Basic. Aquí tienes un ejemplo básico:

      Sub EjecutarPython
      # Código de Python
      resultado = mi_funcion_python()

      # Escribir el resultado en una celda de Calc
      hoja = ThisComponent.Sheets(0)
      celda = hoja.getCellRangeByName("A1")
      celda.Value = resultado
      End Sub

- Guarda el código y cierra el editor de macros.
- Regresa a la hoja de cálculo en LibreOffice Calc.
- Haz clic derecho en la barra de herramientas y selecciona "Personalizar la barra de herramientas".
- En la pestaña "Comandos", selecciona la categoría "Macro" en el panel izquierdo.
- En el panel derecho, busca la macro que creaste ("EjecutarPython") y arrástrala a la barra de herramientas.
- Ahora tendrás un botón en la barra de herramientas que ejecutará la macro y aplicará el código Python a la hoja de cálculo.
