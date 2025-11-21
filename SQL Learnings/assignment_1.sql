use yethishwar;
show tables;

show databses

drop table students;
create table Students_Table(
	student_id Int Primary key,
    name Varchar(20),
    class Int,
    fees Int,
    age Int,
    teacher_id int);
    
Insert into Students_Table values(101, 'Rana', 8, 30000, 14, 1);
Insert into Students_Table values(102, 'Farhan', 2, 20000, 12, 2);
Insert into Students_Table values(103, 'Sadat', 5, 35000, 11, 3);
Insert into Students_Table values(104, 'Yethishwar', 7, 60000, 17, 4);
Insert into Students_Table values(105, 'Iqra', 10, 50000, 14, 5);
Insert into Students_Table values(106, 'Niharika', 2, 20000, 13, 2);
Insert into Students_Table values(107, 'Jhahnavi', 5, 10000, 10, 3);



create table Teachers_Table(
	teacher_id Int Primary key,
    name Varchar(20),
    subject varchar(10),
    gender Varchar(10),
    salary Int);
    
    
    
Insert into Teachers_Table values(1,"Arjun",'Python','Male', 50000);
Insert into Teachers_Table values(2,"Keerthi",'Java','FeMale', 20000);
Insert into Teachers_Table values(3,"Kiara",'Social','Female', 25000);
Insert into Teachers_Table values(4,"Preethi",'maths','FeMale', 10000);
Insert into Teachers_Table values(5,"Muneeb",'telugu','Male', 15000);
Insert into Teachers_Table values(6,"Chaitanya",'english','Male', 60000);
Insert into Teachers_Table values(7,"Siri",'OS','Female', 74000);
Insert into Teachers_Table values(8,"Anil",'SE','Male', 100000);



-- Display all student names and their class.
select name,class from Students_Table order by class; 

-- Show the names of teachers who teach Mathematics.
select name from Teachers_Table where subject = 'maths';

-- Find all students who are older than 15 years.
select * from Students_Table where age > 15;

-- List all students whose fees are greater than 5000, sorted from highest to lowest.
select * from Students_Table where fees > 50000 order by fees DESC;

-- Show all teachers with salary between 30,000 and 50,000.
select * from Teachers_Table where salary between 30000 and 75000;


-- Display each student’s name along with their teacher’s name.
select Students_Table.name, Teachers_Table.name 
from Students_table join Teachers_Table on Students_Table.teacher_id = Teachers_Table.teacher_id;

-- List students along with the subject taught by their teacher.
select Students_Table.name, Teachers_Table.subject 
from Students_table join Teachers_Table on Students_Table.teacher_id = Teachers_Table.teacher_id;

-- Find all female teachers and list the students assigned to them.
select Students_Table.name, Teachers_Table.name 
from Students_table join Teachers_Table on Students_Table.teacher_id = Teachers_Table.teacher_id
where Gender = 'FeMale';




-- Show total number of students in each class.
select count(student_id) as total_count from Students_Table;

-- Find the average fees paid by students for each class (GROUP BY class).
select class, avg(fees) as average_fees from Students_Table group by class order by class;



-- Show classes having more than 2 students.
select Students_Table.class, COUNT(Students_Table.student_id) as class_count
from Students_Table
group by Students_Table.class
having COUNT(Students_Table.student_id) < 1
order by Students_Table.class;



-- Find students whose teacher has a salary greater than 40,000.
select Students_Table.name, Teachers_Table.salary 
from Teachers_Table inner join Students_Table on Students_Table.teacher_id = Teachers_Table.teacher_id
where Teachers_Table.salary > 40000;


-- Fetch students who are assigned to teachers teaching ‘Social’.
select Students_Table.name, Teachers_Table.subject 
from Students_table join Teachers_Table on Students_Table.teacher_id = Teachers_Table.teacher_id
where Teachers_Table.subject = 'social';

