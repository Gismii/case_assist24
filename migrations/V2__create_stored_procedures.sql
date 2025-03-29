-- Remova as procedures existentes, se houver
DROP PROCEDURE IF EXISTS sp_get_user_by_email;
DROP PROCEDURE IF EXISTS sp_list_users;

DELIMITER $$

-- Stored procedure para buscar um usuário pelo email
CREATE PROCEDURE sp_get_user_by_email(IN p_email VARCHAR(255))
BEGIN
    SELECT * FROM user
    WHERE email = p_email;
END$$

-- Stored procedure para listar todos os usuários
CREATE PROCEDURE sp_list_users()
BEGIN
    SELECT * FROM user;
END$$

DELIMITER ;