--Написать 2 любые хранимые процедуры.


--выводит максимальный индекс пользователя
CREATE PROCEDURE user_id_max() 
LANGUAGE plpgsql 
AS 
$$
DECLARE
id users.user_id%type;
BEGIN
SELECT max(user_id) FROM users INTO id;
RAIsE NOTICE 'Maximum of user_id is: %', id;
END;
$$;




--добавляет нового пользователя
CREATE OR REPLACE PROCEDURE public.user_ins(
	u_email character varying DEFAULT NULL::character varying,
	u_pwd character varying DEFAULT NULL::character varying,
	u_f_name character varying DEFAULT NULL::character varying,
	u_l_name character varying DEFAULT NULL::character varying,
	u_m_name character varying DEFAULT NULL::character varying,
	u_staff integer DEFAULT NULL::integer,
	u_country character varying DEFAULT NULL::character varying,
	u_city character varying DEFAULT NULL::character varying,
	u_address text DEFAULT NULL::text,
	u_phone character varying DEFAULT NULL::character varying)
LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
INSERT INTO users(email, password, first_name, last_name, middle_name, is_staff, country, city, address, phone_number) 
VALUES(u_email, u_pwd, u_f_name, u_l_name, u_m_name, u_staff, u_country, u_city, u_address, u_phone);
END
$BODY$;




