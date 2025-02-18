-- 01 One-To-One Relationship


CREATE TABLE Persons (
		PersonID INT NOT NULL,
		FirstName VARCHAR(64),
		Salary MONEY,
		PassportID INT
)

CREATE TABLE Passports (
		PassportID INT,
		PassportNumber VARCHAR(64) UNIQUE
		
	
)

INSERT INTO Passports	
	VALUES (101, 'N34FG21B'),
	 (102, 'K65LO4R7'),
	 (103, 'ZE657QP2')

INSERT INTO Persons 
	VALUES (1, 'Roberto', 43300, 102),

		(2, 'Tom', 56100, 103),
		(3, 'Yana', 60200, 101 )

		--select * from Persons
		--select * from Passports

-- Part 03 - Create Primary Keys
ALTER TABLE Persons
ALTER COLUMN PersonID INT NOT NULL


ALTER TABLE Persons
ADD CONSTRAINT PK_Persons_PersonID PRIMARY KEY(PersonID)

ALTER TABLE Passports
ALTER COLUMN PassportID INT NOT NULL


ALTER TABLE Passports
ADD CONSTRAINT PK_Passports_PassportID PRIMARY KEY(PassportID)

--select * from Persons
--select * from Passports


-- Foreign key
ALTER TABLE Persons
ADD CONSTRAINT FK_Persons_Passports_PassportID 
	FOREIGN KEY(PassportID) REFERENCES Passports(PassportID)

--
ALTER TABLE Persons
ADD CONSTRAINT UQ_Person_PassportID UNIQUE(PassportID)

-----------------------------------------------------------------------------------------------------
-- 02. One-To-Many Relationship

CREATE TABLE Manufacturers
(
	ManufacturerID INT IDENTITY PRIMARY KEY,
	[Name] VARCHAR(20) NOT NULL,
	EstablishedOn DATE NOT NULL
)

CREATE TABLE Models
(
	ModelID INT IDENTITY(101,1) PRIMARY KEY,
	[Name] VARCHAR(20) NOT NULL,
	ManufacturerID INT REFERENCES Manufacturers(ManufacturerID) NOT NULL
)

INSERT INTO Manufacturers VALUES 
('BMW', '1916-03-07'),
('Tesla', '2003-01-01'),
('Lada', '1966-05-01')

INSERT INTO Models VALUES
('X1', 1),
('i6', 1),
('Model S', 2),
('Model X', 2),
('Model 3', 2),
('Nova', 3)

--select * FROM Manufacturers
---select * FROM Models

-------------------------------------------------------------------------------------------------------
---03. Many-To-Many Relationship
CREATE TABLE Students
(
	StudentID INT IDENTITY PRIMARY KEY,
	[Name] VARCHAR(20) NOT NULL
)

CREATE TABLE Exams
(
	ExamID INT IDENTITY(101,1) PRIMARY KEY,
	[Name] VARCHAR(20) NOT NULL
)

CREATE TABLE StudentsExams
(
	StudentID INT REFERENCES Students(StudentID),
	ExamID INT REFERENCES Exams(ExamID),

	CONSTRAINT PK_Students_Exams PRIMARY KEY(StudentID, ExamID)
)

INSERT INTO Students VALUES
('Mila'),
('Toni'),
('Ron')

INSERT INTO Exams VALUES
('SpringMVC'),
('Neo4j'),
('Oracle 11g')

INSERT INTO StudentsExams VALUES
(1, 101),
(1, 102),
(2, 101),
(3, 103),
(2, 102),
(2, 103)

----------------------------------------------------------------------------------------------
------------- 04. Self-Referencing

CREATE TABLE Teachers
(
	TeacherID INT IDENTITY(101,1) PRIMARY KEY,
	[Name] VARCHAR(20) NOT NULL,
	ManagerID INT REFERENCES Teachers(TeacherID)
)

INSERT INTO Teachers VALUES
('John', NULL),
('Maya', 106),
('Silvia', 106),
('Ted', 105),
('Mark', 101),
('Greta', 101)

---------------------------------------------------------------------------------


