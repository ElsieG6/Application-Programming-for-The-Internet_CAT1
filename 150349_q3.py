class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Displays the employee's details."""
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        """Updates the employee's salary."""
        self.salary = new_salary
        print(f"Salary updated for {self.name} to {self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        """Adds an employee to the department."""
        if isinstance(employee, Employee):
            self.employees.append(employee)
            print(f"Added {employee.name} to {self.department_name} department.")

    def remove_employee(self, employee_id):
        """Removes an employee from the department by their employee ID."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print(f"Removed employee with ID {employee_id} from {self.department_name}.")
                return
        print(f"Employee with ID {employee_id} not found in {self.department_name}.")

    def display_all_employees(self):
        """Displays details of all employees in the department."""
        print(f"Department: {self.department_name}")
        for employee in self.employees:
            employee.display_details()
