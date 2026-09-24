from fastapi import APIRouter

router = APIRouter(prefix="/personajes", tags=["Universo Personajes"])

# =====================================================================
# LISTA MAESTRA DEL UNIVERSO
# Instrucciones: Cada aprendiz debe agregar un diccionario a esta lista 
# con los datos de su personaje. ¡NO BORRES LOS PERSONAJES DE OTROS!
# =====================================================================

UNIVERSO = [
    {
        "creador": "Instructor",
        "nombre": "El Arquitecto FastAPI",
        "clase": "Mago del Backend",
        "habilidad_especial": "Resuelve Bugs 500 con la mirada",
        "nivel": 99
    }
    # ⬇ AGREGA TU PERSONAJE AQUÍ ABAJO (Recuerda poner la coma si eres el primero) ⬇
    ,{
        "creador": "Christian Martínez",
        "nombre": "El Mago SQL",
        "clase": "Hechicero de las bases de datos",
        "habilidad_especial": "Hace inner joins con un solo hechizo",
        "nivel": 100
    }
    ,{
        "creador": "Luna Hernandez",
        "nombre": "Lyra Noctis",
        "clase": "Hechicero Espacial",
        "habilidad_especial": "Crear portales entre planetas",
        "nivel": 150
    ,{
        "creador": "Maria Paula Padilla Calderon",
        "nombre": "Don Error 500",
        "clase": "Villano informatico",
        "habilidad_especial": "Crear mucho caos a su alrededor",
        "nivel": 98
    }
    ,{
        "creador": "Michell Aranzalez",
        "nombre": "El Guerrero Del Codigo",
        "clase": "Heroe del codigo",
        "habilidad_especial": "Rafagas de codigo limpio que elimina varios enemigos en segundos",
        "nivel": 90
    }
]

@router.get("/")
def obtener_todos_los_personajes():
    """Retorna el censo completo de personajes creados por la clase."""
    return {
        "total_creadores": len(UNIVERSO),
        "personajes": UNIVERSO
    }

@router.get("/{creador}")
def buscar_por_creador(creador: str):
    """Filtra los personajes creados por un aprendiz específico."""
    resultados = [p for p in UNIVERSO if p["creador"].lower() == creador.lower()]
    return {"personajes": resultados}