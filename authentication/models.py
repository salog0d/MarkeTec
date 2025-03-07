from django.db import models
from django.core.exceptions import ValidationError  # Use the correct import
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class User(models.Model):
    # Define validator function outside the class or as a static method
    def validate_email_domain(value):
        # Get the domain part of the email
        try:
            domain = value.split('@')[1]
        except IndexError:
            # This will catch invalid email formats, though Django's EmailField
            # should already catch most formatting issues
            raise ValidationError("Invalid email format")
        
        # Check if domain matches your requirements
        allowed_domains = ['tec.mx', 'tecmilenio.mx']
        if domain not in allowed_domains:
            raise ValidationError(f"Email must be from one of these domains: {', '.join(allowed_domains)}")

    # Convert CAMPUS_OPTIONS to the correct format for choices
    CAMPUS_CHOICES = [
        (item["abbreviation"], item["campus"]) 
        for item in [
            {"campus": "Aguascalientes", "abbreviation": "AGS"},
            {"campus": "Chiapas", "abbreviation": "CHP"},
            {"campus": "Chihuahua", "abbreviation": "CHI"},
            {"campus": "Mexico City", "abbreviation": "CDMX"},
            {"campus": "Ciudad Juárez", "abbreviation": "CJZ"},
            {"campus": "Cuernavaca", "abbreviation": "CVA"},
            {"campus": "State of Mexico", "abbreviation": "CEM"},
            {"campus": "Guadalajara", "abbreviation": "GDL"},
            {"campus": "Hidalgo", "abbreviation": "HGO"},
            {"campus": "Irapuato", "abbreviation": "IRA"},
            {"campus": "Laguna", "abbreviation": "LAG"},
            {"campus": "León", "abbreviation": "LEO"},
            {"campus": "Monterrey", "abbreviation": "MTY"},
            {"campus": "Morelia", "abbreviation": "MOR"},
            {"campus": "Puebla", "abbreviation": "PUE"},
            {"campus": "Querétaro", "abbreviation": "QRO"},
            {"campus": "San Luis Potosí", "abbreviation": "SLP"},
            {"campus": "Santa Fe", "abbreviation": "CSF"},
            {"campus": "Sinaloa", "abbreviation": "SIN"},
            {"campus": "Sonora Norte", "abbreviation": "SON"},
            {"campus": "Tampico", "abbreviation": "TAM"},
            {"campus": "Toluca", "abbreviation": "TOL"},
            {"campus": "Veracruz", "abbreviation": "VER"},
            {"campus": "Zacatecas", "abbreviation": "ZAC"}
        ]
    ]

    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)  # Fixed typo 'mac_length'
    bio = models.CharField(max_length=200)
    age = models.IntegerField(MinValueValidator(18), MaxValueValidator(100))  # Changed to IntegerField as age is typically a number
    email = models.EmailField(validators=[validate_email_domain], unique=True)  # Added brackets to make it a list
    campus = models.CharField(max_length=10, choices=CAMPUS_CHOICES)  # Changed to CharField, not DateField