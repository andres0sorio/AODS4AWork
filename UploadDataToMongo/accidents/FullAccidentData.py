from .AccidentData import AccidentData


class FullAccidentData(AccidentData):
    """Clase que describe los datos entregados por el cliente sobre accidentes viales"""
    def __init__(self, information):
        super().__init__()

        self.client = information.client
        self.client_name = information.client_name
        self.client_contact = information.client_contact
        self.client_phone = information.client_phone
        self.data_origin = information.data_origin

        self.id_accident = 0
        self.date = None
        self.day_week = ""
        self.month = ""
        self.year = ""
        self.location = ""
        self.abs_design = 0
        self.n_incident = 0
        self.vehicles_involved = ""
        self.total_injured = 0
        self.total_death = 0
        self.total_minor_injured = 0
        self.total_serious_injured = 0
        self.accident_class = ""
        self.infrastructure_affected = ""
        self.accident_type = ""
        self.accident_cause = ""
        self.conditions = ""
        self.description = ""
        self.post_accident_actions = None

    def set_id_accident(self, x):
        if x is "":
            self.id_accident = float('nan')
        else:
            self.id_accident = int(x)

    def set_date(self, x):
        if x is "":
            self.date = float('nan')
        else:
            self.date = x

    def set_day_week(self, x):
        if x is "":
            self.day_week = float('nan')
        else:
            self.day_week = x

    def set_month(self, x):
        if x is "":
            self.month = float('nan')
        else:
            self.month = x

    def set_year(self, x):
        if x is "":
            self.year = float('nan')
        else:
            self.year = int(x)

    def set_location(self, x):
        if x is "":
            self.location = float('nan')
        else:
            self.location = x

    def set_abs_design(self, x):
        if x is "":
            self.abs_design = float('nan')
        else:
            self.abs_design = x

    def set_n_incident(self, x):
        if x is "":
            self.n_incident = float('nan')
        else:
            self.n_incident = int(x)

    def set_vehicles_involved(self, x):
        if x is "":
            self.vehicles_involved = float('nan')
        else:
            self.vehicles_involved = x

    def set_total_injured(self, x):
        if x is "":
            self.total_injured = float('nan')
        else:
            self.total_injured = int(x)

    def set_total_death(self, x):
        if x is "":
            self.total_death = float('nan')
        else:
            self.total_death = int(x)

    def set_total_minor_injured(self, x):
        if x is "":
            self.total_minor_injured = float('nan')
        else:
            self.total_minor_injured = int(x)

    def set_total_serious_injured(self, x):
        if x is "":
            self.total_serious_injured = float('nan')
        else:
            self.total_serious_injured = int(x)

    def set_accident_class(self, x):
        if x is "":
            self.accident_class = float('nan')
        else:
            self.accident_class = x

    def set_infrastructure_affected(self, x):
        if x is "":
            self.infrastructure_affected = float('nan')
        else:
            self.infrastructure_affected = x

    def set_accident_type(self, x):
        if x is "":
            self.accident_type = float('nan')
        else:
            self.accident_type = x

    def set_accident_cause(self, x):
        if x is "":
            self.accident_cause = float('nan')
        else:
            self.accident_cause = x

    def set_conditions(self, x):
        if x is "":
            self.conditions = float('nan')
        else:
            self.conditions = x

    def set_description(self, x):
        if x is "":
            self.description = float('nan')
        else:
            self.description = x

