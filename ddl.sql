create user security with password 'security';
grant select on passenger to security;

create user agency with password 'agency';
grant insert, select on flight to agency;

create user atc with password 'atc';
grant select on runway, runs_on to atc;
grant insert, update on flight to atc;

create user scheduler with password 'scheduler';
grant select, insert, update on flight to scheduler; 

create user luggage_team with password 'luggage_team';
grant select, update, insert on luggage to luggage_team;
