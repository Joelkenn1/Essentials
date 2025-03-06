-- create database Final;

CREATE TABLE Parent (
    Parent_Id INTEGER,
    Parent_Name VARCHAR(100) unique,
    Email VARCHAR(100),
    Social_Media VARCHAR(100),
    Phone_Number VARCHAR(20),
    Zip_Code INTEGER,
    In_Need BOOLEAN,
    Hourly_Pay VARCHAR(100),
    
    primary key (Parent_Id, Parent_Name)
);


CREATE TABLE BabySitter (
    BabySitter_Id INTEGER,
    BabySitter_Name VARCHAR(100) unique,
    Age VARCHAR(100),
    Email VARCHAR(100),
    Social_Media VARCHAR(100),
    Phone_Number VARCHAR(20),
    Zip_Code INTEGER,
    Experience_Years VARCHAR(100),
    Current_Availability BOOLEAN,
    Suggested_Hourly_Pay VARCHAR(100),
    Rating Integer,
    
    primary key(BabySitter_Id)
);

CREATE TABLE Child (
    Parent_Id INTEGER,
    Parent_Name VARCHAR(100),
    Child_Name VARCHAR(100),
    Age VARCHAR(100),
    Gender VARCHAR(20),
    Birth_Order VARCHAR(50),

    
    foreign key (Parent_Id, Parent_Name) references Parent (Parent_Id, Parent_Name),
    primary key(Parent_Id, Parent_Name, Child_Name)
    
);


CREATE TABLE Child_Needs (
    Parent_Id INTEGER,
	Parent_Name VARCHAR(100),
    Child_Name VARCHAR(100),
    Allergies VARCHAR(100),
    Diseases VARCHAR(100),
    Medications VARCHAR(100),
    Disabilities VARCHAR(100),
    Intrests VARCHAR(100),
    
    foreign key (Parent_Id, Parent_Name, Child_Name) references Child (Parent_Id, Parent_Name, Child_Name),
    primary key(Parent_Id, Parent_Name, Child_Name, Intrests)
);

CREATE TABLE Reviews (
    Parent_Id INTEGER,
    Parent_Name VARCHAR(100),
    BabySitter_Name VARCHAR(100),
    Rating Integer,
    Review VARCHAR(1000),

	foreign key (Parent_Id, Parent_Name) references Parent (Parent_Id, Parent_Name),
	foreign key (BabySitter_Name) references BabySitter (BabySitter_Name),
	primary key (Parent_Id, Parent_Name, BabySitter_Name, Rating) );

