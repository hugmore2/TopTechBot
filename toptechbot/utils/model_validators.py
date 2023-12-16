from django.core.exceptions import ValidationError


def validate_png(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError(
            'Apenas imagens em formato PNG são aceites pelo sistema')
