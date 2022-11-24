class listings():
    """
    Esta clase contiene los modelos de la tabla listings de la base de datos
    , contiene los campos: 
    owner es el usuario que crea el anuncio, es decir el dueño de la publicacion
    , title es el titulo del anuncio, de tipo string, max lenght 50.
    , category es la categoria del anuncio # validaciones multiselect con choices igualado a la funcion que contiene choices.py llamada CATEGORY_CHOICES
    , address es la direccion del anuncio, es un string
    , city es la ciudad del anuncio, es de tipo string
    , state es el estado del anuncio, aunque el campo no es usado, se preevee usarlo en un futuro, de tipo string, seria validado con un CITY_CHOICES
    , zipcode para el codigo postal del anuncio  tipo campo positivo, maxlenght de 4
    , description es la descripcion del anuncio, de tipo string.
    , price es el precio del anuncio, por defecto es 100MXN, esto se encuentra detallado en la pagina de politicas. price es un tipo de campo positivo

    photo_main, photo_1 es la foto principal del anuncio
    , photo_2, photo_3, photo_4, photo_5, photo_6, 
    is_published, es un booleano que indica si el anuncio esta publicado o no

    list_date es la fecha de creacion del anuncio, en este caso se usa la fecha actual por default
    
    choices.py es un archivo que se importa a models desde la aplicacion listings para poder obtener las opciones en el multiselect field.
    
    
    """
    #Modelos creados por Alexis Garcia Con validaciones y ajustes hechos por Antonio Hernandez.
