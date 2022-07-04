package com.ndgit.entities;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import com.ndgit.enums.PaymentProductType;
import lombok.Getter;
import lombok.Setter;

/**
 * Payment information
 */
@Getter
@Setter
@Entity(name = "payments")
public class Payment {

    @Id
    @Column
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;

    @Enumerated(EnumType.STRING)
    private PaymentProductType type;

    @Column
    private String bankPaymentId;

    @Column
    private String status;

    @Override
    public String toString() {
        return "Payment{" +
                "id=" + id +
                ", type=" + type +
                ", bankPaymentId='" + bankPaymentId + '\'' +
                ", status='" + status + '\'' +
                '}';
    }
}

