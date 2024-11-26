from rest_framework import serializers
from main.models.candidates import Candidate
from datetime import date
class CandidateSerializer(serializers.ModelSerializer):
    # SerializerMethodField bilan status_choices metodini aniqlash
    status_choices = serializers.SerializerMethodField()
    date_of_birth = serializers.DateField(format='%d.%m.%Y')
    age = serializers.SerializerMethodField()
    class Meta:
        model = Candidate
        fields = [
            'id',
            'name',  # Nomzod ismi
            'date_of_birth',  # Tug'ilgan sanasi
            'age',
            'address',  # Nomzod Manzili
            'experience',  # Tajriba yili
            'experience_name',  # Qaysi sohalarda ishlagani
            'skill',  # Ko'nikmalar
            'expected_salary',  # Kutilayotgan oylik maosh miqdori (so‘m)
            'phone_number',  # Nomzod telefon raqami
            'tg_username',  # Nomzod telegram username
            'description',  # Nomzod ozi haqida batafsil
            'created_on',  # Yaratilgan sana
            'status',
            'status_choices',  # Nomzodning statusi
        ]

    def get_status_choices(self, obj):
    # Barcha statuslar, ammo hozirgi statusni chiqarib tashlash
        all_choices = dict(Candidate.STATUS_CHOICES)
        all_choices.pop(obj.status, None)
        return list(all_choices.keys())
    
    def get_age(self, obj):
        # Calculate the age by subtracting the birth year from the current year
        today = date.today()
        age = today.year - obj.date_of_birth.year
        
        # Check if the birthday has occurred this year, if not subtract 1 from the age
        if today.month < obj.date_of_birth.month or (today.month == obj.date_of_birth.month and today.day < obj.date_of_birth.day):
            age -= 1
        
        return age

        