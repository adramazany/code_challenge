package com.ndgit.services.impl;

import com.ndgit.entities.Payment;
import com.ndgit.enums.PaymentProductType;
import com.ndgit.exception.PaymentNotFoundException;
import com.ndgit.repo.PaymentRepository;
import com.ndgit.services.PaymentService;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;

@Slf4j
@SpringBootTest
class PaymentServiceImplTest {

    @Autowired
    PaymentService paymentService;
    @Autowired
    PaymentRepository paymentRepository;

    @Test
    void addPayment() {
        Payment payment = paymentService.addPayment(PaymentProductType.TARGET_2_PAYMENT);
        assertEquals(PaymentProductType.TARGET_2_PAYMENT,payment.getType());
        assertTrue(payment.getId()>0);
        assertNull(payment.getStatus());
        assertNull(payment.getBankPaymentId());

    }

    @Test
    void updateStatus_paymentIdNotFound() {
        PaymentNotFoundException ex = assertThrows(PaymentNotFoundException.class
                ,()->paymentService.updateStatus(99999999999999999L,"ACCEPTED")
                ,"Payment not found Exception expected!"
        );
        assertEquals("Could not find payment: 99999999999999999",ex.getMessage());
    }

    @Test
    void updateStatus_afterAddPayment() {
        final Payment payment = paymentService.addPayment(PaymentProductType.SEPA_CREDIT_TRANSFER);
        assertTrue(payment.getId()>0);
        paymentService.updateStatus(payment.getId(),"ACCEPTED");

        Payment paymentExists = paymentRepository.findById(payment.getId()).orElseThrow(()->new PaymentNotFoundException(payment.getId()));
        assertEquals(PaymentProductType.SEPA_CREDIT_TRANSFER,paymentExists.getType());
        assertEquals(payment.getId(), paymentExists.getId());
        assertEquals("ACCEPTED", paymentExists.getStatus());
        assertNull(paymentExists.getBankPaymentId());
    }

}