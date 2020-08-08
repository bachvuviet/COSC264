drop table book_copy;
drop table member;
drop table branch;
drop table author_of;
drop table book;
drop table author;
drop table publisher;


/* Creating tables */
create table publisher
(Code char(2) not null,
 Name varchar(30) not null,
 City varchar(15) not null,
 constraint pk_publisher primary key (Code));

create table author
(AuthorId integer not null check (AuthorId > 0), 
 Lname varchar(20) not null,
 Fname varchar(15) not null,
 constraint pk_author primary key (AuthorId));

create table book
 (Book_id char(4) not null,
  Title varchar(60) not null,
  Publisher char(2),
  constraint pk_item primary key (Book_Id),
  constraint fk_item foreign key (publisher) references PUBLISHER);

create table AUTHOR_OF
 (Book char(4) not null,
  Author integer not null,
  sequence integer check (sequence>0),
  constraint pk_AuthorOf primary key (book,author),
  constraint fk2_AuthorFor foreign key (book) references book,
  constraint fk_writtenBy foreign key (author) references author); 

create table BRANCH
 (BranchId char(3) not null,
  Bname varchar(12) not null,
  Address varchar(25),
  constraint pk_branch primary key (BranchId));


/* Adding data into the PUBLISHER table */
insert into PUBLISHER values('AH','Arkham House','Sauk City WI');
insert into PUBLISHER values('AP','Arcade Publishing','New York');
insert into PUBLISHER values('BA','Basic Books','Boulder CO');
insert into PUBLISHER values('BP','Berkley Publishing','Boston');
insert into PUBLISHER values('BY','Back Bay Books','New York');
insert into PUBLISHER values('CT','Course Technology','Boston');
insert into PUBLISHER values('FA','Fawcett Books','New York');
insert into PUBLISHER values('FS','Farrar Straus Giroux','New York');
insert into PUBLISHER values('HC','HarperCollins Publishers','New York');
insert into PUBLISHER values('JP','Jove Publications','New York');
insert into PUBLISHER values('JT','Jeremy P. Tarcher','Los Angeles');
insert into PUBLISHER values('LB','Lb Books','New York');
insert into PUBLISHER values('MP','McPherson and Co.','Kingston');
insert into PUBLISHER values('PE','Penguin USA','New York');
insert into PUBLISHER values('PL','Plume','New York');
insert into PUBLISHER values('PU','Putnam Publishing Group','New York');
insert into PUBLISHER values('RH','Random House','New York');
insert into PUBLISHER values('SB','Schoken Books','New York');
insert into PUBLISHER values('SC','Scribner','New York');
insert into PUBLISHER values('SS','Simon Schuster','New York');
insert into PUBLISHER values('ST','Scholastic Trade','New York');
insert into PUBLISHER values('TA','Taunton Press','Newtown CT');
insert into PUBLISHER values('TB','Tor Books','New York');
insert into PUBLISHER values('TH','Thames and Hudson','New York');
insert into PUBLISHER values('TO','Touchstone Books','Westport CT');
insert into PUBLISHER values('VB','Vintage Books','New York');
insert into PUBLISHER values('WN','W.W.Norton','New York');
insert into PUBLISHER values('WP','Westview Press','Boulder CO');

/* Adding data into the PUBLISHER table */
insert into AUTHOR values(1,'Morisson','Toni');
insert into AUTHOR values(2,'Solotaroff','Paul');
insert into AUTHOR values(3,'Vintage','Vernor');
insert into AUTHOR values(4,'Francis','Dick');
insert into AUTHOR values(5,'Straub','Peter');
insert into AUTHOR values(6,'King','Stephen');
insert into AUTHOR values(7,'Pratt','Phillip');
insert into AUTHOR values(8,'Chase','Truddi');
insert into AUTHOR values(9,'Collins','Bradley');
insert into AUTHOR values(10,'Heller','Joseph');
insert into AUTHOR values(11,'Wills','Gary');
insert into AUTHOR values(12,'Hofstadter','Douglas R.');
insert into AUTHOR values(13,'Lee','Harper');
insert into AUTHOR values(14,'Ambrose','Stephen E.');
insert into AUTHOR values(15,'Rowling','J.K.');
insert into AUTHOR values(16,'Salinger','J.D.');
insert into AUTHOR values(17,'Heaney','Seamus');
insert into AUTHOR values(18,'Camus','Albert');
insert into AUTHOR values(19,'Collins Jr.','Bradley');
insert into AUTHOR values(20,'Steinbeck','John');
insert into AUTHOR values(21,'Castelman','Riva');
insert into AUTHOR values(22,'Owen','Barbara');
insert into AUTHOR values(23,'O''Rourke','Randy');
insert into AUTHOR values(24,'Kidder','Tracy');
insert into AUTHOR values(25,'Schleining','Lon');

