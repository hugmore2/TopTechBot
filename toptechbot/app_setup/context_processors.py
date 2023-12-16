from app_setup.models import AppSetup


def context_processors_example(request):
    return {
        'example': 'Veio do context processor (example)'
    }


def app_setup(request):
    setup = AppSetup.objects.order_by('-id').first()
    return {
        'app_setup': setup,
    }
