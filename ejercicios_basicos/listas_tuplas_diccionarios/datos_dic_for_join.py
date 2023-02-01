lista_data: list[dict] = [
    {
        "fechahora": '2023-01-12',
        "transportadora": '2323',
        "tipobloqueo": 11,
        "ventana": '08:59:59',
        "flag_account": 'COSAS_HOGAR',
        "account": 'cosashogar55'
    },
    {
        "fechahora": '2023-01-12',
        "transportadora": '1111',
        "tipobloqueo": 11,
        "ventana": '08:59:59',
        "flag_account": 'COSAS_HOGAR',
        "account": 'cosashogar55'
    },
    {
        "fechahora": '2023-01-12',
        "transportadora": '5555',
        "tipobloqueo": 11,
        "ventana": '08:59:59',
        "flag_account": 'COSAS_HOGAR',
        "account": 'cosashogar55'
    },
]

values: str = ",".join(
    ''.join(
        f"('{carrier['fechahora']}','{carrier['transportadora']}',{carrier['tipobloqueo']},'{carrier['ventana']}','{carrier['flag_account']}','{carrier['account']}')"
    )
    for carrier in lista_data
)

print(values)