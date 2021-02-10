from .models import Doctor
from table import Table
from table.columns import Column

class DoctorTable(Table):
    # id = Column(field='id')
    # name = Column(field='frist_name')
    class Meta:
        model = Doctor
        fields='__all__'