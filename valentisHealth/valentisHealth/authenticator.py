from django.db.models import Q

def is_labs(self):
    return self.request.user.groups.filter(Q(name='Labs') | Q(name='Admin') | Q(name='Superadmin')).exists()

def is_radiology(self):
    return self.request.user.groups.filter(Q(name='Radiologist') | Q(name='Admin') | Q(name='Superadmin')).exists()

def is_doctor(self):
    return self.request.user.groups.filter(Q(name='Doctor') | Q(name='Admin') | Q(name='Superadmin')).exists()

def is_callcenter(self):
    return self.request.user.groups.filter(Q(name='Callcenter') | Q(name='Admin') | Q(name='Superadmin')).exists()

def is_nurse(self):
    return self.request.user.groups.filter(Q(name='Nurse') | Q(name='Admin') | Q(name='Superadmin')).exists()

def is_admin(self):
    return self.request.user.groups.filter(QQ(name='Admin') | Q(name='Superadmin')).exists()

def is_superadmin(self):
    return self.request.user.groups.filter(Q(name='Superadmin')).exists()
