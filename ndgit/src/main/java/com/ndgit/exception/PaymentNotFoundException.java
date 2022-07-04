package com.ndgit.exception;
/*
 * @created 6/30/2022 - 5:19 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

public class PaymentNotFoundException extends RuntimeException {
    public PaymentNotFoundException(long paymentId) {
        super("Could not find payment: "+paymentId);
    }
}
