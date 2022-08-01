from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError

# valid_unit_measurements = ['kg', 'gm', 'oz', 'lbs', 'pounds']

#base validation to test what exactly user is entering
def validate_unit(value):
    # if value not in valid_unit_measurements:
    #     raise ValidationError(f"your {value} is not valide unit of measure")
    # better to use pint
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"your {value} is not valide unit of measure")
    except:
        raise ValidationError(f"your {value} is invalid")
    
