package com.ndgit.services;

import com.ndgit.rest.BankResponse;

/**
 * Client to communicate with Client API
 */
public interface BankClientApi {

    BankResponse getPaymentData(long paymentId);

}
