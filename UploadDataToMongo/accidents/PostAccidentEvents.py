class PostAccidentEvents:
    """Clase que describe los datos entregados por el cliente sobre accidentes viales
     - Acciones y eventos que ocurren despues del accidente"""
    def __init__(self):
        self.first_call_time = None
        self.arrival_time = None
        self.response_time = None
        self.ambulance_dep_time = None
        self.ambulance_arr_time = None
        self.hospital = None
        self.ambulance_required = None
        self.time_departure_from_base = None
        self.time_arrival_to_base = None

    @property
    def first_call_time(self):
        return self.__first_call_time

    @first_call_time.setter
    def first_call_time(self, x):
        if x is "":
            self.__first_call_time = float('nan')
        else:
            self.__first_call_time = x

    def set_arrival_time(self, x):
        if x is "":
            self.arrival_time = float('nan')
        else:
            self.arrival_time = x

    def set_response_time(self, x):
        if x is "":
            self.response_time = float('nan')
        else:
            self.response_time = x

    def set_ambulance_dep_time(self, x):
        if x is "":
            self.ambulance_dep_time = float('nan')
        else:
            self.ambulance_dep_time = x

    def set_ambulance_arr_time(self, x):
        if x is "":
            self.ambulance_arr_time = float('nan')
        else:
            self.ambulance_arr_time = x

    def set_hospital(self, x):
        if x is "":
            self.hospital = float('nan')
        else:
            self.hospital = x

    def set_ambulance_required(self, x):
        if x is "":
            self.ambulance_required = float('nan')
        else:
            self.ambulance_required = x

    def set_time_departure_from_base(self, x):
        if x is "":
            self.time_departure_from_base = float('nan')
        else:
            self.time_departure_from_base = x

    def set_time_arrival_to_base(self, x):
        if x is "":
            self.time_arrival_to_base = float('nan')
        else:
            self.time_arrival_to_base = x

