package com.ndgit.rest;

import com.ndgit.entities.Payment;
import com.ndgit.enums.PaymentProductType;
import com.ndgit.services.PaymentService;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/payment-synchroniser/payments/")
public class PaymentsApi {

    private final PaymentService paymentService;

    public PaymentsApi(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    @PostMapping("/{type}")
    public Payment add(@PathVariable PaymentProductType type) {
        return paymentService.addPayment(type);
    }

    @PutMapping("{paymentId}/{status}")
    public void updateStatus(@PathVariable Long paymentId, @PathVariable String status) {
        paymentService.updateStatus(paymentId, status);
    }
}
