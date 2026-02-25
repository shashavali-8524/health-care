"""Display all database tables and data"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings')
django.setup()

from django.contrib.auth.models import User
from patients.models import Patient
from doctors.models import Doctor
from mappings.models import PatientDoctorMapping

print("\n" + "="*120)
print("HEALTHCARE DATABASE - ALL TABLES AND DATA")
print("="*120)

# ═══════════════════════════════════════════════════════════════════
print("\n📋 TABLE: auth_user (Users)")
print("-"*120)
print(f"{'ID':<5} {'Username':<20} {'Email':<35} {'Active':<8} {'Staff':<8} {'Superuser':<10}")
print("-"*120)
for u in User.objects.all():
    print(f"{u.id:<5} {u.username:<20} {u.email:<35} {str(u.is_active):<8} {str(u.is_staff):<8} {str(u.is_superuser):<10}")
print(f"\nTotal Users: {User.objects.count()}")

# ═══════════════════════════════════════════════════════════════════
print("\n\n🏥 TABLE: doctors_doctor")
print("-"*120)
print(f"{'ID':<5} {'Name':<25} {'Specialization':<20} {'Phone':<16} {'Exp(yrs)':<10} {'Email':<30} {'Created By':<15}")
print("-"*120)
for d in Doctor.objects.all().select_related('created_by'):
    print(f"{d.id:<5} {d.name:<25} {d.specialization:<20} {d.phone or 'N/A':<16} {d.experience_years:<10} {d.email or 'N/A':<30} {d.created_by.username:<15}")
print(f"\nTotal Doctors: {Doctor.objects.count()}")

# ═══════════════════════════════════════════════════════════════════
print("\n\n👥 TABLE: patients_patient")
print("-"*120)
print(f"{'ID':<5} {'Name':<25} {'Age':<5} {'Gender':<8} {'Phone':<16} {'Address':<40} {'Created By':<15}")
print("-"*120)
for p in Patient.objects.all().select_related('created_by'):
    address_short = (p.address[:37] + '...') if p.address and len(p.address) > 40 else (p.address or 'N/A')
    print(f"{p.id:<5} {p.name:<25} {p.age:<5} {p.gender:<8} {p.phone or 'N/A':<16} {address_short:<40} {p.created_by.username:<15}")

print(f"\nTotal Patients: {Patient.objects.count()}")

# Show sample medical histories
print("\n📝 Sample Medical Histories:")
for p in Patient.objects.all()[:3]:
    print(f"\n  • {p.name} (Age {p.age}):")
    print(f"    {p.medical_history}")

# ═══════════════════════════════════════════════════════════════════
print("\n\n🔗 TABLE: mappings_patientdoctormapping")
print("-"*120)
print(f"{'ID':<5} {'Patient':<25} {'Age':<5} {'Doctor':<25} {'Specialization':<20} {'Assigned At':<20}")
print("-"*120)
for m in PatientDoctorMapping.objects.all().select_related('patient', 'doctor'):
    assigned = m.assigned_at.strftime('%Y-%m-%d %H:%M:%S')
    print(f"{m.id:<5} {m.patient.name:<25} {m.patient.age:<5} {m.doctor.name:<25} {m.doctor.specialization:<20} {assigned:<20}")

print(f"\nTotal Mappings: {PatientDoctorMapping.objects.count()}")

# ═══════════════════════════════════════════════════════════════════
print("\n\n📊 DATABASE STATISTICS")
print("-"*120)
print(f"  Users:    {User.objects.count()}")
print(f"  Doctors:  {Doctor.objects.count()}")
print(f"  Patients: {Patient.objects.count()}")
print(f"  Mappings: {PatientDoctorMapping.objects.count()}")

print("\n" + "="*120)
print("END OF DATABASE DUMP")
print("="*120 + "\n")
