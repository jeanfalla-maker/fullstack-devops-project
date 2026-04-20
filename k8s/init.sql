CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO usuarios (nombre, email) VALUES
    ('Usuario Demo', 'demo@correo.com'),
    ('Admin', 'admin@correo.com');
