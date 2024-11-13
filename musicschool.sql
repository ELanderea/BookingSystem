CREATE DATABASE musicschool;

USE musicschool;

CREATE TABLE `students` (
  `student_id` INT UNIQUE NOT NULL PRIMARY KEY,
  `student_first_name` VARCHAR(20) NOT NULL,
  `student_last_name` VARCHAR(20) NOT NULL,
  `student_phone` VARCHAR(20) NOT NULL,
  `student_instrument` VARCHAR(20) NOT NULL
);

CREATE TABLE `teachers` (
  `teacher_id` int (11) UNIQUE NOT NULL PRIMARY KEY,
  `teacher_first_name` VARCHAR(20) NOT NULL,
  `teacher_last_name` VARCHAR(20) NOT NULL,
  `teacher_phone` VARCHAR(20) NOT NULL,
  `teacher_instrument` VARCHAR(20) NOT NULL
);

CREATE TABLE `bookings` (
  `bookingdate` DATE NOT NULL,
  `teacher_id` int (11) NOT NULL,
  `teacher_instrument` VARCHAR(20) DEFAULT NULL,
  `10-11` INT DEFAULT NULL,
  `10-11-student-id` VARCHAR(20) DEFAULT NULL,
  `11-12` INT DEFAULT NULL,
  `11-12-student-id` VARCHAR(20) DEFAULT NULL,
  `12-13` INT DEFAULT NULL,
  `12-13-student-id` VARCHAR(20) DEFAULT NULL,
  `13-14` INT DEFAULT NULL,
  `13-14-student-id` VARCHAR(20) DEFAULT NULL,
  `14-15` INT DEFAULT NULL,
  `14-15-student-id` VARCHAR(20) DEFAULT NULL,
  `15-16` INT DEFAULT NULL,
  `15-16-student-id` VARCHAR(20) DEFAULT NULL,
  `16-17` INT DEFAULT NULL,
  `16-17-student-id` VARCHAR(20) DEFAULT NULL,
  `17-18` INT DEFAULT NULL,
  `17-18-student-id` VARCHAR(20) DEFAULT NULL,
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

INSERT INTO `teachers` 
VALUES 
(12345,'Anne','Strings','+4412345','violin'),
(11111,'Ben','Steel','+4411111','guitar'),
(22222,'Cat','Wind','+4422222','flute'),
(33333,'Dan','Brass','+4433333','trumpet'),
(44444,'Prima','Donna','+4444444','voice'),
(55555,'Pete','Beats','+4455555','drums'),
(12222,'Fiona','Field','+4422345','violin'),
(13333,'Glenn','Gould','+4431111','guitar'),
(24444,'Harry','Hats','+4424222','flute'),
(35555,'Ian','Isloud','+4434333','trumpet'),
(46666,'Jan','Jolena','+4445444','voice'),
(57777,'King','Kong','+4455655','drums'),
(19999,'Leena','Lioness','+4417345','violin'),
(18888,'Mikey','Mouse','+4411171','guitar'),
(22223,'Nina','Nesta','+44222282','flute'),
(33334,'Oisin','Opus','+44333393','trumpet'),
(44445,'Parma','Piazza','+4444944','voice'),
(55556,'Rachel','Rice','+4455575','drums')
;

INSERT INTO `students` 
VALUES 
(66666,'Bob','Notes','+4466666','violin'),
(77777,'Lee','Steel','+4477777','guitar'),
(88888,'Willow','Winds','+4488888','flute'),
(99999,'Flora','Clef','+4499999','trumpet'),
(11112,'Andy','Voces','+4411112','voice'),
(11113,'Mezzo','Forte','+4411113','drums');

DELIMITER $$

CREATE definer = `root`@`localhost` PROCEDURE `inputavailability` (dateSTART DATE, dateEND DATE, teacher_id INT, teacher_instrument VARCHAR(20))
Begin
	While dateSTART <= dateEND DO
    INSERT INTO musicschool.bookings (teacher_id, bookingdate, teacher_instrument) value (teacher_id, dateSTART, teacher_instrument);
    SET dateSTART = date_add(dateSTART, INTERVAL 1 DAY);
    
End While;
End $$

DELIMITER ;

CALL inputavailability(20240901,20240907, 12345,'violin');
CALL inputavailability(20240901,20240905, 11111,'guitar');
CALL inputavailability(20240901,20240906, 22222,'violin');
CALL inputavailability(20240902,20240905, 33333,'trumpet');
CALL inputavailability(20240904,20240906, 44444,'voice');
CALL inputavailability(20240903,20240907, 55555,'drums');
CALL inputavailability(20240902,20240907, 12222,'violin');
CALL inputavailability(20240904,20240905, 13333,'guitar');
CALL inputavailability(20240905,20240906, 24444,'flute');
CALL inputavailability(20240901,20240905, 35555,'trumpet');
CALL inputavailability(20240902,20240906, 46666,'voice');
CALL inputavailability(20240901,20240907, 57777,'drums');
CALL inputavailability(20240904,20240907, 19999,'violin');
CALL inputavailability(20240903,20240905, 18888,'guitar');
CALL inputavailability(20240901,20240903, 22223,'flute');
CALL inputavailability(20240902,20240906, 33334,'trumpet');
CALL inputavailability(20240901,20240905, 44445,'voice');
CALL inputavailability(20240903,20240907, 55556,'drums');


SELECT*FROM bookings
ORDER BY bookingdate;

SELECT * FROM teachers
WHERE teacher_instrument = 'violin';

SELECT bookingdate,teacher_id, '10-11', '11-12','12-13','13-14','14-15', '15-16', '16-17','17-18'
FROM bookings WHERE teacher_id = '11111'
ORDER BY bookingdate;
