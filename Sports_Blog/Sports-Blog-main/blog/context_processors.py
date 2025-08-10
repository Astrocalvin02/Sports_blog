from .models import SportCategory

def categories_processor(request):
    return {'categories': SportCategory.objects.all()}