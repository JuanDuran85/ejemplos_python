preguntas_basicas: dict = {
    'pregunta_1': {
        'enunciado': ['Capital del Zulia: '],
        'alternativas': [
            ['Barinas', 0],
            ['Maracaibo', 1],
            ['San Fernando', 0],
            ['Barquisimeto', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['Capital de Barinas'],
        'alternativas': [
            ['Guanare', 0],
            ['Maracaibo', 0],
            ['Barinas', 1],
            ['Coro', 0]
        ]
    },

    'pregunta_3': {
        'enunciado': ['Capital de Tachira'],
        'alternativas': [
            ['San Cristobal', 1],
            ['Barinas', 0],
            ['Merida', 0],
            ['Trujillo', 0]
        ]
    }
}

preguntas_intermedias: dict = {
    'pregunta_1': {
        'enunciado': ['Capital de Paraguay'],
        'alternativas': [
            ['Lima', 0],
            ['Buenos Aires', 0],
            ['Sau Paulo', 0],
            ['Asuncion', 1]
        ]
    },
    'pregunta_2': {
        'enunciado': ['Capital de Finlandia'],
        'alternativas': [
            ['Dublín', 0],
            ['Lisboa', 0],
            ['Helsinki', 1],
            ['Madrid', 0]
        ]
    },

    'pregunta_3': {
        'enunciado': ['Capital de Dinamarca'],
        'alternativas': [
            ['Copenhague', 1],
            ['Belgrado', 0],
            ['Viena', 0],
            ['Lisboa', 0]
        ]
    }
}

preguntas_avanzadas: dict = {
    'pregunta_1': {
        'enunciado': ['Capital de Kenia'],
        'alternativas': [
            ['Bamako', 0],
            ['Nairobi', 1],
            ['Windhoek', 0],
            ['Maputo', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['Capital de Zambia'],
        'alternativas': [
            ['Lome', 0],
            ['Lusaka', 1],
            ['Tunez', 0],
            ['Kigali', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['Capital de  Nigeria'],
        'alternativas': [
            ['Pretoria', 0],
            ['Maputo', 0],
            ['Windhoek', 0],
            ['Abuya', 1]
        ]
    }
}

pool_preguntas: dict = {
    'basicas': preguntas_basicas,
    'intermedias': preguntas_intermedias,
    'avanzadas': preguntas_avanzadas
}