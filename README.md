# Gestor de Tareas con Recordatorios

Este proyecto consiste en una aplicación de consola que permite a los usuarios gestionar sus tareas diarias y recibir recordatorios sobre tareas próximas. La aplicación está diseñada para cumplir con los siguientes requisitos:

## Funcionalidades principales:
1. **Agregar tarea:** Los usuarios pueden agregar una nueva tarea especificando el título, la descripción, la prioridad, la categoría y la fecha de vencimiento.
2. **Marcar tarea como completada:** Los usuarios pueden marcar una tarea como completada, lo que la moverá a la lista de tareas completadas.
3. **Mostrar tareas pendientes:** Los usuarios pueden ver todas las tareas que aún no han sido completadas.
4. **Mostrar tareas completadas:** Los usuarios pueden ver todas las tareas que han sido marcadas como completadas.
5. **Cambiar estado de tarea:** Los usuarios pueden cambiar el estado de una tarea pendiente a completada o viceversa.
6. **Salir:** Los usuarios pueden salir de la aplicación cuando lo deseen.

Estas funcionalidades permiten a los usuarios gestionar sus tareas de manera efectiva, manteniendo un registro claro de las tareas pendientes y completadas, así como la capacidad de agregar nuevas tareas y ajustar su estado según sea necesario.

## Patrones de Diseño Utilizados:
1. **Singleton:** Se utiliza el patrón Singleton para el Gestor de Tareas, asegurando que solo exista una única instancia de la clase TaskManagerSingleton en toda la aplicación. Esto garantiza que todas las operaciones de gestión de tareas se realicen en la misma instancia y se mantenga la coherencia de los datos.
2. **Strategy:** Se emplea el patrón Strategy para la visualización de las tareas en la consola. Esto permite cambiar fácilmente el modo en que se muestran las tareas sin modificar el código de la lógica de negocio. En este caso, se ha implementado una estrategia específica, ConsoleTaskDisplayStrategy, para mostrar las tareas en forma de tabla en la consola.

## Cumplimiento de Requisitos:
- La aplicación cumple con todos los requisitos especificados en la descripción del proyecto.
- Permite a los usuarios agregar nuevas tareas con título, descripción y fecha de vencimiento opcional.
- Los usuarios pueden marcar tareas como completadas y ver tanto las tareas pendientes como las completadas.
- Se han implementado notificaciones para informar a los usuarios cuando una tarea está próxima a su fecha de vencimiento, lo que les permite estar al tanto de las tareas importantes.

La aplicación ha sido desarrollada siguiendo los principios de los patrones de diseño Singleton y Strategy, lo que contribuye a su estructura modular y mantenibilidad. Además, cumple con todas las funcionalidades requeridas y proporciona una experiencia de usuario intuitiva para la gestión efectiva de tareas.
