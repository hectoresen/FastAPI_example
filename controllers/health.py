import psutil
from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health"])
def get_health():
    memory_info = psutil.virtual_memory()
    
    return {
        "status": "OK",
        "memory": {
            "total": memory_info.total,
            "available": memory_info.available,
            "used": memory_info.used,
            "percent": memory_info.percent
        }
    }

class HealthController:
    pass
