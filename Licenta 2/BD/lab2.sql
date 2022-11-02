--1
select first_name || ' ' || last_name || ' castiga ' || salary || 
  ' lunar dar doreste ' || 3 * salary "Salariu ideal"
from employees;

--2 
--var1
select initcap(first_name) "FIRST NAME", upper(last_name) "LAST NAME", 
  length(last_name) "NAME LENGTH"
from employees
where last_name like 'J%' or last_name like 'M%' 
  or lower(last_name) like '__a%'
order by length(last_name) desc;

--var2
select initcap(first_name) "FIRST NAME", upper(last_name) "LAST NAME", 
  length(last_name) "NAME LENGTH"
from employees
where substr(last_name, 1, 1) = 'J' or substr(last_name, 1, 1) = 'M' 
  or substr(lower(last_name), 3, 1) = 'a'
order by length(last_name) desc;

--3
select employee_id, last_name, department_id
from employees
where lower(trim(both from first_name)) = 'steven';

--4
select employee_id "Codul", last_name "Numele", 
  length(last_name) "Lungimea numelui", 
  instr(lower(last_name), 'a') "Prima aparitie a literei 'a'"
from employees
where instr(reverse(lower(last_name)), 'e') = 1;

--5 ?
--select last_name, sysdate, hire_date, months_between(sysdate, hire_date)
--from employees
--where months_between(sysdate, hire_date) = round(months_between(sysdate, hire_date));

--6 de rescris numar sute
select employee_id, first_name, salary, salary + 
  trunc(salary * 15 / 100, 2) "Salariu nou", 
  round(salary + salary * 15 / 100, 2) "Numar sute"
from employees
where salary / 1000 != round(salary / 1000);

--7  + RPAD?
select last_name "Nume angajat", hire_date "Data angajarii"
from employees
where commission_pct is not null;

--8
select to_char(sysdate + 30, 'dd-mon-yyyy/hh:mi:ss')
from dual;

--9
select trunc(last_day('02-dec-2020') - sysdate)
from dual;

--10 nu merge
--a
select to_char(0,00347222 + sysdate, 'dd-mon-yyyy/hh:mi')
from dual;

--b
select to_date(sysdate + interval '12' hour, 'dd-mon-yyyy/hh:mi:ss')
from dual;

--11
select first_name || ' ' || last_name, hire_date, 
  next_day(add_months(hire_date, 6), 'Luni') "Negociere"
from employees;

--12
select last_name, round(months_between(sysdate, hire_date)) "Luni lucrate"
from employees
order by round(months_between(sysdate, hire_date));

--13
select first_name, last_name, hire_date, to_char(hire_date, 'day') "Zi"
from employees
order by to_char(hire_date, 'd'), first_name;

--14 ceva e dubi la ultimul argument din decode 
select last_name, decode(commission_pct, null, 
  'Fara comision', '0' || commission_pct) "Comision"
from employees;

--15
select last_name, salary, commission_pct
from employees
where salary * nvl(commission_pct, 1) > 10000;

--16
select last_name, job_id, salary, 
  case job_id
  when 'IT_PROG' then salary + salary * 20 / 100
  when 'SA_REP' then salary + salary * 25 / 100
  when 'SA_MAN' then salary + salary * 35 / 100
  else salary
  end "Salariu renegociat"
from employees;

--17
select e.last_name, e.employee_id, d.department_name
from employees e
left join departments d using(department_id);

--18
select distinct j.job_title
from jobs j
join employees e using(job_id)
where e.department_id = 30;

--19
select e.last_name, d.department_name, l.city
from employees e
left join departments d using(department_id)
left join locations l using(location_id)
where e.commission_pct is not null;

--DE AICI NU AM TESTAT
--20
select e.last_name, d.department_name
from employees e, departments d
where e.department_id = d.department_id (+) and upper(e.first_name) like '%A%';

--21
select e.last_name, e.job_id, e.employee_id, d.department_name
from employees e
join department d using(department_id)
join locations l using(location_id)
where lower(l.city) = 'oxford';

--22
select e.employee_id "Ang#", e.last_name "Angajat", sef.employee_id "Mgr#",
  sef.last_name "Manager"
from employees e
join employees sef on e.manager_id = sef.employee_id;

--23


--24
select e.last_name "Salariat 1", e.department_id "Departament", 
  p.last_name "Salariat 2"
from employees e
join employees p on e.department_id = p.department_id
where e.employee_id != p.employee_id;

--25
-- + sa se listeze structura tabelului jobs
select e.last_name, j.job_id, j.job_title, d.department_name, e.salary
from employees e
join jobs j using(job_id)
join departments d using(department_id);

--26
select e.last_name, e.hire_date
from employees e, employees g
where lower(g.last_name) = 'gates' and e.hire_date > g.hire_date;

--27
select e.last_name "Angajat", e.hire_date "Data_ang", p.last_name "Manager", 
  p.hire_date "Data_mgr"
from employees e
join employees p on e.manager_id = p.employee_id
where e.hire_date < p.hire_date;
