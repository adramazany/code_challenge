package com.ndgit.rest;

import lombok.Getter;
import lombok.Setter;

/**
 * Bank API Response containing bank-generated id
 */
@Getter
@Setter
public class BankResponse {

    private String status;

    private String bankPaymentId;

    @Override
    public String toString() {
        return "BankResponse{" +
                "status='" + status + '\'' +
                ", bankPaymentId='" + bankPaymentId + '\'' +
                '}';
    }
}
