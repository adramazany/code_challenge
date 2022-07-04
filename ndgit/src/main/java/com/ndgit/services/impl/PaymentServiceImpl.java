package com.ndgit.services.impl;

import com.ndgit.entities.Payment;
import com.ndgit.enums.PaymentProductType;
import com.ndgit.exception.PaymentNotFoundException;
import com.ndgit.repo.PaymentRepository;
import com.ndgit.rest.BankResponse;
import com.ndgit.services.PaymentService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Slf4j
@Service
public class PaymentServiceImpl implements PaymentService {

    @Autowired
    PaymentRepository paymentRepository;

    @Override
    public void updateStatus(long paymentId, String status) {
        Payment payment = paymentRepository.findById(paymentId)
                .orElseThrow(()->new PaymentNotFoundException(paymentId));
        payment.setStatus(status);
        paymentRepository.save(payment);
    }

    @Override
    public Payment addPayment(PaymentProductType type) {
        Payment payment = new Payment();
        payment.setType(type);
        payment = paymentRepository.save(payment);
        return payment;
    }

    public void updateBankResponse(long paymentId, BankResponse bankResponse) {
        Payment payment = paymentRepository.findById(paymentId)
                .orElseThrow(()->new PaymentNotFoundException(paymentId));

        if(payment.getStatus()==null || "".equals(payment.getStatus()) ) {
            payment.setStatus(bankResponse.getStatus());
        }

        if(payment.getBankPaymentId()==null
                || "".equals(payment.getBankPaymentId())
                || "IN-PROGRESS".equals(payment.getBankPaymentId()) ){
            payment.setBankPaymentId(bankResponse.getBankPaymentId());
        }

        paymentRepository.save(payment);
    }



}