/* Adding data into the BOOK table */
insert into BOOK values('0180','A Deepness in the Sky','TB');
insert into BOOK values('0189','Magic Terror','FA');
insert into BOOK values('0200','The Stranger','VB');
insert into BOOK values('0378','Venice','SS');
insert into BOOK values('0797','Second Wind','PU');
insert into BOOK values('0808','The Edge','JP');
insert into BOOK values('1351','Dreamcatcher','SC');
insert into BOOK values('1382','Treasure Chests','TA');
insert into BOOK values('1387','Beloved','PL');
insert into BOOK values('2226','Harry Potter and the Prisoner of Azkaban','ST');
insert into BOOK values('2281','Van Gogh and Gauguin','WP');
insert into BOOK values('2766','Of Mice and Men','PE');
insert into BOOK values('2908','Electric Light','FS');
insert into BOOK values('3350','Group: Six People in Search of a Life','BP');
insert into BOOK values('3683','The Catcher in the Rye','RH');
insert into BOOK values('3743','Nine Stories','LB');
insert into BOOK values('3906','The Soul of a New Machine','BY');
insert into BOOK values('5163','Travels with Charley','PE');
insert into BOOK values('5790','Catch-22','SC');
insert into BOOK values('6128','Jazz','PL');
insert into BOOK values('6328','Band of Brothers','TO');
insert into BOOK values('6697','A Guide to SQL','CT');
insert into BOOK values('6908','Franny and Zooey','LB');
insert into BOOK values('7405','East of Eden','PE');
insert into BOOK values('7443','Harry Potter and the Goblet of Fire','ST');
insert into BOOK values('7559','The Fall','VB');
insert into BOOK values('8720','When Rabbit Howls','JP');
insert into BOOK values('9611','Black House','RH');
insert into BOOK values('9627','Song of Solomon','PL');
insert into BOOK values('9701','The Grapes of Wrath','PE');
insert into BOOK values('9882','Slay Ride','JP');
insert into BOOK values('9883','The Catcher in the Rye','LB');
insert into BOOK values('9931','To Kill a Mockingbird','HC');
insert into BOOK values('8092','Godel Escher Bach','BA');
insert into BOOK values('9991','Harry Potter and the Order of Phoenix','ST');


/* Adding data into the AUTHOR_OF table */
insert into AUTHOR_OF values('0180',3,1);
insert into AUTHOR_OF values('0189',5,1);
insert into AUTHOR_OF values('0200',18,1);
insert into AUTHOR_OF values('0378',11,1);
insert into AUTHOR_OF values('0797',4,1);
insert into AUTHOR_OF values('0808',4,1);
insert into AUTHOR_OF values('1351',6,1);
insert into AUTHOR_OF values('1382',23,2);
insert into AUTHOR_OF values('1382',25,1);
insert into AUTHOR_OF values('1387',1,1);
insert into AUTHOR_OF values('2226',15,1);
insert into AUTHOR_OF values('2281',9,2);
insert into AUTHOR_OF values('2281',19,1);
insert into AUTHOR_OF values('2766',20,1);
insert into AUTHOR_OF values('2908',17,1);
insert into AUTHOR_OF values('3350',2,1);
insert into AUTHOR_OF values('3683',16,1);
insert into AUTHOR_OF values('3743',16,1);
insert into AUTHOR_OF values('3906',24,1);
insert into AUTHOR_OF values('5163',20,1);
insert into AUTHOR_OF values('5790',10,1);
insert into AUTHOR_OF values('6128',1,1);
insert into AUTHOR_OF values('6328',14,1);
insert into AUTHOR_OF values('6697',7,1);
insert into AUTHOR_OF values('6908',16,1);
insert into AUTHOR_OF values('7405',20,1);
insert into AUTHOR_OF values('7443',15,1);
insert into AUTHOR_OF values('7559',18,1);
insert into AUTHOR_OF values('8092',12,1);
insert into AUTHOR_OF values('8720',8,1);
insert into AUTHOR_OF values('9611',6,1);
insert into AUTHOR_OF values('9627',1,1);
insert into AUTHOR_OF values('9701',20,1);
insert into AUTHOR_OF values('9882',4,1);
insert into AUTHOR_OF values('9883',16,1);
insert into AUTHOR_OF values('9931',13,1);


/* Adding data into the BRANCH table */
insert into BRANCH values('CEN','Central','Library Tower
');
insert into BRANCH values('ENG','Engineering','Engineering Building');
insert into BRANCH values('SCI','Science','Science Block');