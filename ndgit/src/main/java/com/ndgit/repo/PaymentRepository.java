package com.ndgit.repo;


import com.ndgit.entities.Payment;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface PaymentRepository extends JpaRepository<Payment,Long> {

    /**
     * get next payment with empty bankPaymentId that status is not in-progress
     */
    @Query(nativeQuery = true, name = "Payment.findNextEmptyBankPaymentId"
            ,value = "SELECT * FROM Payments p " +
            " WHERE p.bank_payment_id is null " +
            " AND p.status<>'IN-PROGRESS'" +
            " limit :limit")
    List<Payment> findNextEmptyBankPaymentId(int limit);

}
