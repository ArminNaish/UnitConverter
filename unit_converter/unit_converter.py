unit_conversions = []
# 1 step conversions
unit_conversions.append({'from': 'milligram', 'to': 'gram','from_offset': 0,  'multiplicand': 1, 'denominator': 10**3, 'to_offset': 0})
unit_conversions.append({'from': 'gram', 'to': 'kilogram','from_offset': 0,  'multiplicand': 1, 'denominator': 10**3, 'to_offset': 0})
unit_conversions.append({'from': 'gram', 'to': 'megagram', 'from_offset': 0, 'multiplicand': 1, 'denominator': 10**6, 'to_offset': 0})
unit_conversions.append({'from': 'gram', 'to': 'gigagram','from_offset': 0,  'multiplicand': 1, 'denominator': 10**9, 'to_offset': 0})

unit_conversions.append({'from': 'gram', 'to': 'milligram','from_offset': 0,  'multiplicand': 10**3, 'denominator': 1, 'to_offset': 0})
unit_conversions.append({'from': 'kilogram', 'to': 'gram', 'from_offset': 0, 'multiplicand': 10**3, 'denominator': 1, 'to_offset': 0})
unit_conversions.append({'from': 'megagram', 'to': 'gram','from_offset': 0,  'multiplicand': 10**6, 'denominator': 1, 'to_offset': 0})
unit_conversions.append({'from': 'gigagram', 'to': 'gram','from_offset': 0,  'multiplicand': 10**9, 'denominator': 1, 'to_offset': 0})

unit_conversions.append({'from': 'degree fahrenheit', 'to': 'kelvin', 'from_offset': 459.67, 'multiplicand': 1, 'denominator': 1.8, 'to_offset': 0})
unit_conversions.append({'from': 'kelvin', 'to': 'degree celsius', 'from_offset': 0, 'multiplicand': 1, 'denominator': 1, 'to_offset': -273.15})

unit_conversions.append({'from': 'kelvin', 'to': 'degree fahrenheit', 'from_offset': 0, 'multiplicand': 1.8, 'denominator': 1, 'to_offset': -459.67})
unit_conversions.append({'from': 'degree celsius', 'to': 'kelvin', 'from_offset': 273.15, 'multiplicand': 1, 'denominator': 1, 'to_offset': 0})


units = []
units.append({'name': 'gram', 'symbol': 'g', 'quantity': 'mass', 'type': 'base', 'base_unit': 'gram'})
units.append({'name': 'kilogram', 'symbol': 'kg', 'quantity': 'mass', 'type': 'derived', 'base_unit': 'gram'})
units.append({'name': 'milligram', 'symbol': 'mg', 'quantity': 'mass', 'type': 'derived', 'base_unit': 'gram'})
units.append({'name': 'megagram', 'symbol': 'Mg', 'quantity': 'mass', 'type': 'derived', 'base_unit': 'gram'})
units.append({'name': 'gigagram', 'symbol': 'Gg', 'quantity': 'mass', 'type': 'derived', 'base_unit': 'gram'})
units.append({'name': 'nanogram', 'symbol': 'Ng', 'quantity': 'mass', 'type': 'derived', 'base_unit': 'gram'})

units.append({'name': 'kelvin', 'symbol': 'K', 'quantity': 'temperature', 'type': 'base', 'base_unit': 'kelvin'})
units.append({'name': 'degree fahrenheit', 'symbol': 'F', 'quantity': 'temperature', 'type': 'derived', 'base_unit': 'kelvin'})
units.append({'name': 'degree celsius', 'symbol': 'C', 'quantity': 'temperature', 'type': 'derived', 'base_unit': 'kelvin'})


# todo: use decimal
# todo: add rounding param or general rounding rule

def convert(value, from_unit, to_unit):

    if from_unit == to_unit:
        return value, from_unit

    [unit1] = [u for u in units if u['name'] == from_unit]
    [unit2] = [u for u in units if u['name'] == to_unit]

    if unit1['base_unit'] != unit2['base_unit']:
        raise Exception('Units are not convertable')

    # one step conversion
    uc = first_or_default([uc for uc in unit_conversions if uc['from'] == from_unit and uc['to'] == to_unit])
    if uc:
        result = ((value + uc['from_offset']) * uc['multiplicand'] / uc['denominator']) + uc['to_offset']
        return (result, uc['to'])
    
    # no conversion exists -> try two step conversion
    [base_unit] = [u['base_unit'] for u in units if u['name'] == to_unit]

    x1 = convert(value, from_unit, base_unit)
    return convert(*x1, to_unit)


def first_or_default(list, default=None):
    if list is None: return default
    if not list: return default
    return list[0]