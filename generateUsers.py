from allauth.account.models import EmailAddress
from authentication.models import User, Patient
import random

students = [
    ("ABBACI", "Rania Chahinez"),
    ("AGGOUNE", "LINA"),
    ("ALAMI", "BOUDKHIL"),
    ("BOUCHELAGHEM", "ZAKARIA"),
    ("BOUFELDJA", "MANEL"),
    ("BRAHIMI", "Denia"),
    ("CHOUIEUR", "ABDELHAMMID"),
    ("DIK", "AHMED YACINE"),
    ("DJAMAI", "ABDALLAH ALAA EDDINE"),
    ("DJEFFAL", "Belkis"),
    ("GUENANOU", "ABDELKRIM"),
    ("KADDOUR", "AYOUB"),
    ("KECHIDI", "ABDELILAH"),
    ("KERMALI", "ABDELFATAH"),
    ("KHALFI", "Sirine"),
    ("LAHMAR", "MOHAMMED ABDRRAHIM"),
    ("LAOUEDJ", "Sarah"),
    ("LARKEM", "MANEL"),
    ("MIMOUNI", "WAFAA"),
    ("OURRAD", "IMANE"),
    ("SAIDANI", "Celia"),
    ("TERTAG", "Maroua"),
    ("YALAOUI", "QADDOUR"),
    ("BELAMBRI", "SAMY"),
    ("BELIL", "ABDERRAOUF"),
    ("BEN KADDOUR", "ZOUBIDA IMENE"),
    ("BENDJEDDOU", "Randa Cheima"),
    ("BENMAMMAR", "MOHAMED HOUSSAM EDDINE"),
    ("BERKANE", "NAOUL"),
    ("BOUGHEDDA", "MEROUAN"),
    ("BOUKHELKHAL", "NASREDDINE"),
    ("BOUZIANE", "DJIHANE"),
    ("CHERIF", "ACHOUAK"),
    ("DERBALE", "MOHAMMED ISMAIL"),
    ("DJEBBAR", "MOHAMED AYMEN"),
    ("DJENANDAR", "MOHAMMED YACINE"),
    ("HANANI", "FETH-EDDINE"),
    ("KHATIR", "ABDELKADER"),
    ("LAKHMI", "KHAOULA"),
    ("LEKKAF", "SELSABIL"),
    ("MERZOUK BENSELLOUA", "AHMED YASSER"),
    ("MESMOUDI", "MOHAMMED AMINE"),
    ("MESSADI", "SAID ABDESSLEM"),
    ("RABIAI", "MAHFOUD"),
    ("SMATI", "Meriem"),
    ("ZELLAGUI", "ISKANDER"),
    ("ANNAD", "Walid"),
    ("BENGHAREZ", "SALAH EDDINE"),
    ("BENSALAH", "AMDJED"),
    ("BOUCHAFA", "MOHAMED EL AMINE"),
    ("BOULMA DACINE", "YOUSRA"),
    ("BOUSBA", "Mohamed Ali"),
    ("DELFI", "AYA"),
    ("DJOUAD", "KAWTHER"),
    ("FEDDAG", "MOHAMMED ZINEDDINE"),
    ("GHENNAI", "MOHAMMED"),
    ("KAGHOUCHE", "AHMED"),
    ("KEBBATI", "KHAOULA"),
    ("MAHDAOUI", "ABDELOUADOUD"),
    ("MAMOUR", "MOUNIRA"),
    ("MEBSOUT", "MAHMOUD- ABDELKHALEK"),
    ("MEGOURA", "HADJER"),
    ("MELKI", "YASSER"),
    ("MERZOUK", "ILYES REDA"),
    ("MORDI", "RIAD ZAKARIA"),
    ("MOULOUD", "Ahmed Abdelhakim"),
    ("MOUZAOUI", "ZAKARIA MOHAMMED"),
    ("SAHRAOUI", "SID AHMED"),
    ("ZAOUI", "Walid"),
    ("AKEBLERSANE", "MOHAMED AKRAM"),
    ("AZZAGE", "Houssem Eddine"),
    ("BENHOCINE", "AYYOUB"),
    ("BOUHERAOUA", "SARAH"),
    ("BOUSMAT", "ABDELMOUNAIM"),
    ("CHERGUI", "ZAKARIA"),
    ("DJELLALI", "FOUAD"),
    ("FAREK", "KHALED BAHAA EDDINE"),
    ("FIDMA", "MOHAMED ABDELILLAH"),
    ("HAMIDANI", "SARRA"),
    ("HAMMOUDA", "SELOUANE"),
    ("HARMEL", "AHMED RIAD"),
    ("KADDOURI", "HAMZA"),
    ("KADIRI", "MEHDI"),
    ("KREBBAZA", "ABDELBAKI"),
    ("LEBCIR", "ROUMAISSA"),
    ("MANAA", "ANOUAR"),
    ("MANSOUR", "ABOUBAKER"),
    ("SADOUN", "FERIEL"),
    ("SAFARI", "MAOUADDA"),
    ("TEBABNA", "AHMED RAMI"),
    ("YAHIAOUI", "ABDELKADER"),
    ("ABDELALI", "MOHAMED AMINE"),
    ("ABDELKADER KHAROUBI", "MOHAMED YASSINE"),
    ("AIT", "AKIL INASS KAOUTAR"),
    ("BAAHMED", "AHMED-RAFIK-EL MEHDI"),
    ("BENLARIA", "Ayyoub Yassine"),
    ("BERREGUI", "MOUSSAAB"),
    ("BOUAMRA", "Yousra"),
    ("BOUDINAR", "MOHAMED EL AMINE"),
    ("BOUMARAF", "Malak"),
    ("BOUNAB", "ABDELMOUNAIM"),
    ("DELENDA", "LAHCENE MOHAMMED EL AMINE"),
    ("FRICHE", "AMMAR NOUR EL-ISLAM"),
    ("GREBICI", "NOUR EL-HOUDA"),
    ("GUENDOUZI", "MOHAMED YANISS"),
    ("HADJ", "SADOK MOHAMMED NAZIM"),
    ("HARIRI", "ALI"),
    ("HASNAOUI", "SEYF EDDINE"),
    ("KHEMKHAM", "MOHAMED"),
    ("LOUADJ", "RANIA"),
    ("MEHADJI", "Mohamed anes"),
    ("OMARI", "SOUHIL"),
    ("TOUATI", "ABDERRAHMANE"),
    ("ABDELLATIF", "ABDERAOUF"),
    ("BENAISSA", "Abir"),
    ("BENGUEDDA", "ILHEM"),
    ("BOUMEZOUED", "Nadjet"),
    ("BOURIBA", "MANAL"),
    ("BOUSSAID", "ABDELKADER"),
    ("CHAALEL", "Idris"),
    ("DAFI", "Adel"),
    ("DJELLOUL DAOUADJI", "FADELA"),
    ("GUERZIZ", "Ines"),
    ("HAMDI", "Asma"),
    ("HAMMA", "RAHMA"),
    ("LACHEMAT", "MOHAMED FOUAD"),
    ("LAMRI", "ABDELLAH RAMDANE"),
    ("MARREF", "NOUR EL IMENE"),
    ("MEDDAH", "AMINA"),
    ("OUAHAB", "WAIL"),
    ("OUARAB", "Sarah"),
    ("SEDDAOUI", "M'HAMMED"),
    ("SELAMA", "ABDESSAMIE"),
    ("TALBI", "FERYAL BATOUL"),
    ("TOUNSI", "HIND"),
    ("ARBAOUI", "SLIMANE"),
    ("BELFAR", "ILYAS"),
    ("BELMILOUD", "ILIES DHIAEDDINE"),
    ("BENDADA", "AHMED MOUNSF RAFIK"),
    ("BENSALEM", "AKRAM"),
    ("CHOUGUI", "Abdeldjalil"),
    ("DADOUA", "HADRIA KAWTHAR"),
    ("DAOUD", "MOHAMMED-RYAD"),
    ("FERHI", "Asma"),
    ("KINIOUAR", "CHAIMA"),
    ("MANSOUR", "IMAD EDDINE"),
    ("MANSOURI", "IMENE"),
    ("MAZOUNI", "ABDELKADER"),
    ("MEDDAH", "HAFSA"),
    ("MEKHTICHE", "MOHAMED"),
    ("MERABET", "MUSTAPHA ZAKARIA"),
    ("NAIT", "MOHAMED SORAYA"),
    ("NOURINE", "YASSINE"),
    ("RAHMANI", "ABDELDJALIL"),
    ("SEGOUAT", "MOHCENE ABDELOUAHED"),
    ("ZAIRI", "AIMEN"),
    ("ZIANE", "MOHAMED"),
    ("ZITOUNI", "AYMEN"),
]

