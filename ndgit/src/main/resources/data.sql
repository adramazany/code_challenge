DROP TABLE IF EXISTS payments;
CREATE TABLE payments
(
    id              NUMBER AUTO_INCREMENT PRIMARY KEY,
    type            VARCHAR(60) NOT NULL,
    bank_payment_id VARCHAR(36),
    status          VARCHAR(30)
);

INSERT INTO payments (type, bank_payment_id, status)
VALUES ('SEPA_CREDIT_TRANSFER', null, 'RECEIVED'),
       ('INSTANT_SEPA_CREDIT_TRANSFER', '3fb3ab45-24fa-475f-b8bd-4082ee539046', 'RECEIVED'),
       ('CROSS_BORDER_CREDIT_TRANSFER', null, null),
       ('DOMESTIC_ELIXIR', '1a4a2191-2f75-4e0b-a9d5-a96a0c1e734c', null),
       ('SEPA_CREDIT_TRANSFER', 'dde7e9c1-8118-458b-acd8-330a2ce986bb', 'ACCEPTED'),
       ('SEPA_CREDIT_TRANSFER', '1ae6193c-6f55-49cd-9c4f-28ef7c07f410', 'REJECTED'),
--     ... 1.000.000+ records
       ('DOMESTIC_ELIXIR', null, null);