-- Problem 01
CREATE DATABASE [Minions]

GO

USE [Minions]

GO

-- Problem 02
CREATE TABLE [Minions](
	[Id] INT PRIMARY KEY NOT NULL,
	[Name] NVARCHAR(50) NOT NULL,
	[Age] INT

)

CREATE TABLE [Towns](
	[Id] INT PRIMARY KEY NOT NULL,
	[Name] NVARCHAR(85) NOT NULL

)

-- Problem 03
-- Alter is command to update STRUCTURE and CONSTRAINTS of the Table
ALTER TABLE Minions
ADD TownId INT;

ALTER TABLE Minions
ADD CONSTRAINT FK_Minions_Towns FOREIGN KEY (TownId) REFERENCES Towns(Id);
GO

-- Problem 04
-- Within INSERT Statenent () means a single row
INSERT INTO [Towns]([Id], [Name])
VALUES
(1, 'Sofia'),
(2, 'Plovdiv'),
(3, 'Varna')

INSERT INTO Minions (Id, Name, Age, TownId)
VALUES
    (1, 'Kevin', 22, 1),
    (2, 'Bob', 15, 3),
    (3, 'Steward', NULL, 2);
GO

--Problem 05
-- TRUNCATE = Factory Reset = Delete All Data
--TRUNCATE TABLE [Minions]

-- Problem 08
CREATE TABLE [Users](
	[Id] BIGINT PRIMARY KEY IDENTITY NOT NULL,
	[Username] 

)

