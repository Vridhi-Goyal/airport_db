drop database airport_db;
create database airport_db;

\c airport_db

CREATE TABLE Gates
(	GateNo INT NOT NULL,
	Gatelocation VARCHAR NOT NULL,
	PRIMARY KEY (GateNo)
 );

CREATE TABLE Crew
(	id INT NOT NULL,
	Fname VARCHAR(15) NOT NULL,
	Lname VARCHAR(15) NOT NULL,
	Age INT NOT NULL,
	SSN INT NOT NULL,
	Gender CHAR NOT NULL,
	GateNo INT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (GateNo) REFERENCES GATES(GateNo)
 );

CREATE TABLE Hangar
(	h_id INT NOT NULL,
	h_loc VARCHAR NOT NULL,
	PRIMARY KEY (h_id)
 );

CREATE TABLE Airline
(	Airline_id INT NOT NULL,
	AName VARCHAR(20) NOT NULL,
	PRIMARY KEY (Airline_id)
 );

CREATE TABLE Flight
(	Flight_id INT NOT NULL,
	No_of_Seats INT NOT NULL,
	Destination VARCHAR(20),
	Airline_id INT NOT NULL,
	GateNo INT NOT NULL,
	PRIMARY KEY (Flight_id),
	FOREIGN KEY (Airline_id) REFERENCES AIRLINE(Airline_id),
	FOREIGN KEY (GateNo) REFERENCES GATES(GateNo)
	
 );


CREATE TABLE Passenger
(	SSN INT NOT NULL,
	Firstnm VARCHAR(15) NOT NULL,
	Lastnm VARCHAR(15) NOT NULL,
	Phone INT NOT NULL, 
	Email VARCHAR(20),
	Gender CHAR NOT NULL,
	Age INT NOT NULL,
	Class VARCHAR(19) NOT NULL,
	Seat_No VARCHAR(8),
	Boarding_Date DATE NOT NULL,
	Boarding_time TIME NOT NULL,
	Flight_id INT NOT NULL,
	PRIMARY KEY (SSN),
	FOREIGN KEY (Flight_id) REFERENCES FLIGHT(Flight_id)
 );


CREATE TABLE Luggage
(	l_id INT NOT NULL,
	Pass_SSN INT NOT NULL,
	PRIMARY KEY (l_id),
	FOREIGN KEY (Pass_SSN) REFERENCES PASSENGER(SSN) 
 );



CREATE TABLE Runway
(	R_id INT NOT NULL,
	Length INT NOT NULL,
	PRIMARY KEY (R_id)
 );


CREATE TABLE Pilot
(	Pid INT NOT NULL,
	Fname VARCHAR(15) NOT NULL,
	Lname VARCHAR(15) NOT NULL,
	Age INT NOT NULL,
	PSSN INT NOT NULL,
	Gender CHAR(2) NOT NULL,
	Salary DECIMAL(10,2),
	Status VARCHAR, 
	Airline_id INT,
	Flight_id INT,
	PRIMARY KEY (Pid,PSSN),
	FOREIGN KEY (Airline_id) REFERENCES AIRLINE(Airline_id),
	FOREIGN KEY (Flight_id) REFERENCES FLIGHT(Flight_id)
 );

CREATE TABLE Plane
(	Tail_id INT NOT NULL,
	Manufacturer VARCHAR(15) NOT NULL,
	Serviced_last DATE,
	h_id INT NOT NULL,
	Airline_id INT NOT NULL,
	PRIMARY KEY (Tail_id),
	FOREIGN KEY (Airline_id) REFERENCES AIRLINE(Airline_id),
	FOREIGN KEY (h_id) REFERENCES HANGAR(h_id)
 );

CREATE TABLE Runs_on
(	Runway_id INT NOT NULL,
	Flight_id INT NOT NULL,
	PRIMARY KEY (Runway_id,Flight_id),
	FOREIGN KEY (Flight_id) REFERENCES FLIGHT(Flight_id),
	FOREIGN KEY (Runway_id) REFERENCES RUNWAY(R_id)
 );
CREATE TABLE Managed_by
(	id INT NOT NULL,
	Gate_No INT NOT NULL,
	PRIMARY KEY (id,Gate_No),
	FOREIGN KEY (id) REFERENCES CREW(id),
	FOREIGN KEY (Gate_No) REFERENCES GATES(GateNo)
 );

