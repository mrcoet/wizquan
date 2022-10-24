from db.models import Years, Months, States
from db import session


def get_years() -> list[dict]:
    options = []
    q = session.query(Years).all()
    for qq in q:
        temp_dict = {}
        temp_dict['value'] = str(qq.id)
        temp_dict['label'] = str(qq.id)
        options.append(temp_dict)
    return options


def get_months() -> list[dict]:
    options = []
    q = session.query(Months).all()
    for qq in q:
        tem_dict = {}
        tem_dict['value'] = str(qq.id)
        tem_dict['label'] = str(qq.month)
        options.append(tem_dict)
    return options 

def get_regions() -> list[dict]:
    options = []
    q = session.query(States).all()
    for qq in q:
        tem_dict = {}
        tem_dict['value'] = str(qq.id)
        tem_dict['label'] = f"{qq.name} - {qq.type}"
        options.append(tem_dict)
    return options 