package com.ndgit.services;

import com.ndgit.entities.Payment;
import com.ndgit.enums.PaymentProductType;
import com.ndgit.rest.BankResponse;

public interface PaymentService {

    /**
     * Updates the payment status by id
     */
    void updateStatus(long paymentId, String status);

    /**
     * Persists new payment record
     */
    Payment addPayment(PaymentProductType type);

    /**
     * Updates the payment with bank response by id
     */
    void updateBankResponse(long paymentId, BankResponse bankResponse);

}
