CREATE DATABASE Revaturedb;

USE Revaturedb;
CREATE TABLE student(
rollno int,
sname varchar(25)not null,
addr varchar(50),
CONSTRAINT pk_rollno primary key(rollno)
);
alter table student add city varchar(20),pin int;
alter table student alter column addr varchar(100);
alter table student add dummycol  int;
exec sp_rename 'student.dummycol','dummy','column';
alter
table student drop column dummycol;
select * from student;

USE Revaturedb;
save transaction level1;
insert into dbo.student values(101,'AAA','QWERY','BLR',4328);
insert into dbo.student values(102,'AAA','QWERY','BLR',4890);



update student set city='mad',addr='kbhb'
where rollno=102

CREATE DATABASE Revcompany

USE Revcompany


create table department(
    deptno SMALLINT,
    dname VARCHAR(30) NOT NULL,
    CONSTRAINT pk_deptno PRIMARY KEY (deptno),
      
);
CREATE TABLE employee(
    deptno SMALLINT,
    ename VARCHAR(30) NOT NULL,
    mgr SMALLINT,
    salary NUMERIC(10,2),
    comm NUMERIC(7,2),
    empno SMALLINT,
    CONSTRAINT pk_empno PRIMARY KEY (empno),
    CONSTRAINT fk_deptno FOREIGN KEY (deptno) REFERENCES department(deptno)
);
insert into department values(10,'IT')
insert into department values(20,'HR')
insert into department values(30,'SAL')
insert into department values(40,'MGR')
insert into department values(50,'OPS')


INSERT INTO employee (empno, ename, mgr, salary, comm, deptno) VALUES
(1001, 'Alice', NULL, 60000.00, NULL, 10), -- HR
(1002, 'Bob', 1001, 75000.00, NULL, 20), -- IT
(1003, 'Charlie', 1002, 50000.00, 500.00, 30), -- Sales
(1004, 'Diana', 1003, 52000.00, 300.00, 30), -- Sales
(1005, 'Ethan', 1002, 58000.00, NULL, 40), -- Finance
(1006, 'Fiona', 1005, 62000.00, NULL, 50); -- Marketing


select * from employee;
select * from department;
 

 select empno as "number",ename as "name"
 from employee;

 select empno as "number",ename as "name"
 from employee
 where salary>70000;

 select empno as "number",ename as "name"
 from employee
 where empno not in(1002,1003,1005);

 select empno as "number",ename as "name"
 from employee
 where salary between 40000 and 60000;

 select empno as "number",ename as "name"
 from employee
 where ename like  'a%';

 select empno as "number",ename as "name"
 from employee
 where ename like  '__a%';

 select empno as "number",ename as "name"
 from employee
 where ename in ('alice','bob');

 select empno as "number",ename as "name"
 from employee
 where empno=1004 or ename like '%a%';


 select empno as "number",ename as "name", salary
 from employee
 where salary>50000
 order by salary;

 select empno as "number",ename as "name", salary,comm as 'commission'
 from employee
 where salary>50000
 order by comm,salary desc;


 select count(empno) as "number of emp",sum(salary) as "Total", 
 avg(comm) as 'avg commision',min(salary) as'least salary',
 max(salary) as 'Top earner'
 from employee


 select deptno, sum(salary) as 'total salary'
 from employee
 group by deptno

 select deptno, sum(salary) as 'total salary'
 from employee
 where deptno in (10,30,50)
 group by deptno
 having sum(salary) >= 62000
 order by sum(salary)



select e.ename,d.dname
from employee e join department d
on d.deptno = e.deptno;

select e.ename,d.dname
from employee e left outer join department d
on d.deptno = e.deptno;

select e.ename,d.dname
from employee e right outer join department d
on d.deptno = e.deptno;

select e.ename,d.dname
from employee e full outer join department d
on d.deptno = e.deptno;









 


 


