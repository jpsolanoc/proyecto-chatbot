import requests
from .configuracion import ipServer

def obtener_todas_empresas(page_init, page_end, token, filtro, valor, unidad_negocio, unidades_negocio):
    try:
        # Construir el cuerpo de la solicitud
        request_body = {
            'unidadNegocio': unidad_negocio,
            'unidadesNegocio': unidades_negocio,
        }
        if filtro and valor:
            request_body[filtro] = valor
        
        # Realizar la solicitud POST
        url = ipServer + 'empresa/busqueda'
        headers = {'token': token}
        params = {'page': page_init, 'size': page_end}
        response = requests.post(url, json=request_body, params=params, headers=headers)

        return response
    except requests.exceptions.RequestException as e:
        raise Exception('Error al realizar la solicitud: {}'.format(str(e)))
