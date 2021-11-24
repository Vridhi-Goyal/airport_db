create user security with password 'security';
grant select on passenger to security;

create user agency with password 'agency';
grant insert, select on flight to agency;

create user atc with password 'atc';
grant insert, update on flight,runway, runs_on to atc;

create user scheduler with password 'scheduler';
grant select, insert, update on flight to scheduler; 

create user luggage_team with password 'luggage_team';
grant select, update, insert on luggage to luggage_team;

create user transport with password 'transport';
grant select (gateno) from flight to transport;
grant select on gates to transport;

create user service with password 'service';
grant update (h_id) on plane to service;
grant select on hangar to service;
