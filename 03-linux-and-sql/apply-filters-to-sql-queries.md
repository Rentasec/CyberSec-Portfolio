# Apply Filters to SQL Queries

---

## Project Description

My organization needed to investigate potential security incidents and prepare machines for security updates. The following examples show how I used SQL filters to retrieve specific information from the `log_in_attempts` and `employees` tables.

---

## Retrieve After-Hours Failed Login Attempts

A potential security incident occurred after business hours (after 18:00). All failed login attempts during that window needed to be reviewed.

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00' AND success = FALSE;
```

The `WHERE` clause uses `AND` to require both conditions: the login must have occurred after 18:00, and it must have failed (`success = FALSE`).

---

## Retrieve Login Attempts on Specific Dates

A suspicious event was flagged on 2022-05-09. Any login activity on that date or the day prior required investigation.

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';
```

`OR` is used here because either date is relevant. `AND` would return no results since a single login cannot occur on two dates simultaneously.

---

## Retrieve Login Attempts Outside of Mexico

Investigation suggested that login attempts from outside Mexico were suspicious and needed to be reviewed.

```sql
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';
```

The dataset stores Mexico as both `MEX` and `MEXICO`, so `LIKE 'MEX%'` matches both variations. `NOT` excludes all rows where the country starts with `MEX`.

---

## Retrieve Employees in Marketing (East Building)

The Marketing team in the East building needed computer updates. I needed a list of their machines.

```sql
SELECT *
FROM employees
WHERE department = 'Marketing' AND office LIKE 'East%';
```

`AND` ensures only employees who are both in Marketing and physically in the East building are returned. The `East%` pattern accounts for specific office numbers appended to the building name.

---

## Retrieve Employees in Finance or Sales

A separate security update was required for Finance and Sales department machines.

```sql
SELECT *
FROM employees
WHERE department = 'Finance' OR department = 'Sales';
```

`OR` is the correct operator here since employees can belong to one department or the other, not both.

---

## Retrieve All Employees Not in IT

A final update needed to be applied to all employees outside the IT department.

```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

`NOT` excludes IT employees, returning everyone else in a single query.

---

## Summary

These queries demonstrate filtering with `AND`, `OR`, `NOT`, `LIKE`, and wildcard patterns across two tables. Each query was written to retrieve the minimum data needed for the task, reducing noise and improving investigation efficiency.
