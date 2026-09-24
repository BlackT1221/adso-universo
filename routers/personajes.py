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
    {
        "creador": "Christian Martínez",
        "nombre": "El Mago SQL",
        "clase": "Hechicero de las bases de datos",
        "habilidad_especial": "Hace inner joins con un solo hechizo",
        "nivel": 100
    },
    
    ,{
        "creador": "Duvan Rodriguez",
        "nombre": "Cristian Chiquitin",
        "clase": "Maestro six seven",
        "habilidad_especial": "Hacer perder aura a sus enemigos",
        "nivel": 10000
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