teachers = [
    ("ALLAL", "Lamia", "MC-B"),
    ("ACED", "Mohammed Reda", "MA-A"),
    ("BELFEDHAL", "Alaa Eddine", "MC-B"),
    ("BENDAOUD", "Fayssal", "MC-B"),
    ("ELOUALI", "Nadia", "MC-A"),
    ("FERROUI", "RAMZI", "MC-B"),
    ("CHAIB", "Souleyman", "MC-B"),
    ("GHEID", "Zakaria", "MC-B"),
    ("KECHAR", "Mohamed", "MC-B"),
    ("KAZI TANI", "Mohammed Yassine", "MC-B"),
    ("MALKI", "Abdelhamid", "MC-A"),
    ("MAHAMMED", "Nadir", "MC-A"),
    ("MESSABIHI", "Nafissa", "MC-B"),
    ("BADSI", "Hichem", "MC-B"),
    ("BELLAL", "Zouhir", "MC-B "),
    ("BENSLIMANE", "Sidi Mohammed", "Professor"),
]

teachers_edu_level = {
    "ALLAL": "MC-B",
    "ACED": "MA-A",
    "BELFEDHAL": "MC-B",
    "BENDAOUD": "MC-B",
    "ELOUALI": "MC-A",
    "FERROUI": "MC-B",
    "CHAIB": "MC-B",
    "GHEID": "MC-B",
    "KECHAR": "MC-B",
    "KAZI TANI": "MC-B",
    "MALKI": "MC-A",
    "MAHAMMED": "MC-A",
    "MESSABIHI": "MC-B",
    "BADSI": "MC-B",
    "BELLAL": "MC-B ",
    "BENSLIMANE": "Professor",
}


