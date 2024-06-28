use dcmsdb;
create table tb_dentist(id int primary key AUTO_INCREMENT, dfirstname varchar(45), dlastname varchar(45), speciality varchar(45), tel varchar(20), email varchar(45), status varchar(20), role varchar(20), password varchar(250), UNIQUE(email));
insert into tb_dentist(dfirstname, dlastname, speciality, tel, email, status, role, password) values('June', 'Gaual', 'ICT', '2097841656', 'admin@gmail.com', 'Active', 'ICT Manager', 'password');

select *from tb_dentist;