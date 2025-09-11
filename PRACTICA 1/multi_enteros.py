def _normaliza_entrada(x: str) -> tuple[int, str]:
    """
    Convierte una cadena con signo opcional a (signo, dígitos).
    signo: 1 o -1
    dígitos: solo caracteres '0'-'9' sin ceros a la izquierda (salvo "0")
    """
    x = str(x).strip()
    if not x:
        raise ValueError("Entrada vacía.")
    signo = 1
    if x[0] in "+-":
        signo = -1 if x[0] == "-" else 1
        x = x[1:]
    if not x.isdigit():
        raise ValueError(f"Entrada inválida: {x!r}")
    # quitar ceros a la izquierda
    x = x.lstrip("0") or "0"
    return signo, x


def _suma_cadenas(a: str, b: str) -> str:
    """
    Suma dos enteros no negativos representados como cadenas.
    Retorna la suma como cadena.
    """
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []

    while i >= 0 or j >= 0 or carry:
        da = ord(a[i]) - 48 if i >= 0 else 0
        db = ord(b[j]) - 48 if j >= 0 else 0
        s = da + db + carry
        res.append(chr((s % 10) + 48))
        carry = s // 10
        i -= 1
        j -= 1

    return "".join(reversed(res))


def _multiplica_por_digito(num: str, dig: int) -> str:
    """
    Multiplica una cadena numérica no negativa 'num' por un dígito 0..9.
    Retorna el producto como cadena.
    """
    if dig == 0 or num == "0":
        return "0"
    carry = 0
    res = []
    for i in range(len(num) - 1, -1, -1):
        d = ord(num[i]) - 48
        p = d * dig + carry
        res.append(chr((p % 10) + 48))
        carry = p // 10
    if carry:
        # descomponer carry en dígitos
        while carry:
            res.append(chr((carry % 10) + 48))
            carry //= 10
    return "".join(reversed(res))


def multiplicacion_primaria(a, b) -> str:
    """
    Multiplica dos enteros (str o int) usando el algoritmo de primaria con acarreos.
    Retorna el resultado como cadena (con signo si aplica).
    """
    sa, da = _normaliza_entrada(str(a))
    sb, db = _normaliza_entrada(str(b))

    # Si alguno es cero
    if da == "0" or db == "0":
        return "0"

    signo = 1 if sa == sb else -1

    # Construir suma de productos parciales
    acumulado = "0"
    ceros_sufijo = ""
    for ch in reversed(db):  # recorrer dígitos del multiplicador de derecha a izquierda
        dig = ord(ch) - 48
        parcial = _multiplica_por_digito(da, dig)
        if parcial != "0":
            parcial += ceros_sufijo
        acumulado = _suma_cadenas(acumulado, parcial)
        ceros_sufijo += "0"

    return ("-" if signo < 0 else "") + acumulado


if __name__ == "__main__":
    # Interfaz simple por consola
    try:
        x = input("Ingresa el primer número: ").strip()
        y = input("Ingresa el segundo número: ").strip()
        print("Resultado:", multiplicacion_primaria(x, y))
    except Exception as e:
        print("Error:", e)