def rand_date(year1, year2):
    """
    Generate random date from 2 years
    """
    import datetime

    start_date = datetime.date(year1, 1, 1)
    end_date = datetime.date(year2, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def get_email(first_name, last_name):
    """
    Generate email from first name and last name
    """
    return f"{first_name[0].lower()}.{last_name.replace(' ','').lower()}@esi-sba.dz"


generatedUsers = [
    User(
        first_name=name[1],
        last_name=name[0],
        email=get_email(name[1], name[0]),
        date_of_birth=rand_date(1999, 2001),
        role="Patient",
    )
    for name in students
]
generatedTeacherUsers = [
    User(
        first_name=name[1],
        last_name=name[0],
        email=get_email(name[1], name[0]),
        date_of_birth=rand_date(1970, 1987),
        role="Patient",
    )
    for name in teachers
]
generatedEmails = [
    EmailAddress(user=user, email=user.email, verified=True, primary=True)
    for user in [*generatedUsers, *generatedTeacherUsers]
]
edu_levels = [
    "1CPI",
    "2CPI",
    "1CS",
    "2CS-ISI",
    "2CS-SIW",
    "3CS-ISI",
    "3CS-SIW",
]
generatedPatients = [
    Patient(user=user, type="Student", education_level=random.choice(edu_levels))
    for user in generatedUsers
]
generatedTeacherPatients = [
    Patient(
        user=user, type="Teacher", education_level=teachers_edu_level[user.last_name]
    )
    for user in generatedTeacherUsers
]
User.objects.bulk_create([*generatedUsers, *generatedTeacherUsers])
EmailAddress.objects.bulk_create(generatedEmails)
Patient.objects.bulk_create([*generatedTeacherPatients, *generatedPatients])
