while True:
    name = input('What is your first name/last name?')
    sugar_intake = float(input('What is the amount of your daily sugar intake (in grams)?'))
    fat_intake = float(input('What is the amount of your daily fat intake (in grams)?'))
    salt_intake = float(input('What is the amount of your daily salt intake (in milligrams)?'))
    health_status = 0
    if sugar_intake > 37.5 or fat_intake > 77 or salt_intake > 2300:
        health_status = 'unhealthy'
    else:
        health_status = 'healthy'

    class Patient:
        def __init__(self, name, sugar_intake, fat_intake, salt_intake, health_status):
            self.name = name
            self.sugar_intake = sugar_intake
            self.fat_intake = fat_intake
            self.salt_intake = salt_intake
            self.health_status = health_status
        def patient_health(self):
            print(f'Name: {self.name} / Sugar intake (grams): {self.sugar_intake} / Fat intake (grams): {self.fat_intake} / '
              f'Salt intake (milligrams): {self.salt_intake} / Health status: {self.health_status}')

    patient_object = Patient(name, sugar_intake, fat_intake, salt_intake, health_status)
    patient_object.patient_health()








