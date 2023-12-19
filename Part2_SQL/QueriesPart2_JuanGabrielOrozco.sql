/*
2. Write a query to create a data table ‘Student’ with the following attributes in it: 
‘Name', ‘Code', ‘Class’, ‘Age’, ‘Favorite Subject', ‘GPA’ (5.0 scale)
*/
CREATE TABLE Students (
	Name varchar(255),
	Code int,
	Class varchar(255),
	Age int,
	FavoriteSubject varchar(255),
	Gpa float(8)
);

--3. Insert at least 40 records in the last table with close to real data
INSERT INTO Students (Name, Code, Class, Age, FavoriteSubject, Gpa)
VALUES
('Juan', '1', 'Engineering', '25', 'Physics', '3.1'),
('Andrea', '2', 'Engineering', '19', 'Calculus', '4.2'),
('Carlos', '3', 'Engineering', '20', 'Physics', '3.5'),
('Esteban', '4', 'Engineering', '23', 'Mechanics', '4.8'),
('Sofia', '5', 'Engineering', '25', 'Metalurgy', '3.1'),
('Paula', '6', 'Engineering', '21', 'Physics', '3.5'),
('Andrey', '7', 'Engineering', '22', 'Calculus', '4.2'),
('Pablo', '8', 'Engineering', '25', 'Electromagnetism', '3.1'),
('Gabriel', '9', 'Engineering', '21', 'Physics', '3.7'),
('Andrey', '10', 'Engineering', '22', 'Calculus', '3.1'),
('Mary', '11', 'Medicine', '20', 'Biology', '3.5'),
('Isabella', '12', 'Medicine', '30', 'Morphology', '4.8'),
('Arturo', '13', 'Medicine', '28', 'Morphology', '4.1'),
('Anna', '14', 'Medicine', '23', 'Pathology', '4.8'),
('Sebastian', '15', 'Medicine', '20', 'Biology', '3.1'),
('Daniel', '16', 'Medicine', '21', 'Pathology', '4.1'),
('Lauren', '17', 'Medicine', '22', 'Pathology', '3.1'),
('Manuel', '18', 'Medicine', '26', 'Biology', '4.1'),
('Rodrigo', '19', 'Medicine', '21', 'Biology', '3.2'),
('Fernando', '20', 'Medicine', '23', 'Chemistry', '3.5'),
('Mara', '21', 'Pyshics', '25', 'Calculus', '3.2'),
('Antony', '22', 'Pyshics', '33', 'Thermodynamics', '4.6'),
('Antonella', '23', 'Pyshics', '20', 'Thermodynamics', '4.2'),
('Valentina', '24', 'Pyshics', '22', 'Thermodynamics', '3.5'),
('Alvaro', '25', 'Pyshics', '23', 'Quantum Mechanics', '3.7'),
('laura', '26', 'Pyshics', '21', 'Quantum Mechanics', '3.7'),
('Marcos', '27', 'Pyshics', '21', 'Thermodynamics', '3.5'),
('Mateo', '28', 'Pyshics', '25', 'Quantum Mechanics', '4.2'),
('Jimmy', '29', 'Pyshics', '21', 'Quantum Mechanics', '3.1'),
('Michael', '30', 'Pyshics', '22', 'Calculus', '2.8'),
('Allyson', '31', 'Nursing', '22', 'First Aids', '3.9'),
('Laura', '32', 'Nursing', '35', 'First Aids', '3.2'),
('John', '33', 'Nursing', '20', 'Palliative Care', '4.2'),
('Jhonny', '34', 'Nursing', '19', 'First Aids', '3.9'),
('Sergio', '35', 'Nursing', '23', 'Palliative Care', '4'),
('Vanessa', '36', 'Nursing', '22', 'First Aids', '3.9'),
('Daniela', '37', 'Nursing', '26', 'First Aids', '3.5'),
('Alejandro', '38', 'Nursing', '25', 'Palliative Care', '3.4'),
('Paul', '39', 'Nursing', '24', 'First Aids', '3.1'),
('Michelle', '40', 'Nursing', '26', 'Palliative Care', '4.2');

--4. Write a query to get the average GPA from all the students whose name starts with ‘A’.
SELECT AVG(gpa) FROM Students
WHERE name LIKE 'A%';

/*
5. Write a query to get the list of students that are in the same class, 
have a GPA higher than 3.5/5.0 and order them by Age and Name
SELECT * FROM Students
*/
WHERE Class='Nursing'
AND gpa > 3.5
ORDER BY age, name;

/*
6. Write a query to get the list of all the students with 
‘Name', ‘Code', ‘Class’, ‘Age’, ‘Favorite Subject', ‘GPA’
*/
SELECT Name, Code, Class, Age, FavoriteSubject, Gpa
FROM Students


