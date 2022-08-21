# write a script that takes a scv file as input and outputs a csv file as output.
# from the csv file, extract the first name, last name, and email address of each person.
# in the csv file, first name is the first column, last name is the second column, and email address is the third column.

import csv


class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return "{0} {1} {2}".format(self.first_name, self.last_name, self.email)

    def __repr__(self):
        return "{0} {1} {2}".format(self.first_name, self.last_name, self.email)

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and self.email == other.email

    def __ne__(self, other):
        return self.first_name != other.first_name or self.last_name != other.last_name or self.email != other.email

    def __lt__(self, other):
        return self.first_name < other.first_name or self.last_name < other.last_name or self.email < other.email

    def __le__(self, other):
        return self.first_name <= other.first_name or self.last_name <= other.last_name or self.email <= other.email

    def __gt__(self, other):
        return self.first_name > other.first_name or self.last_name > other.last_name or self.email > other.email

    def __ge__(self, other):
        return self.first_name >= other.first_name or self.last_name >= other.last_name or self.email >= other.email

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.email))

    def __add__(self, other):
        return Person(self.first_name + other.first_name, self.last_name + other.last_name, self.email + other.email)


def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            yield Person(row[0], row[1], row[2])


def write_csv(filename, people):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for person in people:
            writer.writerow(
                [person.first_name, person.last_name, person.email])


def main():
    people = list(read_csv("people.csv"))
    print(people)
    write_csv("people_copy.csv", people)


if __name__ == "__main__":
    main()
