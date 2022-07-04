package com.ndgit.services.impl;

import com.ndgit.entities.Payment;
import com.ndgit.exception.PaymentNotFoundException;
import com.ndgit.repo.PaymentRepository;
import com.ndgit.rest.BankResponse;
import com.ndgit.services.PaymentService;
import com.ndgit.services.PeriodicallyRequestBank;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.*;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Slf4j
@Service
public class PeriodicallyRequestBankImpl implements PeriodicallyRequestBank {

    @Autowired
    PaymentService paymentService;

    @Autowired
    BankClientApiImpl bankClientApi;

    @Autowired
    PaymentRepository paymentRepository;

    @Scheduled(fixedDelayString = "${bank.call.fixedDelay}")
    public List<Long> scheduleBankRequest() {
        List<Long> updatedPaymentIds = new ArrayList<>();

        Payment next = findNextEmptyBankPaymentId();
        while(next!=null){
            String oldStatus = next.getStatus();
            paymentService.updateStatus(next.getId(),"IN-PROGRESS");

            try{
                BankResponse bankResponse = bankClientApi.getPaymentData( next.getId() );
                paymentService.updateBankResponse(next.getId(),bankResponse);
                updatedPaymentIds.add(next.getId());
            }catch (Exception ex){
                paymentService.updateStatus(next.getId(),oldStatus);
                break;
            }

            next = findNextEmptyBankPaymentId();
        }
        return updatedPaymentIds;
    }

    public Payment findNextEmptyBankPaymentId(){
        List<Payment> result = paymentRepository.findNextEmptyBankPaymentId(1);
        if(result.size()>0){
            return result.get(0);
        }else{
            return null;
        }
    }

}
