CREATE TABLE IF NOT EXISTS staff_role (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS staff (
    id BIGSERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    role_id BIGINT NOT NULL REFERENCES staff_role(id)
    phone_number VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS customer (
    id BIGSERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL
);

CREATE TABLE IF NOT EXISTS equipment (
    id BIGSERIAL PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS installation_status (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS installation (
    id BIGSERIAL PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    customer_id BIGINT NOT NULL REFERENCES customer(id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NULL,
    status_id BIGINT NOT NULL REFERENCES installation_status(id)
);

CREATE TABLE IF NOT EXISTS staff_assignment (
    id BIGSERIAL PRIMARY KEY,
    staff_id BIGINT NOT NULL REFERENCES staff(id) ON DELETE CASCADE,
    installation_id BIGINT NOT NULL REFERENCES installation(id) ON DELETE CASCADE,
    quantity INT NOT NULL CHECK (quantity > 0),
    start_date DATE NOT NULL,
    end_date DATE NULL
);

CREATE TABLE IF NOT EXISTS installation_equipment (
    id BIGSERIAL PRIMARY KEY,
    installation_id BIGINT NOT NULL REFERENCES installation(id) ON DELETE CASCADE,
    equipment_id BIGINT NOT NULL REFERENCES equipment(id) ON DELETE CASCADE,
    quantity INT NOT NULL CHECK (quantity > 0)
);
