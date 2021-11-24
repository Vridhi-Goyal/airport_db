ALTER TABLE crew
ADD dept varchar(20);
UPDATE crew
set dept=
CASE 
WHEN ID =1 THEN 'Ground'
WHEN ID =2 THEN 'Security Team'
WHEN ID =3 THEN 'Service'
WHEN ID =4 THEN 'Operations'
WHEN ID =5 THEN 'Ground'
WHEN ID =6 THEN 'Security Team'
WHEN ID =7 THEN 'Operations'
WHEN ID =8 THEN 'Ground'
WHEN ID =9 THEN 'Ground'
WHEN ID =10 THEN 'Service'
WHEN ID =11 THEN 'Service'
WHEN ID =12 THEN 'Operations'
WHEN ID =13 THEN 'Ground'
WHEN ID =14 THEN 'Ground'
WHEN ID =15 THEN 'Security Team'

END
WHERE id between 1 and 15