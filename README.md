# CasoFandroid_BoletosTren_U-K
En este repositorio se encuentra la actividad de los Boletos de Tren, el desarrolló del Caso FAndroid, con su debida lista de requisitos. Trabajo fue realizado por Kelly Triviño y Ubeimar Yepes

Lista de requisitos Funcionales y No Funcionales - Boletos de Tren
**Requisitos Funcionales:**

1. **Selección de Destino:**
   - El sistema debe mostrar un menú con una lista de posibles destinos de tren.
   - El usuario debe poder seleccionar un destino de la lista.

2. **Validación de Destino:**
   - El sistema debe verificar que el destino seleccionado es válido y existe en la lista de destinos disponibles.
   - Si el destino no es válido, el sistema debe mostrar un mensaje de error al usuario.

3. **Introducción de Tarjeta de Crédito:**
   - El usuario debe poder insertar una tarjeta de crédito válida en el lector correspondiente.
   - El sistema debe ser capaz de leer y validar la información de la tarjeta de crédito.

4. **Introducción de Identificación Personal:**
   - Después de seleccionar el destino y validar la tarjeta de crédito, el usuario debe introducir un número de identificación personal (PIN).
   - El sistema debe verificar la autenticidad del PIN introducido.

5. **Validación de Transacción:**
   - El sistema debe comunicarse con el servicio de procesamiento de pagos para validar la transacción con la tarjeta de crédito proporcionada.
   - Debe haber un mecanismo para manejar respuestas de aprobación o denegación de la transacción.

6. **Expedición de Billete:**
   - Si la transacción es aprobada y todas las validaciones son exitosas, el sistema debe generar y expedir un billete de tren al usuario.
   - El billete debe incluir la información relevante, como el destino, la fecha y la hora del viaje.

**Requisitos No Funcionales:**

1. **Seguridad:**
   - El sistema debe garantizar la seguridad de la información sensible, como los datos de la tarjeta de crédito y los PINS.
   - Debe cumplir con las normativas de seguridad y privacidad de datos, como el estándar PCI DSS.

2. **Usabilidad:**
   - La interfaz de usuario debe ser intuitiva y fácil de usar, con indicaciones claras para cada paso del proceso.
   - Los mensajes de error deben ser comprensibles para los usuarios y proporcionar orientación sobre cómo resolver problemas.

3. **Rendimiento:**
   - El sistema debe responder de manera rápida a las interacciones del usuario, evitando largos tiempos de espera.
   - La validación de la tarjeta de crédito y la transacción debe completarse en un tiempo razonable.

4. **Disponibilidad:**
   - El sistema debe estar disponible durante las horas de operación previamente definidas para que los usuarios puedan comprar billetes en cualquier momento.

5. **Tolerancia a Fallos:**
   - El sistema debe ser capaz de manejar errores inesperados, como interrupciones de conexión o fallos en la validación de tarjetas, de manera que los usuarios no se vean perjudicados.

6. **Escalabilidad:**
   - El sistema debe ser capaz de manejar un alto número de transacciones simultáneas, especialmente en momentos de alta demanda, como temporadas de vacaciones.

7. **Mantenimiento:**
   - Debe haber un plan de mantenimiento regular para garantizar que el sistema funcione correctamente y esté actualizado con los últimos estándares de seguridad y tecnología.

8. **Auditabilidad:**
   - El sistema debe ser capaz de registrar y mantener un historial de transacciones realizadas, incluyendo detalles como destinos, fechas y resultados de validación.
