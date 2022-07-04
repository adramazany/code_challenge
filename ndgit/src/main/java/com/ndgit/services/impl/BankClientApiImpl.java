package com.ndgit.services.impl;
/*
 * @created 7/3/2022 - 7:08 PM
 * @project ndgit
 * @author adel.ramezani (adramazany@gmail.com)
 */

import com.ndgit.entities.Payment;
import com.ndgit.exception.PaymentNotFoundException;
import com.ndgit.repo.PaymentRepository;
import com.ndgit.rest.BankResponse;
import com.ndgit.services.BankClientApi;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Slf4j
@Component
public class BankClientApiImpl implements BankClientApi {

    @Autowired
    RestTemplate restTemplate;

    @Value("${bank.api.url}")
    String bank_url;

    @Override
    public BankResponse getPaymentData(long paymentId) {
        ResponseEntity<BankResponse> response = restTemplate.getForEntity(
                bank_url, BankResponse.class, paymentId );

        if (response.getStatusCode().is2xxSuccessful()) {
            return response.getBody();
        }else{
            throw new RuntimeException("Bank API Error! : "+response.getStatusCode());
        }
    }
}
