from fastapi import APIRouter

router = APIRouter()

@router.get("/personaje/lorena")
def obtener_personaje():
    return {
        "nombre": "Maga Lorena",
        "clase": "Hechicera Python",
        "nivel": 10,
        "habilidad_especial": "Lanzar FastAPIs a supervelocidad"
    }
