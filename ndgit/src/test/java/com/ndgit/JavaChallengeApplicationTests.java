package com.ndgit;

import com.ndgit.entities.Payment;
import com.ndgit.repo.PaymentRepository;
import com.ndgit.services.impl.PeriodicallyRequestBankImpl;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;

@SpringBootTest
class JavaChallengeApplicationTests {

	@Autowired
	PeriodicallyRequestBankImpl periodicallyRequestBank;

	@Autowired
	PaymentRepository paymentRepository;

	@Test
	void contextLoads() {
	}

	@Test
	void scheduleRequestBank() {
		List<Payment> emptyBankPaymentsBefore = paymentRepository.findNextEmptyBankPaymentId(Integer.MAX_VALUE);

		List<Long> updatedPaymentIds = periodicallyRequestBank.scheduleBankRequest();

		List<Payment> emptyBankPaymentsAfter = paymentRepository.findNextEmptyBankPaymentId(Integer.MAX_VALUE);

		Set<Long> updatedPaymentIdsMap = new HashSet<>(updatedPaymentIds);
		emptyBankPaymentsAfter.forEach(p-> assertFalse(updatedPaymentIdsMap.contains(p.getId())));

		List<Payment> updatedPayments = paymentRepository.findAllById(updatedPaymentIds);
		updatedPayments.forEach(p-> assertNotNull(p.getBankPaymentId()));
	}

}
