--3
desc employees;

--4
select * from employees;

--5 - proiectie
select employee_id, first_name, job_id, hire_date
from employees;

--6
select distinct job_id
from employees;

--7
select first_name || ', ' || job_id "Angajat si titlu"
from employees;

--8 ?
--select * from employees;

--9
select first_name, salary
from employees
where salary > 2850;

--10 ?
--select first_name, department_id
--from employees
--where rownum = 104;

--11
select first_name, salary
from employees
where salary < 1500 or salary > 2850;

--12
select first_name, job_id, hire_date
from employees
where hire_date between '20-02-1987' and '1-05-1989'
order by hire_date;

--13
select first_name, department_id
from employees
where department_id in (10, 30)
order by first_name;

--14
select first_name "Angajat", salary "Salariu lunar"
from employees
where salary > 3500 and department_id in (10, 30);

--15
select sysdate
from dual;

--16
select first_name, hire_date
from employees
where hire_date like ('%87%');

select first_name, hire_date
from employees
where to_char(hire_date, 'YYYY') = 1987;

--17
select first_name, job_id
from employees
where manager_id is null;

--18
select last_name, salary, commission_pct
from employees
where commission_pct is not null
order by salary desc, commission_pct desc;

--19
select last_name, salary, commission_pct
from employees
order by salary desc, commission_pct desc;

--20
select first_name, last_name
from employees
where lower(last_name) like '__a%';

--21
select first_name, last_name
from employees
where lower(last_name) like '%l%l%' 
and (department_id = 30 or manager_id = 101);

--22
select first_name, last_name, job_id, salary
from employees
where (lower(job_id) like '%clerk%' or lower(job_id) like '%rep%')
  and salary not in (1000, 2000, 3000);

--23
select last_name, salary, commission_pct
from employees
where salary > salary * commission_pct * 5;
