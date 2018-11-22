from advanced_python_training.examples.ch2Classes.person import Person


class Employee(Person):

    def __init__(self, first_name, last_name, age, job_title, salary):
        super().__init__(first_name, last_name, age)
        self.job_title = job_title
        self.salary = salary

    def get_person(self):
        person = super().get_person()
        person['job_title'] = self.job_title
        person['salary'] = self.salary
        return person
